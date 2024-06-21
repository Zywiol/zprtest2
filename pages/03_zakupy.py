import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(layout="wide")

st.markdown("""Opis danej strony""")

st.header("Lista zakupów")

# Przykładowe dane dla wyszukiwania na podstawie indeksu z uwzględnieniem tygodni
lookup_data = {
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

if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=[
        "Indeks ZPR", "Nazwa dostawcy", "Nazwa produktu dostawcy",
        "Indeks dostawcy", "Jednostka dostawcy",
        "Masa w przypadku opakowań [KG]", "Cena netto",
        "Data obowiązywania od", "Data obowiązywania do",
        "Różnica procentowa", "Ilość", "Wartość zamówienia"
    ])

def get_week_range(date_str):
    date = pd.to_datetime(date_str)
    start_of_week = date - pd.DateOffset(days=date.weekday())
    end_of_week = start_of_week + pd.DateOffset(days=6)
    return start_of_week, end_of_week

def add_row():
    new_index = st.session_state.new_index
    quantity = st.session_state.quantity
    if new_index in lookup_data:
        products = lookup_data[new_index]
        current_week = pd.to_datetime("today").strftime("%Y-%U")
        previous_week = (pd.to_datetime("today") - pd.DateOffset(weeks=1)).strftime("%Y-%U")
        
        # Filtruj produkty na podstawie aktualnego tygodnia
        weekly_products = [product for product in products if get_week_range(product[6])[0].strftime("%Y-%U") == current_week]
        # Filtruj produkty na podstawie poprzedniego tygodnia
        previous_week_products = [product for product in products if get_week_range(product[6])[0].strftime("%Y-%U") == previous_week]
        
        if weekly_products:
            lowest_price_product = min(weekly_products, key=lambda x: x[5])
            new_row = [new_index] + lowest_price_product
            
            # Znajdź najniższą cenę z poprzedniego tygodnia
            if previous_week_products:
                lowest_previous_week_price = min(previous_week_products, key=lambda x: x[5])[5]
                price_difference = ((lowest_price_product[5] - lowest_previous_week_price) / lowest_previous_week_price) * 100
                new_row.append(price_difference)
            else:
                new_row.append("Brak danych")
            
            new_row.append(quantity)
            new_row.append(quantity * lowest_price_product[5])
            
            st.session_state.df.loc[len(st.session_state.df)] = new_row
        else:
            st.warning("Nie znaleziono danych dla wybranego indeksu w tym tygodniu.")
    else:
        st.warning("Nie znaleziono danych dla wybranego indeksu.")

def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    writer.close()
    processed_data = output.getvalue()
    return processed_data

col1, col2 = st.columns(spec=2)
col3, col4 = st.columns(spec=2)

# Pole do wyboru indeksu dla nowego wiersza
with col1:
    st.selectbox("Wybierz indeks ZPR", options=list(lookup_data.keys()), key='new_index')

with col3:
    st.number_input("Ilość", min_value=1, key='quantity')

st.button("Dodaj wiersz", on_click=add_row)

# Wyświetlanie wartości zamówienia i różnicy procentowej dynamicznie
if 'quantity' in st.session_state and 'new_index' in st.session_state:
    selected_index = st.session_state.new_index
    quantity = st.session_state.quantity
    if selected_index in lookup_data:
        products = lookup_data[selected_index]
        current_week = pd.to_datetime("today").strftime("%Y-%U")
        previous_week = (pd.to_datetime("today") - pd.DateOffset(weeks=1)).strftime("%Y-%U")
        weekly_products = [product for product in products if get_week_range(product[6])[0].strftime("%Y-%U") == current_week]
        previous_week_products = [product for product in products if get_week_range(product[6])[0].strftime("%Y-%U") == previous_week]
        if weekly_products:
            lowest_price_product = min(weekly_products, key=lambda x: x[5])
            order_value = quantity * lowest_price_product[5]
            st.write(f"Wartość zamówienia: {order_value} PLN")
            if previous_week_products:
                lowest_previous_week_price = min(previous_week_products, key=lambda x: x[5])[5]
                price_difference = ((lowest_price_product[5] - lowest_previous_week_price) / lowest_previous_week_price) * 100
                if price_difference < 0:
                    st.markdown(f'Różnica procentowa z poprzednim tygodniem: <span style="color:green;">{price_difference:.2f}%</span>', unsafe_allow_html=True)
                else:
                    st.markdown(f'Różnica procentowa z poprzednim tygodniem: <span style="color:red;">{price_difference:.2f}%</span>', unsafe_allow_html=True)
            else:
                st.write("Różnica procentowa: Brak danych")

st.write(" ")
st.write(" ")
st.write(" ")

def delete_rows():
    original_df = st.session_state.df
    edited_values = edited_df.values.tolist()
    original_values = original_df.values.tolist()

    # Znajdź wiersze, które zostały usunięte
    deleted_values = [row for row in original_values if row not in edited_values]

    if deleted_values:
        # Usuwanie wierszy na podstawie ich wartości
        for row in deleted_values:
            original_df = original_df[original_df.apply(lambda x: x.tolist() != row, axis=1)]
        
        # Resetowanie indeksu po usunięciu wierszy
        st.session_state.df = original_df.reset_index(drop=True)

# Wyświetlenie tabeli z możliwością edycji
edited_df = st.data_editor(
    data=st.session_state.df,
    num_rows="dynamic",
    column_config={
        "Indeks ZPR": st.column_config.TextColumn(disabled=False),
        "Nazwa dostawcy": st.column_config.TextColumn(disabled=False),
        "Nazwa produktu dostawcy": st.column_config.TextColumn(disabled=False),
        "Indeks dostawcy": st.column_config.NumberColumn(disabled=False),
        "Jednostka dostawcy": st.column_config.TextColumn(disabled=False),
        "Masa w przypadku opakowań [KG]": st.column_config.TextColumn(disabled=False),
        "Cena netto": st.column_config.NumberColumn(
            label="Cena netto",
            format="%.2f"
        ),
        "Data obowiązywania od": st.column_config.TextColumn(disabled=False),
        "Data obowiązywania do": st.column_config.TextColumn(disabled=False),
        "Różnica procentowa": st.column_config.NumberColumn(
            label="Różnica procentowa",
            format="%.2f%%",
            disabled=True
        ),
        "Ilość": st.column_config.NumberColumn(
            label="Ilość",
            disabled=True
        ),
        "Wartość zamówienia": st.column_config.NumberColumn(
            label="Wartość zamówienia",
            format="%.2f",
            disabled=True
        )
    }
)

# Wykrywanie usuniętych wierszy
delete_rows()

# Dodanie przycisku do pobierania pliku XLSX
edited_df_excel = to_excel(edited_df)
st.download_button(
    label="Pobierz XLSX",
    data=edited_df_excel,
    file_name='zakupy.xlsx',
    mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
)