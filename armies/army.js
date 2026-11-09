(function () {
  "use strict";

  const baseData = window.CAMPAIGN_ARMY_DATA;
  const variantData = window.CAMPAIGN_ARMY_VARIANTS;
  const data = variantData && baseData
    ? {
        ...baseData,
        armies: { ...baseData.armies, ...(variantData.armies || {}) },
        entries: { ...baseData.entries, ...(variantData.entries || {}) }
      }
    : baseData;
  const indexedRules = (window.WHFB_RULE_DEFINITIONS || {}).definitions || {};
  const campaignRuleData = window.CAMPAIGN_RULE_DEFINITIONS || {};
  const campaignRules = campaignRuleData.definitions || {};
  const campaignRuleOverrides = campaignRuleData.entryOverrides || {};
  const app = document.getElementById("army-app");

  if (!data || !app) return;

  const armyFiles = {
    "rebels-of-bretonnia": "rebels-of-bretonnia.html",
    mousillon: "mousillon.html",
    "wildwood-host": "wildwood-host.html",
    "alliance-against-undeath": "alliance-against-undeath.html",
    "crusade-army": "crusade-army.html",
    "morrsliebs-laughing-masses": "morrsliebs-laughing-masses.html"
  };

  const leaderDestinations = {
    "gilles-king": "index.html#post-campaign-leadership",
    "louen-high-paladin": "crusade-army.html#outcome-louen-high-paladin",
    sacremor: "crusade-army.html#outcome-sacremor",
    "mallobaude-vampire-king": "mousillon.html#outcome-mallobaude-vampire-king",
    "louen-dispossessed": "index.html#post-campaign-leadership"
  };

  function escapeHtml(value) {
    return String(value ?? "")
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }

  function slug(value) {
    return String(value).toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
  }

  function renderList(values, emptyText) {
    if (!values || !values.length) return `<p class="empty-field">${escapeHtml(emptyText)}</p>`;
    return `<ul>${values.map((value) => `<li>${escapeHtml(value)}</li>`).join("")}</ul>`;
  }

  function ruleDefinition(ruleName, entryId) {
    const override = entryId && campaignRuleOverrides[entryId] && campaignRuleOverrides[entryId][ruleName];
    return override || campaignRules[ruleName] || indexedRules[ruleName] || null;
  }

  function renderRuleSource(definition) {
    if (!definition) return "";
    const label = definition.sourceReference || definition.sourceTitle || "Rule source";
    if (!definition.sourceUrl) return `<p class="rule-source">${escapeHtml(label)}</p>`;
    const external = definition.sourceUrl.startsWith("http");
    return `<p class="rule-source"><a href="${escapeHtml(definition.sourceUrl)}"${external ? ' target="_blank" rel="noreferrer"' : ""}>${escapeHtml(label)}</a></p>`;
  }

  function renderRuleDisclosure(ruleName, entryId) {
    const definition = ruleDefinition(ruleName, entryId);
    const hasDefinition = Boolean(definition && definition.html);
    const searchUrl = definition && definition.searchUrl
      ? definition.searchUrl
      : `https://8th.whfb.app/search?q=${encodeURIComponent(ruleName)}`;
    return `
      <details class="rule-reference${hasDefinition ? "" : " unresolved"}">
        <summary>${escapeHtml(ruleName)}</summary>
        <div class="rule-definition">
          ${hasDefinition ? definition.html : `<a class="rule-search-link" href="${escapeHtml(searchUrl)}" target="_blank" rel="noreferrer">Search the WHFB8 index</a>`}
          ${renderRuleSource(definition)}
        </div>
      </details>`;
  }

  function renderSpecialRules(values, entryId) {
    if (!values || !values.length) return '<p class="empty-field">Not specified in this supplement.</p>';
    return `<div class="rule-reference-list">${values.map((value) => renderRuleDisclosure(value, entryId)).join("")}</div>`;
  }

  function renderArmyRule(rule) {
    return `
      <details class="rule-reference army-rule-reference">
        <summary>${escapeHtml(rule.name)}</summary>
        <div class="rule-definition">
          ${rule.detail ? `<p>${escapeHtml(rule.detail)}</p>` : ""}
          ${rule.sourcePage ? `<p class="rule-source"><a href="../rules.html#rules-page-${escapeHtml(rule.sourcePage)}">The Revolt of Mallobaude, p. ${escapeHtml(rule.sourcePage)}</a></p>` : ""}
        </div>
      </details>`;
  }

  function renderProfiles(profiles) {
    if (!profiles || !profiles.length) {
      return '<p class="empty-field">Profile not specified in this supplement.</p>';
    }

    const preferred = ["M", "WS", "BS", "S", "T", "W", "I", "A", "Ld"];
    const present = new Set(profiles.flatMap((profile) => Object.keys(profile.stats || {})));
    const columns = preferred.filter((key) => present.has(key));
    [...present].filter((key) => !columns.includes(key)).forEach((key) => columns.push(key));

    return `
      <div class="profile-wrap">
        <table class="profile-table">
          <thead><tr><th>Profile</th>${columns.map((key) => `<th>${escapeHtml(key)}</th>`).join("")}</tr></thead>
          <tbody>
            ${profiles.map((profile) => `
              <tr>
                <td>${escapeHtml(profile.name)}</td>
                ${columns.map((key) => `<td>${escapeHtml((profile.stats || {})[key] ?? "—")}</td>`).join("")}
              </tr>`).join("")}
          </tbody>
        </table>
      </div>`;
  }

  function renderOptions(options) {
    if (!options || !options.length) return '<p class="empty-field">Options not listed here.</p>';
    return options.map((option) => `
      <div class="option-row">
        <span class="option-label">
          <span>${escapeHtml(option.name)}${option.group ? ` <small>(${escapeHtml(option.group)})</small>` : ""}</span>
          ${option.description ? `<small class="option-description">${escapeHtml(option.description)}</small>` : ""}
        </span>
        <span class="option-cost">${escapeHtml(option.cost || "Not specified")}</span>
      </div>`).join("");
  }

  function renderUnitCard(reference, idPrefix) {
    const entry = data.entries[reference.id];
    if (!entry) return "";
    const cardId = `${idPrefix || "unit"}-${reference.id}`;
    const notes = [...(entry.notes || [])];
    if (reference.note) notes.unshift(reference.note);
    const searchText = [
      entry.name,
      entry.comparedTo,
      ...(entry.profiles || []).map((profile) => profile.name),
      ...(entry.specialRules || []),
      ...(entry.equipment || []),
      entry.source,
      ...notes
    ].filter(Boolean).join(" ").toLowerCase();

    const statusLabel = entry.statusLabel || (entry.status === "referenced" ? "Army-book reference" : "Campaign rule");

    return `
      <details class="unit-card" id="${escapeHtml(cardId)}" data-search="${escapeHtml(searchText)}">
        <summary>
          <span class="unit-name">${escapeHtml(entry.name)}</span>
          <span class="unit-price">${escapeHtml(entry.points || "Points not specified")}</span>
        </summary>
        <div class="unit-body">
          ${entry.comparedTo ? `<p class="unit-comparison"><strong>Based on:</strong> ${escapeHtml(entry.comparedTo)}</p>` : ""}
          ${notes.map((note) => `<p class="unit-note">${escapeHtml(note)}</p>`).join("")}
          <div class="unit-meta">
            <span><strong>Unit size:</strong> ${escapeHtml(entry.unitSize || "Not specified")}</span>
            <span><strong>Troop type:</strong> ${escapeHtml(entry.troopType || "Not specified")}</span>
            <span class="status-pill ${entry.status === "referenced" ? "referenced" : ""}">${escapeHtml(statusLabel)}</span>
          </div>
          ${renderProfiles(entry.profiles)}
          <div class="unit-details">
            <section class="unit-detail">
              <h4>Equipment</h4>
              ${renderList(entry.equipment, "Not specified in this supplement.")}
            </section>
            <section class="unit-detail special-rules-panel">
              <h4>Special Rules</h4>
              ${renderSpecialRules(entry.specialRules, reference.id)}
            </section>
            <section class="unit-detail options-list">
              <h4>Options</h4>
              ${renderOptions(entry.options)}
            </section>
          </div>
          <p class="unit-source"><strong>Reference:</strong> ${entry.sourceHref ? `<a href="${escapeHtml(entry.sourceHref)}">${escapeHtml(entry.source || "The Revolt of Mallobaude")}</a>` : escapeHtml(entry.source || "The Revolt of Mallobaude")}.</p>
        </div>
      </details>`;
  }

  function renderNav(title) {
    return `
      <nav class="army-nav" aria-label="Campaign armies navigation">
        <a class="nav-title" href="index.html">${escapeHtml(title || "Campaign Armies")}</a>
        <a href="../index.html">Project Home</a>
        <a href="index.html">All Armies</a>
        <a href="../rules.html">Rules</a>
        <a href="../guide.html">Game Guide</a>
        <a href="../editorial/decisions.html">Editorial Decisions</a>
      </nav>`;
  }

  function renderCampaignRole(items) {
    if (!items || !items.length) return "";
    return `
      <section class="outcome-panel campaign-role" aria-labelledby="campaign-role-title">
        <h2 id="campaign-role-title">Campaign Use</h2>
        <div class="army-rules-grid">
          ${items.map((item) => `
            <div class="army-rule-item">
              <strong>${item.guideAnchor ? `<a href="../guide.html#${escapeHtml(item.guideAnchor)}">${escapeHtml(item.title)}</a>` : escapeHtml(item.title)}</strong>
              <p>${escapeHtml(item.detail)}</p>
              ${item.changes && item.changes.length ? `
                <div class="campaign-change-grid">
                  ${item.changes.map((change) => `<div class="campaign-change"><strong>${escapeHtml(change.title)}</strong><p>${escapeHtml(change.detail)}</p></div>`).join("")}
                </div>` : ""}
            </div>`).join("")}
        </div>
      </section>`;
  }

  function renderDesignNotes(notes) {
    if (!notes) return "";
    const columns = [
      ...(notes.settled && notes.settled.length ? [{ title: "Army Rules", items: notes.settled }] : []),
      ...(notes.open && notes.open.length ? [{ title: "Questions for Playtesting", items: notes.open }] : [])
    ];
    return `
      <section class="outcome-panel" aria-labelledby="design-notes-title">
        <h2 id="design-notes-title">${escapeHtml(notes.title || "Playtest Notes")}</h2>
        ${notes.intro ? `<p>${escapeHtml(notes.intro)}</p>` : ""}
        <div class="army-rules-grid">
          ${columns.map((column) => `<div class="army-rule-item"><strong>${escapeHtml(column.title)}</strong>${renderList(column.items, "Nothing recorded.")}</div>`).join("")}
        </div>
      </section>`;
  }

  function renderOutcomeAdditions(additions) {
    if (!additions || !additions.length) return "";
    return `
      <section class="outcome-panel" aria-labelledby="outcome-title">
        <h2 id="outcome-title">Outcome-Dependent Additions</h2>
        <p>Use these entries only when permitted by the campaign outcome listed below.</p>
        <div class="outcome-links">
          ${additions.map((reference) => {
            const entry = data.entries[reference.id];
            return `<div class="outcome-link"><a href="#outcome-${escapeHtml(reference.id)}">${escapeHtml(entry.name)}</a><span>${escapeHtml(reference.note || "See the campaign outcome.")}</span></div>`;
          }).join("")}
        </div>
      </section>`;
  }

  function renderArmyPage(armyId) {
    const army = data.armies[armyId];
    if (!army) {
      app.innerHTML = `${renderNav("Campaign Armies")}<main class="army-hub"><h1>Army not found</h1></main>`;
      return;
    }

    document.title = `${army.name} — Campaign Armies`;
    const categoryLinks = army.categories.map((category) => `<a href="#${slug(category.name)}">${escapeHtml(category.name)}</a>`).join("");

    app.innerHTML = `
      ${renderNav(army.name)}
      <header class="army-header">
        <p class="eyebrow">${escapeHtml(army.eyebrow || "The Revolt of Mallobaude · Campaign Army Reference")}</p>
        <h1>${escapeHtml(army.name)}</h1>
        <p class="subtitle">${escapeHtml(army.subtitle)}</p>
        <div class="army-toolbar">
          <div>
            <div class="source-chip-row">
              <a class="source-chip" href="${escapeHtml(army.sourceHref || `../rules.html#rules-page-${army.sourcePage}`)}">${escapeHtml(army.sourceLabel || `Campaign rules, p. ${army.sourcePage}`)}</a>
              ${army.books.map((book) => `<span class="source-chip">${escapeHtml(book)}</span>`).join("")}
            </div>
            <nav class="category-jump" aria-label="Army categories">${categoryLinks}</nav>
          </div>
          <div class="army-filter">
            <label for="army-search">Find a unit or rule</label>
            <input id="army-search" type="search" placeholder="Search this army…" autocomplete="off">
            <div class="army-actions">
              <button id="expand-all" type="button">Expand all</button>
              <button id="collapse-all" type="button">Collapse all</button>
            </div>
          </div>
        </div>
      </header>
      <main class="army-content">
        ${renderCampaignRole(army.campaignRole)}
        ${renderDesignNotes(army.designNotes)}
        <section class="army-rules" aria-labelledby="army-rules-title">
          <h2 id="army-rules-title">Army-Specific Rules</h2>
          <p class="army-rules-intro">Open a rule for its complete campaign wording.</p>
          <div class="army-rule-disclosures">
            ${army.rules.map(renderArmyRule).join("")}
          </div>
        </section>
        ${renderOutcomeAdditions(army.outcomeAdditions)}
        ${army.sourceNote
          ? `<p class="source-note">${escapeHtml(army.sourceNote)} <a href="../editorial/army-notes.html">Reference notes</a>.</p>`
          : `<p class="source-note">${escapeHtml(data.sourceNote)} <a href="../editorial/army-notes.html">Reference notes</a>.</p>`}
        ${army.categories.map((category) => `
          <section class="army-category" id="${slug(category.name)}">
            <h2 class="category-title">${escapeHtml(category.name)}</h2>
            <div class="unit-list">${category.entries.map((reference) => renderUnitCard(reference, "unit")).join("")}</div>
          </section>`).join("")}
        ${army.outcomeAdditions && army.outcomeAdditions.length ? `
          <section class="army-category outcome-category" id="outcome-dependent-profiles">
            <h2 class="category-title">Outcome-Dependent Profiles</h2>
            <div class="unit-list">${army.outcomeAdditions.map((reference) => renderUnitCard(reference, "outcome")).join("")}</div>
          </section>` : ""}
      </main>`;

    const cards = [...document.querySelectorAll(".unit-card")];
    const disclosures = [...document.querySelectorAll("details")];
    const search = document.getElementById("army-search");
    search.addEventListener("input", () => {
      const query = search.value.trim().toLowerCase();
      cards.forEach((card) => {
        card.hidden = Boolean(query) && !card.dataset.search.includes(query);
        if (query && !card.hidden) card.open = true;
      });
    });
    document.getElementById("expand-all").addEventListener("click", () => disclosures.forEach((item) => { if (!item.closest(".unit-card[hidden]")) item.open = true; }));
    document.getElementById("collapse-all").addEventListener("click", () => disclosures.forEach((item) => { item.open = false; }));

    let printState = [];
    window.addEventListener("beforeprint", () => {
      printState = disclosures.map((item) => item.open);
      disclosures.forEach((item) => { item.open = true; });
    });
    window.addEventListener("afterprint", () => disclosures.forEach((item, index) => { item.open = printState[index]; }));

    if (location.hash) {
      const target = document.querySelector(location.hash);
      if (target && target.matches("details")) target.open = true;
    }
  }

  function renderHub() {
    document.title = "Campaign Armies — The Revolt of Mallobaude";
    const armies = Object.entries(data.armies);
    app.innerHTML = `
      ${renderNav("Campaign Armies")}
      <main class="army-hub">
        <p class="eyebrow">The Revolt of Mallobaude · Army-List Reference</p>
        <h1>Campaign Armies</h1>
        <p class="intro">Choose a campaign army below. Campaign rules take precedence over the army books. Morrslieb's Laughing Masses is an optional four-player variant.</p>
        <section class="army-card-grid" aria-label="Campaign army lists">
          ${armies.map(([id, army]) => `
            <a class="army-choice-card" href="${armyFiles[id]}">
              <span class="card-label">${escapeHtml(army.cardLabel || `Rules page ${army.sourcePage}`)}</span>
              <h2>${escapeHtml(army.name)}</h2>
              <p>${escapeHtml(army.subtitle)}</p>
              <span class="card-footer">Open army reference →</span>
            </a>`).join("")}
        </section>
        <section class="leadership-panel" id="post-campaign-leadership" aria-labelledby="leadership-title">
          <p class="eyebrow">Branching Campaign Outcomes</p>
          <h2 id="leadership-title">Post-Campaign Leadership</h2>
          <p>Use the rulers and commanders allowed by your campaign ending; these alternatives are not available together.</p>
          <div class="outcome-links">
            ${data.postCampaignLeaders.map((reference) => {
              const entry = data.entries[reference.id];
              return `<div class="outcome-link"><a href="${leaderDestinations[reference.id]}">${escapeHtml(entry.name)}</a><span>${escapeHtml(reference.note)}</span></div>`;
            }).join("")}
          </div>
        </section>
        <p class="hub-note"><strong>Crusade distinction:</strong> the page 41 Crusade Army serves Conclusions I and II. Conclusion III's “Crusaders of Despair” are instead represented by Bretonnian mercenary allies in an Order army; they do not use the page 41 roster.</p>
      </main>`;
  }

  const armyId = document.body.dataset.army;
  if (armyId) renderArmyPage(armyId);
  else renderHub();
})();
