from __future__ import annotations

import pathlib
from typing import Iterable

from PIL import Image


def iter_source_images(root: pathlib.Path) -> Iterable[pathlib.Path]:
    """Yield source images (JPEG/PNG) recursively under root."""
    for path in root.rglob("*"):
        if path.suffix.lower() in {".jpg", ".jpeg", ".png"}:
            yield path


def to_webp(source: pathlib.Path) -> pathlib.Path:
    """Return the destination path for the WebP version of source."""
    return source.with_suffix(".webp")


def needs_update(source: pathlib.Path, dest: pathlib.Path) -> bool:
    """Return True if dest is missing or older than source."""
    if not dest.exists():
        return True
    return source.stat().st_mtime > dest.stat().st_mtime


def convert_image(source: pathlib.Path, dest: pathlib.Path) -> None:
    """Convert source to WebP and write it to dest."""
    with Image.open(source) as img:
        img.load()

        save_kwargs = {"method": 6}

        if source.suffix.lower() in {".png"}:
            # PNGs often contain transparency; keep them lossless.
            save_kwargs.update({"lossless": True})
        else:
            if img.mode in {"P", "LA"}:
                img = img.convert("RGBA")
            elif img.mode in {"L", "CMYK"}:
                img = img.convert("RGB")

            save_kwargs.update({"quality": 85, "optimize": True})

        dest.parent.mkdir(parents=True, exist_ok=True)
        img.save(dest, format="WEBP", **save_kwargs)


def main() -> None:
    root = pathlib.Path(__file__).parents[1] / "assets" / "images"

    for source in iter_source_images(root):
        dest = to_webp(source)
        if needs_update(source, dest):
            convert_image(source, dest)


if __name__ == "__main__":
    main()
