
import streamlit as st
import pandas as pd
import altair as alt
# import seaborn as sns
# import matplotlib.pyplot as plt

st.title("Matthew Shotts' Experience")
# st.header("People Supervisor")
# st.write("Matthew has supervised teams from 3 to 11 staff and consultants during his 15 years as a manager.")
# st.write("He successfully promoted team members to the highest levels of their respective job titles and 2 of his former mentees have since been promoted to management.  Additionally, 2 staff followed Matthew to a new company in order to stay under his leadership.")

df_years_exp=pd.DataFrame({
    "Domain": ["Project Mgmt","People Mgmt","SAS/SQL","DataViz/PBI","Cloud DW","Agile"],
    "Years_Experience": [16,15,11,5,4,4]
})

years_exp_chart = alt.Chart(df_years_exp).mark_bar().encode(
    x=alt.X('Years_Experience',axis=alt.Axis(tickCount=5)),
    y=alt.Y('Domain',sort='-x',title=None)
)
st.altair_chart(years_exp_chart, use_container_width=True)

# fig, ax = plt.subplots(figsize=(10, 6))
# sns.barplot(data=df_years_exp, x='Domain', y='Years_Experience', ax=ax, orient='h')
# # ax.set_title('Monthly Sales (Horizontal)')
# st.pyplot(fig)

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
