"""Curated reading order for the two-duke spreads (12–17) and rebel vows (18).

Each duke spans left THEN right column in one horizontal band. Reading the full
left column first would incorrectly interleave two biographies. Coordinates are
source-page points, deliberately explicit rather than an inferred PDF order.
"""
from html import escape
import re

TITLES = {
    12: 'Armand of Aquitaine and Adalhard of Lyonesse',
    13: 'Tancred II of Quenelles and Alberic of Bordeleaux',
    14: 'Huebald of Carcassonne and Bohemond of Bastonne',
    15: 'Hagen of Gisoreux and Folcard of Montfort',
    16: 'Taubert of L’Anguille and Cassyon of Parravon',
    17: 'Chilfroy of Artois and Theodoric of Brionne',
    18: 'Enemies of the Lady',
}
# Beginning of the second duke; p17 has a separate full-width credits footer.
BANDS = {12: 520, 13: 460, 14: 420, 15: 480, 16: 490, 17: 420}
CONTINUATIONS = {(12, 1), (15, 0), (15, 1), (16, 0), (16, 1), (17, 0)}


def join_columns(left, right, continuing):
    if continuing:
        # A single sentence crosses the original column boundary. Keep it in
        # one paragraph rather than presenting two sentence fragments.
        assert left.endswith('</p>') and right.startswith('<p>')
        return left[:-4] + ' ' + right[3:]
    return left + '\n' + right


def render_page(number, page):
    from build_rules_reader import style, prose
    layer = next(page.find(lambda n: n.has('rules-text')))
    lines = [n for n in layer.children if hasattr(n, 'has') and n.has('pdf-line') and style(n, 'top') < 800]
    assert not list(layer.find(lambda n:n.has('rules-semantic'))), 'New semantic source requires explicit duke-reader review'
    consumed = []
    output = []
    if number <= 17:
        cutoff = 690 if number == 17 else 800
        for band, (top, bottom) in enumerate(((0, BANDS[number]), (BANDS[number], cutoff))):
            columns = []
            for start, end in ((0, 300), (300, 600)):
                selected = [n for n in lines if top <= style(n, 'top') < bottom and start <= style(n, 'left') < end]
                consumed.extend(selected)
                columns.append(prose(selected))
            output.append('<div class="reader-block">' + join_columns(*columns, (number, band) in CONTINUATIONS) + '</div>')
        credits = [n for n in lines if style(n, 'top') >= cutoff]
        consumed.extend(credits)
        if credits:
            output.append('<div class="reader-block reader-credits">' + prose(credits) + '</div>')
    else:
        for start, end in ((0, 300), (300, 600)):
            selected = [n for n in lines if start <= style(n, 'left') < end]
            consumed.extend(selected)
            text = prose(selected)
            # These named rules run into adjacent body text in the reconstructed
            # PDF. Promote only their exact source labels, without rewriting.
            labels = ('The Black Grail Vow', 'Death to the Lady!', 'Sworn Enemy of the Lady', 'Standard of Mousillon', 'Cursed Pennon of Mousillon')
            for label in labels:
                escaped = escape(label)
                if label == 'Standard of Mousillon':
                    text = text.replace(' ' + escaped + ' ', '</p><h3>' + escaped + '</h3><p>', 1)
                else:
                    text = text.replace('<p>' + escaped + ' ', '<h3>' + escaped + '</h3><p>', 1)
            output.append('<div class="reader-block">' + text + '</div>')
        for image in page.find(lambda n:n.tag=='img' and not n.has('page-background')):
            output.append('<figure><img src="' + escape(image.attrs['src'], quote=True) + '" alt="Illustration from source page 18"></figure>')
    assert len(consumed) == len(lines) and len({id(n) for n in consumed}) == len(lines), f'Unassigned or repeated source text on page {number}'
    return '\n'.join(output)
