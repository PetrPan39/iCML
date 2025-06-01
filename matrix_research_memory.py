from cml_c_matrix_research_memory import MatrixResearchMemory

# Inicializace paměti
mrm = MatrixResearchMemory()

# Ukázkový výzkum: Matice pro optimalizaci toku energie ve fúzním modulu
mrm.add_research(
    name="Optimalizace toku energie v grafenovém fúzním reaktoru",
    description=(
        "Výzkum analyzuje optimalizaci toku energie v grafenovém jádru fúzního reaktoru pomocí maticového modelu přenosu "
        "tepelné energie. Cílem je minimalizovat ztráty a maximalizovat přenos mezi aktivní zónou a chladicím systémem."
    ),
    references=[
        "https://doi.org/10.1016/j.physleta.2024.128900",
        "https://arxiv.org/abs/2401.12345"
    ],
    physics_context=[
        "Zákon zachování energie",
        "Fourierův zákon vedení tepla",
        "Kvaziklasická teorie tepelné vodivosti v grafenových strukturách"
    ],
    data={
        'A': [[0.85, 0.10], [0.10, 0.90]],  # Přenosová matice (ideální, úniky)
        'b': [100, 30]  # Vstupní energie (MW), výstupní energie do chlazení (MW)
    },
    mathematics="Ax = b, kde x jsou optimální toky energie mezi subsystémy.",
    statistics="Regrese mezi vstupní a výstupní energií, p-hodnota < 0.05",
    logic=(
        "Pokud optimalizované x (toky) odpovídají reálným datům a splňují zákony zachování energie, "
        "lze tvrdit, že model je validní."
    ),
    prediction=(
        "Na základě matice A a vektoru b předpovídáme optimální rozložení toku energie pro nové konfigurace reaktoru."
    )
)

# Výpis vysvětlení
print(mrm.explain_research("Optimalizace toku energie v grafenovém fúzním reaktoru"))

# Výpis doporučených knihoven a matematických vzorů
print("\nDoporučené knihovny pro matematiku/statistiku:")
print("\n".join(mrm.required_libraries()))
print("\nMatematické vzory pro analýzu:")
print("\n".join(mrm.mathematical_templates()))