import numpy as np
import sympy as sp
from scipy import linalg, stats

class MatrixResearchMemory:
    """
    Paměťová sekce pro ukládání a vysvětlování výzkumů v oblasti maticových systémů.
    Umožňuje vkládání nových výzkumných poznatků, jejich propojení s existujícími fyzikálními zákony,
    generování odborného vysvětlení na základě známé fyziky, matematickou/statistickou analýzu a predikci.
    Implementuje koncepční trojbokou váhu (nebo vícebokou) pro ověřování pravdivosti tvrzení:
        - 1. fyzika
        - 2. matematika (analýza, vzorce)
        - 3. statistika a logika
        - + predikce/modelování
    Tvrzení je uznáno za objev, je-li na váze dosažena harmonická rovnováha všech složek.
    """

    def __init__(self):
        # Slovník: název výzkumu -> { ... }
        self.researches = {}

    def add_research(self, name, description, references=None, physics_context=None, data=None, mathematics=None, statistics=None, logic=None, prediction=None):
        """
        Vloží nový výzkum do paměti.
        :param name: Název výzkumu
        :param description: Popis výzkumu
        :param references: Odkazy na literaturu
        :param physics_context: Fyzikální zákony
        :param data: Experimentální data, matice, vzorce
        :param mathematics: Matematický model, symbolické výrazy (sympy), algoritmy
        :param statistics: Statistická analýza, distribuce, p-hodnoty, korelace (scipy.stats)
        :param logic: Logická argumentace, implikace, pravidla
        :param prediction: Predikční model (ML, analytika, extrapolace)
        """
        self.researches[name] = {
            'popis': description,
            'odkazy': references or [],
            'fyzika': physics_context or [],
            'data': data,
            'matematika': mathematics,
            'statistika': statistics,
            'logika': logic,
            'predikce': prediction
        }

    def explain_research(self, name):
        """
        Vysvětlí výzkum s využitím harmonické trojboké váhy (fyzika, matematika, statistika+logika, predikce).
        Pokud jsou všechny složky v rovnováze, jde o objev. Pokud chybí – fikce. Pokud převažuje – pouze varianta známého faktu.
        """
        if name not in self.researches:
            return f"Výzkum '{name}' nebyl nalezen v paměti."
        r = self.researches[name]
        explanation = f"Výzkum: {name}\n"
        explanation += f"Popis: {r['popis']}\n"

        # Sběr vah pro koncepční rovnováhu
        weight = {
            "fyzika": bool(r['fyzika']),
            "matematika": bool(r['matematika']),
            "statistika_logika": bool(r['statistika']) and bool(r['logika']),
            "predikce": bool(r['predikce'])
        }
        present = sum(weight.values())

        # Výklad jednotlivých složek
        if r['fyzika']:
            explanation += f"Fyzikální podklad: {', '.join(r['fyzika']) if isinstance(r['fyzika'], list) else r['fyzika']}\n"
        if r['matematika']:
            explanation += f"Matematický model: {r['matematika']}\n"
        if r['statistika']:
            explanation += f"Statistická analýza: {r['statistika']}\n"
        if r['logika']:
            explanation += f"Logická argumentace: {r['logika']}\n"
        if r['predikce']:
            explanation += f"Predikce/modelování: {r['predikce']}\n"
        if r['data']:
            explanation += f"Experimentální data/vzorce: {r['data']}\n"
        if r['odkazy']:
            explanation += f"Odkazy: {', '.join(r['odkazy'])}\n"

        # Výsledek váhy
        if present == 4:
            explanation += "\nZÁVĚR: Všechny složky váhy jsou v harmonické roznováze – tvrzení lze považovat za OBĚV (vědecky podložený, nový poznatek).\n"
        elif present >= 2:
            explanation += "\nZÁVĚR: Některé složky převažují – tvrzení je variantou, modifikací či novou aplikací známých faktů.\n"
        else:
            explanation += "\nZÁVĚR: Chybí harmonická roznováha – tvrzení je FIKCE nebo zatím neověřený nápad.\n"

        return explanation

    def required_libraries(self):
        """
        Vrací seznam doporučených knihoven potřebných pro matematické/statistické modelování a predikci.
        """
        libs = [
            "numpy        # základní matice, lineární algebra, výpočty",
            "scipy        # pokročilá matematika, statistika, optimalizace, linalg, stats",
            "sympy        # symbolická matematika, analytické výrazy, derivace, integrace",
            "statsmodels  # pokročilé statistické modely, regrese, testování",
            "sklearn      # machine learning pro predikci (regrese, klasifikace)",
            "pandas       # datová analytika, tabulky, příprava dat"
        ]
        return libs

    def mathematical_templates(self):
        """
        Vrací přehled matematických vzorů vhodných pro analýzu výzkumů:
        """
        return [
            "Lineární soustava: Ax = b (numpy.linalg.solve)",
            "Spektrální rozklad: A = QΛQ⁻¹ (numpy.linalg.eig)",
            "Regrese: y = a + bx (scipy.stats.linregress, statsmodels)",
            "Korelační matice: numpy.corrcoef(X, rowvar=False)",
            "Rozptyl, směrodatná odchylka: numpy.var(X), numpy.std(X)",
            "Symbolické rovnice: sympy.Eq, sympy.solve, sympy.diff, sympy.integrate",
            "Bayesovská inference: scipy.stats.bayes_mvs",
            "Strojové učení: sklearn.linear_model, sklearn.ensemble apod.",
            "Hypotézové testy: scipy.stats.ttest_ind, scipy.stats.chi2_contingency"
        ]

# --- Ukázka použití ---
if __name__ == "__main__":
    mrm = MatrixResearchMemory()
    mrm.add_research(
        name="Trojboká váha pro validaci poznatků",
        description="Použití trojboké váhy pro ověřování vědeckých tvrzení – vyžaduje rovnováhu mezi fyzikou, matematikou, statistikou/logikou a predikcí.",
        references=["https://en.wikipedia.org/wiki/Scientific_method"],
        physics_context=["Zákon zachování energie"],
        data={'A': [[2, 1], [1, 3]], 'b': [8, 13]},  # Příklad dat pro maticovou analýzu
        mathematics="Ax = b",
        statistics="Pearsonova korelace, p-hodnota < 0.05",
        logic="Implikace: Pokud je rovnováha, lze tvrdit objev.",
        prediction="Predikce výsledku pomocí řešení soustavy Ax = b"
    )
    print(mrm.explain_research("Trojboká váha pro validaci poznatků"))
    print("Doporučené knihovny pro matematiku/statistiku:")
    print("\n".join(mrm.required_libraries()))
    print("Matematické vzory pro analýzu:")
    print("\n".join(mrm.mathematical_templates()))