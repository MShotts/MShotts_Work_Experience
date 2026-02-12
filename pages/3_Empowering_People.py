
import streamlit as st
import pandas as pd
import altair as alt

# st.sidebar.header("TBD")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom, #336699, #2F4858);
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<span style="font-size:48px; color:#9EE493">**Empowering People**</span>', unsafe_allow_html=True)
st.write("")

pexp_col1, pexp_col2, pexp_col3 = st.columns(3)

with pexp_col1:
    st.markdown('''
        <div style="text-align: center;">
            <p style="color: #FFFFFF; font-size: 18px; margin-bottom: 0px;">
                Years Experience
            </p>
            <h1 style="color: #DAF7DC; font-size: 42px; margin: 0; margin-top:0;">
                15
            </h1>
        </div>
        ''', unsafe_allow_html=True)

with pexp_col2:
    st.markdown('''
        <div style="text-align: center;">
            <p style="color: #FFFFFF; font-size: 18px; margin-bottom: 0px;">
                Max Team Size
            </p>
            <h1 style="color: #DAF7DC; font-size: 42px; margin: 0; margin-top:0;">
                12
            </h1>
        </div>
        ''', unsafe_allow_html=True)

with pexp_col3:
    st.markdown('''
        <div style="text-align: center;">
            <p style="color: #FFFFFF; font-size: 18px; margin-bottom: 0px;">
                Staff Hired
            </p>
            <h1 style="color: #DAF7DC; font-size: 42px; margin: 0; margin-top:0;">
                ~15
            </h1>
        </div>
        ''', unsafe_allow_html=True)

st.write("")
st.markdown('<span style="font-size:22px; color:#DAF7DC">Highlights:</span>', unsafe_allow_html=True)
st.markdown('<span style="font-size:14px; color:#FFFFFF">During his tenure as manager, Matthew has promoted many team members to higher job titles and increased levels of responsibility; including one team member promoted to the highest level of a 4-tier job title.</span>', unsafe_allow_html=True)
st.markdown('<span style="font-size:14px; color:#FFFFFF">Members of the team were recognized each year as high performers during performance calibrations across the department.  Two staff previously mentored by Matthew have been promoted to managerial positions.</span>', unsafe_allow_html=True)
st.markdown('<span style="font-size:14px; color:#FFFFFF">His teams had excellent retention with only one team member leaving for another company.  Additionally, two team members followed Matthew from ETS to Burlington Stores to stay under his leadership and participate in the Merch 2.0 reporting initiative.</span>', unsafe_allow_html=True)
st.markdown('<span style="font-size:14px; color:#FFFFFF">Initiated monthly training seminars across the Analytics and Research orgs and showcased various coding optimization and best practices to audiences of ~50 staff.</span>', unsafe_allow_html=True)


# Use the following in terminal (lower side ribbon) to run the app
# streamlit run C:\Users\DrShotts\PycharmProjects\Streamlit\streamlit_app.py

