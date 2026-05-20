# Editing Guide — The DePaolo Dispatch

A practical reference for making the two most common changes to the site:
adding figures (images) and editing body text.

---

## 1. Adding a figure (image)

### Step 1 — Add the image file

Put the image in the `assets/` folder. Keep filenames lowercase with hyphens:

```
assets/
  style.css
  nqr-binding-site.png      ← your new image goes here
  vae-latent-space.png
```

### Step 2 — Replace a placeholder in projects.html

Open [projects.html](projects.html). Each figure currently looks like this:

```html
<figure style="margin: 0;">
  <div class="photo h-92">[ fig. 03 ]</div>
  <div class="tiny-label" style="margin-top: 6px;">FIG. 03</div>
  <div class="headline h4">HIV-1 protease ensemble</div>
  <div class="caption">Molecular dynamics · 2026</div>
</figure>
```

Replace the `<div class="photo h-92">` placeholder with an `<img>` tag:

```html
<figure style="margin: 0;">
  <img src="assets/your-image-filename.png"
       alt="Brief description of the figure"
       class="photo h-92"
       style="object-fit: cover;" />
  <div class="tiny-label" style="margin-top: 6px;">FIG. 03</div>
  <div class="headline h4">HIV-1 protease ensemble</div>
  <div class="caption">Molecular dynamics · 2026</div>
</figure>
```

### Figure size classes

Control the height by choosing one of these CSS classes on the `<img>`:

| Class    | Aspect ratio | Min height | Best for              |
|----------|-------------|------------|-----------------------|
| `h-92`   | 4 : 3       | 92 px      | Grid thumbnails       |
| `h-140`  | 4 : 3       | 140 px     | Sidebar portrait      |
| `h-180`  | 16 : 9      | 180 px     | Wide landscape figure |

### Featured (starred) figure

Add the `feat` class and a badge span to mark a figure as a key plate:

```html
<img src="assets/your-image.png"
     alt="Description"
     class="photo h-92 feat"
     style="object-fit: cover;" />
<span class="badge">★ KEY</span>
```

The `feat` class draws a coloured border; the badge appears in the top-right corner.

### Adding a figure to index.html (the portrait slot)

In [index.html](index.html) the sidebar has a portrait placeholder at line 55:

```html
<div class="photo h-140">[ portrait · in lab ]</div>
```

Replace it the same way:

```html
<img src="assets/portrait-lab-2026.jpg"
     alt="Joseph DePaolo-Boisvert in the lab, 2026"
     class="photo h-140"
     style="object-fit: cover;" />
```

---

## 2. Editing text

### Body paragraphs

All body text lives inside `<p>` tags. Open the relevant HTML file and find
the paragraph you want to change. For example, in [index.html](index.html)
the bio starts at the `<div class="col-flow c2">` block:

```html
<p class="dropcap">Joseph A. DePaolo-Boisvert is a doctoral candidate …</p>
<p>Away from the bench he is the co-founder …</p>
```

Edit the text between the tags. The `dropcap` class on the first paragraph
creates the large decorative first letter — keep that class on whichever
paragraph should open the section.

### Page headlines

Each page has a main headline inside an `<h2>` tag (or `<h3>`/`<h4>` for
smaller articles). In [index.html](index.html):

```html
<h2 class="headline h1">Chemist, Founder, Deckhand —<br/>One Person, Three Beats</h2>
```

Change the text between the tags. The `<br/>` forces a line break — remove it
if you want the headline on one line.

### The pull-quote (writing.html)

The pull-quote in [writing.html](writing.html) is inside a `<div class="pull">`:

```html
<div class="pull">
  "Biologically meaningful dynamics often reside on low-dimensional manifolds …"
</div>
```

Replace the quoted text with whatever you want to emphasise.

### The "Now" / latest dispatch text

Open [now.html](now.html) and edit the paragraphs in the main `<section>`.
This is the page visitors see for the most recent update, so it changes the
most often.

### The top rule line (date, weather, volume)

Every page has a decorative top bar:

```html
<div class="rule-top">
  <span>VOL. MMXXVI · NO. CCXIII</span>
  <span class="center">FRONT</span>
  <span>FAIR · W WINDS · 14°</span>
</div>
```

Update the issue number and weather string here. The center label (`FRONT`,
`ARTS`, `OPINION`, etc.) is the section name — leave it unless you rename a
section.

---

## 3. Saving and publishing changes

After editing any file, push the changes to GitHub and the site updates
automatically (usually within 60 seconds):

```bash
git add index.html projects.html writing.html now.html assets/
git commit -m "Update figures and text"
git push
```

If you added a new image file, make sure it is included in the `git add` line,
either by name or by adding `assets/` to include the whole folder.

---

## Quick-reference: which file controls what

| File                        | What to edit there                                  |
|-----------------------------|-----------------------------------------------------|
| [index.html](index.html)    | Bio text, portrait image, front-page teasers        |
| [projects.html](projects.html) | Figure grid, publications index                  |
| [writing.html](writing.html)| Essay previews, pull-quote, archive count           |
| [resume.html](resume.html)  | CV entries, positions, publications                 |
| [now.html](now.html)        | Latest dispatch / current status                    |
| [contact.html](contact.html)| Contact info, classifieds                           |
| [assets/style.css](assets/style.css) | Fonts, colours, layout — edit carefully   |
