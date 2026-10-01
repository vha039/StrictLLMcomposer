import sys,json,re
from pathlib import Path
sys.path.insert(0,'runtime')
from jobbsok.paths import Layout
from jobbsok import render, pdf
root=Path('.').resolve()
md=Path('runs/manual_20260930_vend_strawberry/PACKS.md').read_text(encoding='utf8')
v=md.split('# 1. VEND')[1].split('# 2. STRAWBERRY')[0]
brev=v.split('## Brev')[1].split('## CV')[0].strip().split('\n\n')
cv=v.split('## CV')[1].split('## Review')[0]
def fld(n): return re.search(r'\*\*'+n+r':\*\* (.*)',cv).group(1).strip()
comp=[l[2:] for l in cv.split('**Nøkkelkompetanser:**')[1].split('**EMP_OUS_ANALYSE')[0].strip().split('\n') if l.startswith('- ')]
def bl(tag):
    s=cv.split(tag)[1].split('\n\n',1)[1] if False else cv.split(tag)[1]
    out=[]
    for l in s.split('\n')[1:]:
        if l.startswith('- '): out.append(l[2:])
        elif out and l.strip()=='' : break
    return out
pkg={'cv':{'headline':fld('Overskrift'),'profile':fld('Profil'),'competencies':comp,
 'employment_overrides':[{'employment_id':'EMP_OUS_ANALYSE','bullets':bl('**EMP_OUS_ANALYSE')},{'employment_id':'EMP_OUS_BAR','bullets':bl('**EMP_OUS_BAR')}]},
 'letter':{'opening':brev[0],'body_paragraphs':brev[1:-1],'closing':brev[-1]}}
print(json.dumps(pkg,ensure_ascii=False,indent=1)[:600], [len(x['bullets']) for x in pkg['cv']['employment_overrides']],len(comp))
layout=Layout(root)
bm=json.load(open('runs/r20260930-205909-0aff47/frozen/generated/baseline_map.json',encoding='utf8'))
tm=json.load(open('templates/template_map.json',encoding='utf8'))
eff=render.merge_module.effective_cv(bm,pkg)
job={'employer':'Vend','title':'Senior Product Analyst - ReCommerce','unit':None,'reference':'476098887'}
out=Path('runs/manual_20260930_vend_strawberry/vend'); out.mkdir(parents=True,exist_ok=True)
for comp_name,stem in (('cv','CV_Vegard_Haaland_Vend'),('letter','Soknad_Vegard_Haaland_Vend')):
    spec=tm['documents'][comp_name]
    d=out/f'{stem}.docx'
    render._build_document(layout,spec,d,effective=eff,package=pkg,job=job,document_date='2026-09-30')
    r=pdf.convert(d,out/f'{stem}.pdf',converter='word_com',timeout=180)
    print(stem,r)
