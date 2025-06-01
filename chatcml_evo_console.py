import os
from dotenv import load_dotenv

try:
    from main_cml_orchestrator import CML_CentralOrchestrator
except ImportError:
    print("Nelze importovat orchestrátor! Zkontroluj cesty a instalaci.")
    exit(1)

# Načti .env soubor ze stejné složky jako tento skript
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

def main():
    print("=== AI EVO chatCML ===")
    print("Napiš 'help' pro nápovědu. Ukonči 'exit'.\n")

    orch = CML_CentralOrchestrator()
    openai_key = os.environ.get("OPENAI_API_KEY", "")

    while True:
        cmd = input("chatCML> ").strip()
        if cmd.lower() in ("exit", "quit"):
            print("Konec.")
            break
        elif cmd.lower() == "help":
            print("""
Možné příkazy:
  add_research         - Přidat nový výzkum (interaktivně)
  explain <název>      - Vysvětlit výzkum
  compare <a> <b> ...  - Porovnat výzkumy podle jmen
  evo_init [n]         - Inicializovat EVO s n jedinci (default 5)
  evo_step             - Proveď evoluční krok
  ai <dotaz>           - Polož dotaz OpenAI (pokud máš API klíč v OPENAI_API_KEY)
  help                 - Zobraz tuto nápovědu
  exit                 - Konec
""")
        elif cmd.startswith("add_research"):
            print("Zadávání nového výzkumu:")
            name = input("Název: ")
            desc = input("Popis: ")
            fys = input("Fyzikální zákony (čárkami): ").split(",")
            math = input("Matematický model: ")
            stat = input("Statistika: ")
            log = input("Logická argumentace: ")
            pred = input("Predikce: ")
            data_A = input("Data matice A (např. 1,2;3,4): ")
            data_b = input("Data vektor b (např. 5,6): ")
            try:
                A = [list(map(float, row.split(","))) for row in data_A.split(";")]
                b = list(map(float, data_b.split(",")))
                data = {"A": A, "b": b}
            except Exception:
                data = None
            orch.add_research(
                name=name,
                description=desc,
                physics_context=[f.strip() for f in fys if f.strip()],
                data=data,
                mathematics=math,
                statistics=stat,
                logic=log,
                prediction=pred
            )
            print(f"Výzkum '{name}' uložen.\n")
        elif cmd.startswith("explain "):
            name = cmd[len("explain "):].strip()
            print(orch.explain_research(name))
        elif cmd.startswith("compare "):
            names = cmd[len("compare "):].strip().split()
            print(orch.compare_researches(names))
        elif cmd.startswith("evo_init"):
            parts = cmd.split()
            n = int(parts[1]) if len(parts) > 1 else 5
            print(orch.start_evo(n))
        elif cmd.startswith("evo_step"):
            print(orch.step_evo())
        elif cmd.startswith("ai "):
            if not openai_key:
                print("Chybí API klíč v proměnné OPENAI_API_KEY!")
                continue
            q = cmd[len("ai "):]
            try:
                odp = orch.chat_with_ai(q, openai_key)
                print("AI:", odp)
            except Exception as e:
                print(f"Chyba při volání AI: {e}")
        else:
            print("Neznámý příkaz. Napiš 'help'.")

if __name__ == "__main__":
    main()