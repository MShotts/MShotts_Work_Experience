
import streamlit as st
import pandas as pd
import altair as alt

st.sidebar.header("TBD")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom, #336699, #2F4858);
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<span style="font-size:48px; color:#9EE493">**Matthew Shotts**</span>', unsafe_allow_html=True)
st.markdown('<span style="font-size:22px; color:#DAF7DC">People Manager Experience</span>', unsafe_allow_html=True)

# df_years_exp=pd.DataFrame({
#     "Domain": ["Project Mgmt","People Mgmt","SAS/SQL","DataViz/PBI","Cloud DW","Agile"],
#     "Years_Experience": [16,15,11,5,4,4]
# })
#
# years_exp_chart = alt.Chart(df_years_exp).mark_bar(
#     color='#86BBD8'
# ).encode(
#     x=alt.X('Years_Experience',title='Years of Experience',axis=alt.Axis(tickCount=5)),
#     y=alt.Y('Domain',sort='-x',title=None)
# ).configure(
#     background='transparent'
# ).configure_axis(
#     labelColor='#FFFFFF',
#     titleColor='#FFFFFF'
# ).properties(
#     width=510,
#     height=250
# )
# st.altair_chart(years_exp_chart, use_container_width=False)

st.markdown('<span style="font-size:22px; color:#DAF7DC">Work in progress</span>', unsafe_allow_html=True)
st.markdown('<span style="font-size:14px; color:#FFFFFF">Work in progress</span>', unsafe_allow_html=True)

# Use the following in terminal (lower side ribbon) to run the app
# streamlit run C:\Users\DrShotts\PycharmProjects\Streamlit\Streamlit_Test.py