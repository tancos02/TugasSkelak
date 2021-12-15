import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

nation_name = df_js['name']

with st.container():
    option = st.selectbox(
        "Nation",
        nation_name
    )
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
