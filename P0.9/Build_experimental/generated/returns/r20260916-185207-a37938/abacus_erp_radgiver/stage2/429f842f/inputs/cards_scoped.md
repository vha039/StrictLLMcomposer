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
