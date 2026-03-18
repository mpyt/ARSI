# video_sample.py

Skript pro extrakci snímků z videa podle zadaného sample rate.

## Použití
Vstupní proměnné
- `VIDEO_PATH` - cesta k videu
- `OUTPUT_DIR` - výstupní složka
- `SAMPLE_RATE` - každý N-tý snímek (např. 30 = 1 fotka/s při 30 FPS)
## Výstup

Snímky se uloží do `frames/<název_videa>/` jako JPEG soubory.

# mask_windows.py

Skript pro maskování oken pomocí polygonů z .json souboru vytvořeného pomocí labelme.

## Použití
Vstupní proměnné
- `INPUT_PATH` - cesta k fotce, nebo celé složce s fotkami
- `JSON_PATH` - cesta k hlavnímu .jsonu souboru
- `OUTPUT_DIR` - cesta k výstupní složce pro zpracované soubory 
- `COLOR` - nastavení pomocí RGB barvu masky
- `OUTPUT_SUFFIX` - suffix pro zpracované soubory