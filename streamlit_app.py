
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
st.markdown('<span style="font-size:22px; color:#DAF7DC">Delivering Insights | Improving Processes | Empowering Staff</span>', unsafe_allow_html=True)

df_years_exp=pd.DataFrame({
    "Domain": ["Project Mgmt","People Mgmt","SAS/SQL","DataViz/PBI","Cloud DW","Agile"],
    "Years_Experience": [16,15,11,5,4,4]
})

years_exp_chart = alt.Chart(df_years_exp).mark_bar().encode(
    x=alt.X('Years_Experience',title='Years of Experience',axis=alt.Axis(tickCount=5)),
    y=alt.Y('Domain',sort='-x',title=None)
).configure(
    background='transparent'
).properties(
    # width='container',
    width=510,
    height=250
)
st.altair_chart(years_exp_chart, use_container_width=False)

st.subheader("Drove enterprise-level analytics strategy and execution across healthcare, retail, and assessment organizations:")
st.text("Delivering cost savings (six-figure annual vendor fee reductions), improved decision-making, and scalable data products used by hundreds of users weekly.")
st.write("")
st.subheader("Built and led high-performing analytics and visualization teams:")
st.text("Recruiting and developing talent, defining roles and operating models, and stabilizing organizations through change including re-organizations that reduced team size by 50% yet had no disruption to service or user experience.")
st.write("")
st.subheader("Designed and operationalized modern data platforms and semantic layers:")
st.text("Standing up a Power BI ecosystem (Center of Excellence, standards, governance, and support) and contributing to the launch of new healthcare and assessment products.")
st.write("")
st.subheader("Partnered cross-functionally with executives, internal stakeholders, and external vendors:")
st.text("Resolving complex data and process issues, validating third-party solutions, and representing analytics functions to senior leadership and international clients.")
st.write("")
st.subheader("Delivered sustained efficiency and quality improvements:")
st.text("Modernizing systems and statistical models, introducing agile delivery practices, and reducing critical workflows by up to 3-4 weeks while maintaining accuracy, compliance, and stakeholder trust.")
