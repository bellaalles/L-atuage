#!/usr/bin/env python3
"""Генератор статических страниц L'ATUAGE (шапка/подвал общие)."""
import pathlib

OUT = pathlib.Path(__file__).resolve().parent.parent

from index_body import INDEX  # noqa: E402

ARROW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
         'stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>')

ICONS = {
    'heart': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 20s-7-4.35-7-9a4 4 0 0 1 7-2.65A4 4 0 0 1 19 11c0 4.65-7 9-7 9Z"/></svg>',
    'menu': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 7h16M4 12h16M4 17h10"/></svg>',
    'close': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="m6 6 12 12M18 6 6 18"/></svg>',
    'up': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 19V5M6 11l6-6 6 6"/></svg>',
    'search': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>',
    'ig': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r="1" fill="currentColor" stroke="none"/></svg>',
    'fb': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M13.5 21v-7h2.4l.4-2.9h-2.8V9.2c0-.8.2-1.4 1.4-1.4h1.5V5.2c-.3 0-1.2-.1-2.3-.1-2.3 0-3.9 1.4-3.9 4v2h-2.4V14h2.4v7h3.3Z"/></svg>',
    'yt': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M21.6 7.2c-.2-1-1-1.7-2-1.9C17.8 5 12 5 12 5s-5.8 0-7.6.3c-1 .2-1.8.9-2 1.9C2 9 2 12 2 12s0 3 .4 4.8c.2 1 1 1.7 2 1.9C6.2 19 12 19 12 19s5.8 0 7.6-.3c1-.2 1.8-.9 2-1.9.4-1.8.4-4.8.4-4.8s0-3-.4-4.8ZM10 15.5v-7l6 3.5-6 3.5Z"/></svg>',
    'vk': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12.8 17.3c-5.4 0-8.6-3.7-8.7-9.9h2.8c.1 4.6 2.2 6.5 3.8 6.9V7.4h2.6v3.9c1.5-.2 3.1-1.9 3.6-3.9h2.6c-.4 2.5-2.1 4.2-3.3 4.9 1.2.6 3.1 2 3.9 4.9h-2.9c-.6-1.9-2-3.3-3.9-3.5v3.6h-.5Z"/></svg>',
}

NAV = [
    ('catalog.html', 'Каталог'),
    ('index.html#best', 'Хиты'),
    ('about.html', 'О бренде'),
    ('contacts.html', 'Где купить'),
    ('index.html#journal', 'Журнал'),
]

HEAD = """<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#ffffff">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="assets/img/products/teni-smart-touch.webp">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' fill='%230b0b0c'/%3E%3Crect x='0' y='56' width='64' height='8' fill='%23e5112b'/%3E%3Ctext x='32' y='40' font-family='Helvetica,Arial' font-size='30' font-weight='600' fill='%23fff' text-anchor='middle'%3EL%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css?v=6">
</head>
<body>
<div class="loader" aria-hidden="true">
  <div class="loader__inner">
    <div class="loader__word"><span>L'ATUAGE</span></div>
    <div class="loader__bar"><i></i></div>
  </div>
</div>
<div class="progress"></div>
"""

HEADER = """
<header class="header">
  <div class="header__inner">
    <a class="logo" href="index.html" aria-label="L'ATUAGE cosmetic — на главную">
      <span class="logo__word">L'Atuage</span>
      <span class="logo__sub">Cosmetic</span>
    </a>
    <nav class="nav" aria-label="Основная навигация">
      {nav}
    </nav>
    <div class="header__actions">
      <a class="icon-btn" href="catalog.html" aria-label="Избранное" style="position:relative">
        {heart}
        <span data-fav-count style="position:absolute;top:-4px;right:-4px;min-width:16px;height:16px;border-radius:9px;background:var(--red);color:#fff;font-size:9px;font-weight:700;display:none;place-items:center;line-height:1"></span>
      </a>
      <a class="btn" href="catalog.html"><span>Каталог</span>{arrow}</a>
      <button class="icon-btn burger" aria-label="Открыть меню" aria-expanded="false" aria-controls="menu">{menu}</button>
    </div>
  </div>
</header>

<div class="menu" id="menu">
  <button class="icon-btn menu-close" aria-label="Закрыть меню">{close}</button>
  <nav class="menu__list" aria-label="Мобильное меню">
    {menu_items}
  </nav>
  <div class="menu__foot">
    <a href="tel:+375173962311">+375 (17) 396-23-11</a>
    <a href="mailto:info@latuage.com">info@latuage.com</a>
    <span>Минск, ул. Ложинская, 14, оф. 23</span>
  </div>
</div>
"""

FOOTER = """
<footer class="footer">
  <div class="container">
    <div class="footer__top">
      <div class="footer__brand">
        <a class="logo" href="index.html">
          <span class="logo__word">L'Atuage</span>
          <span class="logo__sub">Cosmetic</span>
        </a>
        <p>Белорусская декоративная косметика полного цикла. Более 300 наименований и 500+ магазинов по СНГ.</p>
        <div class="footer__socials">
          <a href="https://www.instagram.com/latuage_cosmetic/" target="_blank" rel="noopener" aria-label="Instagram">{ig}</a>
          <a href="https://www.facebook.com/latuagecosmetic" target="_blank" rel="noopener" aria-label="Facebook">{fb}</a>
          <a href="https://vk.com/latuage" target="_blank" rel="noopener" aria-label="ВКонтакте">{vk}</a>
          <a href="https://www.youtube.com/channel/UCGLxuns5dPyCUeEu_8ONjWw" target="_blank" rel="noopener" aria-label="YouTube">{yt}</a>
        </div>
      </div>
      <div>
        <h4>Каталог</h4>
        <ul>
          <li><a href="catalog.html?cat=eyes">Глаза</a></li>
          <li><a href="catalog.html?cat=lips">Губы</a></li>
          <li><a href="catalog.html?cat=face">Лицо</a></li>
          <li><a href="catalog.html?cat=hands">Руки и ногти</a></li>
          <li><a href="catalog.html?cat=accessories">Аксессуары</a></li>
        </ul>
      </div>
      <div>
        <h4>Компания</h4>
        <ul>
          <li><a href="about.html">О бренде</a></li>
          <li><a href="about.html#production">Производство</a></li>
          <li><a href="contacts.html">Контакты</a></li>
          <li><a href="contacts.html#wholesale">Оптовым клиентам</a></li>
          <li><a href="contacts.html#faq">Вопросы и ответы</a></li>
        </ul>
      </div>
      <div>
        <h4>Связаться</h4>
        <ul>
          <li><a href="tel:+375173962311">+375 (17) 396-23-11</a></li>
          <li><a href="mailto:info@latuage.com">info@latuage.com</a></li>
          <li>220114, Минск,<br>ул. Ложинская, 14, оф. 23</li>
          <li>Пн–Пт, 9:00–18:00</li>
        </ul>
      </div>
    </div>
  </div>
  <div class="footer__giant" aria-hidden="true">L'ATUAGE</div>
  <div class="container">
    <div class="footer__bottom">
      <span>© 2014–2026 ЧТУП «ДЮПАМ КОСМЕТИК». Все права защищены.</span>
      <span style="display:flex;gap:18px;flex-wrap:wrap">
        <a href="#">Политика конфиденциальности</a>
        <a href="#">Условия использования</a>
        <a href="#">Карта сайта</a>
      </span>
    </div>
  </div>
</footer>
<button class="to-top" aria-label="Наверх">{up}</button>
<script src="assets/js/data.js?v=4"></script>
<script src="assets/js/app.js?v=4"></script>
</body>
</html>
"""


def page(filename, title, desc, body, active=''):
    nav = '\n      '.join(
        '<a href="{}"{}>{}</a>'.format(href, ' class="is-active"' if href == active else '', label)
        for href, label in NAV
    )
    menu_items = '\n    '.join(
        '<a href="{}"><small>0{}</small>{}</a>'.format(href, i + 1, label)
        for i, (href, label) in enumerate(NAV)
    )
    html = (
        HEAD.format(title=title, desc=desc)
        + HEADER.format(nav=nav, menu_items=menu_items, heart=ICONS['heart'],
                        menu=ICONS['menu'], close=ICONS['close'], arrow=ARROW)
        + body
        + FOOTER.format(**ICONS)
    )
    (OUT / filename).write_text(html, encoding='utf-8')
    print('written', filename, len(html))


# ============================ CATALOG ============================
CATALOG = """
<main>
<section class="phero">
  <div class="phero__bg"></div>
  <div class="container">
    <nav class="crumbs" aria-label="Хлебные крошки">
      <a href="index.html">Главная</a><span>/</span><span style="color:var(--ink)">Каталог</span>
    </nav>
    <h1>Каталог <em>продуктов</em></h1>
    <div class="phero__sub">
      <p>60 продуктов, 4 категории и палитры, из которых сложно выбрать одну.
      Фильтруйте по категории или ищите по названию.</p>
      <span class="badge-round"><i></i>300+ наименований в полном ассортименте</span>
    </div>
  </div>
</section>

<div class="toolbar">
  <div class="container toolbar__inner">
    <div class="chips" role="tablist" aria-label="Категории">
      <button class="chip is-active" data-cat="all">Все <span>60</span></button>
      <button class="chip" data-cat="eyes">Глаза <span>21</span></button>
      <button class="chip" data-cat="lips">Губы <span>7</span></button>
      <button class="chip" data-cat="face">Лицо <span>18</span></button>
      <button class="chip" data-cat="hands">Руки <span>10</span></button>
      <button class="chip" data-cat="accessories">Аксессуары <span>4</span></button>
    </div>
    <div class="toolbar__tools">
      <label class="search">
        {search_icon}
        <input id="catalog-search" type="search" placeholder="Поиск продукта" aria-label="Поиск по каталогу">
      </label>
      <div class="sort">
        <select id="catalog-sort" aria-label="Сортировка">
          <option value="default">По популярности</option>
          <option value="new">Сначала новинки</option>
          <option value="name">По названию</option>
        </select>
      </div>
    </div>
  </div>
</div>

<section class="section section--tight">
  <div class="container">
    <div class="catalog__count" id="catalog-count">60 продуктов</div>
    <div class="cgrid u-mt-16" id="catalog-grid"></div>
  </div>
</section>

<section class="section cta">
  <div class="container">
    <div class="cta__inner">
      <div>
        <span class="eyebrow label" style="color:rgba(244,239,232,.5)">Опт и партнёрство</span>
        <h2>Нужен <em>прайс-лист</em>?</h2>
        <p>Отправим полный каталог с ценами, условиями поставки и материалами для витрины.</p>
      </div>
      <form class="cta__form" data-fake>
        <div class="field">
          <input type="email" required placeholder="Рабочий e-mail" aria-label="E-mail">
          <button type="submit" aria-label="Отправить">{arrow}</button>
        </div>
        <span class="cta__note">Ответим в течение рабочего дня.</span>
        <span class="cta__ok" data-ok></span>
      </form>
    </div>
  </div>
</section>
</main>

<div class="modal" id="quick" role="dialog" aria-modal="true" aria-label="Быстрый просмотр">
  <div class="modal__backdrop"></div>
  <div class="modal__box"></div>
</div>
"""


# ============================ PRODUCT ============================
PRODUCT = """
<main>
<section class="phero" style="padding-bottom:clamp(18px,2vw,28px)">
  <div class="phero__bg"></div>
  <div class="container">
    <nav class="crumbs" aria-label="Хлебные крошки">
      <a href="index.html">Главная</a><span>/</span>
      <a href="catalog.html">Каталог</a><span>/</span>
      <a id="crumb-cat" href="catalog.html">Категория</a><span>/</span>
      <span style="color:var(--ink)" id="crumb-name">Продукт</span>
    </nav>
  </div>
</section>

<section class="section" style="padding-top:clamp(20px,3vw,36px)">
  <div class="container">
    <div class="pdp" id="pdp"></div>

    <div class="acc u-mt-40" style="margin-top:clamp(40px,6vw,80px)">
      <div class="acc__item">
        <button class="acc__btn">Состав и безопасность <i></i></button>
        <div class="acc__panel"><div>Продукт разработан и произведён в Республике Беларусь. Формула без спирта,
        прошла дерматологический контроль. Полный состав указан на упаковке и в сертификате соответствия.</div></div>
      </div>
      <div class="acc__item">
        <button class="acc__btn">Как применять <i></i></button>
        <div class="acc__panel"><div>Наносите на подготовленную кожу. Для стойкого результата используйте базу
        и закрепите финишной пудрой. Смывается обычным средством для снятия макияжа.</div></div>
      </div>
      <div class="acc__item">
        <button class="acc__btn">Доставка и покупка <i></i></button>
        <div class="acc__panel"><div>Продукт представлен в 500+ магазинах-партнёрах СНГ. Оптовые поставки —
        от одного короба, срок отгрузки 3–7 рабочих дней. Контакты отдела продаж — на странице «Контакты».</div></div>
      </div>
    </div>
  </div>
</section>

<section class="section section--tight" style="padding-top:0">
  <div class="container">
    <div class="section-head">
      <div>
        <span class="eyebrow label">Из этой же категории</span>
        <h2>Смотрится <em>вместе</em></h2>
      </div>
      <a class="link-arrow" href="catalog.html">Весь каталог {arrow}</a>
    </div>
    <div class="cgrid" id="related-grid"></div>
  </div>
</section>
</main>

<div class="modal" id="quick" role="dialog" aria-modal="true" aria-label="Быстрый просмотр">
  <div class="modal__backdrop"></div>
  <div class="modal__box"></div>
</div>
"""


# ============================ ABOUT ============================
ABOUT = """
<main>
<section class="phero">
  <div class="phero__bg"></div>
  <div class="container">
    <nav class="crumbs" aria-label="Хлебные крошки">
      <a href="index.html">Главная</a><span>/</span><span style="color:var(--ink)">О бренде</span>
    </nav>
    <h1>Косметика<br>с <em>характером</em></h1>
    <div class="phero__sub">
      <p>L'ATUAGE cosmetic — белорусский производитель декоративной косметики.
      С 2014 года мы делаем продукты, которые не приходится «дотягивать» кистью и фантазией.</p>
      <span class="badge-round"><i></i>ЧТУП «ДЮПАМ КОСМЕТИК» · Минск</span>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="container">
    <div class="split split--reverse">
      <div class="plate" style="--tint:#f7d7d4;aspect-ratio:1/1">
        <span class="plate__idx">12 лет</span>
        <img src="assets/img/products/pomada-inred.webp" alt="Помада L'ATUAGE in Red" loading="lazy">
        <span class="plate__cap">Помада in Red · флагман линейки</span>
      </div>
      <div>
        <span class="eyebrow label">Наша идея</span>
        <p class="statement">Мы верим, что хороший макияж — это не про «дорого», а про <em>точность формулы</em> и уважение к человеку перед зеркалом.</p>
        <p class="u-dim u-mt-24">Бренд вырос из оптовой компании, которая знала рынок изнутри:
        какие текстуры реально покупают, а какие остаются лежать на полке. Поэтому в L'ATUAGE сначала
        появляется задача покупателя — и только потом флакон.</p>
        <div class="facts u-mt-40">
          <div class="fact"><b data-count="300" data-suffix="+">300+</b><span>наименований</span></div>
          <div class="fact"><b data-count="500" data-suffix="+">500+</b><span>магазинов</span></div>
          <div class="fact"><b data-count="6">6</b><span>стран</span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--tight" id="production">
  <div class="container">
    <div class="section-head">
      <div>
        <span class="eyebrow label">Производство</span>
        <h2>Полный цикл —<br><em>в одном месте</em></h2>
      </div>
      <p class="u-dim" style="max-width:34ch;font-size:14px">Разработка, тестирование, производство и логистика — внутри компании. Так мы отвечаем за каждый этап.</p>
    </div>
    <div class="steps">
      <div class="step reveal"><b>01</b><h3>Исследование</h3><p>Тренд-аналитика и обратная связь от 500+ точек продаж.</p></div>
      <div class="step reveal" style="--d:1"><b>02</b><h3>Формула</h3><p>Собственная лаборатория: текстуры, пигменты, стойкость.</p></div>
      <div class="step reveal" style="--d:2"><b>03</b><h3>Производство</h3><p>Полный цикл: смешивание, фасовка, маркировка, контроль партии.</p></div>
      <div class="step reveal" style="--d:3"><b>04</b><h3>Логистика</h3><p>Доставка и мерчандайзинг в шести странах присутствия.</p></div>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="container">
    <div class="mosaic">
      <figure style="--tint:#e9e3d8"><img src="assets/img/products/teni-smart-touch.webp" alt="Палетка Smart Touch" loading="lazy"></figure>
      <figure style="--tint:#f7d7d4"><img src="assets/img/products/blesk-gub.webp" alt="Блеск для губ" loading="lazy"></figure>
      <figure style="--tint:#f1e4c3"><img src="assets/img/products/pudra-mineral.webp" alt="Пудра Mineral Balance" loading="lazy"></figure>
      <figure style="--tint:#dee3d4"><img src="assets/img/products/lak-effect.webp" alt="Лак Effect" loading="lazy"></figure>
      <figure style="--tint:#e4ddeb"><img src="assets/img/products/tush-full-hd.webp" alt="Тушь Full HD" loading="lazy"></figure>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <div>
        <span class="eyebrow label">История</span>
        <h2>Как всё <em>начиналось</em></h2>
      </div>
    </div>
    <div class="history">
      <div class="hrow reveal"><b>2014</b><div><h3>Первый каталог</h3></div><p>Компания выходит на рынок декоративной косметики с собственной торговой маркой и первыми 30 продуктами.</p></div>
      <div class="hrow reveal" style="--d:1"><b>2017</b><div><h3>Собственное производство</h3></div><p>Запуск полного цикла в Минске: от разработки формулы до фасовки и контроля качества.</p></div>
      <div class="hrow reveal" style="--d:2"><b>2019</b><div><h3>Выход за пределы Беларуси</h3></div><p>Партнёрская сеть расширяется до 300 магазинов в России, Казахстане и Украине.</p></div>
      <div class="hrow reveal" style="--d:3"><b>2022</b><div><h3>Минеральная линейка</h3></div><p>Запуск Mineral Balance — рассыпчатые пудры и бронзеры, которые стали хитами.</p></div>
      <div class="hrow reveal" style="--d:4"><b>2025</b><div><h3>Новая коллекция Liquid Metal</h3></div><p>Моно-тени с эффектом жидкого металла и обновлённый визуальный язык бренда.</p></div>
    </div>
  </div>
</section>

<section class="section quotes">
  <div class="container">
    <p class="quote-big">«Наша задача — чтобы косметика <em>не подводила</em> в самый важный день».</p>
    <p class="u-center u-dim u-mt-24" style="font-size:12px;letter-spacing:.16em;text-transform:uppercase">Команда L'ATUAGE cosmetic</p>
  </div>
</section>

<section class="section cta">
  <div class="container">
    <div class="cta__inner">
      <div>
        <span class="eyebrow label" style="color:rgba(244,239,232,.5)">Сотрудничество</span>
        <h2>Хотите <em>продавать L'ATUAGE</em>?</h2>
        <p>Расскажите о вашем магазине — пришлём условия, прайс и маркетинговые материалы.</p>
      </div>
      <div style="display:flex;gap:12px;flex-wrap:wrap">
        <a class="btn btn--light" href="contacts.html#wholesale"><span>Стать партнёром</span>{arrow}</a>
        <a class="btn btn--light" href="catalog.html"><span>Каталог</span></a>
      </div>
    </div>
  </div>
</section>
</main>
"""


# ============================ CONTACTS ============================
CONTACTS = """
<main>
<section class="phero">
  <div class="phero__bg"></div>
  <div class="container">
    <nav class="crumbs" aria-label="Хлебные крошки">
      <a href="index.html">Главная</a><span>/</span><span style="color:var(--ink)">Контакты</span>
    </nav>
    <h1>Давайте <em>поговорим</em></h1>
    <div class="phero__sub">
      <p>Вопрос по продукту, оптовая заявка или предложение о сотрудничестве —
      выберите удобный способ связи. Отвечаем в течение рабочего дня.</p>
      <span class="badge-round"><i></i>Пн–Пт · 9:00–18:00 (Минск)</span>
    </div>
  </div>
</section>

<section class="section section--tight" id="where">
  <div class="container">
    <div class="contact">
      <div>
        <span class="eyebrow label">Головной офис</span>
        <h2 style="font-size:clamp(28px,3.4vw,44px);margin-bottom:18px">Минск,<br>ул. Ложинская, 14</h2>
        <ul class="contact__list">
          <li><span class="k">Адрес</span><span class="v">220114, Республика Беларусь,<br>г. Минск, ул. Ложинская, 14, офис 23</span></li>
          <li><span class="k">Телефон</span><span class="v"><a href="tel:+375173962311">+375 (17) 396-23-11</a></span></li>
          <li><span class="k">Факс</span><span class="v">+375 (17) 396-23-12</span></li>
          <li><span class="k">E-mail</span><span class="v"><a href="mailto:info@latuage.com">info@latuage.com</a></span></li>
          <li><span class="k">Соцсети</span><span class="v"><a href="https://www.instagram.com/latuage_cosmetic/" target="_blank" rel="noopener">Instagram</a> · <a href="https://www.facebook.com/latuagecosmetic" target="_blank" rel="noopener">Facebook</a> · <a href="https://vk.com/latuage" target="_blank" rel="noopener">VK</a></span></li>
        </ul>
      </div>
      <form class="form" data-fake>
        <div>
          <label for="f-name">Имя</label>
          <input id="f-name" name="name" required placeholder="Как к вам обращаться">
        </div>
        <div>
          <label for="f-phone">Телефон</label>
          <input id="f-phone" name="phone" type="tel" placeholder="+375">
        </div>
        <div class="form__full">
          <label for="f-email">E-mail</label>
          <input id="f-email" name="email" type="email" required placeholder="you@example.com">
        </div>
        <div class="form__full">
          <label for="f-topic">Тема</label>
          <select id="f-topic" name="topic">
            <option>Вопрос о продукте</option>
            <option>Оптовая закупка</option>
            <option>Стать партнёром / представителем</option>
            <option>Сотрудничество с блогером</option>
            <option>Другое</option>
          </select>
        </div>
        <div class="form__full">
          <label for="f-msg">Сообщение</label>
          <textarea id="f-msg" name="message" placeholder="Расскажите, чем мы можем помочь"></textarea>
        </div>
        <button class="btn btn--red" type="submit"><span>Отправить</span>{arrow}</button>
        <span class="form__ok" data-ok></span>
      </form>
    </div>
  </div>
</section>

<section class="section stores" id="wholesale">
  <div class="container">
    <div class="stores__inner">
      <div>
        <span class="eyebrow label">Бизнес-клиентам</span>
        <h2>Опт и <em>представительство</em></h2>
        <p class="u-dim" style="max-width:46ch">Работаем с магазинами косметики, сетями и маркетплейсами.
        Предоставляем тестеры, консультации по выкладке и маркетинговые материалы.</p>
        <ul class="split__list">
          <li><b>01</b><span>Минимальная партия — один короб</span></li>
          <li><b>02</b><span>Отгрузка со склада в Минске за 3–7 дней</span></li>
          <li><b>03</b><span>Тестеры и POS-материалы в комплекте</span></li>
          <li><b>04</b><span>Персональный менеджер и обучение персонала</span></li>
        </ul>
        <a class="btn btn--red u-mt-24" href="mailto:info@latuage.com"><span>Запросить прайс</span>{arrow}</a>
      </div>
      <div class="stores__map">
        {map_svg}
      </div>
    </div>
  </div>
</section>

<section class="section" id="faq">
  <div class="container">
    <div class="section-head">
      <div>
        <span class="eyebrow label">FAQ</span>
        <h2>Частые <em>вопросы</em></h2>
      </div>
    </div>
    <div class="acc">
      <div class="acc__item">
        <button class="acc__btn">Где купить продукцию L'ATUAGE? <i></i></button>
        <div class="acc__panel"><div>Продукция представлена более чем в 500 магазинах Беларуси, России, Казахстана,
        Украины, Молдовы и Польши. Напишите нам — подскажем ближайшую точку в вашем городе.</div></div>
      </div>
      <div class="acc__item">
        <button class="acc__btn">Продукция тестируется на животных? <i></i></button>
        <div class="acc__panel"><div>Нет. Мы не тестируем готовую продукцию и компоненты на животных
        и выбираем поставщиков сырья с соответствующей политикой.</div></div>
      </div>
      <div class="acc__item">
        <button class="acc__btn">Подходит ли косметика для чувствительной кожи? <i></i></button>
        <div class="acc__panel"><div>Большинство формул не содержат спирта и прошли дерматологический контроль.
        Для склонной к реакциям кожи рекомендуем минеральную линейку и органические туши.</div></div>
      </div>
      <div class="acc__item">
        <button class="acc__btn">Можно ли купить продукт напрямую у производителя? <i></i></button>
        <div class="acc__panel"><div>Да, для оптовых заказов. Для розничной покупки удобнее обратиться
        к партнёрам бренда или на маркетплейсы, где представлен ассортимент.</div></div>
      </div>
      <div class="acc__item">
        <button class="acc__btn">Как стать представителем в своём городе? <i></i></button>
        <div class="acc__panel"><div>Заполните форму выше с темой «Стать партнёром» — менеджер свяжется с вами,
        расскажет об условиях и поможет с первой поставкой.</div></div>
      </div>
    </div>
  </div>
</section>
</main>
"""


# ============================ RUN ============================
ARROW_LEFT = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
              'stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M11 18l-6-6 6-6"/></svg>')
STAR = ('<svg viewBox="0 0 24 24"><path d="m12 2 2.9 6.3 6.9.8-5.1 4.7 1.4 6.8L12 17.3 5.9 20.6l1.4-6.8L2.2 9.1l6.9-.8L12 2Z"/></svg>')
STARS = STAR * 5

MAP_SVG = """<svg viewBox="0 0 520 420" role="img" aria-label="География продаж L'ATUAGE">
  <defs>
    <pattern id="mapgrid" width="26" height="26" patternUnits="userSpaceOnUse">
      <path d="M26 0H0v26" fill="none" stroke="rgba(23,18,15,.08)" stroke-width="1"/>
    </pattern>
  </defs>
  <rect width="520" height="420" fill="url(#mapgrid)"/>
  <g stroke="rgba(23,18,15,.3)" stroke-width="1" stroke-dasharray="3 6" fill="none">
    <path d="M196 232 98 148"/><path d="M196 232 352 118"/><path d="M196 232 262 300"/>
    <path d="M196 232 150 340"/><path d="M196 232 438 250"/>
  </g>
  <g class="map-node" font-family="JetBrains Mono, monospace" font-size="11" letter-spacing=".12em" fill="rgba(23,18,15,.62)">
    <circle cx="98" cy="148" r="4" fill="#17120f"/><text x="98" y="132" text-anchor="middle">ВАРШАВА</text>
    <circle cx="352" cy="118" r="4" fill="#17120f"/><text x="352" y="102" text-anchor="middle">МОСКВА</text>
    <circle cx="262" cy="300" r="4" fill="#17120f"/><text x="262" y="324" text-anchor="middle">КИЕВ</text>
    <circle cx="150" cy="340" r="4" fill="#17120f"/><text x="150" y="364" text-anchor="middle">КИШИНЁВ</text>
    <circle cx="438" cy="250" r="4" fill="#17120f"/><text x="438" y="234" text-anchor="middle">АЛМАТЫ</text>
  </g>
  <g>
    <circle cx="196" cy="232" r="26" fill="rgba(210,33,44,.10)" class="map-ping"/>
    <circle cx="196" cy="232" r="7" fill="#d2212c"/>
    <circle cx="196" cy="232" r="2.4" fill="#fff"/>
    <text x="196" y="200" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="11"
          font-weight="700" letter-spacing=".14em" fill="#d2212c">МИНСК</text>
  </g>
  <g font-family="JetBrains Mono, monospace" font-size="10" letter-spacing=".1em" fill="rgba(23,18,15,.4)">
    <text x="24" y="396">500+ ТОЧЕК ПРОДАЖ</text>
    <text x="496" y="396" text-anchor="end">6 СТРАН</text>
  </g>
</svg>"""

SUB = dict(arrow=ARROW, arrow_left=ARROW_LEFT, stars=STARS, map_svg=MAP_SVG, search_icon=ICONS['search'])

page(
    'index.html',
    "L'ATUAGE COSMETIC — белорусская декоративная косметика",
    "Официальный сайт L'ATUAGE cosmetic: 300+ наименований декоративной косметики, 500+ магазинов по СНГ, "
    "производство полного цикла в Минске. Без спирта, стойкость до 24 часов.",
    INDEX.format(**SUB),
)

page(
    'catalog.html',
    "Каталог — L'ATUAGE COSMETIC",
    "Каталог L'ATUAGE cosmetic: тени, туши, помады, пудры, лаки и аксессуары. Фильтр по категориям и поиск.",
    CATALOG.format(**SUB),
    active='catalog.html',
)

page(
    'product.html',
    "Продукт — L'ATUAGE COSMETIC",
    "Подробная карточка продукта L'ATUAGE cosmetic: описание, оттенки и характеристики.",
    PRODUCT.format(**SUB),
    active='catalog.html',
)

page(
    'about.html',
    "О бренде — L'ATUAGE COSMETIC",
    "L'ATUAGE cosmetic — белорусский производитель декоративной косметики с 2014 года: "
    "собственные формулы, производство полного цикла в Минске, 500+ магазинов.",
    ABOUT.format(**SUB),
    active='about.html',
)

page(
    'contacts.html',
    "Контакты — L'ATUAGE COSMETIC",
    "Контакты L'ATUAGE cosmetic: Минск, ул. Ложинская, 14. Телефон +375 (17) 396-23-11, e-mail info@latuage.com. "
    "Опт и представительство, вопросы и ответы.",
    CONTACTS.format(**SUB),
    active='contacts.html',
)
