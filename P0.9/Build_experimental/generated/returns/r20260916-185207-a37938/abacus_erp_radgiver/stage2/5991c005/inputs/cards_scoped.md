# Evidence named in the brief

### EV:WORK#025-4-6-prj-06-ste-gevinstfordeling-og-inves · WORK 550-598 · 4.6 `PRJ-06` — STE-gevinstfordeling og investeringsmodell for steril logistikk

*Digest:* COMPLETED | can prove: Omforming av en ustøttet direktefordeling til en transparent vektet proxy-modell; fem arbeidsbøker med fire grenmodeller og én konsolideringsmodell; synlige og konfigurerbare forutsetninger og vekter; Power Query-overføring med skjemakontroll; revisjoner for umappede rader og skjema- eller kontrollavvik; modellen ferdigstilt tidlig i 2026 og overlevert til controllere, bekreftet 2026-09-06 | live ceilings: Ingen direkte måling, eierskap til klinikkestimater, realisert gevinst eller ROI-påstand; implementering per gren, endelige vekter, organisatorisk bruk og realiserte gevinster er fortsatt uavklart

### 4.6 `PRJ-06` — STE-gevinstfordeling og investeringsmodell for steril logistikk

**Problem and reframing**

Direct service-use tracking was insufficient to allocate sterile-logistics benefits defensibly by clinic. Vegard rejected false precision and reframed the request as a transparent proxy-based distribution model based on weighted indirect indicators, explicit assumptions and uncertainty.

**Design contribution**

- Designed a multi-indicator proxy approach rather than presenting indirect evidence as observed use.
- Structured operational, financial, quality/resilience, avoided-cost and transferred-burden mechanisms across clinic/enterprise levels.
- Designed five workbooks: four branch models plus one consolidation model.
- Kept formulas and weights visible/configurable.
- Used Power Query for schema-controlled transfer from branch outputs to consolidation.
- Avoided core VBA deliberately so controllers/domain owners could inspect and adjust assumptions without permanent developer dependence.
- Defined audits for unmapped rows, schema/control drift and nonfunctional validation elements.

Modellen ble ferdigstilt tidlig i 2026 og overlevert til controllere.
Bekreftet 2026-09-06. Dette dokumenterer en ferdigstilt og overlevert
beslutningsstøttemodell, ikke organisatorisk bruk, realiserte gevinster
eller at alle grenmodeller og endelige vekter er tatt i operativ bruk.

**Intended use**

Warehouse, equipment, automation, feature and investment choices. The architecture is decision support under missing data, not direct measurement.

**Ceiling**

Vegard owns framework/system design, not permanent substantive ownership of clinic estimates or final domain judgments. Implementation by branch, final weights, organizational use and realized benefits remain unresolved; controller handover and artifact completion are confirmed. Business-case amounts and recalled ROI are context-only, not personal achievements or realized savings.

**Claim atoms**

| Atom | Supported content |
|---|---|
| `CONTEXT` | Direct service-use data insufficient for defensible clinic allocation |
| `PERSONAL_CONTRIBUTION` | Reframed problem; designed weighted multi-indicator proxy and five-workbook architecture |
| `METHOD_CONTROL` | Visible/configurable assumptions and weights; Power Query schema transfer; mapping/schema/control audits |
| `HUMAN_CHANGE` | Controller/domain-owner inspectability and reduced permanent developer dependence were explicit design goals; the completed model was handed over to controllers early 2026, confirmed 2026-09-06 |
| `STATUS_OUTCOME` | `COMPLETED`: decision-support model designed, finished early 2026 and handed over to controllers; implementation/adoption unresolved |
| `BOUNDARY` | No direct measurement, clinic-estimate ownership, realized benefit or ROI claim |

### EV:WORK#022-4-3-prj-03-modernisering-og-nyutvikling · WORK 375-435 · 4.3 `PRJ-03` — Modernisering og nyutvikling av sykehusets budsjetteringsverktøy

*Digest:* IN_USE | can prove: Arvet ca. 20 år gammelt Excel/VBA-budsjetteringsverktøy på ca. 15 ark og 78 globale navn; 2025-moderniseringen integrerte ansatt-, ansettelses- og bemanningsdata; i praksis eneste kodende utvikler for kodeendringene, bekreftet 2026-09-06, innenfor en bred interessentprosess på ca. 50 personer; ca. 80 prosent atferdsbevarende funksjon-for-funksjon-refaktorering med differansekontroll, akseptansekriterier og risikoregister; controller-onboarding; sykehusdekkende bruk i budsjettprosessene for 2026 og 2027 og ferdigstilt 2027-modernisering | live ceilings: Ikke opphavsperson eller budsjetteier; ingen eierskap til hele moderniseringen eller budsjettprosessen; ingen besparelse tilsvarende budsjettskala, nulldefekt eller kvantifisert tids- og feilreduksjon; det foreligger ikke godkjente målinger av effekt

### 4.3 `PRJ-03` — Modernisering og nyutvikling av sykehusets budsjetteringsverktøy

**Origin and system**

Inherited approximately 20-year-old Excel/VBA budgeting tool originally created by Vegard’s former department leader. Vegard did not create the original. Over time it became business-critical and accumulated technical debt across formulas, named ranges, VBA architecture and distributed workbook copies.

The FY-2025 workbook is supported at approximately 15 worksheets and 78 global named ranges. It contains logic for employee/employment/staffing data, organization, finance, FTE, activity, periodization, aggregation, analysis, control and export.

**2025 modernization**

The main change added native employee, employment and staffing/labour information, replacing a process that required copying data from another workbook and involved significant manual work. Approximately 50 people participated across workgroups, requirements discussions and implementation-adjacent activity. Vegard was effectively the principal/sole coder changing workbook/VBA; preserve the broader stakeholder process.

The implementation lead required a narrow, function-by-function refactor even though Vegard recommended broader restructuring. Approximately 80% of the changes were behaviour-preserving one-to-one refactors. This demonstrates controlled modernization under constraint, not Vegard’s preferred target architecture.

**Technical contribution**

- Reconstructed architecture from VBA source, workbook metadata, formulas, names and prior reports.
- Integrated staffing/labour data and related organization, finance, FTE, periodization, analysis, control and export logic.
- Compared original/refactored functions and identified logic drift.
- Introduced `Option Explicit`, centralized constants, clearer Norwegian comments and explicit parity/zero-regression expectations.
- Used differential/code comparison, workbook comparison/hash-style gates, acceptance criteria and gap/risk registers.
- Cleaned opaque formulas, hidden white-text formulas, inconsistent references/names and logic distributed across cells, names and VBA.
- Improved refresh/orchestration, generated sheets, periodization keys, rounding/validation logic, logging, protection/visibility and performance modes.
- Evaluated VBA, Office Scripts, Python and AI-assisted approaches against compatibility, operational risk and maintainability.
- Produced controller onboarding and presentation material.

**Delivered/current status**

- Den moderniserte versjonen ble brukt sykehusdekkende i budsjettprosessen
  for 2026.
- Den avsluttende moderniseringen for 2027 er ferdigstilt. Vegard hadde
  vesentlig større frihet i denne runden; verktøyet er nå i sykehusdekkende
  bruk i den pågående budsjettprosessen for 2027. Bekreftet 2026-09-06.
- Bruk og leveranse er dokumentert. Det foreligger ikke godkjente målinger
  av tidsbesparelse, feilreduksjon eller økonomisk effekt.

**Claim atoms**

| Atom | Supported content |
|---|---|
| `CONTEXT` | Inherited approximately 20-year-old business-critical Excel/VBA budgeting tool with technical debt and distributed copies |
| `PROCESS_PROBLEM` | Staffing/labour data had to be copied from a separate workbook; significant manual work and change risk |
| `PERSONAL_CONTRIBUTION` | Reconstructed architecture; principal/effectively sole coder changing workbook/VBA; integrated staffing data; improved orchestration, controls and documentation |
| `METHOD_CONTROL` | Function-by-function constrained refactor; differential/parity review; acceptance criteria; risk/gap register; explicit zero-regression expectations |
| `ADOPTION_HUMAN_CHANGE` | Approximately 50-person stakeholder context; controller onboarding/presentation material |
| `STATUS_OUTCOME` | Sykehusdekkende bruk i budsjettprosessene for 2026 og 2027; 2027-moderniseringen ferdigstilt, bekreftet 2026-09-06 |
| `BOUNDARY` | Not original creator or budget owner; no savings, zero-defect or quantified time/error claim |

**Ceiling**

Never claim original creation, sole ownership of the complete modernization or budget process, personal control of hospital budgets, savings equal to budget scale, zero defects or quantified time/error reduction. Approximate hospital budget values are context-only and require separate approval before external use.

### EV:WORK#020-4-1-prj-01-styrings-bi-for-sykehus-og-se · WORK 272-335 · 4.1 `PRJ-01` — Styrings-BI for sykehus og semantisk modell

*Digest:* DECOMMISSIONED | can prove: Greenfield styrings-BI i en firepersoners analyseavdeling; hovedbidrag i backend med nesten hele den semantiske modellen, mesteparten av ETL/M og ca. 80–90 prosent av DAX; drift, testing, brukerobservasjon og avgrenset livsløpseierskap ca. aug. 2025–feb. 2026 | live ceilings: Kolleger ledet innhold og visualisering; ingen nåværende eller flerårig eierskap, kvantifisert adopsjon eller effekt, eksakt side-, tabell-, mål- eller brukerskala og ingen virksomhetsarkitekturmyndighet

*Boundaries naming this record:*

- WORK 8: | Approximately 80–90% of dashboard DAX; almost all semantic model; most ETL/M | Contribution scale for `PRJ-01` | Self-reported share; colleagues led visual/content work |

### 4.1 `PRJ-01` — Styrings-BI for sykehus og semantisk modell

**Problem/context**

A four-person analysis department received a broad, lightly specified assignment to build a management dashboard spanning financial, staffing, sickness absence, activity/DRG and related management information. The solution was built from scratch. Source/environment limitations made monthly operation burdensome.

**Division of labour**

Vegard was the principal backend developer. He reports:

- almost all semantic-model design;
- most ETL logic in Power Query M;
- approximately 80–90% of DAX;
- primary technical troubleshooting due to deepest backend/model knowledge.

Colleagues mainly led content selection, visual design and front-end presentation, with some report work after technical guidance.

**Technical contribution**

- Chose star-schema patterns after evaluating alternatives, including snowflake concepts, based on Power BI suitability and maintainability.
- Designed fact/dimension separation, organizational/period keys, dimensions and relationships across finance, staffing and activity/DRG contexts.
- Implemented Power Query M pipelines, custom functions, schema/type handling, transformations, null handling and data-quality controls.
- Developed/debugged DAX for deviations, ratios, accumulated values, cut-off periods, year-to-date comparisons, DRG performance and hierarchical context.
- Handled organizational hierarchies, period/calendar logic, historical/current alignment, SAS/Excel dependencies and model-size/performance trade-offs.
- Identified redundant descriptive fields in fact tables and strengthened fact/dimension discipline.
- Contributed to navigation, tooltips, bookmarks, report structure and extension planning.
- Separated large-model modernization from routine extension work when model limits created delivery risk.
- Maintained documentation, technical backlogs and monthly operating context.

**Lifecycle and user orientation**

- Official owner approximately August 2025–February 2026.
- Maintained monthly updates during that period.
- Conducted supervised tests with actual users, observed confusing interactions, collected feedback and ran focused improvement sprints.
- Dashboard decommissioned around February 2026; this is historical delivered/operated evidence, not current ownership.

**Separate BI workshop**

Vegard led an internal workshop for economist/health-economist colleagues covering process mapping, ETL, star schemas, semantic-model practices, Power Query, DAX optimization, governance, performance, data quality and action planning. Slides and a Loop workspace were workshop artifacts, not dashboard infrastructure.

**Claim atoms**

| Atom | Supported content |
|---|---|
| `CONTEXT` | Greenfield hospital-management BI solution; four-person analysis department; broad/lightly specified brief |
| `PERSONAL_CONTRIBUTION` | Principal backend developer; almost all semantic-model design; most ETL/M; approximately 80–90% of DAX |
| `METHOD_CONTROL` | Star schema, keys/relationships, data-quality controls, technical troubleshooting, documentation and operating backlog |
| `ADOPTION_HUMAN_CHANGE` | Monthly operation; supervised tests with actual users; observed friction; focused improvement sprints; internal BI workshop |
| `STATUS_OUTCOME` | Built and operated; Vegard owner approximately Aug. 2025–Feb. 2026; decommissioned around Feb. 2026 |
| `BOUNDARY` | Colleagues led content/visuals; no current ownership, quantified effect or enterprise-architecture authority |

**Ceiling**

Do not claim all visuals/content, current ownership, multi-year ownership, quantified adoption/efficiency, exact page/table/measure/user scale or enterprise-architecture authority.

## Boundaries (global, verbatim)

## 8. Godkjente måltall og resultatgrenser

| Metric | Approved use | Required qualifier / prohibited implication |
|---|---|---|
| Four-person analysis department | Team/context scale | Never imply sole department/project ownership |
| Approximately 1.5 months before gradually taking over month-close tasks; full assigned flow within approximately 3 months | Ramp-up and learning-speed signal from BAR | Self-reported approximate timing; not expert-from-day-one or all-OUS close ownership |
| REGERP conversion tools used relatively frequently by finance advisers in several clinics shortly after transition | Operational adoption beyond own desk | No exact clinic/user/run count, quantified saving or central-system ownership |
| Complete `budsjetthjelpeark.xlsx` built by Vegard | Personal artifact ownership in BAR budget support | Does not transfer ownership of inherited main budget workbooks or clinic budget |
| One monthly BAR DRG estimate matched realized DRG exactly when rounded to the nearest whole point | Narrow concrete forecast observation | Never generalize to model accuracy, repeated performance or validated production forecasting |
| Approximately 80–90% of dashboard DAX; almost all semantic model; most ETL/M | Contribution scale for `PRJ-01` | Self-reported share; colleagues led visual/content work |
| Dashboard owner approximately Aug. 2025–Feb. 2026 | Former lifecycle ownership | Not current ownership |
| Approximately 15 worksheets and 78 global names | Budget-workbook architecture scale | Retain `approximately`; verify before headline use |
| Approximately 20-year-old inherited budgeting tool | Legacy context | Vegard did not create it |
| Approximately 50 participants/stakeholders; Vegard effectively sole coder | Role/process scale | Bekreftet 2026-09-06; gjelder kodeendringene, ikke hele budsjettprosessen; broad stakeholder process remains |
| Sykehusdekkende bruk i budsjettprosessene for 2026 og 2027; 2027-moderniseringen ferdigstilt, bekreftet 2026-09-06 | Operational use | Not zero defects, savings or personal budget authority |
| Hospital-wide benefits framework active approximately 2.5 years later | Team-delivered durability/adoption | No personal ownership or measured effect |
| 14-, 90- and 365-day forecast horizons | Project scope | Active development; no production claim |
| Approximately 40,000 repository lines | Project scale | Distributed coworker/AI authorship |
| Five-workbook STE architecture | Designed and completed scope; model handed over to controllers early 2026 | Not proof of full implementation/adoption |

Never use contextual hospital budget values, STE business-case amounts, recalled ROI, rare-access population figures or unverified productivity/adoption measures externally without explicit reclassification.

### 10.1 Eksplisitt forbudt

Do not claim that Vegard:

- owned month-end close for all OUS, held formal accounting/controller leadership or performed year-end close;
- built every inherited BAR accounting/reporting workbook or owned all underlying source data;
- developed or owned the central REGERP/Oracle solution or ERP transition programme;
- delivered quantified time/error savings from the BAR conversion tools without new evidence;
- owned all BAR projects, invoices, budget work, management-report content or clinic decisions;
- achieved generally exact or validated forecast performance because one rounded monthly DRG estimate matched actual;
- created the original budgeting tool;
- owned or controlled the hospital budgets processed through it;
- designed every dashboard visual/content element or currently owns the decommissioned dashboard;
- built the original XGBoost model or completed all data preparation/features;
- manually authored the entire forecasting repository;
- completed Prophet, Chronos or the final ensemble;
- deployed the forecasting system as a completed production platform;
- has mature enterprise MLOps/CI/CD;
- led enterprise Fabric adoption or owns a central platform;
- personally owned/solely authored the hospital-wide benefits framework;
- owns the full recruitment process or has hiring authority;
- has formal line-management, enterprise architecture, enterprise data-governance, AI-governance or security authority;
- realized business-case estimates or contextual budget values as personal results.

### 10.2 Uavklart – utelat eller behold smal kvalifikator

- exact BAR month-close task list by period, report cadence/recipient count and types/frequency of errors found;
- number/names of clinics, advisers, conversions and duration of REGERP-tool use; quantified time/error effects;
- exact categories, volume and duration of project-economics cases beyond the documented demand-driven assignment model;
- exact recurring methodology, model selection, code authorship, forecast horizon and performance series for the 2023 BAR DRG estimates;
- full personal modification scope in inherited BAR accounting/reporting workbooks and the partially decoded binary VBA content;
- exact dashboard name, start/delivery date, pages/tables/measures/sources/users and decommission reason;
- exact operations-report unit/name/dates/components/current status;
- exact benefits-framework name, individual split, approval route, use and effect;
- forecasting deployment/performance and language-specific coding split;
- STE implementation, weights, adoption and realized benefits;
- exact platform-pilot names, access scope and governance;
- AI-superuser assistance: exact dates, user count and formal organization-wide support mandate;
- adoption, time saved, error reduction, cycle-time change, AI productivity and other quantified outcomes not explicitly approved above.

When an unresolved item is decisive, ask one targeted question. Otherwise omit it.

### 4.2 Forbudte oppgraderinger

Do not infer:

- health-economics degree/certification;
- computer-science or software-engineering degree;
- AI-engineer or data-engineer qualification;
- professional mastery of Python, databases or ML from courses alone;
- financial-engineering specialization;
- formal leadership/management qualification;
- thesis topic, grade, specialization or result;
- degree completion for the ongoing UiA programme.

### 4.3 Uavklarte punkter

- UiA study pace, current progression, expected completion and detailed current modules.
- NTNU award date, thesis title/topic, specialization and grade.
- UiB exact award date and grade.
- Historical page/title/code alignment for `ECON210`, `ECON263`, `ECON264`, `INFO132`, `ECON290`, `FIN3005`, `FIN3006`.
- Detailed content for `RET100`, `PSY3813` and the four listed UiA courses.
- Formal Norwegian equivalence of Canadian upper-secondary study.

If a strict vacancy criterion depends on any unresolved detail, ask one targeted question or request official documentation. Otherwise use the conservative degree/capability wording above.

### 0.3 Ufravikelige claim-kontroller

Aldri:

- finn på datoer, titler, kvalifikasjoner, resultater, besparelser, produksjonssetting eller myndighet;
- gjør teamarbeid til soloeierskap;
- gjør deltakelse til ledelse eller formelt mandat;
- gjør planlagt/aktivt/pilotarbeid til ferdig leveranse;
- gjør kontekstuell skala til personlig effekt eller autoritet;
- gjør estimert/forventet gevinst til realisert resultat;
- gjør KI-/kollegaimplementering til Vegards manuelle forfatterskap;
- bruk uavklarte fakta uten lagret smal kvalifikator;
- bruk arbeidsgiverresearch, tidligere søknader, modellprosa eller minne som kandidatbevis.

### 4.5 KI-grenser

Do not claim:

- production LLM applications;
- RAG, fine-tuning, model serving or LLM observability;
- enterprise AI governance;
- autonomous decision authority;
- quantified AI productivity gain;
- sole manual authorship;
- production ML-platform/MLOps ownership;
- organization-wide AI transformation.
