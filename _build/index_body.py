"""Тело главной страницы."""

INDEX = """
<main id="top">

<section class="hero">
  <div class="hero__inner">
    <div class="hero__text">
      <span class="hero__kicker">Минск · собственное производство · с 2014 года</span>
      <h1>
        <span>Декоративная</span>
        <span>косметика</span>
        <span class="hero__accent">без компромиссов</span>
      </h1>
      <p class="hero__lead">300+ наименований собственного производства. Формулы,
      которые держатся до 24 часов и не требуют «дотягивания» кистью.</p>
      <div class="hero__cta">
        <a class="btn btn--light" href="catalog.html"><span>Смотреть каталог</span>{arrow}</a>
        <a class="btn btn--outline-light" href="about.html"><span>О бренде</span></a>
      </div>
      <ul class="hero__facts">
        <li><b data-count="300" data-suffix="+">300+</b><span>наименований</span></li>
        <li><b data-count="500" data-suffix="+">500+</b><span>магазинов</span></li>
        <li><b data-count="6">6</b><span>стран</span></li>
      </ul>
    </div>
    <div class="hero__media">
      <img src="assets/img/photos/look-sheer.webp" alt="Бьюти-образ L'ATUAGE" fetchpriority="high">
      <span class="hero__tag">In Red · флагманская помада</span>
      <a class="hero__card" href="product.html?id=pomada-inred">
        <span class="hero__card-img"><img src="assets/img/products/pomada-inred.webp" alt="Помада in Red" loading="lazy"></span>
        <span class="hero__card-txt"><small>Флагман</small><b>Помада in Red</b><i>5 оттенков</i></span>
      </a>
    </div>
  </div>
</section>

<div class="shelf">
  <a class="shelf__item" href="catalog.html?cat=eyes" style="--tint:#e7dfd0">
    <span class="shelf__idx">01</span>
    <img src="assets/img/products/teni-mysterious.webp" alt="Тени для век" fetchpriority="high">
    <span class="shelf__meta"><b>Глаза</b><i>21 продукт</i></span>
  </a>
  <a class="shelf__item" href="catalog.html?cat=lips" style="--tint:#f0dbd7">
    <span class="shelf__idx">02</span>
    <img src="assets/img/products/pomada-inred.webp" alt="Помада">
    <span class="shelf__meta"><b>Губы</b><i>7 продуктов</i></span>
  </a>
  <a class="shelf__item" href="catalog.html?cat=face" style="--tint:#efe6cf">
    <span class="shelf__idx">03</span>
    <img src="assets/img/products/pudra-smart.webp" alt="Пудра">
    <span class="shelf__meta"><b>Лицо</b><i>18 продуктов</i></span>
  </a>
  <a class="shelf__item" href="catalog.html?cat=hands" style="--tint:#e2e6db">
    <span class="shelf__idx">04</span>
    <img src="assets/img/products/lak-cream.webp" alt="Лак для ногтей">
    <span class="shelf__meta"><b>Руки</b><i>10 продуктов</i></span>
  </a>
</div>

<div class="ticker">
  <div class="marquee" style="--dur:46s">
    <div class="marquee__track">
      <span>Liquid Metal</span><span>BE chic</span><span>Smart Touch</span><span>Mineral Balance</span>
      <span>Strobing</span><span>Full HD</span><span>Mysterious Eyes</span><span>Perfect Skin</span>
    </div>
  </div>
</div>

<section class="section" id="best">
  <div class="container">
    <div class="section-head">
      <div>
        <span class="label">01 / Хиты</span>
        <h2>Покупают <em>снова и снова</em></h2>
      </div>
      <div class="rail-nav">
        <button class="rail-btn" data-rail-prev aria-label="Назад">{arrow_left}</button>
        <button class="rail-btn" data-rail-next aria-label="Вперёд">{arrow}</button>
      </div>
    </div>
  </div>
  <div class="container" data-rail>
    <div class="rail" id="rail-best"></div>
  </div>
</section>


<section class="section" id="looks">
  <div class="container">
    <div class="section-head">
      <div>
        <span class="label">02 / Образы</span>
        <h2>Три образа <em>одной коллекции</em></h2>
      </div>
      <p class="u-dim" style="max-width:32ch;font-size:14px;margin:0">
        Каждый образ собран из продуктов L'ATUAGE — от базы до финального блика.
      </p>
    </div>
  </div>
  <div class="container">
    <div class="looks">
      <a class="look reveal" href="catalog.html?cat=lips">
        <img src="assets/img/photos/warm-portrait.webp" alt="Образ с тёплым нюдом" loading="lazy">
        <span class="look__cap"><b>Тёплый нюд</b><span>Губы</span></span>
      </a>
      <a class="look reveal" href="catalog.html?cat=eyes" style="--d:1">
        <img src="assets/img/photos/makeup-apply.webp" alt="Образ со стрелками" loading="lazy">
        <span class="look__cap"><b>Тонкая стрелка</b><span>Глаза</span></span>
      </a>
      <a class="look reveal" href="catalog.html?cat=face" style="--d:2">
        <img src="assets/img/photos/hero-portrait.webp" alt="Образ со светящейся кожей" loading="lazy">
        <span class="look__cap"><b>Сияние кожи</b><span>Лицо</span></span>
      </a>
    </div>
  </div>
</section>

<section class="section" id="manifest">
  <div class="container">
    <div class="ed">
      <div class="ed__media">
        <img src="assets/img/photos/bw-portrait.webp" alt="Бьюти-съёмка L'ATUAGE" loading="lazy">
      </div>
      <div class="ed__body">
        <span class="label">03 / Манифест</span>
        <h2>Красота <span class="dash"></span> это<br><em>уверенность</em>,<br>а не маска</h2>
        <p>Мы делаем косметику для реальной жизни: плотные пигменты, которые
        не осыпаются, текстуры, которые не требуют ретуши, и оттенки, которые
        подходят с первого раза.</p>
        <p>Каждая партия собирается в Минске на собственном производстве —
        от первого пигмента до последней крышки.</p>
        <span class="ed__sign">L'Atuage, с 2014 года</span>
        <a class="btn btn--ghost" href="about.html"><span>О бренде</span>{arrow}</a>
      </div>
    </div>
  </div>
</section>

<section class="section" id="formula">
  <div class="container">
    <div class="formula">
      <div class="formula__lead">
        <span class="label">04 / Формула</span>
        <h2>Что внутри <span class="dash"></span><br><em>то и на коже</em></h2>
        <p>Мы не гонимся за «вау-составом» на упаковке. В формулах только то,
        что реально работает: пигмент, текстура и стойкость, проверенные лабораторией.</p>
        <a class="btn btn--ghost" href="about.html#production"><span>О производстве</span>{arrow}</a>
      </div>
      <div class="specs">
        <div class="spec"><span>Спирт</span><b class="is-no">Не содержится</b></div>
        <div class="spec"><span>Стойкость</span><b>До 24 часов</b></div>
        <div class="spec"><span>Дерматологический контроль</span><b>Каждая партия</b></div>
        <div class="spec"><span>Тесты на животных</span><b class="is-no">Не проводятся</b></div>
        <div class="spec"><span>Производство</span><b>Минск, Беларусь</b></div>
        <div class="spec"><span>Сертификация</span><b>Республика Беларусь</b></div>
      </div>
    </div>
  </div>
</section>

<section class="section" id="shades">
  <div class="container">
    <div class="section-head">
      <div>
        <span class="label">05 / Оттенки</span>
        <h2>Подбери оттенок <em>за пару кликов</em></h2>
      </div>
      <p class="u-dim" style="max-width:30ch;font-size:14px;margin:0">Четыре семейства оттенков — от нюдовых до винных. Нажмите на цвет, чтобы увидеть продукт.</p>
    </div>
  </div>
  <div class="shadex" data-shadex>
    <div class="shadex__stage" data-shadex-stage style="--c:#c2182a">
      <img data-shadex-img src="assets/img/products/pomada-inred.webp" alt="Помада in Red">
      <span class="shadex__name" data-shadex-name>Губы · 01</span>
    </div>
    <div class="shadex__panel">
      <div class="shadex__tabs" data-shadex-tabs></div>
      <div class="shadex__sw" data-shadex-sw></div>
      <dl class="shadex__info">
        <div><dt>Продукт</dt><dd data-shadex-prod>Помада in Red</dd></div>
        <div><dt>Финиш</dt><dd data-shadex-fin>Сатиновый</dd></div>
        <div><dt>Стойкость</dt><dd data-shadex-hold>до 8 часов</dd></div>
      </dl>
      <a class="btn btn--red" data-shadex-link href="product.html?id=pomada-inred"><span>Смотреть продукт</span>{arrow}</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="split">
      <div class="plate" style="--tint:#e9e3d8">
        <span class="plate__idx">100%</span>
        <img src="assets/img/products/teni-smart-touch.webp" alt="Палетка L'ATUAGE Smart Touch" loading="lazy">
        <span class="plate__cap">Палетка Smart Touch · 12 оттенков</span>
      </div>
      <div>
        <span class="label">06 / Производство</span>
        <h2 style="margin-top:16px">Свои формулы.<br><em>Своя лаборатория.</em></h2>
        <p>Мы не перепродаём чужое. Каждая формула разрабатывается и тестируется в Минске,
        а партия проходит контроль качества до того, как попадёт на полку.</p>
        <ul class="split__list">
          <li><b>01</b><span>Разработка формулы и подбор пигментов</span></li>
          <li><b>02</b><span>Дерматологический контроль и тесты на стойкость</span></li>
          <li><b>03</b><span>Производство полного цикла на одной площадке</span></li>
          <li><b>04</b><span>Логистика в 500+ магазинов СНГ</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section textures" style="padding-inline:0">
  <div class="container">
    <div class="section-head">
      <div>
        <span class="label">07 / Витрина</span>
        <h2>Вся палитра <em>на одном экране</em></h2>
      </div>
      <div class="rail-nav">
        <span class="drag-hint">Тяни<i></i></span>
        <button class="rail-btn" data-rail-prev aria-label="Назад">{arrow_left}</button>
        <button class="rail-btn" data-rail-next aria-label="Вперёд">{arrow}</button>
      </div>
    </div>
  </div>
  <div data-rail>
    <div class="textures__track">
      <figure class="texture" style="--tint:#f7d7d4"><img src="assets/img/products/pomada-inred.webp" alt="Помада in Red" loading="lazy"><figcaption><b>Помада in Red</b><span>Губы</span></figcaption></figure>
      <figure class="texture" style="--tint:#e9e3d8"><img src="assets/img/products/teni-metal-show.webp" alt="Тени Liquid Metal" loading="lazy"><figcaption><b>Тени Liquid Metal</b><span>Глаза</span></figcaption></figure>
      <figure class="texture" style="--tint:#f1e4c3"><img src="assets/img/products/pudra-smart.webp" alt="Пудра Smart Touch" loading="lazy"><figcaption><b>Пудра Smart Touch</b><span>Лицо</span></figcaption></figure>
      <figure class="texture" style="--tint:#dee3d4"><img src="assets/img/products/lak-cream.webp" alt="Лак Cream" loading="lazy"><figcaption><b>Лак Cream</b><span>Руки</span></figcaption></figure>
      <figure class="texture" style="--tint:#e4ddeb"><img src="assets/img/products/blesk-gub.webp" alt="Блеск для губ" loading="lazy"><figcaption><b>Блеск для губ</b><span>Губы</span></figcaption></figure>
      <figure class="texture" style="--tint:#efe6dc"><img src="assets/img/products/tush-5d.webp" alt="Тушь Panoramic Eyes 5D" loading="lazy"><figcaption><b>Тушь 5D</b><span>Глаза</span></figcaption></figure>
      <figure class="texture" style="--tint:#f3e8d6"><img src="assets/img/products/highlighter-liquid.webp" alt="Хайлайтер" loading="lazy"><figcaption><b>Хайлайтер Liquid</b><span>Лицо</span></figcaption></figure>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <div>
        <span class="label">08 / Как это делается</span>
        <h2>От идеи до <em>витрины</em></h2>
      </div>
      <a class="link-arrow" href="about.html">Подробнее о бренде {arrow}</a>
    </div>
    <div class="steps">
      <div class="step reveal"><b>01 / Идея</b><h3>Тренд-ресёрч</h3><p>Смотрим на подиумы, соцсети и запросы покупателей — выбираем, что действительно нужно.</p></div>
      <div class="step reveal" style="--d:1"><b>04 / Формула</b><h3>Лаборатория</h3><p>Технологи подбирают текстуру, пигменты и консерванты под задачу продукта.</p></div>
      <div class="step reveal" style="--d:2"><b>03 / Производство</b><h3>Своя площадка</h3><p>Полный цикл в Минске: смешивание, фасовка, маркировка, контроль партии.</p></div>
      <div class="step reveal" style="--d:3"><b>04 / Витрина</b><h3>500+ магазинов</h3><p>Логистика и мерчандайзинг: продукт приезжает готовым к продаже.</p></div>
    </div>
  </div>
</section>

<section class="section" id="journal">
  <div class="container">
    <div class="section-head">
      <div>
        <span class="label">09 / Журнал</span>
        <h2>Читать <em>перед покупкой</em></h2>
      </div>
      <a class="link-arrow" href="journal.html">Все статьи {arrow}</a>
    </div>
    <div class="journal__grid">
      <a class="post reveal" href="article.html?id=strelki">
        <div class="post__media"><img src="assets/img/photos/makeup-apply.webp" alt="Макияж L'ATUAGE" loading="lazy"></div>
        <div class="post__meta"><em>Гид</em><span>12 ноября 2025</span></div>
        <h3>Стрелки без права на ошибку: 4 способа для новичков</h3>
        <p>Разбираем подводки и фломастеры L'ATUAGE — какая форма линии получается с каждым.</p>
      </a>
      <a class="post reveal" href="article.html?id=krasnyj" style="--d:1">
        <div class="post__media"><img src="assets/img/photos/look-lavender.webp" alt="Образ с помадой" loading="lazy"></div>
        <div class="post__meta"><em>Тренды</em><span>28 октября 2025</span></div>
        <h3>Красный <span class="dash"></span> новый нюд: как выбрать свой оттенок</h3>
        <p>Тёплый, холодный, винный — показываем, как подобрать красную помаду.</p>
      </a>
      <a class="post reveal" href="article.html?id=sloi" style="--d:2">
        <div class="post__media"><img src="assets/img/photos/pink-back.webp" alt="Бьюти-съёмка" loading="lazy"></div>
        <div class="post__meta"><em>Уход</em><span>10 октября 2025</span></div>
        <h3>Сыворотка, тоник, пудра: правильный порядок слоёв</h3>
        <p>Как уход и макияж сочетаются, чтобы тон держался до вечера.</p>
      </a>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="container">
    <div class="section-head">
      <div>
        <span class="label">10 / Отзывы</span>
        <h2>Что говорят <em>о нас</em></h2>
      </div>
      <span class="badge-round"><i></i>4.8 из 5 · 1 200+ отзывов</span>
    </div>
    <div class="quotes__grid">
      <figure class="quote reveal">
        <div class="quote__stars">{stars}</div>
        <blockquote>«Кто спрашивал о помаде? Это #LATUAGECOSMETIC №108 <span class="dash"></span> бюджетная и офигенная. Она уже в блоге».</blockquote>
        <figcaption><div><b>@rysichka_makeup</b>Instagram</div></figcaption>
      </figure>
      <figure class="quote reveal" style="--d:1">
        <div class="quote__stars">{stars}</div>
        <blockquote>«Скоро обзор теней от L'ATUAGE. Все тени и тестеры в наличии <span class="dash"></span> в Минске больше нигде нет этой косметики».</blockquote>
        <figcaption><div><b>@kolesnikova_elena</b>Instagram</div></figcaption>
      </figure>
      <figure class="quote reveal" style="--d:2">
        <div class="quote__stars">{stars}</div>
        <blockquote>«Плотность и пигмент как у люкса, а цена <span class="dash"></span> как у масс-маркета. Мои клиентки возвращаются именно за этим».</blockquote>
        <figcaption><div><b>Инна Леута</b>Арт-директор «Академия Стиля»</div></figcaption>
      </figure>
    </div>
  </div>
</section>

<section class="section stores" id="where">
  <div class="container">
    <div class="stores__inner">
      <div>
        <span class="label">11 / Где купить</span>
        <h2 style="margin-top:16px">500<span class="plus">+</span> магазинов<br><em>в шести странах</em></h2>
        <p>Беларусь, Россия, Казахстан, Украина, Молдова и Польша.
        Ищем партнёров в новых городах — пишите, если у вас есть магазин.</p>
        <div class="stores__legend">
          <span><b>210</b>Беларусь</span><span><b>160</b>Россия</span><span><b>64</b>Казахстан</span>
          <span><b>42</b>Украина</span><span><b>18</b>Молдова</span><span><b>12</b>Польша</span>
        </div>
        <div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:26px">
          <a class="btn btn--red" href="contacts.html#where"><span>Найти магазин</span>{arrow}</a>
          <a class="btn btn--ghost" href="contacts.html#wholesale"><span>Стать партнёром</span></a>
        </div>
      </div>
      <div class="stores__map">
        {map_svg}
      </div>
    </div>
  </div>
</section>

<section class="section cta">
  <div class="container">
    <div class="cta__inner">
      <div>
        <span class="label" style="color:rgba(255,255,255,.45)">Новинки первыми</span>
        <h2 style="margin-top:16px">Не пропусти <em>новые коллекции</em></h2>
        <p>Раз в месяц присылаем письмо: новые продукты, разборы оттенков и промокоды для подписчиков. Без спама.</p>
      </div>
      <form class="cta__form" data-fake>
        <div class="field">
          <input type="email" required placeholder="Ваш e-mail" aria-label="E-mail">
          <button type="submit" aria-label="Подписаться">{arrow}</button>
        </div>
        <span class="cta__note">Подписываясь, вы соглашаетесь с политикой конфиденциальности.</span>
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
