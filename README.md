# Luke Doney portfolio

Static site, no build step. Open `index.html` in a browser to preview.

To publish on GitHub Pages: push this folder to a repo named `<username>.github.io`
(or any repo, then Settings → Pages → Deploy from branch → `main` / root).

- `assets/img/` photos (add new ones here)
- `assets/video/` web-compressed clips

## Editing content
Case studies (problem, constraints, solution, result) live in `tools/content.py`.
After editing, rebuild the pages from this folder with:

    python3 tools/build.py .
