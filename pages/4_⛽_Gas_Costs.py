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
    initial_sidebar_state="auto",
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

url2 = "https://flipsidecrypto.xyz/edit/queries/585330c0-7820-4195-b1a2-faae610a4154"
@st.cache_data
def load_df2():
    req = Request(f"https://api.flipsidecrypto.com/api/v2/queries/{url2.split('/')[-1]}/data/latest", headers={"User-Agent": "Mozilla/5.0"})
    response = urlopen(req).read()
    df2 = pd.read_json(response.decode('utf-8'))
    return df2

df2 = load_df2()

df2_fig1 = px.bar(df2, x='CHAIN', y='AVG_GAS_COST', color='CHAIN')

df2_fig1.update_layout(title='Average Gas Cost (USD) on Uniswap',
                  xaxis_title='Chain',
                  yaxis_title='Average Gas Cost (USD)',
                  hovermode="x unified")

url3 = "https://flipsidecrypto.xyz/edit/queries/37397424-4baf-487f-9437-40ef7db4f41d"
@st.cache_data
def load_df3():
    req = Request(f"https://api.flipsidecrypto.com/api/v2/queries/{url3.split('/')[-1]}/data/latest", headers={"User-Agent": "Mozilla/5.0"})
    response = urlopen(req).read()
    df3 = pd.read_json(response.decode('utf-8'))
    return df3

df3 = load_df3()

df3_fig1 = px.bar(df3, x='CHAIN', y='COST_PER_DOLLAR', color='CHAIN')
df3_fig1.update_layout(title='Average Gas Cost (USD) of Swapping $1 on Uniswap',
                  xaxis_title='Chain',
                  yaxis_title='Average Gas Cost (USD)',
                  hovermode="x unified")

url24 = "https://flipsidecrypto.xyz/edit/queries/531ec317-6c5d-4556-b4c7-d8c7daa46143"
@st.cache_data
def load_df24():
    req = Request(f"https://api.flipsidecrypto.com/api/v2/queries/{url24.split('/')[-1]}/data/latest", headers={"User-Agent": "Mozilla/5.0"})
    response = urlopen(req).read()
    df24 = pd.read_json(response.decode('utf-8'))
    return df24

df24 = load_df24()

###############################___________________DF24_____________________#############################

df24_fig1 = px.line(df24,
              x="WEEK",
              y="AVG_GAS_FEE",
              color="CHAIN",
              title="Weekly Average Gas Fee (USD) On Uniswap")
df24_fig1.update_layout(hovermode="x unified")

st.markdown(f'<h1 style="color:#434346;font-size:60px;text-align:center;">{"Gas Costs"}</h1>', unsafe_allow_html=True)
st.info("This page examines gas cost fluctuations within Uniswap, delving into variations in gas fees across different L2s.", icon="ℹ️")

st.plotly_chart(df24_fig1, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url24}")

col_1a, col_1b = st.columns(2)
with col_1a:
    st.plotly_chart(df2_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url2}")
with col_1b:
    st.plotly_chart(df3_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url3}")

colored_header(
    label="",
    description="",
    color_name="gray-70",
)

insight_1 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">The weekly average gas fee has generally trended downward, but there has been an uptick in gas fee since the end of 2023, particularly on Optimism and Avalanche. This trend is noteworthy, especially when considering the gas fee in USD rather than the native token. The recent rise in Ethereum and other cryptocurrency prices could potentially exacerbate this situation. While users may be paying the same fee on average in crypto tokens, the increase in the value of these tokens translates to a higher dollar cost. For Avalanche in particular, the recent surge in gas fee on December 18, 2023, can be attributed to a network congestion caused by <a href="https://cryptopotato.com/avalanche-network-gas-fees-surge-linked-to-trader-joe-founders-social-experiment/">$BEEG minting</a>.</p>'
st.markdown(insight_1, unsafe_allow_html=True)

insight_2 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">Among Layer 2s, Polygon stands out as the most economical, boasting the lowest average gas cost and the lowest average gas cost for swapping $1. This cost efficiency likely contributes to Polygon\'s dominance, evident in its significantly higher number of active pools compared to other L2s. On the flip side, Optimism and Avalanche emerge as the costliest chains with an average gas cost of $0.5 each.</p>'
st.markdown(insight_2, unsafe_allow_html=True)

colored_header(
    label="",
    description="",
    color_name="gray-70",
)
