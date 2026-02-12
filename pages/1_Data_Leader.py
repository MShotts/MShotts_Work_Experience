
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

st.markdown('<span style="font-size:48px; color:#9EE493">**Data and Analytics Leader**</span>', unsafe_allow_html=True)
st.write("")

daxp_col1, daxp_col2, daxp_col3 = st.columns(3)

with daxp_col1:
    st.markdown('''
        <div style="text-align: center;">
            <p style="color: #FFFFFF; font-size: 18px; margin-bottom: 0px;">
                Different Industries
            </p>
            <h1 style="color: #DAF7DC; font-size: 42px; margin: 0; margin-top:0;">
                3
            </h1>
        </div>
        ''', unsafe_allow_html=True)

with daxp_col2:
    st.markdown('''
        <div style="text-align: center;">
            <p style="color: #FFFFFF; font-size: 18px; margin-bottom: 0px;">
                Metrics calculated
            </p>
            <h1 style="color: #DAF7DC; font-size: 42px; margin: 0; margin-top:0;">
                ~500
            </h1>
        </div>
        ''', unsafe_allow_html=True)

with daxp_col3:
    st.markdown('''
        <div style="text-align: center;">
            <p style="color: #FFFFFF; font-size: 18px; margin-bottom: 0px;">
                Ad hoc requests completed
            </p>
            <h1 style="color: #DAF7DC; font-size: 42px; margin: 0; margin-top:0;">
                ~1000
            </h1>
        </div>
        ''', unsafe_allow_html=True)

st.write("")

st.markdown('<span style="font-size:22px; color:#DAF7DC">Overview:</span>', unsafe_allow_html=True)
st.markdown('<span style="font-size:14px; color:#FFFFFF">Matthew has worked across three different industries and been exposed to many metrics and analytical ad hoc demands.  In educational assessment, he analyzed and reported on test taker trends, analyses of each test question and its performance, and the scoring of many tests.  In retail, Matthew defined, calculated, and deployed a wide array of metrics across a 7-level product hierarchy.  In healthcare, he has calculated performance guarantees, processed claims data for billing, reviewed provider surveys for compliance, and performed deep dives into the member population and the services used.</span>', unsafe_allow_html=True)

st.markdown('<span style="font-size:22px; color:#DAF7DC">Pseudo-Equivalent Groups (PEG) Equating</span>', unsafe_allow_html=True)
st.markdown('<span style="font-size:14px; color:#FFFFFF">Scoring tests requires accounting for variations in test difficulty and test taker capability in a process called equating. Traditional equating methods were deemed unfit for this particular test product.  Matthew partnered with a senior advisor and two senior psychometricians to implement a novel methodology, pseudo-equivalent groups, to also account for historical trends and rein in scoring drift. Matthew wrote the production code base for this methodology and its supporting outputs since the existing systems could not integrate anything outside the standard methods. The effort was a success and became the default equating method for a major test-taking demographic.</span>', unsafe_allow_html=True)

st.markdown('<span style="font-size:22px; color:#DAF7DC">Assessing Additional Skills</span>', unsafe_allow_html=True)
st.markdown('<span style="font-size:14px; color:#FFFFFF">To increase the appeal of our assessment, the test was expanded to assess an additional skill.  To facilitate this change, Matthew finalized the test changes with the test developers, translated those changes into technical requirements, collaborated with IT to implement the necessary changes while also overseeing the changes needed for his own processes and systems.  He made extensive contributions to the validation efforts and the change was launched without issue.</span>', unsafe_allow_html=True)

st.markdown('<span style="font-size:22px; color:#DAF7DC">Merch 2.0</span>', unsafe_allow_html=True)
st.markdown('<span style="font-size:14px; color:#FFFFFF">Burlington Stores launched a Merch 2.0 initiative to better enable merchandise buyers to chase trends and deliver value to shoppers.  This initiative entailed shifting reporting away from existing Microstrategy reports to Power BI.  However, this was not a simple lift and shift but a re-imagining of what the merchandising org should focus on.  The team and I partnered with Accenture and business stakeholders to discuss user stories, outline report use cases, and define ~100 metrics. During his tenure, Matthew and the team deployed ~20 reports to the ~1000 merchandising user base.  The reports were lauded as game-changers and the CEO touted the impact of the initiative in several earnings calls with investors.</span>', unsafe_allow_html=True)

st.markdown('<span style="font-size:22px; color:#DAF7DC">Shortage Indicator Report</span>', unsafe_allow_html=True)
st.markdown('<span style="font-size:14px; color:#FFFFFF">Shortage is a significant concern for retailers and novel methods to detect and manage it are necessary. Performing inventories is time-intensive and are only possible several times each year.  During his time as temporary Data Science Manager, Matthew and the Data Science team worked with Shortage to define a method by which recurring store activities could predict shrink.  The team landed on using the discrepancy between recorded inventory numbers versus the number of markdown scans performed on merchandise.  There were limitations to this method since markdowns are performed after a product has been in the inventory for some time.  To compensate, results were summarized at a higher level of the product hierarchy to give store staff a sense of what product categories were currently most at-risk in their specific store. Immediately after the its launch, the insights from the SIR helped the Shortage team identify a store team member who had thrown $20k of shoes away rather than stocking shelves.</span>', unsafe_allow_html=True)

# Use the following in terminal (lower side ribbon) to run the app
# streamlit run C:\Users\DrShotts\PycharmProjects\Streamlit\streamlit_app.py