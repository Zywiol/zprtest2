import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")


with st.expander("Instrukcje użytkownika"):
    st.markdown("""
        ### Instrukcje użytkownika


        #### Przegląd dostępnych cenników:
        - Poniżej znajduje się tabela z wszystkimi dostępnymi cennikami.

        Jeśli masz jakiekolwiek pytania lub potrzebujesz pomocy, prosimy o kontakt z działem wsparcia.
    """)

st.header("Wszystkie dostępne cenniki")

pricing_list_format = {
    'Piwo': [
        ["Zenek", "Piwo Kasztelan", 999, "szt.", "-", 5, "2024-06-17", "2024-06-23"],
        ["Kasia", "Piwo Lubuskie", 888, "but.", "-", 6, "2024-06-17", "2024-06-23"],
        ["Ania", "Piwo Lech", 777, "litr", "-", 4, "2024-06-17", "2024-06-23"],
        ["Piotr", "Piwo Żywiec", 666, "but.", "-", 3, "2024-06-10", "2024-06-16"]
    ],
    "Wódka": [
        ["Adam", "Wódka Bocian", 777, "litr", "-", 25, "2024-06-17", "2024-06-23"],
        ["Ola", "Wódka Bols", 666, "litr", "-", 20, "2024-06-17", "2024-06-23"],
        ["Bartek", "Wódka Smirnof", 555, "szt.", "-", 15, "2024-06-17", "2024-06-23"],
        ["Kasia", "Wódka Tania", 444, "but.", "-", 18, "2024-06-10", "2024-06-16"]
    ],
    "Gin": [
        ["Jacek", "Gin", 333, "litr", "-", 30, "2024-06-17", "2024-06-23"],
        ["Monika", "Gin", 222, "but.", "-", 28, "2024-06-17", "2024-06-23"],
        ["Ola", "Gin", 666, "litr", "-", 20, "2024-06-17", "2024-06-23"],
        ["Anna", "Gin", 111, "but.", "-", 32, "2024-06-10", "2024-06-16"]
    ],
    "Likier": [
        ["Marek", "Likier", 999, "but.", "-", 22, "2024-06-17", "2024-06-23"],
        ["Zenek", "Likier", 888, "but.", "-", 35, "2024-06-17", "2024-06-23"],
        ["Marta", "Likier", 777, "but.", "-", 10, "2024-06-17", "2024-06-23"],
        ["Paweł", "Likier", 666, "szt.", "-", 8, "2024-06-10", "2024-06-16"]
    ],
    "Wino": [
        ["Karol", "Wino", 555, "litr", "-", 25, "2024-06-17", "2024-06-23"],
        ["Ewa", "Wino", 444, "litr", "-", 22, "2024-06-17", "2024-06-23"],
        ["Olga", "Wino", 333, "szt.", "-", 5, "2024-06-17", "2024-06-23"],
        ["Tomek", "Wino", 222, "but.", "-", 6, "2024-06-10", "2024-06-16"]
    ]
}

# Tworzenie DataFrame z pricing_list_format
# Przekształcenie danych w format odpowiedni dla DataFrame
flattened_data = []
for category, items in pricing_list_format.items():
    for item in items:
        flattened_data.append([category] + item)

df = pd.DataFrame(flattened_data, columns=[
    "Kategoria", "Nazwa dostawcy", "Nazwa produktu dostawcy", "Indeks dostawcy", "Jednostka dostawcy",
    "Masa w przypadku opakowań [KG]", "Cena netto", "Data obowiązywania od", "Data obowiązywania do"
])

# Dodanie kolumny "Indeks ZPR"
df["Indeks ZPR"] = ""

# Inicjalizacja st.session_state.df
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=[
        "Indeks ZPR", "Nazwa produktu dostawcy", "Nazwa dostawcy",
        "Cena netto", "Ilość", "Wartość zamówienia",
        "Różnica procentowa", "Indeks dostawcy",
        "Jednostka dostawcy", "Masa w przypadku opakowań [KG]",
        "Data obowiązywania od", "Data obowiązywania do"
    ])

# Wyświetlenie DataFrame z możliwością edycji
st.data_editor(data=df,
               column_config={
                   "Indeks ZPR": st.column_config.SelectboxColumn(
                       options=[1, 2, 3, 4, 5]
                   )
               })
