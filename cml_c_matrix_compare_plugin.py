import numpy as np
import sympy as sp
from scipy import stats

class MatrixResearchComparator:
    """
    Porovnávací plugin pro výzkumy v oblasti maticových systémů.
    Umožňuje srovnání dvou nebo více výzkumů (uložených např. v MatrixResearchMemory) z hlediska:
    - matematických modelů (matice, rovnice)
    - fyzikálních podkladů
    - statistických charakteristik (shoda, rozdíl, korelace)
    - predikčních výsledků
    Výstupem je objektivní, odborně odůvodněné srovnání.
    """

    def __init__(self, memory):
        """
        :param memory: Instance MatrixResearchMemory s uloženými výzkumy
        """
        self.memory = memory

    def compare(self, names):
        """
        Provede srovnání zadaných výzkumů podle všech dostupných kritérií.
        :param names: Seznam názvů výzkumů (minimálně 2)
        :return: Textový report s porovnáním
        """
        if len(names) < 2:
            return "Je třeba zadat alespoň dva výzkumy k porovnání."

        researches = [self.memory.researches.get(n) for n in names]
        if not all(researches):
            return "Jeden nebo více výzkumů nebyl nalezen v paměti."

        report = f"Porovnání výzkumů: {', '.join(names)}\n\n"

        # Fyzikální podklad
        physics_sets = [set(r['fyzika']) if isinstance(r['fyzika'], list) else set() for r in researches]
        common_physics = set.intersection(*physics_sets) if physics_sets else set()
        all_physics = set.union(*physics_sets)
        report += f"Společné fyzikální zákony: {', '.join(common_physics) if common_physics else 'žádné'}\n"
        report += f"Ve všech zahrnuté fyzikální zákony: {', '.join(all_physics) if all_physics else 'žádné'}\n\n"

        # Matematický model
        math_models = [str(r['matematika']) for r in researches]
        unique_models = set(math_models)
        if len(unique_models) == 1:
            report += f"Matematický model: Všechny výzkumy používají stejný model: {unique_models.pop()}\n"
        else:
            report += "Matematické modely:\n"
            for n, m in zip(names, math_models):
                report += f"  - {n}: {m}\n"
        report += "\n"

        # Statistická analýza
        stats_analyses = [str(r['statistika']) for r in researches]
        unique_stats = set(stats_analyses)
        if len(unique_stats) == 1:
            report += f"Statistika: Shodná statistická metodika: {unique_stats.pop()}\n"
        else:
            report += "Statistické metody:\n"
            for n, s in zip(names, stats_analyses):
                report += f"  - {n}: {s}\n"
        report += "\n"

        # Data/matice: Pokud lze, provede kvantitativní srovnání matic a vektorů
        matrices = []
        for r in researches:
            if r['data'] and isinstance(r['data'], dict) and 'A' in r['data']:
                matrices.append(np.array(r['data']['A']))
            else:
                matrices.append(None)
        if all(m is not None for m in matrices):
            diffs = [np.linalg.norm(matrices[i] - matrices[0]) for i in range(1, len(matrices))]
            for i, d in enumerate(diffs, 1):
                report += f"Rozdíl matice {names[0]} a {names[i]} (Frobeniova norma): {d}\n"
            # Pokud jsou i vektory b:
            bs = [np.array(r['data']['b']) if (r['data'] and 'b' in r['data']) else None for r in researches]
            if all(b is not None for b in bs):
                for i in range(1, len(bs)):
                    corr = np.corrcoef(bs[0], bs[i])[0, 1]
                    report += f"Korelace vektorů b ({names[0]} vs {names[i]}): {corr:.3f}\n"
        else:
            report += "Nejsou dostupná kompletní data pro kvantitativní srovnání matic.\n"
        report += "\n"

        # Predikce/modely
        predictions = [str(r['predikce']) for r in researches]
        if len(set(predictions)) == 1:
            report += f"Predikce: Všechny výzkumy mají shodný predikční přístup.\n"
        else:
            report += "Predikční modely:\n"
            for n, p in zip(names, predictions):
                report += f"  - {n}: {p}\n"

        # Závěrečné shrnutí
        if len(unique_models) == 1 and len(unique_stats) == 1 and all(m is not None for m in matrices):
            report += "\nZÁVĚR: Výzkumy jsou metodicky srovnatelné a lze je objektivně porovnávat.\n"
        else:
            report += "\nZÁVĚR: Výzkumy mají odlišné přístupy nebo nedostatek kvantitativních dat pro plné srovnání.\n"

        return report

# --- Ukázka použití ---
if __name__ == "__main__":
    from cml_c_matrix_research_memory import MatrixResearchMemory

    mrm = MatrixResearchMemory()
    mrm.add_research(
        name="Model A",
        description="Výzkum A s maticovým modelem.",
        physics_context=["Zákon zachování energie"],
        data={'A': [[2, 1], [1, 3]], 'b': [10, 20]},
        mathematics="Ax = b",
        statistics="Regrese",
        logic="Test logiky",
        prediction="Predikce X"
    )
    mrm.add_research(
        name="Model B",
        description="Výzkum B s modifikovanou maticí.",
        physics_context=["Zákon zachování energie"],
        data={'A': [[2.1, 1.0], [1.0, 3.1]], 'b': [11, 19]},
        mathematics="Ax = b",
        statistics="Regrese",
        logic="Test logiky",
        prediction="Predikce Y"
    )
    comparator = MatrixResearchComparator(mrm)
    print(comparator.compare(["Model A", "Model B"]))