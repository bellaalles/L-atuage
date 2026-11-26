"""Тело главной страницы."""
INDEX = """
<main id="top">

<section class="hero grain">
  <div class="hero__bg"></div>
  <div class="hero__ghost" aria-hidden="true">L'ATUAGE</div>
  <div class="container">
    <div class="hero__inner">
      <div class="hero__copy">
        <span class="badge-round"><i></i>Сделано в Беларуси · с 2014</span>
        <h1>
          <span class="line"><span>Красиво.</span></span>
          <span class="line"><span>Честно.</span></span>
          <span class="line"><span><em>На 24 часа.</em></span></span>
        </h1>
        <p class="hero__text">L'ATUAGE cosmetic — белорусская декоративная косметика полного цикла.
        Более 300 наименований, собственные формулы и стойкость, которой доверяют визажисты.</p>
        <div class="hero__cta">
          <a class="btn btn--red" href="catalog.html"><span>Смотреть каталог</span>{arrow}</a>
          <a class="btn btn--ghost" href="about.html"><span>О бренде</span></a>
        </div>
        <div class="hero__meta">
          <div><strong data-count="300" data-suffix="+">300+</strong><span>наименований</span></div>
          <div><strong data-count="500" data-suffix="+">500+</strong><span>магазинов</span></div>
          <div><strong data-count="12">12</strong><span>лет на рынке</span></div>
        </div>
      </div>

      <div class="hero__visual">
        <div class="hero__frame" data-depth="10">
          <img src="assets/img/photos/hero-portrait.webp" alt="Макияж L'ATUAGE: красная помада и выразительный взгляд" width="800" height="1000" fetchpriority="high">
        </div>
        <div class="hero__float hero__float--a" data-depth="34"><img src="assets/img/products/pomada-inred.webp" alt="Помада in Red"></div>
        <div class="hero__float hero__float--b" data-depth="46"><img src="assets/img/products/tush-5d.webp" alt="Тушь Panoramic Eyes 5D"></div>
        <div class="hero__float hero__float--c" data-depth="26"><img src="assets/img/products/pudra-smart.webp" alt="Пудра Smart Touch"></div>
        <div class="hero__badge" data-depth="-16"><span>24 часа<small>стойкость</small></span></div>
      </div>
    </div>
  </div>
  <div class="hero__scroll" aria-hidden="true"><span>листай</span><i></i></div>
</section>

<div class="ticker">
  <div class="marquee" style="--dur:42s">
    <div class="marquee__track">
      <span>Liquid Metal</span><span>BE chic</span><span>Smart Touch</span><span>Mineral Balance</span><span>Strobing</span><span>Full HD</span>
    </div>
  </div>
</div>

<section class="stats">
  <div class="container">
    <div class="stats__grid">
      <div class="stats__item"><b data-count="500" data-suffix="+">500+</b><span>магазинов-партнёров</span></div>
      <div class="stats__item"><b data-count="300" data-suffix="+">300+</b><span>наименований в каталоге</span></div>
      <div class="stats__item"><b data-count="12">12</b><span>лет на рынке</span></div>
      <div class="stats__item"><b data-count="6">6</b><span>стран присутствия</span></div>
    </div>
  </div>
</section>

<section class="section" id="collections">
  <div class="container">
    <div class="section-head">
      <div>
        <span class="eyebrow label">01 — Коллекции</span>
        <h2>Выбери свою <em>территорию</em></h2>
      </div>
      <a class="link-arrow" href="catalog.html">Весь каталог {arrow}</a>
    </div>

    <div class="cats__grid">
      <a class="cat reveal" href="catalog.html?cat=eyes" style="--tint:#e6c9c1">
        <div class="cat__top"><span class="cat__idx">01</span><span class="cat__count">21 продукт</span></div>
        <div class="cat__img"><img src="assets/img/products/teni-mysterious.webp" alt="Тени для век"></div>
        <div class="cat__foot">
          <div><h3>Глаза</h3><p>Тени, туши, подводки</p></div>
          <span class="cat__arrow">{arrow}</span>
        </div>
      </a>
      <a class="cat reveal" href="catalog.html?cat=lips" style="--tint:#efc9c6;--d:1">
        <div class="cat__top"><span class="cat__idx">02</span><span class="cat__count">7 продуктов</span></div>
        <div class="cat__img"><img src="assets/img/products/pomada-inred.webp" alt="Помада"></div>
        <div class="cat__foot">
          <div><h3>Губы</h3><p>Помады, блески, бальзамы</p></div>
          <span class="cat__arrow">{arrow}</span>
        </div>
      </a>
      <a class="cat reveal" href="catalog.html?cat=face" style="--tint:#f0dcc9;--d:2">
        <div class="cat__top"><span class="cat__idx">03</span><span class="cat__count">18 продуктов</span></div>
        <div class="cat__img"><img src="assets/img/products/pudra-smart.webp" alt="Пудра"></div>
        <div class="cat__foot">
          <div><h3>Лицо</h3><p>Тон, пудры, хайлайтеры</p></div>
          <span class="cat__arrow">{arrow}</span>
        </div>
      </a>
      <a class="cat reveal" href="catalog.html?cat=hands" style="--tint:#e2d5cf;--d:3">
        <div class="cat__top"><span class="cat__idx">04</span><span class="cat__count">10 продуктов</span></div>
        <div class="cat__img"><img src="assets/img/products/lak-cream.webp" alt="Лак для ногтей"></div>
        <div class="cat__foot">
          <div><h3>Руки</h3><p>Лаки и уход</p></div>
          <span class="cat__arrow">{arrow}</span>
        </div>
      </a>
    </div>
  </div>
</section>

<section class="section section--tight" style="padding-top:0">
  <div class="container">
    <div class="section-head">
      <div>
        <span class="eyebrow label">02 — Хиты</span>
        <h2>То, что <em>покупают снова</em></h2>
      </div>
      <div class="rail-nav" data-rail>
        <button class="rail-btn" data-rail-prev aria-label="Назад">{arrow_left}</button>
        <button class="rail-btn" data-rail-next aria-label="Вперёд">{arrow}</button>
      </div>
    </div>
  </div>
  <div class="container" data-rail>
    <div class="rail" id="rail-best"></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="split">
      <div class="split__media reveal-img">
        <img src="assets/img/photos/makeup-apply.webp" alt="Визажист наносит макияж L'ATUAGE" loading="lazy">
        <div class="split__tag">
          <b>100%</b>
          <span>собственное производство в Минске — от идеи до витрины</span>
        </div>
      </div>
      <div>
        <span class="eyebrow label">03 — Производство</span>
        <h2>Свои формулы.<br><em>Своя лаборатория.</em></h2>
        <p>Мы не перепродаём чужое. Каждая формула разрабатывается и тестируется в Минске,
        а партия проходит контроль качества до того, как попадёт на полку.</p>
        <ul class="split__list">
          <li><b>01</b><span>Разработка формулы и подбор пигментов</span></li>
          <li><b>02</b><span>Дерматологический контроль и тесты на стойкость</span></li>
          <li><b>03</b><span>Производство полного цикла на одной площадке</span></li>
          <li><b>04</b><span>Логистика в 500+ магазинов СНГ</span></li>
        </ul>
        <a class="btn btn--ghost u-mt-24" href="about.html"><span>Как мы работаем</span>{arrow}</a>
      </div>
    </div>
  </div>
</section>

<section class="section features grain">
  <div class="container">
    <div class="section-head">
      <div>
        <span class="eyebrow label">04 — Принципы</span>
        <h2 style="color:#f4efe8">Четыре вещи,<br>за которые <em style="color:#e8cfc6">мы отвечаем</em></h2>
      </div>
      <p style="max-width:34ch;color:rgba(244,239,232,.55);font-size:14px">Мы сознательно не гонимся за «вау-составом» на упаковке. Только то, что реально работает на коже.</p>
    </div>
    <div class="features__grid">
      <div class="feature reveal">
        <svg viewBox="0 0 32 32"><path d="M16 4c4 4 7 8 7 12a7 7 0 0 1-14 0c0-4 3-8 7-12Z"/><path d="M16 12v10"/></svg>
        <h3>Без спирта</h3>
        <p>Формулы без агрессивных растворителей — не сушат кожу и не оставляют белых пятен.</p>
      </div>
      <div class="feature reveal" style="--d:1">
        <svg viewBox="0 0 32 32"><circle cx="16" cy="16" r="11"/><path d="M16 10v6l4 2"/></svg>
        <h3>24 часа стойкости</h3>
        <p>Макияж, который доживает до конца дня: без отпечатков на чашке и осыпания.</p>
      </div>
      <div class="feature reveal" style="--d:2">
        <svg viewBox="0 0 32 32"><path d="M16 4 6 9v7c0 6 4.4 10 10 12 5.6-2 10-6 10-12V9L16 4Z"/><path d="m12 16 3 3 6-6"/></svg>
        <h3>Дерматологический контроль</h3>
        <p>Каждая партия проходит тесты — продукт подходит для чувствительной кожи.</p>
      </div>
      <div class="feature reveal" style="--d:3">
        <svg viewBox="0 0 32 32"><path d="M11 20c-3 0-5-2-5-5s2-5 5-5c1-3 4-5 7-5 4 0 7 3 7 7 2 .5 3 2 3 4 0 2.5-2 4-4 4H11Z"/><circle cx="12" cy="15" r="1"/><circle cx="19" cy="14" r="1"/></svg>
        <h3>Без тестов на животных</h3>
        <p>Не тестируем продукцию на животных и выбираем ответственных поставщиков сырья.</p>
      </div>
    </div>
  </div>
</section>
"""

INDEX += """
<section class="section lookbook">
  <div class="container">
    <div class="lookbook__head">
      <div>
        <span class="eyebrow label">05 — Лукбук</span>
        <h2 style="font-size:clamp(32px,4.6vw,62px)">Пять настроений <em style="font-style:italic;color:var(--red)">одной палеткой</em></h2>
      </div>
      <div class="rail-nav" data-rail>
        <span class="drag-hint">Тяни<i></i></span>
        <button class="rail-btn" data-rail-prev aria-label="Назад">{arrow_left}</button>
        <button class="rail-btn" data-rail-next aria-label="Вперёд">{arrow}</button>
      </div>
    </div>
  </div>
  <div data-rail>
    <div class="lookbook__track">
      <figure class="look">
        <img src="assets/img/photos/spa.webp" alt="Неоновый лук" loading="lazy">
        <figcaption class="look__cap"><h3>Neon Muse</h3><span>Metal Show</span></figcaption>
      </figure>
      <div class="look look--text">
        <span class="label" style="opacity:.7">Look 01</span>
        <div><h3>Собери свой оттенок</h3><p>Смешивай, наслаивай, экспериментируй — формулы это позволяют.</p></div>
        <a class="link-arrow" href="catalog.html" style="border-color:rgba(255,255,255,.5);color:#fff">В каталог {arrow}</a>
      </div>
      <figure class="look">
        <img src="assets/img/photos/look-bluenight.webp" alt="Синий свет" loading="lazy">
        <figcaption class="look__cap"><h3>Blue Hour</h3><span>Liquid Metal</span></figcaption>
      </figure>
      <figure class="look">
        <img src="assets/img/photos/look-lavender.webp" alt="Спокойный образ" loading="lazy">
        <figcaption class="look__cap"><h3>Soft Focus</h3><span>Perfect Skin</span></figcaption>
      </figure>
      <figure class="look">
        <img src="assets/img/photos/look-sheer.webp" alt="Вечерний образ" loading="lazy">
        <figcaption class="look__cap"><h3>After Dark</h3><span>Mysterious Eyes</span></figcaption>
      </figure>
      <figure class="look">
        <img src="assets/img/photos/nails.webp" alt="Маникюр" loading="lazy">
        <figcaption class="look__cap"><h3>Nail Story</h3><span>Smart Nails</span></figcaption>
      </figure>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="container">
    <div class="section-head">
      <div>
        <span class="eyebrow label">06 — Путь продукта</span>
        <h2>От идеи до <em>витрины</em></h2>
      </div>
    </div>
    <div class="steps">
      <div class="step reveal"><b>01 / Идея</b><h3>Тренд-ресёрч</h3><p>Смотрим на подиумы, соцсети и запросы покупателей — выбираем, что действительно нужно.</p></div>
      <div class="step reveal" style="--d:1"><b>02 / Формула</b><h3>Лаборатория</h3><p>Технологи подбирают текстуру, пигменты и консерванты под задачу продукта.</p></div>
      <div class="step reveal" style="--d:2"><b>03 / Производство</b><h3>Своя площадка</h3><p>Полный цикл в Минске: смешивание, фасовка, маркировка, контроль партии.</p></div>
      <div class="step reveal" style="--d:3"><b>04 / Витрина</b><h3>500+ магазинов</h3><p>Логистика и мерчандайзинг: продукт приезжает готовым к продаже.</p></div>
    </div>
  </div>
</section>

<section class="section quotes" id="journal">
  <div class="container">
    <div class="section-head">
      <div>
        <span class="eyebrow label">07 — Журнал</span>
        <h2>Читать <em>перед покупкой</em></h2>
      </div>
      <a class="link-arrow" href="#">Все статьи {arrow}</a>
    </div>
    <div class="journal__grid">
      <a class="post reveal" href="#">
        <div class="post__media reveal-img"><img src="assets/img/photos/eyeliner.webp" alt="Стрелки" loading="lazy"></div>
        <div class="post__meta"><em>Гид</em><span>12 ноября 2025</span></div>
        <h3>Стрелки без права на ошибку: 4 способа для новичков</h3>
        <p>Разбираем подводки и фломастеры L'ATUAGE — какая форма линии получается с каждым.</p>
      </a>
      <a class="post reveal" href="#" style="--d:1">
        <div class="post__media reveal-img"><img src="assets/img/photos/lips-flowers.webp" alt="Помады" loading="lazy"></div>
        <div class="post__meta"><em>Тренды</em><span>28 октября 2025</span></div>
        <h3>Красный — новый нюд: как выбрать свой оттенок</h3>
        <p>Тёплый, холодный, винный — показываем на реальных примерах, как подобрать красную помаду.</p>
      </a>
      <a class="post reveal" href="#" style="--d:2">
        <div class="post__media reveal-img"><img src="assets/img/photos/dropper-white.webp" alt="Сыворотка" loading="lazy"></div>
        <div class="post__meta"><em>Уход</em><span>10 октября 2025</span></div>
        <h3>Сыворотка, тоник, пудра: правильный порядок слоёв</h3>
        <p>Как уход и макияж сочетаются, чтобы тон держался до вечера.</p>
      </a>
    </div>
  </div>
</section>

<section class="section section--tight quotes">
  <div class="container">
    <div class="section-head">
      <div>
        <span class="eyebrow label">08 — Отзывы</span>
        <h2>Что говорят <em>о нас</em></h2>
      </div>
      <span class="badge-round"><i></i>4.8 из 5 · 1 200+ отзывов</span>
    </div>
    <div class="quotes__grid">
      <figure class="quote reveal">
        <div class="quote__stars">{stars}</div>
        <blockquote>«Кто спрашивал о помаде? Это #LATUAGECOSMETIC №108 — бюджетная и офигенная. Она уже в блоге».</blockquote>
        <figcaption><img src="assets/img/photos/look-lavender.webp" alt=""><div><b>@rysichka_makeup</b>Instagram</div></figcaption>
      </figure>
      <figure class="quote reveal" style="--d:1">
        <div class="quote__stars">{stars}</div>
        <blockquote>«Скоро обзор теней от L'ATUAGE. Все тени и тестеры в наличии — в Минске больше нигде нет этой косметики».</blockquote>
        <figcaption><img src="assets/img/photos/warm-portrait.webp" alt=""><div><b>@kolesnikova_elena</b>Instagram</div></figcaption>
      </figure>
      <figure class="quote reveal" style="--d:2">
        <div class="quote__stars">{stars}</div>
        <blockquote>«Плотность и пигмент как у люкса, а цена — как у масс-маркета. Мои клиентки возвращаются именно за этим».</blockquote>
        <figcaption><img src="assets/img/photos/look-bluenight.webp" alt=""><div><b>Инна Леута</b>Арт-директор «Академия Стиля»</div></figcaption>
      </figure>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="container">
    <div class="section-head">
      <div>
        <span class="eyebrow label">09 — Сообщество</span>
        <h2>#latuagecosmetic</h2>
      </div>
      <a class="link-arrow" href="https://www.instagram.com/latuage_cosmetic/" target="_blank" rel="noopener">Мы в Instagram {arrow}</a>
    </div>
    <div class="insta">
      <a href="https://www.instagram.com/latuage_cosmetic/" target="_blank" rel="noopener"><img src="assets/img/photos/smile-red.webp" alt="" loading="lazy"></a>
      <a href="https://www.instagram.com/latuage_cosmetic/" target="_blank" rel="noopener"><img src="assets/img/photos/afro-glow.webp" alt="" loading="lazy"></a>
      <a href="https://www.instagram.com/latuage_cosmetic/" target="_blank" rel="noopener"><img src="assets/img/photos/makeup-apply.webp" alt="" loading="lazy"></a>
      <a href="https://www.instagram.com/latuage_cosmetic/" target="_blank" rel="noopener"><img src="assets/img/photos/pink-back.webp" alt="" loading="lazy"></a>
      <a href="https://www.instagram.com/latuage_cosmetic/" target="_blank" rel="noopener"><img src="assets/img/photos/dropper-white.webp" alt="" loading="lazy"></a>
      <a href="https://www.instagram.com/latuage_cosmetic/" target="_blank" rel="noopener"><img src="assets/img/photos/dark-portrait.webp" alt="" loading="lazy"></a>
    </div>
  </div>
</section>

<section class="section stores">
  <div class="container">
    <div class="stores__inner">
      <div>
        <span class="eyebrow label">10 — Где купить</span>
        <h2>500+ магазинов<br><em>в шести странах</em></h2>
        <p class="u-dim" style="max-width:44ch">Беларусь, Россия, Казахстан, Украина, Молдова и Польша.
        Ищем партнёров в новых городах — пишите, если у вас есть магазин.</p>
        <div class="stores__legend">
          <span><b>210</b>Беларусь</span><span><b>160</b>Россия</span><span><b>64</b>Казахстан</span>
          <span><b>42</b>Украина</span><span><b>18</b>Молдова</span><span><b>12</b>Польша</span>
        </div>
        <div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:28px">
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
  <div class="cta__bg"><img src="assets/img/photos/afro-glow.webp" alt="" loading="lazy"></div>
  <div class="container">
    <div class="cta__inner">
      <div>
        <span class="eyebrow label" style="color:rgba(244,239,232,.5)">Новинки первыми</span>
        <h2>Не пропусти <em>новые коллекции</em></h2>
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
