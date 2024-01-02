import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from millify import millify
from streamlit_extras.colored_header import colored_header
from urllib.request import Request, urlopen

st.cache_data.clear()

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

st.markdown(f'<h1 style="color:#434346;font-size:60px;text-align:center;">{"Token Ecosystem Analysis"}</h1>', unsafe_allow_html=True)
st.info("This page explores the Uniswap token ecosystem on L2s, where we unveil the dynamics of listed tokens, top pools, and the most swapped tokens.", icon="ℹ️")
st.warning('Listed tokens include tokens with [warnings](https://support.uniswap.org/hc/en-us/articles/8723118437133). These are tokens not frequently swapped on Uniswap and have not satisfied other quantitative criteria, such as being traded on a leading U.S. centralized exchange.', icon="⚠️")

############################# cache datasets ########################################

url11 = "https://flipsidecrypto.xyz/edit/queries/6a07e76a-e2d7-4e19-994d-ea8fc9ab5cb3"
@st.cache_data
def load_df11():
    req = Request(f"https://api.flipsidecrypto.com/api/v2/queries/{url11.split('/')[-1]}/data/latest", headers={"User-Agent": "Mozilla/5.0"})
    response = urlopen(req).read()
    df11 = pd.read_json(response.decode('utf-8'))
    return df11

url12 = "https://flipsidecrypto.xyz/edit/queries/769501ac-dd3a-4ff4-999b-c1636300b2d6"
@st.cache_data
def load_df12():
    req = Request(f"https://api.flipsidecrypto.com/api/v2/queries/{url12.split('/')[-1]}/data/latest", headers={"User-Agent": "Mozilla/5.0"})
    response = urlopen(req).read()
    df12 = pd.read_json(response.decode('utf-8'))
    return df12

url13 = "https://flipsidecrypto.xyz/edit/queries/28e0cea8-65f2-498d-aa21-de0d531eecbf"
@st.cache_data
def load_df13():
    req = Request(f"https://api.flipsidecrypto.com/api/v2/queries/{url13.split('/')[-1]}/data/latest", headers={"User-Agent": "Mozilla/5.0"})
    response = urlopen(req).read()
    df13 = pd.read_json(response.decode('utf-8'))
    return df13

url14 = "https://flipsidecrypto.xyz/edit/queries/90b45034-cf89-49d2-bf30-ab8906ec385d"
@st.cache_data
def load_df14():
    req = Request(f"https://api.flipsidecrypto.com/api/v2/queries/{url14.split('/')[-1]}/data/latest", headers={"User-Agent": "Mozilla/5.0"})
    response = urlopen(req).read()
    df14 = pd.read_json(response.decode('utf-8'))
    return df14

url15 = "https://flipsidecrypto.xyz/edit/queries/e1b3a5e7-8420-4418-aadb-dd6070c0f7bd"
@st.cache_data
def load_df15():
    req = Request(f"https://api.flipsidecrypto.com/api/v2/queries/{url15.split('/')[-1]}/data/latest", headers={"User-Agent": "Mozilla/5.0"})
    response = urlopen(req).read()
    df15 = pd.read_json(response.decode('utf-8'))
    return df15

url18 = "https://flipsidecrypto.xyz/edit/queries/69c25641-4e12-4e63-9f79-12ebe0542f27"
@st.cache_data
def load_df18():
    req = Request(f"https://api.flipsidecrypto.com/api/v2/queries/{url18.split('/')[-1]}/data/latest", headers={"User-Agent": "Mozilla/5.0"})
    response = urlopen(req).read()
    df18 = pd.read_json(response.decode('utf-8'))
    return df18

url25 = "https://flipsidecrypto.xyz/edit/queries/9ec57d83-0d07-4b46-a481-43d9070d8122"
@st.cache_data
def load_df25():
    req = Request(f"https://api.flipsidecrypto.com/api/v2/queries/{url25.split('/')[-1]}/data/latest", headers={"User-Agent": "Mozilla/5.0"})
    response = urlopen(req).read()
    df25 = pd.read_json(response.decode('utf-8'))
    return df25

############################### load datasets ###########################################

df11 = load_df11()
df12 = load_df12()
df13 = load_df13()
df14 = load_df14()
df15 = load_df15()
df18 = load_df18()
df25 = load_df25()

################################   charts   ##############################################

##########################___________________DF11_____________________######################

df11_fig1 = px.histogram(df11,
                   x="CHAIN",
                   y="SWAP_VOLUME_USD",
                   color="POOL_NAME",
                   title="Top 5 Pools Per Chain By Swap Volume USD [Log Scale]",
                   log_y=True,
                   color_discrete_sequence=px.colors.qualitative.Dark24)
df11_fig1.update_layout(
    yaxis_title="SWAP VOLUME USD")
df11_fig1.update_layout(hovermode="x unified")


##########################___________________DF12_____________________######################

df12_fig1 = px.histogram(df12,
                   x="CHAIN",
                   y="UNIQUE_SWAPPERS",
                   color="TOKEN",
                   title="Top 5 Tokens Swapped From Per Chain By Unique Swappers [Log Scale]",
                   log_y=True,
                   color_discrete_sequence=px.colors.qualitative.Dark24)
df12_fig1.update_layout(
    yaxis_title="UNIQUE SWAPPERS")
df12_fig1.update_layout(hovermode="x unified")

##########################___________________DF13_____________________######################

df13_fig1 = px.histogram(df13,
                   x="CHAIN",
                   y="VOLUME_USD",
                   color="TOKEN",
                   title="Top 5 Tokens Swapped From Per Chain By USD Volume [Log Scale]",
                   log_y=True,
                   color_discrete_sequence=px.colors.qualitative.Light24)
df13_fig1.update_layout(
    yaxis_title="SWAP VOLUME USD")
df13_fig1.update_layout(hovermode="x unified")

##########################___________________DF14_____________________######################

df14_fig1 = px.histogram(df14,
                   x="CHAIN",
                   y="UNIQUE_SWAPPERS",
                   color="TOKEN",
                   title="Top 5 Tokens Swapped To Per Chain By Unique Swappers [Log Scale]",
                   log_y=True,
                   color_discrete_sequence=px.colors.qualitative.Dark24)
df14_fig1.update_layout(
    yaxis_title="UNIQUE SWAPPERS")
df14_fig1.update_layout(hovermode="x unified")

##########################___________________DF15_____________________######################

df15_fig1 = px.histogram(df15,
                   x="CHAIN",
                   y="VOLUME_USD",
                   color="TOKEN",
                   title="Top 5 Tokens Swapped To Per Chain By USD Volume [Log Scale]",
                   log_y=True,
                   color_discrete_sequence=px.colors.qualitative.Light24)

df15_fig1.update_layout(
    yaxis_title="SWAP VOLUME USD")
df15_fig1.update_layout(hovermode="x unified")

##########################___________________DF18_____________________######################

df18_fig1 = px.histogram(df18,
                   x="CHAIN",
                   y="NEW_TOKENS_COUNT",
                   color="CHAIN",
                   title="Tokens Listed per Chain",
                   color_discrete_sequence=px.colors.qualitative.Dark24)

df18_fig1.update_layout(hovermode="x unified")
df18_fig1.update_layout(
    yaxis_title="TOKENS LISTED")
df18_fig1.update_layout(hovermode="x unified")

##########################___________________DF25_____________________######################

df25_fig1 = px.line(df25,
              x="WEEK_START",
              y="NEW_TOKENS_COUNT",
              color="CHAIN",
              title="New Tokens Listed Weekly On Uniswap by Chain")
df25_fig1.update_layout(
    yaxis_title="TOKENS LISTED")
df25_fig1.update_layout(hovermode="x unified")
#################################################### LAYOUT ##############################################

st.plotly_chart(df25_fig1, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url25}")

col_1a, col_1b = st.columns(2)
with col_1a:
    st.plotly_chart(df18_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url18}")

with col_1b:
    st.plotly_chart(df11_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url11}")

col_2a, col_2b = st.columns(2)
with col_2a:
    st.plotly_chart(df13_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url13}")
with col_2b:
    st.plotly_chart(df15_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url15}")

col_3a, col_3b = st.columns(2)
with col_3a:
    st.plotly_chart(df12_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url12}")

with col_3b:
    st.plotly_chart(df14_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url14}")


colored_header(
    label="",
    description="",
    color_name="gray-70",
)

insight_1 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">Polygon boasts the highest number of listed tokens among Layer 2s, totaling an impressive 7571, a statistic aligned with its leading position in terms of active pools per week. Arbitrum follows closely with 5084 listed tokens. It\'s noteworthy, however, that only a fraction of these listed tokens are actively swapped. Notably, there has been a recent surge in token listings on Optimism and Base in recent weeks.</p>'
st.markdown(insight_1, unsafe_allow_html=True)


insight_2 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">The dominance of pools denominated in WETH, stablecoins, and native tokens specific to each Layer 2 is evident when considering trading volume. These categories consistently emerge as the most influential in the overall pool landscape.</p>'
st.markdown(insight_2, unsafe_allow_html=True)


insight_3 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">When examining token swaps, WETH and USDC emerge as the top tokens by volume, except on Avalanche and BSC, where WAVAX and WBNB take precedence. Additionally, on BSC, USDT surpasses USDC in terms of swap volume, setting it apart as the only chain where this particular phenomenon occurs.</p>'
st.markdown(insight_3, unsafe_allow_html=True)

colored_header(
    label="",
    description="",
    color_name="gray-70",
)
