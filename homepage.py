import pandas as pd
import streamlit as st
import datetime as dt
import time
import functions as fun

st.set_page_config(layout="wide")

with st.expander("Instrukcje użytkownika"):
    st.markdown("""
        ### Instrukcje użytkownika

        ##### Wybór dostawcy cennika:
        1. Wybierz dostawcę cennika z listy rozwijanej. Dostępne opcje to "Dostawca 1", "Dostawca 2" oraz "Dostawca 3".

        ##### Wybór tygodnia cennika:
        2. Wybierz tydzień cennika, korzystając z datownika. Domyślnie pokazany jest bieżący tydzień.

        ##### Załadowanie pliku cennika:
        3. Kliknij przycisk "Wybierz cennik który chcesz umieścić", aby załadować plik cennika. Obsługiwane są pliki w formacie Excel.
        4. Jeśli nie załadujesz pliku, zobaczysz komunikat z prośbą o załadowanie pliku.
        
        ##### Dalsze kroki:
        Po załadowaniu pliku, przejdź do sekcji mapowanie aby uzupełnić brakujące pola.
    """)


st.header("Witaj w aplikacji")
st.write(" ")
st.write(" ")

dostawca = st.selectbox("Wybierz dostawcę cennika",
            ("MEGA-FRUIT KAROL TRZEWIK",
             "LADROS S.C. A. LEWCZYK",
             "WARMIA FRUIT",
             "GOBARTO SPÓŁKA AKCYJNA",
             "IMPERIAL-KOŁOBRZEG")
            )

start_date, end_date = fun.get_current_week()

st.date_input("Wybierz tydzień cennika",
            (start_date,end_date)
                )

uploader = st.file_uploader("Wybierz cennik który chcesz umieścić")
if uploader is None:
    st.info("Proszę o załadowanie pliku")
else:
    with open(uploader, mode="wb") as f:
        f.write(uploader.getbuffer())

st.write(" ")
st.write(" ")
st.write(" ")


button = st.button("Wgraj plik")
if button:

    if dostawca == "MEGA-FRUIT KAROL TRZEWIK":
        st.write(f"Teraz będzie procesowane {dostawca}")
        progress_bar = st.progress(0)
        for i in range(101):
            time.sleep(0.04)  
            progress_bar.progress(i)
        st.balloons()

    if dostawca == "LADROS S.C. A. LEWCZYK":
        st.write(f"Teraz będzie procesowane {dostawca}")
        progress_bar = st.progress(0)
        for i in range(101):
            time.sleep(0.04)  
            progress_bar.progress(i)
        st.balloons()

    if dostawca == "WARMIA FRUIT":
        st.write(f"Teraz będzie procesowane {dostawca}")
        progress_bar = st.progress(0)
        for i in range(101):
            time.sleep(0.04)  
            progress_bar.progress(i)
        st.balloons()

    if dostawca == "GOBARTO SPÓŁKA AKCYJNA":
        st.write(f"Teraz będzie procesowane {dostawca}")
        progress_bar = st.progress(0)
        for i in range(101):
            time.sleep(0.04)  
            progress_bar.progress(i)
        st.balloons()

    if dostawca == "IMPERIAL-KOŁOBRZEG":
        st.write(f"Teraz będzie procesowane {dostawca}")
        progress_bar = st.progress(0)
        for i in range(101):
            time.sleep(0.04) 
            progress_bar.progress(i)
        st.balloons()