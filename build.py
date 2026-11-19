# Gera as páginas publicadas a partir de src.html (texto-fonte em português):
#   index.html -> versão em inglês (principal)
#   pt.html    -> versão em português
# campus_data.js traz os contornos dos prédios (© OpenStreetMap contributors).
import re
from pathlib import Path
from i18n_en import EXACT, NODE

d = Path(__file__).parent
src = (d / 'src.html').read_text(encoding='utf-8')
data = (d / 'campus_data.js').read_text(encoding='utf-8')
page = src.replace('/*CAMPUS_DATA*/', data)

BASE = 'https://buehno.github.io/unisense-landing/'
HREFLANG = (f'<link rel="alternate" hreflang="en" href="{BASE}">\n'
            f'<link rel="alternate" hreflang="pt-BR" href="{BASE}pt.html">\n'
            f'<link rel="alternate" hreflang="x-default" href="{BASE}">')
SWITCH_EN = '<div class="lang" role="group" aria-label="Language"><span aria-current="true">EN</span><a href="pt.html" hreflang="pt-BR" lang="pt-BR" aria-label="Ver em português">PT</a></div>'
SWITCH_PT = '<div class="lang" role="group" aria-label="Idioma"><a href="./" hreflang="en" lang="en" aria-label="View in English">EN</a><span aria-current="true">PT</span></div>'


def to_en(s):
    for a, b in EXACT:
        s = s.replace(a, b)
    for a, b in sorted(NODE, key=lambda p: -len(p[0])):
        s = re.sub(r'(?<=[>\'"])(\s*)' + re.escape(a) + r'(\s*)(?=[<\'"])', lambda m: m.group(1) + b + m.group(2), s)
    return s


pt = page.replace('<!--HREFLANG-->', HREFLANG).replace('<!--LANGSWITCH-->', SWITCH_PT)
en = to_en(page.replace('<!--HREFLANG-->', HREFLANG + '\n<meta property="og:locale" content="en_US">')
                .replace('<!--LANGSWITCH-->', SWITCH_EN))
pt = pt.replace('<!--HREFLANG-->', '').replace(HREFLANG, HREFLANG + '\n<meta property="og:locale" content="pt_BR">', 1)

(d / 'pt.html').write_text(pt, encoding='utf-8')
(d / 'index.html').write_text(en, encoding='utf-8')
print('index.html (en) + pt.html ok')
