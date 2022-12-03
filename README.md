# Organize

Tento jednoduchý pythonovský skript umožňuje rozřadit soubory podle jejich typu (obrázek, audio, video, dokument, ...) a přesouvat je do domovských složek. Užitečný třeba pro automatické rozřazování souborů ze složky "Downloads".

Root složku **do** které se mají soubory třídit si uživatel může zvolit pomocí `--root`, defaultní je `cwd`.
Konfigurační soubor nalinkujeme pomocí `--config`.
Lze pustit jako `--dry-run`, kdy nebudou provedeny žádné změny, pouze se vypíše co by se skript pokusil udělat.