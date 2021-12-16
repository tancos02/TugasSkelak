import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

df = pd.read_csv('produksi_minyak_mentah.csv')
df_js = pd.read_json('kode_negara_lengkap.json')

nation_name = df_js['name']

col1, col2= st.columns(2)
container1 = st.container()
container2 = st.container()
with col1 :
    with container1:
        option = st.selectbox(
            "Nation",
            nation_name
        )
        if st.button('Lihat grafik a'):
            choosen_nation = df_js.loc[df_js['name'] == option]
            choosen_nation.reset_index(drop=True, inplace=True)
            nation_code = str(choosen_nation['alpha-3'][0])
            result = df.loc[df['kode_negara'] == nation_code]
            result = result[['tahun', 'produksi']]
            result.reset_index(drop=True, inplace=True)
            chart = alt.Chart(result).mark_line().encode(
                x='tahun',
                y='produksi'
            )
            st.altair_chart(chart, use_container_width=True)
    with container2 :
        num_nation = int(st.number_input('Masukkan jumlah negara yang ditampilkan'))
        year = int(st.number_input('Masukkan tahun'))
        if st.button('Lihat grafik b'):
            result = df.loc[df['tahun'] == year]
            result.sort_values(by=['produksi'], ascending=False, inplace=True)
            result.reset_index(drop=True, inplace=True)
            if(len(result)>num_nation) :
                result = result.head(num_nation)
            result
            bars = alt.Chart(result).mark_bar().encode(
                x='produksi',
                y='kode_negara'
            )
            st.altair_chart(bars, use_container_width=True)
# with col2 :
