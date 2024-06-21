import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

with st.expander("Instrukcje użytkownika"):
    st.markdown("""
        ### Instrukcje użytkownika

        #### Przypisanie indeksu ZPR:
        - Każda pozycja w tabeli musi mieć przypisany indeks ZPR lub wartość 'brak'.
        - W tej sekcji możesz przypisać odpowiednie indeksy ZPR do pozycji, które tego wymagają.

        #### Kroki do wykonania:
        1. Przejrzyj listę pozycji wyświetlaną w tabeli poniżej.
        2. Dla każdej pozycji, która nie ma przypisanego indeksu ZPR, wybierz odpowiedni indeks z listy rozwijanej.
        3. Jeśli nie możesz przypisać indeksu ZPR do danej pozycji, zaznacz wartość 'brak'.

        #### Edytowanie danych:
        - Możesz edytować dane bezpośrednio w tabeli, klikając na odpowiednie komórki.
        - Po wprowadzeniu zmian, tabela zostanie automatycznie zaktualizowana.

        #### Zapis zmian:
        - Po zakończeniu edycji, zmiany zostaną automatycznie zapisane w systemie.
        
        Jeśli masz jakiekolwiek pytania lub potrzebujesz pomocy, prosimy o kontakt z działem wsparcia.
    """)


st.header("Wszystkie pozycje które nie mają przypisanego indeksu zpr lub brak")

pricing_list_format = {
    "Indeks ZPR":[123],
    "Nazwa dostawcy":['Zenek'],
    "Nazwa produktu dostawcy":["Piwo"],
    "Indeks dostawcy":[999],
    "Jednostka dostawcy":["szt."],
    "Masa w przypadku opakowań [KG]":["-"],
    "Cena netto":[5],
    "Data obowiązywania od":["2024-06-17"],
    "Data obowiązywania do":["2024-06-20"]
}

df = pd.DataFrame(pricing_list_format)

st.data_editor(data=df,
               column_config={
                   "Indeks ZPR": st.column_config.SelectboxColumn(
                       options=[1,2,3,4,5]
                   )
               })
