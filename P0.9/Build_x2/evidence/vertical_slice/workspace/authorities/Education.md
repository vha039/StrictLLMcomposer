---
document: Jobbsøk_26 education and academic capability evidence
pack_version: 0.5.3
content_version: 2.3.0
verified_as_of: 2026-07-23
updated_as_of: 2026-07-26
owner: Vegard Håland
authority_domain: education_courses_academic_capabilities
status: PRODUKSJONSKLAR
field_schema: P0.5_SELECTION_AND_CLAIM_ATOMS_V1
language_contract: nb_semantic_runtime_en_machine_ids_bilingual_evidence
source_pack_baseline: Jobbsøk_26 Production pack 1.2.0
claim_index_baseline: 34_EVIDENCE_CLAIM_INDEX.jsonl@1.2.0
derived_from:
  - Jobbsøk_26 Production pack 1.2.0 education objects
  - Verified Higher-Education Knowledge and Skills Report
  - approved CV chronology
  - Jobbsøk_26 P0.5 Architecture and Change Plan
  - Jobbsøk_26 P0.5.2 language-aligned production pack
---

# Utdanning

Denne filen eier grader, studiestatus, emner, akademiske ferdigheter og utdanningsrelaterte påstandsgrenser. Emner dokumenterer akademisk grunnlag eller eksponering; de etablerer ikke alene profesjonell mestring.

Rutingsfelt og utdanningsatomer er konstruksjonsmateriale, ikke ferdig CV-/søknadsprosa. Bygg formuleringene på nytt for stillingen, og attribuer bachelor-, master- og pågående studier korrekt.

**Språkkontrakt:** Norsk runtime-kjerne styrer utdanningspresentasjonen. Stabile engelske metadatafelt/ID-er, offisielle engelske emnenavn og tospråklige søkesynonymer beholdes når de beskytter presisjon eller gjenfinning. Arbeidsgivertekst formuleres alltid på nytt i naturlig Bokmål.

## 0. Runtime-kjerne

### 0.1 Gradskronologi

| ID | Periode/status | Institusjon og program | Godkjent bruk og grense |
|---|---|---|---|
| `EDU-001` | 2024–d.d.; pågående | Universitetet i Agder – femårig masterprogram i kunstig intelligens | Bruk `pågående`. Studiebelastning, forventet fullføring og eksakt progresjon er uavklart. |
| `EDU-002` | 2020–2022; fullført | NTNU – mastergrad i samfunnsøkonomi | Graden er fullført. Eksakt tildelingsdato, spesialisering, oppgave og sluttkarakter er uavklart. |
| `EDU-003` | 2017–2020; fullført | Universitetet i Bergen – bachelorgrad i samfunnsøkonomi | Graden er fullført. Tidligere oppgitt snittkarakter B utelates til ny bekreftelse. |
| `EDU-004` | 2011–2013 | Ernest Manning High School, Calgary – naturfag og avansert matematikk | Internasjonal videregående utdanning og engelskgrunnlag; ikke påstå formell norsk ekvivalens. |

### 0.2 Akademisk profil

Vegards sterkeste formelle grunnlag er samfunnsøkonomi, kvantitative metoder og empirisk analyse: mikro-/makroøkonomi, velferds-/offentlig økonomi, politisk økonomi, arbeidsmarkedsøkonomi, nærings-/konkurranseøkonomi, handel/åpen økonomi, miljø-/ressursøkonomi, økonometri, tidsserier, matematisk analyse, investering/finans og selvstendig vitenskapelig arbeid. Supplerende tekniske studier dokumenterer grunnleggende Python og fagnivåeksponering mot kunstig intelligens, programvareutvikling, databaser og diskret matematikk. Profilen støtter økonomi-/økonometri-baserte analyse- og rådgiverroller sterkere enn ren informatikk- eller produksjonsutviklerposisjonering.

### 0.3 Ferdighetsklynger

| Ferdighet | Trygt claim | Hovedgrunnlag | Grense |
|---|---|---|---|
| Samfunnsøkonomi/offentlig politikk | Formelt grunnlag i mikro, makro, velferd/offentlig, politisk, arbeidsmarked, næring/konkurranse, handel og miljø/ressurs | UiB og NTNU | Ikke egen helseøkonomigrad/-sertifisering |
| Økonometri/kvantitativ metode | Masternivå i økonometri, anvendt empirisk design, tidsserier og matematisk strukturert analyse | ECON240, SØK3001, SØK3514, FIN3006, SØK3004 | Akademisk metode beviser ikke produksjonsdybde i modellering |
| Finans/virksomhetsforståelse | Formelt grunnlag i investering/finans, verdsettelse, regnskap/kontroll og fintech-konsepter | ECON261, ECON263, ECON264, FIN3005/3006 | Ikke spesialiststatus i finansiell ingeniørkunst |
| Forskning/kommunikasjon | Selvstendig vitenskapelig analyse, litteraturbruk, empiri, omfattende skriving, kildehåndtering, argumentasjon og kritisk drøfting | bachelor-/masteroppgaver, ex.phil., EiT/RET100 med kvalifikatorer | Oppgavetema/resultater og noe faginnhold er uavklart |
| Databehandling | Verifiserte Python-grunnferdigheter og supplerende fag i KI, programvareutvikling, datamodellering og diskret matematikk | INFO132 og UiA-fag | Detaljerte UiA-læringsutbytter er ikke verifisert; bruk `fag/eksponering` |

### 0.4 Gjenfinningsindeks

**Rutingsprioritet:** Bruk utdanning i rekkefølgen `korrekt grad og status -> eksplisitt formalkrav -> relevant metodegrunnlag -> teknisk supplement`. Emnetittel kan dekke akademisk grunnlag eller eksponering, aldri alene praktisk mestring.

| Stillingskrav | Hent |
|---|---|
| mastergrad / economics / samfunnsøkonomi | §§1, 2.1, 3.1 |
| økonometri / statistikk / kausalanalyse / kvantitativ metode | §§2.2, 3.2 |
| tidsserie / prognose / matematisk analyse | §§2.2, 3.2 |
| offentlig politikk / insentiver / regulering / arbeidsmarked / konkurranse | §§2.1, 3.1 |
| finans / investering / verdsettelse / regnskap / kontroll | §§2.3, 3.3 |
| Python / KI / databaser / programvare / matematikk / responsible AI / human-in-the-loop | §§2.4, 3.4; koble anvendt KI til `Other_high-value_information.md`, ikke utled praksis fra fag |
| skriving / forskning / tverrfaglig samarbeid | §§2.5, 3.5 |
| prosessforbedring / økonomiprosess / regnskapsnært / controller | §§0.5, 2.1 (`ECON263`, `ECON261`), 2.3, 3.3, 4 |
| regnskap / budsjett / økonomistyring / kontroll / likviditet | §§0.5, 2.1 (`ECON263`), 3.3, 4 |
| prosess-/forbedringsleder / økonomi + teknologi | §§0.5, 3.3–3.5; kombiner med tidlig OUS og `PRJ-03`/`PRJ-04` |
| strengt formalkrav eller emnenavn | §§2, 4 |

### 0.5 `finance_process_role_bridge`

Akademisk regnskap/kontroll er ikke regnskapsbyrå-, lønns-, årsoppgjør-,
revisjons- eller IFRS-erfaring. Emneinnhold dokumenterer akademisk grunnlag
eller eksponering; praktisk ekspertise må komme fra `Work_experience.md`.

| Record | Source section | Lifecycle | Can prove | Live ceilings |
|---|---|---|---|---|
| UiA — pågående masterprogram i kunstig intelligens | 1.1 | Pågående | Femårig masterprogram i kunstig intelligens fra 2024, oppgitt som pågående, som formell teknisk utvikling ved siden av arbeidsbasert KI-, prognose- og programmeringsevidens | Ingen studietakt, forventet fullføring, årstrinn eller modulprogresjon, gradsfullføring eller KI-ingeniørstatus uten ny bekreftelse |
| NTNU — fullført mastergrad i samfunnsøkonomi | 1.2 | COMPLETED | Fullført mastergrad 2020–2022 med avansert økonometri, anvendt empirisk design, tidsserieøkonometri, matematisk analyse, makro og åpen økonomi, insentiver og kontrakter, offentlig beslutning og atferd, finans og selvstendig masteroppgave | Ingen eksakt tildelingsdato, oppgavetittel eller tema, spesialisering eller sluttkarakter uten bekreftelse |
| UiB — fullført bachelorgrad i samfunnsøkonomi | 1.3 | COMPLETED | Fullført bachelorgrad 2017–2020 med bred økonomikjerne, statistikk og økonometri, matematikk, offentlig, politisk, industriell, arbeidsmarkeds- og miljøøkonomi, handel og åpen økonomi, bedriftsøkonomi, finans, Python-introduksjon og selvstendig bacheloroppgave | Eldre CV oppga snittkarakter B; utelates til den er bekreftet på nytt |
| Ernest Manning High School, Calgary | 1.4 | 2011–2013 | Videregående skolegang 2011–2013 med realfag og avansert matematikk, internasjonal utdanningserfaring og praktisk engelsk, samt English 30-1 i Alberta oppgitt som høyeste nivå for elever uten engelsk som morsmål, bekreftet 2026-09-06 | Beskrives konservativt; ingen norsk-ekvivalent kvalifikasjon eller AP-ekvivalens uten dokumentasjon, og ingen CEFR-ekvivalens eller standardisert testscore er fastsatt |
| UiB — økonomi, politikk og virksomhetsforståelse | 2.1 | not applicable | Emnegruppe med godkjent innholdstak per emne, blant annet ECON100, ECON110, ECON116, ECON130, ECON210, ECON218 og ECON225, som dekker mikro, makro, miljø- og ressursøkonomi, velferd og politisk økonomi samt handel og næringsstruktur | Emneinnhold dokumenterer akademisk grunnlag eller eksponering, aldri alene profesjonell mestring; rader merket HISTORICAL_MISMATCH har kjent tittel- eller sideavvik |
| Kvantitative metoder, økonometri og matematikk | 2.2 | not applicable | Emnegruppe fra UiB og NTNU med godkjent innholdstak per emne: ECON140, ECON240, SØK3001, SØK3514, FIN3006 og SØK3004, som dekker matematikk for økonomer, statistikk og økonometri, videregående og anvendt økonometri, tidsserieøkonometri og videregående matematisk analyse | Akademisk grunnlag eller eksponering, ikke praktisk mestring; FIN3006 er merket HISTORICAL_MISMATCH for eksakt periode |
| NTNU — økonomi, insentiver, makro og finans | 2.3 | not applicable | Emnegruppe med godkjent innholdstak per emne: SØK3006 om valuta, olje og makroøkonomisk politikk, SØK3007 om skatt og beslutningsatferd, SØK3008 om insentiver, informasjon og arbeidskontrakter, samt FIN3005 makrofinans | Akademisk grunnlag eller eksponering, ikke praktisk mestring; FIN3005 har verifisert emneeksistens, men utilgjengelige opprinnelige læringsutbytter |
| Programmering, KI, databaser og diskret matematikk | 2.4 | not applicable | Emnegruppe med godkjent innholdstak per emne: INFO132 med Python-grunnlag, og IKT111, IKT105, IKT101 og MA-180 som formell emnenivåeksponering | IKT111, IKT105, IKT101 og MA-180 er merket UNRESOLVED og gir bare formell eksponering uten algoritme-, verktøy-, SQL-, normaliserings- eller DBMS-påstand; anvendt KI-praksis hentes fra Other_high_value_information.md, ikke utledes fra fag |
| Selvstendig arbeid, kommunikasjon og tverrfaglig samarbeid | 2.5 | not applicable | Emnegruppe med godkjent innholdstak per emne: ECON290 bacheloroppgave, SØK3900 masteroppgave, EXPHIL-SVSEM, RET100 og PSY3813 Eksperter i team | RET100 og PSY3813 er merket UNRESOLVED med utilgjengelige detaljerte utbytter; ECON290 er merket HISTORICAL_MISMATCH; akademisk grunnlag, ikke praktisk mestring |

**Claim-atomer**

| Atom | Støttet innhold |
|---|---|
| `COMPLETED_DEGREE` | Master i samfunnsøkonomi fra NTNU; bachelor i samfunnsøkonomi fra UiB |
| `BACHELOR_BUSINESS_ECONOMICS` | `ECON263`: finans-/driftsregnskap, budsjett, likviditet/kontroll, verdsettelse, kapitalstruktur, strategi og økonomisk styring; historisk side-/tittelavvik gjelder |
| `BACHELOR_FINANCE` | `ECON261`: investering/finansiering, verdsettelse, risiko, markeder og porteføljegrunnlag |
| `PUBLIC_ECONOMICS` | Velferds-/offentlig, politisk, arbeidsmarkeds- og konkurranseøkonomi fra UiB/NTNU |
| `MASTER_METHOD` | Avansert økonometri, anvendt empirisk design, tidsserieøkonometri og matematisk analyse |
| `TECHNOLOGY_SUPPLEMENT` | Pågående KI-program, verifisert grunnleggende Python og fagnivåeksponering mot KI/programvare/database/diskret matematikk |
| `BOUNDARY` | Faginnhold støtter akademisk grunnlag; praktisk ekspertise må komme fra `Work_experience.md` |

### 0.6 Stabil claim-proveniens

## 1. Grader og studiestatus

### 1.1 Universitetet i Agder – pågående masterprogram i kunstig intelligens

- Period: 2024–present.
- Programme: five-year master programme in artificial intelligence.
- Status: ongoing.
- Safe role: formal technical development that complements—not replaces—work-derived AI, forecasting, programming and analytical evidence.
- Do not state full-time/part-time pace, expected completion, current year/module progression, degree completion or AI-engineer status without new confirmation.

### 1.2 NTNU – fullført mastergrad i samfunnsøkonomi

- Period: 2020–2022.
- Status: completed.
- Strongest supported academic value: advanced econometrics, applied empirical design, time-series econometrics, mathematical analysis, macro/open-economy policy, incentives/contracts, public decision/behaviour, finance and independent thesis work.
- Do not state exact award date, thesis title/topic, specialization or final grade without confirmation.

### 1.3 Universitetet i Bergen – fullført bachelorgrad i samfunnsøkonomi

- Period: 2017–2020.
- Status: completed.
- Strongest supported academic value: broad economics core, statistics/econometrics, mathematics, public/political/industrial/labour/environment economics, trade/open economy, business economics, finance, Python introduction and independent thesis.
- Older CV reported average grade B; omit until reconfirmed.

### 1.4 Ernest Manning High School, Calgary

- Period: 2011–2013.
- Science and advanced mathematics.
- Supports international educational experience and strong practical English.
- Describe conservatively; do not claim Norwegian-equivalent qualification or AP equivalence without documentation.
- English 30-1 i Alberta; kandidaten opplyser at dette var høyeste nivå for elever uten engelsk som morsmål. Bekreftet 2026-09-06. Ingen CEFR-ekvivalens eller standardisert testscore er fastsatt.

## 2. Faglig evidensoversikt

Status:

- `VERIFIED`: direct official course/content match.
- `HISTORICAL_MISMATCH`: course clearly related but page/title/code/semester is not exact.
- `UNRESOLVED`: course/title evidence exists, but detailed content cannot be safely attributed.

Participation/completion is based on the supplied subject list. For a strict formal criterion, reconcile against transcript or official record before using exact course detail.

### 2.1 Universitetet i Bergen – økonomi, politikk og virksomhetsforståelse

| Course | Status | Safe content ceiling |
|---|---|---|
| `ECON100` Examen facultatum — innføring i samfunnsøkonomi | HISTORICAL_MISMATCH | Economic history, living standards, markets/equilibrium/models, externalities, policy, crises, unemployment, inflation and monetary/fiscal policy. |
| `ECON110` Mikroøkonomiske grunnbegreper og markedsteori | VERIFIED | Consumer and producer theory, costs, market forms and introductory labour supply/demand. |
| `ECON116` Miljø- og ressursøkonomi | VERIFIED | Environmental/resource economics, policy instruments, renewable/non-renewable resources, sustainability and climate-policy framing. |
| `ECON130` Makroøkonomi | VERIFIED | National accounts; consumption, saving, investment, trade, unemployment, inflation, interest rates and Norwegian fiscal/monetary policy. |
| `ECON210` Velferd og økonomisk politikk | HISTORICAL_MISMATCH | Welfare/general-equilibrium analysis, market failure, uncertainty, game theory and optimal taxation; exact historical title/page mismatch. |
| `ECON218` Næringsstruktur og internasjonal handel | VERIFIED | Comparative advantage, scale economies, dumping, market power, sheltered/exposed sectors and factor effects. |
| `ECON225` Politisk økonomi | VERIFIED | Voters, parties, interest groups, collective decision rules, distribution, coalitions and rent seeking. |
| `ECON229` Arbeidsmarkedsøkonomi | VERIFIED | Labour supply/demand, wage formation, income distribution, Norwegian labour market and policy effects. |
| `ECON230` Internasjonal makroøkonomi | VERIFIED | Small-open-economy macro, exchange rates, employment, inflation, growth, capital markets and currency areas. |
| `ECON260` Næringsøkonomi og konkurransepolitikk | VERIFIED | Monopoly/oligopoly, game theory, market power, price discrimination, mergers, cartels, vertical agreements and competition-policy analysis. |
| `ECON263` Bedriftsøkonomi for samfunnsøkonomer | HISTORICAL_MISMATCH | Financial/operating accounts, budgeting, liquidity/control systems, valuation, capital structure, strategy and economic control. |
| `ECON264` Financial Technology | HISTORICAL_MISMATCH | Financial intermediation, peer-to-peer platforms, blockchain/cryptocurrency and fintech innovation; supported through recoded successor page. |
| `ECON261` Investering og finansiering I | VERIFIED | Investment/financing, real/securities valuation, risk, markets, taxation, efficient markets and portfolio basics. |

### 2.2 Kvantitative metoder, økonometri og matematikk

| Course | Institution | Status | Safe content ceiling |
|---|---|---|---|
| `ECON140` Matematikk for økonomer | UiB | VERIFIED | Algebra, equations, differentiation/integration, elasticity, multivariable functions, constrained optimization/Lagrange and financial mathematics. |
| `ECON240` Statistikk og økonometri | UiB | VERIFIED | Probability/distributions, estimation, hypothesis testing and simple regression; STATA, R or Excel relevance. |
| `SØK3001` Videregående økonometri | NTNU | VERIFIED | Model specification, statistical testing and empirical analysis across cross-section, time-series and panel data. |
| `SØK3514` Anvendt økonometri | NTNU | VERIFIED | Empirical-study design, method selection, strengths/weaknesses of approaches, causal identification and independent empirical work. |
| `FIN3006` Anvendt tidsserieøkonometri | NTNU | HISTORICAL_MISMATCH | Dynamic/non-stationary/nonlinear time series, regime shifts, panel data and volatility modelling; exact-period page mismatch. |
| `SØK3004` Videregående matematisk analyse | NTNU | VERIFIED | Linear algebra, eigenvalues/eigenvectors, differential equations, integration and advanced single/multivariable analysis. |

### 2.3 NTNU – økonomi, insentiver, makro og finans

| Course | Status | Safe content ceiling |
|---|---|---|
| `SØK3006` Valuta, olje og makroøkonomisk politikk | VERIFIED | Inflation targeting, exchange rates, business cycles, small-open-economy policy, oil-sector effects and sectoral models. |
| `SØK3007` Skatt, beslutningsatferd og økonomisk politikk | VERIFIED | Collective decisions, public goods/governance/production, taxation and behavioural response. |
| `SØK3008` Insentiver, informasjon og arbeidskontrakter | VERIFIED | Contracts under asymmetric information, efficiency wages, recruitment/turnover/productivity incentives and wage/employment determination. |
| `FIN3005` Makrofinans | HISTORICAL_MISMATCH | Course existence and asset-pricing successor overlap verified; exact original learning outcomes unavailable. |

### 2.4 Programmering, KI, databaser og diskret matematikk

| Course | Institution | Status | Safe content ceiling |
|---|---|---|---|
| `INFO132` Innføring i programmering | UiB | HISTORICAL_MISMATCH | Python fundamentals: variables, types/operations, conditionals, loops, functions, iteration, collections, files, classes and elementary OOP. |
| `IKT111` Concepts of Artificial Intelligence | UiA | UNRESOLVED | Introductory formal exposure to AI concepts only; no specific algorithms/tools claim. |
| `IKT105` Datamodellering og databaser | UiA | UNRESOLVED | Formal course-level exposure to database modelling/databases; no detailed SQL/normalization/DBMS claim. |
| `IKT101` Grunnleggende softwareutvikling | UiA | UNRESOLVED | Introductory formal exposure to software development. |
| `MA-180` Diskret matematikk 1 | UiA | UNRESOLVED | Introductory formal exposure to discrete mathematics. |

### 2.5 Selvstendig arbeid, kommunikasjon og tverrfaglig samarbeid

| Course | Status | Safe content ceiling |
|---|---|---|
| `ECON290` Bacheloroppgave | HISTORICAL_MISMATCH | Independent scientific economics analysis using theory, literature and/or empirical quantitative work. |
| `SØK3900` Masteroppgave i samfunnsøkonomi | VERIFIED | Independent scientific analysis, literature use, study design, supervision/seminars, sustained analytical writing and oral component. |
| `EXPHIL-SVSEM` Examen philosophicum — seminarmodell | VERIFIED | Philosophy of science, ethics, political philosophy, language/argumentation, writing, source handling, presentation and critical discussion. |
| `RET100` Innføring i retorikk | UNRESOLVED | Course title confirmed; detailed outcomes unavailable. |
| `PSY3813` Eksperter i team — psychophysiology village | UNRESOLVED | Generic interdisciplinary teamwork, real-world problem solving and process reflection; village-specific content unverified. |

## 3. Tverrfaglig syntese og stillingsrelevans

### 3.0 Utvalgsruter for utdanning

| Vacancy route | `selection_value` | Lead with | Support with | Do not lead with |
|---|---|---|---|---|
| Economics/public adviser | `VERY_HIGH` | Completed economics master, public/incentive/econometric grounding | Independent analysis and work-based public-sector evidence | Ongoing AI programme |
| Finance/process improvement | `HIGH` | Completed economics degrees + `finance_process_role_bridge` | Work-based finance/process evidence | Missing accounting-firm specialisms |
| BI/quantitative analytics | `HIGH` | Economics master + econometrics/time series | Work-based BI/data delivery | Course exposure as professional mastery |
| Forecasting/data science | `HIGH_SUPPORT` | Econometrics, time series, mathematics | `PRJ-05` professional evidence | Completed-AI-degree or production-ML inference |
| Digitalization/business–technology bridge | `HIGH_SUPPORT` | Economics + ongoing technical study | Work-based Excel/VBA, BI, requirements and AI-enabled delivery | `software engineer`, `AI engineer` or `database specialist` identity |
| Formal computer-science/software role | `LOW/CONDITIONAL` | Only exact verified courses if the requirement is flexible | Strong work evidence where relevant | Any implied CS/software-engineering degree |

**Port for pågående KI-studium:** Det kan være hovedsignal bare når pågående KI-utdanning eksplisitt er et avgjørende og støttet kriterium. Ellers er det et underordnet supplement til valgt rute. Statusordet `pågående` og grensene i §§0.1/1.1 skal følge enhver materiell bruk.

### 3.1 Økonomi, helse og offentlig analyse

Strongly supported academic foundations:

- incentives, market failure, welfare and resource allocation;
- public policy, collective decisions, taxation and governance;
- labour markets, contracts, recruitment/turnover/productivity incentives;
- industrial organization, competition and regulation;
- macro/open-economy analysis and public-policy context;
- business economics, budgeting/control and investment/finance;
- empirical analysis of public/operational questions.

Safe external framing:

`Samfunnsøkonom med bred faglig forankring i mikro- og makroøkonomi, offentlig økonomi, arbeidsmarked, konkurranse, økonometri og kvantitativ analyse.`

For healthcare roles, connect this academic base to supported OUS work. Do not claim a formally verified health-economics specialization from coursework alone.

### 3.2 BI, data, økonometri og prognoser

The combination of statistics/econometrics, advanced econometrics, applied empirical design, time-series econometrics, mathematical analysis and Python fundamentals supports:

- quantitative problem formulation;
- model specification and testing;
- cross-section/time-series/panel reasoning;
- causal-identification awareness;
- dynamic/non-stationary/regime-sensitive time-series concepts;
- optimization and mathematically structured reasoning;
- interpretation and communication of empirical results.

Use professional forecasting/BI depth from `Work_experience.md`; education supplies formal method grounding.

### 3.3 Økonomi- og driftsroller

Safe academic support:

- investment/financing, risk, valuation and portfolio basics;
- budgeting, liquidity and control-system concepts;
- accounting/operating-account awareness;
- macrofinance/asset-pricing exposure;
- fintech concepts.

Do not position as financial engineer, IFRS specialist, auditor or accounting-close owner without separate experience.

For process/improvement roles in finance or accounting-adjacent environments:

- treat the completed economics master as a clear economics-education requirement match;
- use `ECON263` and `ECON261` as correctly attributed bachelor-level grounding;
- connect education to practical evidence from early OUS and `PRJ-03`, rather than presenting course content as work experience;
- present the ongoing AI programme as a technology supplement, not the candidate's primary identity;
- do not introduce the bridge through negative wording about accounting-firm, payroll or year-end-close experience.

### 3.4 Digitaliserings- og teknologiroller

Safe interpretation:

- verified introductory Python;
- ongoing AI programme;
- documented course exposure to AI concepts, software development, database modelling and discrete mathematics;
- strong work-derived evidence in BI, Excel/VBA, forecasting and controlled AI-assisted delivery.

The technical academic strand complements professional evidence; it does not independently support `software engineer`, `AI engineer`, `database specialist` or `computer scientist`.

### 3.5 Seniorrådgiver- og tverrfunksjonelle roller

Education supports:

- structured analysis of incentives, institutions, regulation, distribution and trade-offs;
- independent scientific inquiry and sustained writing;
- source criticism, argumentation and ethical reasoning;
- empirical-method selection and limitations;
- interdisciplinary collaboration with appropriate qualification.

This can support senior-adviser positioning through judgment and analytical depth. It does not establish formal management training or line leadership.

## 4. Godkjente utdanningsformuleringer og grenser

### 4.1 Claim-atomer for utdanning

| Atom ID | Supported content | Attribution/qualifier |
|---|---|---|
| `EDU-A01` | Completed master’s degree in economics | NTNU, 2020–2022 |
| `EDU-A02` | Completed bachelor’s degree in economics | UiB, 2017–2020 |
| `EDU-A03` | Ongoing five-year master programme in artificial intelligence | UiA, 2024–present; pace/progression/completion unresolved |
| `EDU-A04` | Master-level coursework in advanced econometrics, applied econometrics, time-series econometrics and advanced mathematical analysis | NTNU; retain historical mismatch qualifier for `FIN3006` if exact content is material |
| `EDU-A05` | Bachelor-level business-economics grounding in accounts, budgeting, liquidity/control systems, valuation, strategy and economic control | UiB `ECON263`; historical page/title mismatch |
| `EDU-A06` | Bachelor-level investment/finance grounding in valuation, risk, markets and portfolio basics | UiB `ECON261` |
| `EDU-A07` | Broad economics grounding across public/welfare, labour, political, competition, macro/open-economy and environmental/resource economics | UiB/NTNU; exact courses remain separately attributed |
| `EDU-A08` | Verified introductory Python fundamentals | UiB `INFO132`; historical page/code alignment qualifier |
| `EDU-A09` | Course-level exposure to AI concepts, software development, database modelling and discrete mathematics | UiA; detailed outcomes unresolved |
| `EDU-A10` | Independent scientific analysis, empirical design, sustained writing, source handling and critical discussion | Bachelor/master thesis and supporting subjects; thesis topics/results unresolved |

Reconstruct vacancy-specific wording from these atoms. Use `faglig forankring`, `masterfag`, `kursbakgrunn` or `studieeksponering` where needed. Prefer work evidence for practical expertise, and never collapse bachelor- and master-level subjects into an ambiguous course list.

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
