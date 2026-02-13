
import streamlit as st

# st.sidebar.header("TBD")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom, #336699, #2F4858);
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<span style="font-size:48px; color:#9EE493">**Improving Processes**</span>', unsafe_allow_html=True)
st.write("")

ipxp_col1, ipxp_col2, ipxp_col3 = st.columns(3)

with ipxp_col1:
    st.markdown('''
        <div style="text-align: center;">
            <p style="color: #FFFFFF; font-size: 18px; margin-bottom: 0px;">
                Max weeks cut from process
            </p>
            <h1 style="color: #DAF7DC; font-size: 42px; margin: 0; margin-top:0;">
                4
            </h1>
        </div>
        ''', unsafe_allow_html=True)

with ipxp_col2:
    st.markdown('''
        <div style="text-align: center;">
            <p style="color: #FFFFFF; font-size: 18px; margin-bottom: 0px;">
                Cloud platform migrations
            </p>
            <h1 style="color: #DAF7DC; font-size: 42px; margin: 0; margin-top:0;">
                3
            </h1>
        </div>
        ''', unsafe_allow_html=True)

with ipxp_col3:
    st.markdown('''
        <div style="text-align: center;">
            <p style="color: #FFFFFF; font-size: 18px; margin-bottom: 0px;">
                Supported users
            </p>
            <h1 style="color: #DAF7DC; font-size: 42px; margin: 0; margin-top:0;">
                ~1000
            </h1>
        </div>
        ''', unsafe_allow_html=True)

st.write("")

st.markdown('<span style="font-size:22px; color:#DAF7DC">Overview:</span>', unsafe_allow_html=True)
st.markdown('<span style="font-size:14px; color:#FFFFFF">Matthew began his career using legacy proprietary tools developed decades ago. This early exposure to the inefficiencies and tech debt of legacy systems, as well as an ever-increasing work scope, prompted Matthew to embrace new tools as available. This began with leveraging SAS to handle most incoming analysis and reporting work with an emphasis on file processing to avoid manual work. His team happily adopted this mindset and successfully decreased processing times across the board with a notable accomplishment being a 3-4 week reduction in the processing of an externally published annual report.  </span>', unsafe_allow_html=True)
st.markdown('<span style="font-size:14px; color:#FFFFFF">As data visualizations tools became more prominent, Matthew leaped at the chance to stand up Power BI as the reporting platform for Burlington Stores. While there, he also simultaneously supported the transition from on-premise to a cloud data warehouse, Snowflake. The Power BI reports that he and the team delivered dramatically improved the speed with which the business got results.  What previously could take hours was now available within seconds while also allowing slicing and dicing that was not previously possible.</span>', unsafe_allow_html=True)
st.markdown('<span style="font-size:14px; color:#FFFFFF">Matthew moved to build on that success by joining a startup subsidiary within Horizon Blue Cross Blue Shield named NovaOne Health. At NovaOne, he contributed to the development of various data products within the dbt semantic layer built on top of AWS Redshift and provided insights via AWS Quicksuite. He joined just as the NovaOne began operations with its first customer and fielded questions from the business and the customer about the user base and claims activity.</span>', unsafe_allow_html=True)

st.markdown('<span style="font-size:22px; color:#DAF7DC">Proprietary System Migrations</span>', unsafe_allow_html=True)
with st.expander("Click for details"):
    st.markdown('<span style="font-size:14px; color:#FFFFFF">The legacy score key management (SKM) system which housed the answers to every single test question was becoming too onerous for IT to maintain and a more modernized system named eSKM was developed. Matthew managed the transition through providing specifications to the eSKM team, providing and validating test cases, documenting the changes, and providing production deployment support. The launch was seamless.</span>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<span style="font-size:14px; color:#FFFFFF">The Generalized Analysis System (GENASYS) used by the Analytics department had been developed 30 years ago and struggled to meet current demands. Matthew was selected as part of the team tasked to design its successors given his success optimizing the processes of his assessment products. He regularly participated and advocated for increased interoperability to better support the many new tools being adopted by the department. The development of the new platform extended beyond his time at the company but his suggestions were integrated into the system.</span>', unsafe_allow_html=True)

st.markdown('<span style="font-size:22px; color:#DAF7DC">Microstrategy to Power BI Migration</span>', unsafe_allow_html=True)
with st.expander("Click for details"):
    st.markdown('<span style="font-size:14px; color:#FFFFFF">Burlington Stores had ~20,000 Microstrategy reports prior to the Merch 2.0 initiative.  Given the sheer volume, the leadership team decided that paring down reporting to 10-20 reports and dashboards was necessary. Matthew worked with his team to synthesize the most pressing needs into these essential reports. The merchants had some challenging requirements including a 7-level product hierarchy, multiple alternate hierarchies, 20-30 metrics per report, strict row-level security (RLS), a demand to support both dashboard and paginated report form factors as well as mobile support, and a report refresh schedule as frequent as hourly. There was also tremendous pressure from the business and leadership teams that reports had to load within seconds. These were very challenging requirements and Matthew worked with internal and external partners to fulfill them. There were misses along the way but the reports and dashboards ultimately met user requirements and have been hailed as huge advances compared to previous reporting.</span>', unsafe_allow_html=True)

# st.markdown('<span style="font-size:22px; color:#DAF7DC">Semantic Layer Development</span>', unsafe_allow_html=True)
# st.markdown('<span style="font-size:14px; color:#FFFFFF">Shortage is a significant concern for retailers and novel methods to detect and manage it are necessary. Performing inventories is time-intensive and are only possible several times each year. During his time as temporary Data Science Manager, Matthew and the Data Science team worked with Shortage to define a method by which recurring store activities could predict shrink.  The team landed on using the discrepancy between recorded inventory numbers versus the number of markdown scans performed on merchandise.  There were limitations to this method since markdowns are performed after a product has been in the inventory for some time.  To compensate, results were summarized at a higher level of the product hierarchy to give store staff a sense of what product categories were currently most at-risk in their specific store. Immediately after the its launch, the insights from the SIR helped the Shortage team identify a store team member who had thrown $20k of shoes away rather than stocking shelves.</span>', unsafe_allow_html=True)

