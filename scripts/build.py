"""Rebuild the static policy page using only Python's standard library."""

from html import escape
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
source = (ROOT / "privacy.txt").read_text(encoding="utf-8-sig").strip()
blocks = source.split("\n\n")
sections = []
navigation = []
section_number = 0


def linked(text):
    text = escape(text)
    text = re.sub(r"https://[^\s]+", lambda m: f'<a href="{m[0]}">{m[0]}</a>', text)
    return text.replace("missclicklabs@gmail.com", '<a href="mailto:missclicklabs@gmail.com">missclicklabs@gmail.com</a>')


for block in blocks[1:]:
    if block.startswith("# "):
        if section_number:
            sections.append("</section>")
        section_number += 1
        title = escape(block[2:])
        anchor = f"section-{section_number}"
        navigation.append(f'<li><a href="#{anchor}">{title}</a></li>')
        sections.append(f'<section id="{anchor}" aria-labelledby="heading-{section_number}"><h2 id="heading-{section_number}"><span class="number" aria-hidden="true">0{section_number}</span>{title}</h2>')
    else:
        sections.append(f"<p>{linked(block)}</p>")
if section_number:
    sections.append("</section>")

page = '''<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light">
  <meta name="description" content="Политика конфиденциальности приложения «Мудрость волка» (Wolf’s Wisdom): обработка данных, добровольная аналитика и ваши права.">
  <title>Политика конфиденциальности — Мудрость волка</title>
  <link rel="icon" type="image/webp" href="assets/app-icon.webp">
  <link rel="stylesheet" href="styles.css">
</head>
<body id="top">
  <a class="skip-link" href="#policy">Перейти к политике</a>
  <header class="site-header wrap">
    <a class="brand" href="#top" aria-label="Мудрость волка — в начало страницы">
      <img src="assets/app-icon.webp" width="48" height="48" alt="">
      <span>Мудрость волка<small>Wolf’s Wisdom</small></span>
    </a>
    <a class="header-link" href="mailto:missclicklabs@gmail.com">Связаться <span aria-hidden="true">↗</span></a>
  </header>
  <main class="wrap">
    <div class="hero">
      <p class="eyebrow"><span aria-hidden="true"></span> Данные и конфиденциальность</p>
      <h1>Политика<br>конфиденциальности<span class="accent">.</span></h1>
      <p class="hero-caption">Мудрость волка · Wolf’s Wisdom</p>
      <a class="text-download" href="privacy.txt" download>Скачать текст политики <span aria-hidden="true">↓</span></a>
    </div>
    <div class="document-layout">
      <aside>
        <nav aria-label="Содержание политики">
          <p class="nav-title">На этой странице</p>
          <ol>__NAV__</ol>
          <a class="contact-note" href="mailto:missclicklabs@gmail.com">Вопросы о данных?<br><span>Написать разработчику ↗</span></a>
        </nav>
      </aside>
      <article id="policy" aria-label="Полный текст политики конфиденциальности">
        __CONTENT__
        <a class="back-top" href="#top">Вернуться наверх ↑</a>
      </article>
    </div>
  </main>
  <footer class="wrap"><span>Мудрость волка · Wolf’s Wisdom</span><a href="mailto:missclicklabs@gmail.com">missclicklabs@gmail.com</a></footer>
</body>
</html>
'''
(ROOT / "index.html").write_text(page.replace("__NAV__", "\n".join(navigation)).replace("__CONTENT__", "\n".join(sections)), encoding="utf-8")
print(f"Built index.html from privacy.txt ({section_number} sections).")
