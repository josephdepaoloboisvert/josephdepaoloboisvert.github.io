# The DePaolo Dispatch

A personal periodical, built as a static website. Six pages, one stylesheet, no build step.

## Files

```
site/
├── index.html       — front page (about)
├── projects.html    — catalog of figures
├── writing.html     — opinion / essays
├── resume.html      — annual report (cv)
├── contact.html     — classifieds
├── now.html         — latest bulletin
├── 404.html         — error page
├── .nojekyll        — tells GitHub Pages not to process with Jekyll
└── assets/
    └── style.css    — shared stylesheet
```

Fonts load from Google Fonts. No JS, no bundler.

---

## Deploy to GitHub Pages

### Option A · Project site (`username.github.io/personal-website`)

1. Create a new public repo on GitHub — e.g. `personal-website`.
2. Push the **contents of `site/`** to the repo root (so `index.html` is at the top level):
   ```bash
   cd site
   git init
   git add .
   git commit -m "initial publication"
   git branch -M main
   git remote add origin https://github.com/<you>/personal-website.git
   git push -u origin main
   ```
3. On GitHub: **Settings → Pages → Build and deployment**
   Source: *Deploy from a branch* · Branch: `main` · Folder: `/ (root)` · Save.
4. Wait ~60 seconds. Site goes live at `https://<you>.github.io/personal-website/`.

### Option B · Main personal site (`username.github.io`)

Same as above, but name the repo exactly `<you>.github.io`. Site goes live at `https://<you>.github.io/`.

### Option C · Custom domain (e.g. `yourname.com`)

1. Deploy via A or B first.
2. Add a file called `CNAME` (no extension) at the repo root containing just your domain, e.g. `yourname.com`.
3. At your DNS registrar, point an `A` record (apex) or `CNAME` (subdomain) at GitHub Pages. GitHub documents the IPs here: [docs](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site).
4. **Settings → Pages → Custom domain** → enter your domain, save, tick *Enforce HTTPS* once the cert provisions.

---

## Local preview

Any static server works. From inside `site/`:

```bash
python3 -m http.server 8000
# then open http://localhost:8000/
```

---

## Editing

Each page is plain HTML. Common things you may want to change:

- **Bio copy** → `index.html` lead column
- **Projects** → `projects.html` figure grid + index of works
- **Essays** → `writing.html` (the featured op-ed + the side rail)
- **CV** → `resume.html` (publications, positions, skills bars)
- **Contact links** → `contact.html` ad grid
- **Right-now bulletin** → `now.html` (update the date in the section banner too)
- **Colors, fonts, spacing** → `assets/style.css` — see `:root` for the design tokens

To swap the accent color across the whole site, change one line in `style.css`:

```css
--accent: #1f5a8a;   /* try #14365b, #d23a1e, #e08914, #3a6b2e */
```

---

## What is the `.nojekyll` file?

GitHub Pages defaults to processing your repo with Jekyll, which can strip files that start with `_`. The empty `.nojekyll` file disables that. Leave it in place.
