"""Нормализация карточных фото товаров: одинаковая рамка 4:5, единый масштаб, резкость.

Запуск: python3 _build/enhance_products.py [--out DIR]
Без --out перезаписывает assets/img/products/*.webp (оригиналы остаются в git).
"""

import argparse
import pathlib
import sys

from PIL import Image, ImageFilter

RATIO = 4 / 5          # портретная рамка плитки
MARGIN = 0.08          # поля вокруг товара (8% от ограничивающей стороны)
MAX_SIDE = 1000
SHARPEN = ImageFilter.UnsharpMask(radius=1.2, percent=55, threshold=3)


def normalize(path: pathlib.Path, out_dir: pathlib.Path) -> tuple[pathlib.Path, float]:
    img = Image.open(path).convert("RGBA")
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)

    w, h = img.size
    canvas_w = max(w, h * RATIO) / (1 - 2 * MARGIN)
    canvas_h = canvas_w / RATIO

    scale = min(1.0, MAX_SIDE / max(canvas_w, canvas_h))
    canvas = Image.new("RGBA", (round(canvas_w * scale), round(canvas_h * scale)), (0, 0, 0, 0))

    if scale < 1.0:
        img = img.resize((round(w * scale), round(h * scale)), Image.LANCZOS)

    canvas.alpha_composite(img, ((canvas.width - img.width) // 2, (canvas.height - img.height) // 2))
    canvas = canvas.filter(SHARPEN)

    out = out_dir / path.name
    canvas.save(out, "WEBP", quality=92, method=4)
    return out, canvas.width / canvas.height


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="assets/img/products")
    args = ap.parse_args()

    src = pathlib.Path("assets/img/products")
    out_dir = pathlib.Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    files = sorted(src.glob("*.webp"))
    if not files:
        sys.exit("нет исходников в assets/img/products")

    for f in files:
        out, ratio = normalize(f, out_dir)
        print(f"{f.name:34} -> {out.name:34} 4:5")


if __name__ == "__main__":
    main()
