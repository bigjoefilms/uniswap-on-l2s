import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from millify import millify
from streamlit_extras.colored_header import colored_header
from urllib.request import Request, urlopen

# st.cache_data.clear()

st.set_page_config(
    page_title="Uniswap On L2s",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": None,
        "Report a bug": "https://twitter.com/sageOlamide",
        "About": None
    }
)

#style metric containers
st.markdown("""
<style>
div[data-testid="metric-container"] {
   background-color: #c8d7db;
   border: 1px solid rgba(28, 131, 225, 0.1);
   padding: 5% 5% 5% 10%;
   border-radius: 5px;
   color: rgb(30, 103, 119);
   overflow-wrap: break-word;
}

/* breakline for metric text         */
div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
   overflow-wrap: break-word;
   white-space: break-spaces;
   color: #b0020d;
}
</style>
"""
            , unsafe_allow_html=True)

text_1 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 20px;">Back in November 2018, Uniswap introduced its V1 contract on the Ethereum mainnet, setting the stage for a new kind of decentralized exchange. Fast forward six years, and Uniswap has been on quite a journey, constantly evolving with each new version. But it\'s not just Ethereum—it has spread its wings to different blockchains, attracting more users and becoming a hub for trading.</p>'

text_2 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 20px;">In this dashboard, we\'ll take a closer look at the utilization of Uniswap across the following chains — Arbitrum, Avalanche, Base, BSC, Optimism, and Polygon. While some of these chains may technically be categorized as sidechains rather than exclusively Layer 2, for the sake of clarity, we choose to include them under the broader term of L2. You can refer to this <a href="https://www.web3.university/article/sidechains-vs-layer2s">Web3 University article</a> for a detailed explanation of the distinctions between sidechains and L2s. Now, let\'s delve into the specifics and identify the common trends that shape Uniswap\'s functionality within these scaling chains.</p>'

text_3 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 20px;">The data used for this dashboard is <a href="https://flipsidecrypto.xyz/">Flipside Crypto’s</a>. You can click on the <b>View SQL</b> button under each chart to view the underlying SQL query.</p>'

# st.info("Use the menu on the left to select a page (click on > if closed).", icon="👈")
st.markdown(f'<h1 style="color:#434346;font-size:60px;text-align:center;">{"Uniswap On L2s"}</h1>', unsafe_allow_html=True)


st.markdown(text_1, unsafe_allow_html=True)
st.markdown(text_2, unsafe_allow_html=True)
st.markdown(text_3, unsafe_allow_html=True)


############################# cache datasets ########################################

url7 = "https://flipsidecrypto.xyz/edit/queries/6349f677-143b-4774-94d2-c0704633f365"
@st.cache_data
def load_df7():
    req = Request(f"https://api.flipsidecrypto.com/api/v2/queries/{url7.split('/')[-1]}/data/latest", headers={"User-Agent": "Mozilla/5.0"})
    response = urlopen(req).read()
    df7 = pd.read_json(response.decode('utf-8'))
    return df7

url8 = "https://flipsidecrypto.xyz/edit/queries/67409c8d-a5dd-4b4d-b611-710ef891281b"
@st.cache_data
def load_df8():
    req = Request(f"https://api.flipsidecrypto.com/api/v2/queries/{url8.split('/')[-1]}/data/latest", headers={"User-Agent": "Mozilla/5.0"})
    response = urlopen(req).read()
    df8 = pd.read_json(response.decode('utf-8'))
    return df8

url22 = "https://flipsidecrypto.xyz/edit/queries/95beab6d-99e4-4133-ae87-f3f000c46258"
@st.cache_data
def load_df22():
    req = Request(f"https://api.flipsidecrypto.com/api/v2/queries/{url22.split('/')[-1]}/data/latest", headers={"User-Agent": "Mozilla/5.0"})
    response = urlopen(req).read()
    df22 = pd.read_json(response.decode('utf-8'))
    return df22

########################################################################################
url27 = "https://flipsidecrypto.xyz/edit/queries/44323a13-da6a-4c55-b15e-c6821afd8ca1"
@st.cache_data
def load_df27():
    req = Request(f"https://api.flipsidecrypto.com/api/v2/queries/{url27.split('/')[-1]}/data/latest", headers={"User-Agent": "Mozilla/5.0"})
    response = urlopen(req).read()
    df27 = pd.read_json(response.decode('utf-8'))
    return df27

df27 = load_df27()

###############################___________________DF24_____________________#############################

df27_fig1 = px.line(df27,
              x="WEEK",
              y="ACTIVE_POOLS",
              color="CHAIN",
              title="Uniswap Weekly Active Pools")
df27_fig1.update_layout(hovermode="x unified")

df27_fig2 = px.line(df27,
              x="WEEK",
              y="TOTAL_VOLUME",
              color="CHAIN",
              title="Uniswap Weekly Swap Volume (USD)")
df27_fig2.update_layout(hovermode="x unified")

df27_fig3 = px.line(df27,
              x="WEEK",
              y="AVG_VOLUME",
              color="CHAIN",
              title="Uniswap Weekly Average Volume (USD)")
df27_fig3.update_layout(hovermode="x unified")

df27_fig4 = px.line(df27,
              x="WEEK",
              y="MEDIAN_VOLUME",
              color="CHAIN",
              title="Uniswap Weekly Median Volume (USD)")
df27_fig4.update_layout(hovermode="x unified")

########################################################################################

############################### load datasets ###########################################

df7 = load_df7()
df8 = load_df8()
df22 = load_df22()

################################   charts   ##############################################


###############################___________________DF7_____________________#############################

df7_fig1 = px.pie(df7,
               names='CHAIN',
               values='UNIQUE_USERS',
               title='Unique Users on Uniswap',
               color='CHAIN')

df7_fig2 = px.pie(df7,
               names='CHAIN',
               values='VOLUME',
               title='Swap Volume (USD) on Uniswap',
               color='CHAIN')
df7_fig2.update_traces(hovertemplate='%{label}: $%{value:,.0f}')

# Bar chart for avg swap size by chain
df7_fig3 = px.bar(df7, x='CHAIN', y='AVG_SWAP_SIZE_USD', color='CHAIN',
                    title='Average Swap Size (USD) by Chain',
                    labels={'AVG_SWAP_SIZE_USD': 'Average Swap Size'})
df7_fig3.update_traces(hovertemplate='%{label}: $%{value:,.0f}')

# Bar chart for median swap size by chain
df7_fig4 = px.bar(df7, x='CHAIN', y='MEDIAN_SWAP_SIZE_USD', color='CHAIN',
                   title='Median Swap Size (USD) by Chain',
                   labels={'MEDIAN_SWAP_SIZE_USD': 'Median Swap Size'})
df7_fig4.update_traces(hovertemplate='%{label}: $%{value:,.0f}')

###############################___________________DF8_____________________#############################
# single number
# UNIQUE_USERS	VOLUME	AVG_SWAP_SIZE_USD	MEDIAN_SWAP_SIZE_USD

###############################___________________DF22_____________________#############################

df22_fig1 = px.line(df22,
              x="WEEK",
              y="ACTIVE_USERS",
              color="CHAIN",
              title="Uniswap Weekly Active Users")
df22_fig1.update_layout(hovermode="x unified")

df22_fig2 = px.line(df22,
              x="WEEK",
              y="SWAP_COUNT",
              color="CHAIN",
              title="Uniswap Weekly Swap Count")
df22_fig2.update_layout(hovermode="x unified")

#################################################### LAYOUT #############################################

colored_header(
    label="",
    description="",
    color_name="gray-70",
)
st.markdown(f'<h1 style="color:#434346;font-size:40px;text-align:center;">{"General Overview"}</h1>', unsafe_allow_html=True)
colored_header(
    label="",
    description="",
    color_name="gray-70",
)

col_1a, col_1b, col_1c = st.columns(3)
with col_1a:
    st.metric("Total Swap Volume", f"${millify(df8['VOLUME'].sum(), precision=2)}")
    st.link_button("View SQL", f"{url8}")
with col_1b:
    st.metric("Average Swap Amount", f"${millify(df8['AVG_SWAP_SIZE_USD'].sum(), precision=2)}")
    st.link_button("View SQL", f"{url8}")
with col_1c:
    st.metric("Median Swap Amount", f"${millify(df8['MEDIAN_SWAP_SIZE_USD'].sum(), precision=2)}")
    st.link_button("View SQL", f"{url8}")


col_2a, col_2b = st.columns(2)
with col_2a:
    st.plotly_chart(df7_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url7}")
with col_2b:
    st.plotly_chart(df7_fig2, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url7}")

col_3a, col_3b = st.columns(2)
with col_3a:
    st.plotly_chart(df22_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url22}")
with col_3b:
    st.plotly_chart(df22_fig2, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url22}")

col_4a, col_4b = st.columns(2)
with col_4a:
    st.plotly_chart(df27_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url27}")
with col_4b:
    st.plotly_chart(df27_fig2, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url27}")

col_5a, col_5b = st.columns(2)
with col_5a:
    st.plotly_chart(df27_fig3, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url27}")
with col_5b:
    st.plotly_chart(df27_fig4, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url27}")

colored_header(
    label="",
    description="",
    color_name="gray-70",
)

insight_1 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">Arbitrum and Polygon emerge as prominent L2s on Uniswap, each commanding a substantial 30% share of unique users. However, a deeper analysis reveals Arbitrum\'s dominance, boasting a remarkable 57% share of the total swap volume across all six L2s. This stands 90% higher than Polygon\'s respectable 30% share. The significance lies in the fact that while both platforms attract an equal number of users, Arbitrum users are notably more active, collectively engaging in higher-value swaps compared to their Polygon counterparts.</p>'
st.markdown(insight_1, unsafe_allow_html=True)

insight_2 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">This trend is reinforced when examining the weekly active users and swap volume charts. Despite initial parity between the two L2s, with Polygon even enjoying a higher count of active pools per week, a pivotal shift occurred in March 2023. Notably, this surge in Uniswap activity on Arbitrum coincided with the platform\'s inaugural airdrop in the same month. During the peak of this surge, the third week of March 2023 witnessed an impressive $3.5 billion worth of tokens being swapped on Uniswap via Arbitrum. This data underscores Arbitrum\'s growing prominence and user engagement, suggesting that airdrops can significantly impact the usage and adoption of Uniswap.</p>'
st.markdown(insight_2, unsafe_allow_html=True)

colored_header(
    label="",
    description="",
    color_name="gray-70",
)
