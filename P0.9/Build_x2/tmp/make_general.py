import sys,json
from pathlib import Path
sys.path.insert(0,'runtime')
from jobbsok.paths import Layout
from jobbsok import render, pdf
pkg={'cv':{
'headline':'Rådgiver Økonomi og IKT | Digitalisering, data og beslutningsstøtte',
'profile':'Samfunnsøkonom (master, NTNU) og rådgiver i økonomi og IKT ved Oslo universitetssykehus. Omsetter brede og uklare behov til avgrensede løsninger, fra krav og arkitektur til kontrollert implementering, opplæring og overlevering, i et regulert og komplekst miljø. Teknisk og funksjonell pådriver i prosjekter: prioriterer, strukturerer leveranser, integrerer bidrag fra kolleger og kodeagenter og sørger for dokumentasjon og brukerinnføring. Har medutviklet en sykehusdekkende gevinstmetode, gjennomført kodeendringene i moderniseringen av et budsjettverktøy i sykehusdekkende bruk og bygget beslutningsstøtte i Power BI. Arbeider med KI-støttet utvikling under menneskelig kontroll og er registrert KI-superbruker.',
'competencies':[
'Digitalisering og prosessforbedring',
'Behovsavklaring, krav og akseptansekriterier',
'Løsningsarkitektur og kontrollert implementering',
'Prioritering, backlog og leveransestruktur (Scrum/Kanban)',
'Gevinstrealisering, investeringsstøtte og økonomistyring',
'BI, prognoser og analyse (Power BI, DAX, SQL, R, Python)',
'KI-støttet utvikling og arbeidsflyter med menneskelig kontroll',
'Workshops, opplæring og endringsforankring'],
'employment_overrides':[
{'employment_id':'EMP_OUS_ANALYSE','bullets':[
'Gjennomførte kodeendringene i moderniseringen av et arvet Excel/VBA-budsjettverktøy i 2025, i praksis som eneste kodende utvikler, i en interessentprosess med om lag 50 deltakere. Integrerte bemanningsdata som tidligere måtte kopieres manuelt, kontrollerte endringene funksjon for funksjon med akseptansekriterier og risikoregister, og laget opplæringsmateriell for controllere. Moderniserte versjoner er brukt sykehusdekkende i budsjettprosessene for 2026 og 2027.',
'Medutviklet en metode for gevinstrealisering og gevinstestimering i et team på fire, med bidrag i forskningssyntese, økonomisk analyse og standardisering. Innført som sykehusdekkende standard og fortsatt i bruk om lag 2,5 år senere.',
'Utformet en modell for gevinstfordeling og investeringsvalg i steril logistikk der direkte bruksdata ikke bar en forsvarlig fordeling: vektede, indirekte indikatorer, synlige og justerbare forutsetninger og kontroller i fem arbeidsbøker. Ferdigstilt og overlevert til controllere tidlig i 2026.',
'Hovedutvikler av datamodell og beregninger i et styringsdashbord for økonomi, bemanning og aktivitet i en analyseavdeling på fire. Kolleger ledet innhold og visualisering. Brukertestet med faktiske brukere og drevet månedlig av meg som eier fra om lag august 2025 til avviklingen rundt februar 2026.'.replace('drevet månedlig av meg som eier','drevet månedlig med kandidaten som eier'),
'Har arkitektur, orkestrering og automatisering i et pågående prognoseprosjekt (14, 90 og 365 dager) for pasientvolum og kapasitet, sammen med en kollega og kodeagenter, med prosjektinstruksjoner, tester, tidsbevisst validering og gjennomgang. Under utvikling.',
'Utformet strukturerte spørreskjemaer for arbeidsinntak (formål, brukere, beslutningsbehov, avhengigheter, risiko, prioritet og akseptansekriterier) og evaluerte Forms-, Loop-, Power BI-, Pega- og lavkodealternativer. Design og evaluering på prosjektnivå.',
'Deltok i firepersoners etableringsgruppe for Analyseavdelingen. Utformet teamstruktur- og ansvarsalternativer, Scrum/Kanban-oppgavehierarki og WIP-design, og planla og fasiliterte workshops om arbeidsform. Blanding av innførte praksiser og forslag.',
'Ledet en intern BI-workshop for økonomer og helseøkonomer og lærte opp teknisk personale i en annen rapporterings- og dataorganisasjon i Power BI og modellering. Registrert KI-superbruker i om lag tre år, med svar på tekniske henvendelser i en Teams-kanal.',
'Deltok i piloter og tidlig tilgang til Fabric, Power Platform, dbt, Pega og Python, og vurderte mulighetene mot konkrete sykehusbegrensninger. Utforskende.']},
{'employment_id':'EMP_OUS_BAR','bullets':[
'Overtok hele den tildelte månedsoppgjørsflyten innen om lag tre måneder, med avstemming, kvalitetssikring, resultatforklaring og rapportering til klinikkledere.',
'Utviklet på eget initiativ Excel/VBA-verktøy for konvertering og validering ved overgangen til REGERP og lærte VBA gjennom arbeidet. Brukt av økonomirådgivere i flere klinikker kort etter overgangen.',
'Bidro i budsjettarbeidet for 2024, bygget et budsjetthjelpeark, arbeidet med prosjektøkonomi og fakturering etter behov og leverte seksjonsvise DRG-estimater med Stata, R og Power Query til budsjett og planlegging.']}]}}
pkg['cv']['employment_overrides'][0]['bullets'][3]='Hovedutvikler av datamodell og beregninger i et styringsdashbord for økonomi, bemanning og aktivitet i en analyseavdeling på fire. Kolleger ledet innhold og visualisering. Brukertestet med faktiske brukere og drevet månedlig som eier fra om lag august 2025 til avviklingen rundt februar 2026.'
layout=Layout(Path('.').resolve())
bm=json.load(open('runs/r20260930-205909-0aff47/frozen/generated/baseline_map.json',encoding='utf8'))
tm=json.load(open('templates/template_map.json',encoding='utf8'))
eff=render.merge_module.effective_cv(bm,pkg)
job={'employer':'Generalist','title':'Generalist-CV','unit':None,'reference':None}
out=Path('runs/manual_20260930_vend_strawberry/generalist'); out.mkdir(parents=True,exist_ok=True)
d=out/'CV_Vegard_Haaland_Generalist.docx'
render._build_document(layout,tm['documents']['cv'],d,effective=eff,package=pkg,job=job,document_date='2026-10-01')
print(pdf.convert(d,out/'CV_Vegard_Haaland_Generalist.pdf',converter='word_com',timeout=180).ok)
import re;print(len(re.findall(rb'/Type\s*/Page[^s]',open(out/'CV_Vegard_Haaland_Generalist.pdf','rb').read())))
