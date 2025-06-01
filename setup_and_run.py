import os
import sys
import subprocess
import threading
import time

def run_cmd(cmd, cwd=None):
    print(f"Spouštím: {cmd}")
    result = subprocess.run(cmd, shell=True, cwd=cwd)
    if result.returncode != 0:
        print(f"Chyba: {cmd}")
        sys.exit(1)

def setup_venv():
    # 1. Vytvoř virtuální prostředí
    if not os.path.exists("venv"):
        run_cmd("python -m venv venv")
    # 2. Aktivuj venv (pro další procesy)
    activate_script = "venv/Scripts/activate" if os.name == "nt" else "source venv/bin/activate"
    print(f"Aktivuj venv: {activate_script}")
    # 3. Nainstaluj závislosti
    run_cmd(f"{sys.executable} -m pip install --upgrade pip")
    run_cmd(f"{sys.executable} -m pip install -r requirements.txt")

def start_docker_astra():
    # 4. Spusť Docker kontejnery pro Astra DS (např. Cassandra)
    print("Spouštím Docker kontejnery pro Astra DS…")
    run_cmd("docker compose up -d", cwd="docker")

def start_storage():
    # 5. Inicializuj úložiště (případně napojení na Cassandra/Astra)
    print("Inicializuji úložiště…")
    # Pokud používáš např. SQLite:
    # import sqlite3; sqlite3.connect("data/cml.db").close()
    # Pokud Cassandra, předpokládáme, že je už spuštěná v Dockeru.
    time.sleep(5)  # počkej na start DB

def start_gui():
    # 6. Spusť GUI dashboard (asynchronně)
    print("Spouštím GUI dashboard…")
    def _run_gui():
        run_cmd(f"{sys.executable} main_dashboard.py")
    threading.Thread(target=_run_gui, daemon=True).start()
    time.sleep(2)  # počkej na GUI

def activate_openai():
    # 7. Napoj OpenAI (pokud je klíč v .env)
    from dotenv import load_dotenv
    load_dotenv()
    OPENAI_KEY = os.getenv("OPENAI_API_KEY")
    if OPENAI_KEY:
        print("OpenAI API aktivováno.")
    else:
        print("OpenAI API klíč nenalezen, běží pouze lokální engine.")

def greet_all_outputs():
    # 8. Pozdrav na všech kanálech
    text = "Systém CML/EVO je připraven. Vítejte!"
    print(f"[TEXT] {text}")

    # Hlasový výstup (nutno mít nainstalováno pyttsx3 nebo jiný TTS engine)
    try:
        import pyttsx3
        tts = pyttsx3.init()
        tts.say(text)
        tts.runAndWait()
        print("[TTS] Hlasový pozdrav odeslán.")
    except Exception as e:
        print(f"[TTS] Nelze spustit hlasový výstup: {e}")

    # Obrázkový výstup (např. vytvoření/plakát s textem)
    try:
        from PIL import Image, ImageDraw, ImageFont
        img = Image.new("RGB", (600, 200), color=(18, 32, 43))
        d = ImageDraw.Draw(img)
        font = ImageFont.load_default()
        d.text((20, 80), text, font=font, fill=(160, 255, 200))
        img.save("welcome.png")
        print("[IMG] Obrázkový pozdrav uložen jako welcome.png")
    except Exception as e:
        print(f"[IMG] Nelze vytvořit obrázek: {e}")

def main():
    print("=== CML/EVO setup & launch ===")
    setup_venv()
    start_docker_astra()
    start_storage()
    start_gui()
    activate_openai()
    greet_all_outputs()
    print("\nSystém čeká na první zadání…")
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("Ukončuji systém.")

if __name__ == "__main__":
    main()