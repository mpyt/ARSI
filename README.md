# Video Frame Extractor

Skript pro extrakci snímků z videa podle zadaného sample rate.

## Instalace
```bash
pip install opencv-python
```

## Použití

V souboru `extract_frames.py` uprav proměnné:

- `VIDEO_PATH` — cesta k videu
- `OUTPUT_DIR` — výstupní složka
- `SAMPLE_RATE` — každý N-tý snímek (např. 30 = 1 fotka/s při 30 FPS)

Spuštění:
```bash
python extract_frames.py
```

## Výstup

Snímky se uloží do `frames/<název_videa>/` jako JPEG soubory.
