@echo off
REM Nastav kódování konzole na UTF-8, pokud je potřeba
chcp 65001

REM 0. Aktualizace pipu
echo Aktualizuji pip...
python -m pip install --upgrade pip

REM 1. Instalace závislostí (pokud existuje requirements.txt)
IF EXIST requirements.txt (
    echo Instalují se závislosti...
    pip install -r requirements.txt
) ELSE (
    echo Soubor requirements.txt nebyl nalezen, instalace závislostí se přeskočí.
)

REM 2. Spuštění hlavního programu
echo Spouštím hlavní program...
python main.py

pause