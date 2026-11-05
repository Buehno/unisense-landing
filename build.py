# Junta src.html + campus_data.js (contornos do OpenStreetMap) em index.html
from pathlib import Path
d = Path(__file__).parent
src = (d / 'src.html').read_text(encoding='utf-8')
data = (d / 'campus_data.js').read_text(encoding='utf-8')
(d / 'index.html').write_text(src.replace('/*CAMPUS_DATA*/', data), encoding='utf-8')
print('index.html ok')
