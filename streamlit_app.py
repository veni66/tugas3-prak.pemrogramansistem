import streamlit as st
import pandas as pd

# Membaca dataset (contoh CSV)
uploaded_file = st.file_uploader("Pilih file CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Menampilkan dataset
    st.write("Dataframe:")
    st.write(df)

    # Pilih kolom-kolom untuk diplot (maksimum 5 kolom)
    columns_to_plot = st.multiselect("Pilih hingga 5 kolom untuk diplot", df.columns, max_selections=5)

    if columns_to_plot:
        # Plot terpisah untuk setiap kolom menggunakan line_chart dari Streamlit
        for column in columns_to_plot:
            st.write(f"Plot dari kolom: {column}")
            st.line_chart(df[[column]])
