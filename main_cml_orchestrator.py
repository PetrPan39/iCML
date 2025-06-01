from plugins.cml_c_matrix_research_memory import MatrixResearchMemory
from plugins.cml_c_matrix_compare_plugin import MatrixResearchComparator

# PŘÍKLADY: importy pro další jádra, předpokládáme že jsou v plugins/
# from plugins.cml_a_core import CML_A
# from plugins.cml_b_core import CML_B
# from plugins.cml_c_core import CML_C
# from plugins.cml_sales_guard import CML

class CML_CentralOrchestrator:
    """
    Centrální orchestrátor propojující všechna jádra CML (A/B/C/...) a připravený na napojení do učení a inference.
    """

    def __init__(self):
        # Inicializace jednotlivých bloků (použij své reálné třídy)
        self.memory = MatrixResearchMemory()
        self.comparator = MatrixResearchComparator(self.memory)
        # self.cml_a = CML_A()
        # self.cml_b = CML_B()
        # self.cml_c = CML_C()
        # self.cml_sales_guard = CML()

    def add_research(self, *args, **kwargs):
        return self.memory.add_research(*args, **kwargs)

    def explain_research(self, name):
        return self.memory.explain_research(name)

    def compare_researches(self, names):
        return self.comparator.compare(names)

    # Příprava napojení na AI/ChatGPT
    def chat_with_ai(self, prompt, openai_api_key):
        import openai
        openai.api_key = openai_api_key
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=800
        )
        return response.choices[0].message['content']

# --- Testovací blok ---
if __name__ == "__main__":
    orchestrator = CML_CentralOrchestrator()
    orchestrator.add_research(
        name="Test výzkum",
        description="Ukázka plného výzkumu pro orchestrátor.",
        physics_context=["Zákon zachování hybnosti"],
        data={'A': [[1, 2], [3, 4]], 'b': [5, 6]},
        mathematics="Ax = b",
        statistics="Testování korelace",
        logic="Pokud je soustava řešitelná, je výzkum validní.",
        prediction="Predikce chování systému při změně parametrů."
    )
    print(orchestrator.explain_research("Test výzkum"))
    print(orchestrator.compare_researches(["Test výzkum"]))
    # Pro OpenAI/ChatGPT je třeba vložit API klíč (nezveřejňuj!)
    # print(orchestrator.chat_with_ai("Shrň mi výzkum Test výzkum.", "TVŮJ_OPENAI_API_KEY"))