/* L'ATUAGE COSMETIC — interactions */
(function () {
  'use strict';

  const $ = (sel, ctx = document) => ctx.querySelector(sel);
  const $$ = (sel, ctx = document) => [...ctx.querySelectorAll(sel)];
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------------- loader ---------------- */
  function initLoader() {
    const loader = $('.loader');
    document.body.classList.add('is-loaded');
    if (!loader) return;
    const done = () => {
      loader.classList.add('is-done');
      document.body.classList.add('is-loaded');
      setTimeout(() => loader.remove(), 1400);
    };
    if (document.readyState === 'complete') setTimeout(done, 700);
    else window.addEventListener('load', () => setTimeout(done, 550));
    setTimeout(done, 2600);
  }

  /* ---------------- header ---------------- */
  function initHeader() {
    const header = $('.header');
    if (!header) return;
    const onScroll = () => {
      header.classList.toggle('is-stuck', window.scrollY > 24);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });

    const burger = $('.burger');
    const menu = $('.menu');
    if (burger && menu) {
      const toggle = (open) => {
        menu.classList.toggle('is-open', open);
        document.body.classList.toggle('no-scroll', open);
        burger.setAttribute('aria-expanded', open);
        $$('.menu__list a', menu).forEach((a, i) => {
          a.style.transitionDelay = open ? `${80 + i * 55}ms` : '0ms';
        });
      };
      burger.addEventListener('click', () => toggle(!menu.classList.contains('is-open')));
      $$('a', menu).forEach((a) => a.addEventListener('click', () => toggle(false)));
      const close = $('.menu-close');
      if (close) close.addEventListener('click', () => toggle(false));
      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') toggle(false);
      });
    }
  }

  /* ---------------- scroll progress + to top ---------------- */
  function initScrollUI() {
    const bar = $('.progress');
    const top = $('.to-top');
    const onScroll = () => {
      const h = document.documentElement;
      const max = h.scrollHeight - h.clientHeight;
      if (bar) bar.style.transform = `scaleX(${max > 0 ? h.scrollTop / max : 0})`;
      if (top) top.classList.toggle('is-visible', h.scrollTop > 700);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
    if (top) top.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
  }

  /* ---------------- reveal on scroll ---------------- */
  function initReveal() {
    const items = $$('.reveal, .reveal-img, [data-count]');
    if (!items.length) return;
    if (!('IntersectionObserver' in window) || reduce) {
      items.forEach((el) => el.classList.add('is-in'));
      $$('[data-count]').forEach((el) => (el.textContent = el.dataset.count));
      return;
    }
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          const el = entry.target;
          el.classList.add('is-in');
          if (el.dataset.count) countUp(el);
          io.unobserve(el);
        });
      },
      { rootMargin: '0px 0px -8% 0px', threshold: 0.12 }
    );
    items.forEach((el) => io.observe(el));
  }

  function countUp(el) {
    const target = parseFloat(el.dataset.count);
    const suffix = el.dataset.suffix || '';
    const dur = 1500;
    const start = performance.now();
    const step = (now) => {
      const p = Math.min(1, (now - start) / dur);
      const eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(target * eased) + suffix;
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  }

  /* ---------------- marquee ---------------- */
  function initMarquee() {
    $$('.marquee').forEach((m) => {
      const track = $('.marquee__track', m);
      if (!track || track.dataset.dup) return;
      track.innerHTML += track.innerHTML;
      track.dataset.dup = '1';
    });
  }

  /* ---------------- draggable rails ---------------- */
  function initDragScroll(el) {
    if (!el) return;
    let down = false, startX = 0, startLeft = 0, moved = false;
    el.addEventListener('pointerdown', (e) => {
      down = true; moved = false;
      startX = e.clientX;
      startLeft = el.scrollLeft;
      el.classList.add('is-dragging');
    });
    el.addEventListener('pointermove', (e) => {
      if (!down) return;
      const dx = e.clientX - startX;
      if (Math.abs(dx) > 4) moved = true;
      el.scrollLeft = startLeft - dx;
    });
    const up = () => {
      down = false;
      el.classList.remove('is-dragging');
    };
    el.addEventListener('pointerup', up);
    el.addEventListener('pointerleave', up);
    el.addEventListener('click', (e) => {
      if (moved) {
        e.preventDefault();
        e.stopPropagation();
      }
    }, true);
  }

  function initRailNav() {
    $$('[data-rail]').forEach((wrap) => {
      const rail = $('.rail, .textures__track', wrap);
      if (!rail) return;
      const prev = $('[data-rail-prev]', wrap);
      const next = $('[data-rail-next]', wrap);
      const step = () => Math.max(rail.clientWidth * 0.7, 240);
      if (prev) prev.addEventListener('click', () => rail.scrollBy({ left: -step(), behavior: 'smooth' }));
      if (next) next.addEventListener('click', () => rail.scrollBy({ left: step(), behavior: 'smooth' }));
      const update = () => {
        const max = rail.scrollWidth - rail.clientWidth - 4;
        if (prev) prev.disabled = rail.scrollLeft <= 4;
        if (next) next.disabled = rail.scrollLeft >= max;
      };
      update();
      rail.addEventListener('scroll', update, { passive: true });
      window.addEventListener('resize', update);
    });
  }

  /* ---------------- cursor ---------------- */
  function initCursor() {
    if (window.matchMedia('(hover: none)').matches || reduce) return;
    const dot = document.createElement('div');
    dot.className = 'cursor';
    document.body.appendChild(dot);
    let tx = 0, ty = 0, cx = 0, cy = 0;
    window.addEventListener('pointermove', (e) => {
      tx = e.clientX; ty = e.clientY;
      dot.classList.add('is-active');
    });
    (function loop() {
      cx += (tx - cx) * 0.18;
      cy += (ty - cy) * 0.18;
      dot.style.transform = `translate(${cx}px, ${cy}px) translate(-50%, -50%)`;
      requestAnimationFrame(loop);
    })();
    document.addEventListener('pointerover', (e) => {
      const hit = e.target.closest('a, button, .pcard, .cat, .look, input, select, textarea');
      dot.classList.toggle('is-hover', !!hit);
    });
  }

  /* ---------------- hero parallax ---------------- */
  function initHeroParallax() {
    const hero = $('.hero');
    if (!hero || reduce || window.matchMedia('(hover: none)').matches) return;
    const layers = $$('[data-depth]', hero);
    let raf = null;
    hero.addEventListener('pointermove', (e) => {
      const r = hero.getBoundingClientRect();
      const nx = (e.clientX - r.left) / r.width - 0.5;
      const ny = (e.clientY - r.top) / r.height - 0.5;
      if (raf) return;
      raf = requestAnimationFrame(() => {
        layers.forEach((el) => {
          const d = parseFloat(el.dataset.depth) || 10;
          el.style.transform = `translate3d(${-nx * d}px, ${-ny * d}px, 0)`;
        });
        raf = null;
      });
    });
  }

  /* ---------------- favorites ---------------- */
  const FAV_KEY = 'latuage_favs';
  const getFavs = () => {
    try { return JSON.parse(localStorage.getItem(FAV_KEY) || '[]'); } catch { return []; }
  };
  const setFavs = (list) => {
    localStorage.setItem(FAV_KEY, JSON.stringify(list));
    $$('[data-fav-count]').forEach((el) => {
      el.textContent = list.length;
      el.style.display = list.length ? '' : 'none';
    });
  };
  function initFavs() {
    setFavs(getFavs());
    document.addEventListener('click', (e) => {
      const btn = e.target.closest('[data-fav]');
      if (!btn) return;
      e.preventDefault();
      e.stopPropagation();
      const id = btn.dataset.fav;
      const list = getFavs();
      const i = list.indexOf(id);
      if (i > -1) list.splice(i, 1); else list.push(id);
      setFavs(list);
      btn.classList.toggle('is-on', i === -1);
    });
    $$('[data-fav]').forEach((btn) => {
      btn.classList.toggle('is-on', getFavs().includes(btn.dataset.fav));
    });
  }

  /* ---------------- product card ---------------- */
  function cardHTML(p, i) {
    const tint = (window.TINT && window.TINT[p.cat]) || '#efe0d9';
    const shades = (p.shades || []).slice(0, 4)
      .map((c) => `<i style="background:${c}"></i>`).join('');
    const badge = p.badge
      ? `<span class="pcard__badge ${p.badge === 'new' ? 'pcard__badge--red' : ''}">${p.badge}</span>`
      : '';
    const favOn = getFavs().includes(p.id);
    return `
      <article class="pcard reveal" style="--tint:${tint};--d:${i % 4}">
        <a class="pcard__media" href="product.html?id=${p.id}" aria-label="${p.name}">
          ${badge}
          <button class="pcard__fav ${favOn ? 'is-on' : ''}" data-fav="${p.id}" aria-label="В избранное">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 20s-7-4.35-7-9a4 4 0 0 1 7-2.65A4 4 0 0 1 19 11c0 4.65-7 9-7 9Z"/></svg>
          </button>
          <img src="${p.img}" alt="${p.name}" loading="lazy" width="600" height="600">
          <button class="pcard__quick" data-quick="${p.id}">Быстрый просмотр</button>
        </a>
        <div class="pcard__body">
          <span class="pcard__cat">${window.CAT_NAME[p.cat] || ''}</span>
          <h3 class="pcard__name"><a href="product.html?id=${p.id}">${p.name}</a></h3>
          <div class="pcard__row">
            <div class="pcard__shades">${shades}<span>${p.shades ? p.shades.length : 0} оттенков</span></div>
            <span class="pcard__go">Смотреть</span>
          </div>
        </div>
      </article>`;
  }

  /* ---------------- quick view ---------------- */
  function initQuickView() {
    const modal = $('#quick');
    if (!modal) return;
    const box = $('.modal__box', modal);
    const open = (id) => {
      const p = window.PRODUCTS.find((x) => x.id === id);
      if (!p) return;
      const tint = (window.TINT && window.TINT[p.cat]) || '#efe0d9';
      box.innerHTML = `
        <button class="modal__close" aria-label="Закрыть">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="m6 6 12 12M18 6 6 18"/></svg>
        </button>
        <div class="modal__grid">
          <div class="modal__media" style="--tint:${tint}"><img src="${p.img}" alt="${p.name}"></div>
          <div>
            <span class="pdp__cat">${window.CAT_NAME[p.cat] || ''}</span>
            <h3 style="font-size:clamp(26px,3vw,38px);margin-bottom:12px">${p.name}</h3>
            <p class="u-dim" style="font-size:14px;margin-bottom:20px">${p.desc}</p>
            <div class="swatches" style="margin-bottom:22px">
              ${(p.shades || []).map((c, i) => `<button class="swatch ${i === 0 ? 'is-active' : ''}" style="background:${c}" aria-label="Оттенок ${i + 1}"></button>`).join('')}
            </div>
            <div class="pdp__actions">
              <a class="btn btn--red" href="product.html?id=${p.id}"><span>Подробнее</span>
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
              </a>
              <button class="btn btn--ghost" data-fav="${p.id}"><span>В избранное</span></button>
            </div>
          </div>
        </div>`;
      modal.classList.add('is-open');
      document.body.classList.add('no-scroll');
      $('.modal__close', box).addEventListener('click', close);
    };
    const close = () => {
      modal.classList.remove('is-open');
      document.body.classList.remove('no-scroll');
    };
    $('.modal__backdrop', modal).addEventListener('click', close);
    document.addEventListener('keydown', (e) => e.key === 'Escape' && close());
    document.addEventListener('click', (e) => {
      const btn = e.target.closest('[data-quick]');
      if (!btn) return;
      e.preventDefault();
      open(btn.dataset.quick);
    });
  }

  /* ---------------- catalog ---------------- */
  function initCatalog() {
    const grid = $('#catalog-grid');
    if (!grid) return;
    const params = new URLSearchParams(location.search);
    let state = {
      cat: params.get('cat') || 'all',
      q: '',
      sort: 'default'
    };

    const countEl = $('#catalog-count');
    const chips = $$('.chip[data-cat]');

    const apply = () => {
      let list = window.PRODUCTS.slice();
      if (state.cat !== 'all') list = list.filter((p) => p.cat === state.cat);
      if (state.q) {
        const q = state.q.toLowerCase();
        list = list.filter((p) => (p.name + ' ' + p.sub + ' ' + (window.CAT_NAME[p.cat] || '')).toLowerCase().includes(q));
      }
      if (state.sort === 'name') list.sort((a, b) => a.name.localeCompare(b.name, 'ru'));
      if (state.sort === 'new') list.sort((a, b) => (b.badge === 'new') - (a.badge === 'new'));
      grid.innerHTML = list.length
        ? list.map(cardHTML).join('')
        : `<div class="empty" style="grid-column:1/-1"><h3>Ничего не нашлось</h3><p>Попробуйте другой запрос или категорию.</p></div>`;
      if (countEl) countEl.textContent = `${list.length} ${plural(list.length, ['продукт', 'продукта', 'продуктов'])}`;
      $$('.reveal', grid).forEach((el) => el.classList.add('is-in'));
      initFavs();
    };

    chips.forEach((chip) => {
      chip.classList.toggle('is-active', chip.dataset.cat === state.cat);
      chip.addEventListener('click', () => {
        state.cat = chip.dataset.cat;
        chips.forEach((c) => c.classList.toggle('is-active', c === chip));
        history.replaceState(null, '', state.cat === 'all' ? 'catalog.html' : `catalog.html?cat=${state.cat}`);
        apply();
      });
    });

    const search = $('#catalog-search');
    if (search) {
      let t;
      search.addEventListener('input', () => {
        clearTimeout(t);
        t = setTimeout(() => { state.q = search.value.trim(); apply(); }, 160);
      });
    }
    const sort = $('#catalog-sort');
    if (sort) sort.addEventListener('change', () => { state.sort = sort.value; apply(); });

    apply();
  }

  function plural(n, forms) {
    const n10 = n % 10, n100 = n % 100;
    if (n10 === 1 && n100 !== 11) return forms[0];
    if (n10 >= 2 && n10 <= 4 && (n100 < 10 || n100 >= 20)) return forms[1];
    return forms[2];
  }

  /* ---------------- home rails ---------------- */
  function initHomeRails() {
    const best = $('#rail-best');
    if (best) {
      const picks = ['pomada-inred', 'tush-5d', 'pudra-mineral', 'teni-smart-touch', 'pomada-bematte', 'konsiler', 'lak-cream', 'highlighter-loose'];
      best.innerHTML = picks
        .map((id, i) => cardHTML(window.PRODUCTS.find((p) => p.id === id), i))
        .join('');
      $$('.reveal', best).forEach((el) => el.classList.add('is-in'));
    }
    const fresh = $('#rail-new');
    if (fresh) {
      fresh.innerHTML = window.PRODUCTS
        .filter((p) => p.badge === 'new')
        .slice(0, 8)
        .map(cardHTML)
        .join('');
      $$('.reveal', fresh).forEach((el) => el.classList.add('is-in'));
    }
  }

  /* ---------------- product page ---------------- */
  function initProductPage() {
    const root = $('#pdp');
    if (!root) return;
    const id = new URLSearchParams(location.search).get('id');
    const p = window.PRODUCTS.find((x) => x.id === id) || window.PRODUCTS[0];
    const tint = (window.TINT && window.TINT[p.cat]) || '#efe0d9';
    const catName = window.CAT_NAME[p.cat] || '';

    document.title = `${p.name} — L'ATUAGE COSMETIC`;
    $('#crumb-cat').textContent = catName;
    $('#crumb-cat').href = `catalog.html?cat=${p.cat}`;
    $('#crumb-name').textContent = p.name;

    root.innerHTML = `
      <div class="pdp__gallery">
        <div class="pdp__main reveal-img" style="--tint:${tint}">
          <img src="${p.img}" alt="${p.name}" id="pdp-img">
        </div>
        <div class="pdp__thumbs">
          ${(p.shades || []).slice(0, 4).map((c, i) => `
            <button class="${i === 0 ? 'is-active' : ''}" data-shade="${c}" aria-label="Оттенок ${i + 1}">
              <span style="display:block;width:100%;aspect-ratio:1;border-radius:50%;background:${c}"></span>
            </button>`).join('')}
        </div>
      </div>
      <div class="pdp__info">
        <span class="pdp__cat">${catName}</span>
        <h1>${p.name}</h1>
        <p class="pdp__desc">${p.desc}</p>
        <div class="pdp__block">
          <h4>Оттенки · ${(p.shades || []).length}</h4>
          <div class="swatches">
            ${(p.shades || []).map((c, i) => `<button class="swatch ${i === 0 ? 'is-active' : ''}" style="background:${c}" data-shade="${c}" aria-label="Оттенок ${i + 1}"></button>`).join('')}
          </div>
        </div>
        <div class="pdp__block">
          <h4>Характеристики</h4>
          <div class="pdp__specs">
            ${Object.entries(p.specs || {}).map(([k, v]) => `<div><dt>${k}</dt><dd>${v}</dd></div>`).join('')}
          </div>
        </div>
        <div class="pdp__actions">
          <a class="btn btn--red" href="contacts.html#where"><span>Где купить</span>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
          </a>
          <button class="btn btn--ghost" data-fav="${p.id}"><span>В избранное</span></button>
        </div>
        <p class="pdp__note">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 3 4 7v6c0 4 3.5 6.5 8 8 4.5-1.5 8-4 8-8V7l-8-4Z"/></svg>
          Официальный продукт L'ATUAGE cosmetic · сертифицировано в Республике Беларусь
        </p>
      </div>`;

    root.addEventListener('click', (e) => {
      const sw = e.target.closest('[data-shade]');
      if (!sw) return;
      $$('.swatch, .pdp__thumbs button', root).forEach((b) => b.classList.remove('is-active'));
      sw.classList.add('is-active');
    });

    const related = $('#related-grid');
    if (related) {
      const list = window.PRODUCTS.filter((x) => x.cat === p.cat && x.id !== p.id).slice(0, 4);
      related.innerHTML = list.map(cardHTML).join('');
      $$('.reveal', related).forEach((el) => el.classList.add('is-in'));
    }
    initFavs();
  }

  /* ---------------- accordion ---------------- */
  function initAccordion() {
    $$('.acc__item').forEach((item) => {
      const btn = $('.acc__btn', item);
      const panel = $('.acc__panel', item);
      if (!btn || !panel) return;
      btn.addEventListener('click', () => {
        const open = item.classList.contains('is-open');
        $$('.acc__item.is-open').forEach((o) => o.classList.remove('is-open'));
        if (!open) item.classList.add('is-open');
      });
    });
  }


  /* ---------------- подбор оттенка ---------------- */
  function initShades() {
    const root = $('[data-shadex]');
    if (!root) return;
    const groups = [
      { label: 'Губы', pid: 'pomada-inred' },
      { label: 'Глаза', pid: 'teni-smart-touch' },
      { label: 'Лицо', pid: 'pudra-smart' },
      { label: 'Руки', pid: 'lak-cream' }
    ]
      .map((g) => ({ ...g, product: window.PRODUCTS.find((p) => p.id === g.pid) }))
      .filter((g) => g.product);
    if (!groups.length) return;

    const tabsEl = $('[data-shadex-tabs]', root);
    const swEl = $('[data-shadex-sw]', root);
    const stage = $('[data-shadex-stage]', root);
    const img = $('[data-shadex-img]', root);
    const nameEl = $('[data-shadex-name]', root);
    const prodEl = $('[data-shadex-prod]', root);
    const finEl = $('[data-shadex-fin]', root);
    const holdEl = $('[data-shadex-hold]', root);
    const link = $('[data-shadex-link]', root);

    const HOLD = { eyes: 'до 24 часов', lips: 'до 8 часов', face: 'весь день', hands: 'до 10 дней' };
    let gi = 0;
    let si = 0;

    const renderTabs = () => {
      tabsEl.innerHTML = groups
        .map((g, i) => `<button type="button" data-g="${i}" class="${i === gi ? 'is-active' : ''}">${g.label}</button>`)
        .join('');
    };

    const renderSw = () => {
      const shades = groups[gi].product.shades || [];
      swEl.innerHTML = shades
        .map((c, i) => `<button type="button" data-s="${i}" class="${i === si ? 'is-active' : ''}" style="background:${c}" aria-label="Оттенок ${i + 1}"></button>`)
        .join('');
    };

    const apply = () => {
      const g = groups[gi];
      const shades = g.product.shades || [];
      const color = shades[si] || '#c2182a';
      stage.classList.add('is-swapping');
      setTimeout(() => {
        img.src = g.product.img;
        img.alt = g.product.name;
        stage.style.setProperty('--c', color);
        nameEl.textContent = `${g.label} · ${String(si + 1).padStart(2, '0')}`;
        prodEl.textContent = g.product.name;
        finEl.textContent = (g.product.specs && g.product.specs['Финиш']) || '—';
        holdEl.textContent = HOLD[g.product.cat] || 'весь день';
        link.href = `product.html?id=${g.product.id}`;
        stage.classList.remove('is-swapping');
      }, 160);
    };

    renderTabs();
    renderSw();

    root.addEventListener('click', (e) => {
      const tab = e.target.closest('[data-g]');
      if (tab) {
        gi = +tab.dataset.g;
        si = 0;
        renderTabs();
        renderSw();
        apply();
        return;
      }
      const sw = e.target.closest('[data-s]');
      if (sw) {
        si = +sw.dataset.s;
        renderSw();
        apply();
      }
    });
  }

  /* ---------------- forms ---------------- */
  function initForms() {
    $$('form[data-fake]').forEach((form) => {
      form.addEventListener('submit', (e) => {
        e.preventDefault();
        const ok = $('[data-ok]', form);
        const btn = $('button[type=submit]', form);
        if (btn) { btn.disabled = true; btn.style.opacity = '.6'; }
        if (ok) ok.textContent = 'Спасибо! Мы свяжемся с вами в течение рабочего дня.';
        form.reset();
        setTimeout(() => {
          if (btn) { btn.disabled = false; btn.style.opacity = ''; }
        }, 2500);
      });
    });
  }

  /* ---------------- init ---------------- */
  document.addEventListener('DOMContentLoaded', () => {
    initLoader();
    initHeader();
    initScrollUI();
    initMarquee();
    initHomeRails();
    initCatalog();
    initProductPage();
    initQuickView();
    initFavs();
    initReveal();
    initRailNav();
    $$('.rail, .textures__track').forEach(initDragScroll);
    initAccordion();
    initForms();
    initShades();
  });
})();
