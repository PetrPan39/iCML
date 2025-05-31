# EVO_ARMAGEDON

Evoluční framework pro kognitivní systémy, predikci, sebezdokonalování a multiagentní výpočty.

---

## 📊 Přehled funkcionalit

| Modul / Funkce              | Stav       | Popis                                                                 |
|-----------------------------|------------|-----------------------------------------------------------------------|
| `EvolucniOptimalizace`      | ✅ Hotovo  | Jádro systému – logika, validace, historie, výstupy                   |
| `PluginManager`             | ✅ Hotovo  | Načítání a správa pluginů                                             |
| `OpenAIClient`              | ✅ Hotovo  | Jazykové dotazy a odpovědi přes GPT                                   |
| `gui_server.py + gui/`      | ✅ Hotovo  | Chat rozhraní ve stylu ChatGPT                                        |
| `AstraDB` připojení         | ✅ Připraveno | Připojení na cloud DB                                                |
| `Function Calling`          | 🧪 Příprava | Možnost nechat GPT volat výpočetní pluginy                            |
| `Auto-plánování úloh`       | ❌ Chybí    | Budoucí samostatné plánování a sebeřízení                            |
| `Historie + učení`          | 🧪 Příprava | Ukládání a využívání minulé zkušenosti                               |

---

## 🧑‍💻 Přispívání

Přijímáme rozšíření a opravy prostřednictvím pull requestů. Každý kód musí být:

- přehledně komentovaný
- testovatelný
- nesmí obsahovat proprietární knihovny

## ⚠️ Licenční podmínky

Kód je **otevřený pro vývoj a vzdělávací účely**.  
Přispěvatelé souhlasí, že jejich kód může být využit v projektu.

❌ **Nesmí být použit k prodeji, komerčním službám nebo jako SaaS.**  
✅ Smí být použit pro výzkum, komunitní projekty a osobní nástroje.

---

## 🔧 Spuštění

```bash
pip install -r requirements.txt
uvicorn gui_server:app --reload
```

Otevři prohlížeč: http://localhost:8000