# UniSense — Landing page

Landing page de apresentação do **UniSense**, plataforma de gestão operacional inteligente para o campus: sensores contam as entradas nos banheiros, abrem chamados nos limites configurados (20 / 30 / 45 acessos) e mostram tudo em um mapa 3D.

O mapa 3D usa os contornos reais dos prédios do Campus Prof. Pedro C. Fornari (UniAnchieta, Jundiaí/SP), extraídos do OpenStreetMap. Os dados dos sensores são simulados.

## Estrutura

- `src.html` — fonte da página (HTML, CSS e JS inline, Three.js via CDN)
- `campus_data.js` — geometria do campus (© OpenStreetMap contributors, ODbL)
- `build.py` — junta `src.html` + `campus_data.js` em `index.html`
- `index.html` — página final publicada

## Rodar localmente

```bash
python build.py
python -m http.server 5178
```

Abra http://localhost:5178.

## Contato

Defina o e-mail do botão de contato em `window.UNISENSE_CONTACT` dentro de `src.html` e rode `python build.py`.

---

Mapa: © [OpenStreetMap](https://www.openstreetmap.org/copyright) contributors.
