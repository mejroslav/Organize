# Organize

(Written in Czech language.)

Tento jednoduchý skript umožňuje rozřadit soubory podle jejich přípon (`.pdf`, `.mp3`, ...) a přesouvat je do domovských složek (`$HOME/Documents`, `$HOME/Audios`, ...). Je užitečný třeba pro automatické rozřazování souborů ze složky `Downloads`.

---

## Použití

Přípony jednotlivých souborů se nastavují v souboru `extensions.json`. Cesty do složek, kam se mají soubory přesouvat, se nastavují v souboru `paths.json`.

`python3 main.py` spustí program pro přesouvání.