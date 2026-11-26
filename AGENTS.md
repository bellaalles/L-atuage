# AGENTS.md

## Что это
Статический концепт-редизайн latuage.com (L'ATUAGE cosmetic, Минск).

## Как собирается
`python3 _build/gen.py` — генерирует `index.html`, `catalog.html`,
`product.html`, `about.html`, `contacts.html` из шаблонов в `_build/`.
HTML руками не править: правки затрутся при следующей сборке.

- `_build/gen.py` — head, шапка, футер, общая обвязка страниц.
- `_build/index_body.py` — тело главной по секциям.

## Данные
`assets/js/data.js` — единственный источник товаров (60 позиций, id вида
`pomada-inred`). Карточка товара читает `?id=`, каталог — `?cat=`.

## Проверка
```bash
python3 -m http.server 8000
```
`assets/img/photos/` — 24 кадра для лайфстайл-блоков,
`assets/img/products/` — вырезанные продукты на прозрачном фоне.

## Правила
- Никаких внешних зависимостей и сборщиков: только HTML/CSS/JS.
- Токены дизайна — в `:root` в начале `assets/css/style.css`.
- Фото чужих брендов и процедурные стоки не использовать.
