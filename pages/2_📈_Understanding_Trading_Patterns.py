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

st.markdown(f'<h1 style="color:#434346;font-size:60px;text-align:center;">{"Understanding Trading Patterns"}</h1>', unsafe_allow_html=True)
st.info("This page delves into user trading patterns on Uniswap across Layer 2s, exploring evolving trading behaviors and trends.", icon="ℹ️")


############################# cache datasets ########################################

url4 = "https://flipsidecrypto.xyz/edit/queries/d66c80a7-ce8f-419e-ad7d-9319c543f30a"
@st.cache_data
def load_df4():
    req = Request(f"https://api.flipsidecrypto.com/api/v2/queries/{url4.split('/')[-1]}/data/latest", headers={"User-Agent": "Mozilla/5.0"})
    response = urlopen(req).read()
    df4 = pd.read_json(response.decode('utf-8'))
    return df4

url5 = "https://flipsidecrypto.xyz/edit/queries/ada13e9c-7e25-4618-9f24-9e27c6b09c1a"
@st.cache_data
def load_df5():
    req = Request(f"https://api.flipsidecrypto.com/api/v2/queries/{url5.split('/')[-1]}/data/latest", headers={"User-Agent": "Mozilla/5.0"})
    response = urlopen(req).read()
    df5 = pd.read_json(response.decode('utf-8'))
    return df5

url10 = "https://flipsidecrypto.xyz/edit/queries/29687135-0e8f-47af-a84b-2b148fee1db9"
@st.cache_data
def load_df10():
    req = Request(f"https://api.flipsidecrypto.com/api/v2/queries/{url10.split('/')[-1]}/data/latest", headers={"User-Agent": "Mozilla/5.0"})
    response = urlopen(req).read()
    df10 = pd.read_json(response.decode('utf-8'))
    return df10

url9 = "https://flipsidecrypto.xyz/edit/queries/8e4b199c-1f8e-42be-bbfb-3829be128ede"
@st.cache_data
def load_df9():
    req = Request(f"https://api.flipsidecrypto.com/api/v2/queries/{url9.split('/')[-1]}/data/latest", headers={"User-Agent": "Mozilla/5.0"})
    response = urlopen(req).read()
    df9 = pd.read_json(response.decode('utf-8'))
    return df9

url21 = "https://flipsidecrypto.xyz/edit/queries/c61e84bf-7ef2-49bf-b5fe-4211c3d19777"
@st.cache_data
def load_df21():
    req = Request(f"https://api.flipsidecrypto.com/api/v2/queries/{url21.split('/')[-1]}/data/latest", headers={"User-Agent": "Mozilla/5.0"})
    response = urlopen(req).read()
    df21 = pd.read_json(response.decode('utf-8'))
    return df21

url23 = "https://flipsidecrypto.xyz/edit/queries/c3097631-5447-419e-97b6-577886c02600"
@st.cache_data
def load_df23():
    req = Request(f"https://api.flipsidecrypto.com/api/v2/queries/{url23.split('/')[-1]}/data/latest", headers={"User-Agent": "Mozilla/5.0"})
    response = urlopen(req).read()
    df23 = pd.read_json(response.decode('utf-8'))
    return df23

############################### load datasets ###########################################

df4 = load_df4()
df5 = load_df5()
df10 = load_df10()
df9 = load_df9()
df21 = load_df21()
df23 = load_df23()

################################   charts   ##############################################

##########################___________________DF4_____________________######################

rename_dict = {
    'DATE': 'Date',
    'ARBITRUM_CHANGE': 'Arbitrum',
    'AVALANCHE_CHANGE': 'Avalanche',
    'BASE_CHANGE': 'Base',
    'BSC_CHANGE': 'BSC',
    'OPTIMISM_CHANGE': 'Optimism',
    'POLYGON_CHANGE': 'Polygon'
}
df4.rename(columns=rename_dict, inplace=True)

##########################___________________DF5_____________________######################

rename_dict = {
    'DATE': 'Date',
    'ARBITRUM_CHANGE': 'Arbitrum',
    'AVALANCHE_CHANGE': 'Avalanche',
    'BASE_CHANGE': 'Base',
    'BSC_CHANGE': 'BSC',
    'OPTIMISM_CHANGE': 'Optimism',
    'POLYGON_CHANGE': 'Polygon'
}
df5.rename(columns=rename_dict, inplace=True)

##########################___________________DF10_____________________######################

df10_1 = df10[df10['CHAIN'] == 'Arbitrum']
df10_1['volume_usd'] = df10_1['volume'].map('${:,.0f}'.format)

df10_fig1 = px.scatter(df10_1,
                 x="hour",
                 y="day",
                 size="volume",
                 size_max=20,
                 color="volume",
                 hover_data={'volume':False,
                             'day':True,
                             'hour':True,
                             'volume_usd':True
                            },
                 title="Volume Distribution on Uniswap for Arbitrum by Hour and Weekday [30D]")


df10_2 = df10[df10['CHAIN'] == 'Avalanche']
df10_2['volume_usd'] = df10_2['volume'].map('${:,.0f}'.format)

df10_fig2 = px.scatter(df10_2,
                 x="hour",
                 y="day",
                 size="volume",
                 size_max=20,
                 color="volume",
                 hover_data={'volume':False,
                             'day':True,
                             'hour':True,
                             'volume_usd':True
                            },
                 title="Volume Distribution on Uniswap for Avalanche by Hour and Weekday [30D]")


df10_3 = df10[df10['CHAIN'] == 'Base']
df10_3['volume_usd'] = df10_3['volume'].map('${:,.0f}'.format)

df10_fig3 = px.scatter(df10_3,
                 x="hour",
                 y="day",
                 size="volume",
                 size_max=20,
                 color="volume",
                 hover_data={'volume':False,
                             'day':True,
                             'hour':True,
                             'volume_usd':True
                            },
                 title="Volume Distribution on Uniswap for Base by Hour and Weekday [30D]")


df10_4 = df10[df10['CHAIN'] == 'BSC']
df10_4['volume_usd'] = df10_4['volume'].map('${:,.0f}'.format)

df10_fig4 = px.scatter(df10_4,
                 x="hour",
                 y="day",
                 size="volume",
                 size_max=20,
                 color="volume",
                 hover_data={'volume':False,
                             'day':True,
                             'hour':True,
                             'volume_usd':True
                            },
                 title="Volume Distribution on Uniswap for BSC by Hour and Weekday [30D]")


df10_5 = df10[df10['CHAIN'] == 'Optimism']
df10_5['volume_usd'] = df10_5['volume'].map('${:,.0f}'.format)

df10_fig5 = px.scatter(df10_5,
                 x="hour",
                 y="day",
                 size="volume",
                 size_max=20,
                 color="volume",
                 hover_data={'volume':False,
                             'day':True,
                             'hour':True,
                             'volume_usd':True
                            },
                 title="Volume Distribution on Uniswap for Optimism by Hour and Weekday [30D]")


df10_6 = df10[df10['CHAIN'] == 'Polygon']
df10_6['volume_usd'] = df10_6['volume'].map('${:,.0f}'.format)

df10_fig6 = px.scatter(df10_6,
                 x="hour",
                 y="day",
                 size="volume",
                 size_max=20,
                 color="volume",
                 hover_data={'volume':False,
                             'day':True,
                             'hour':True,
                             'volume_usd':True
                            },
                 title="Volume Distribution on Uniswap for Polygon by Hour and Weekday [30D]")

##########################___________________DF9_____________________######################

df9_1 = df9[df9['CHAIN'] == 'Arbitrum']
df9_fig1 = px.bar(df9_1,
               x='CATEGORY',
               y='TXN_COUNT',
               log_y=True,
               title='Swap $ Distribution by Txn Count on Arb [Log]',)
#               labels={'USER_COUNT': 'User Count'})
df9_fig1.update_layout(hovermode="x unified")

df9_2 = df9[df9['CHAIN'] == 'Avalanche']
df9_fig2 = px.bar(df9_2,
               x='CATEGORY',
               y='TXN_COUNT',
               log_y=True,
               title='Swap $ Distribution by Txn Count on Ava [Log]',)
#               labels={'USER_COUNT': 'User Count'})
df9_fig2.update_layout(hovermode="x unified")

df9_3 = df9[df9['CHAIN'] == 'Base']
df9_fig3 = px.bar(df9_3,
               x='CATEGORY',
               y='TXN_COUNT',
               log_y=True,
               title='Swap $ Distribution by Txn Count on Base [Log]',)
#               labels={'USER_COUNT': 'User Count'})
df9_fig3.update_layout(hovermode="x unified")

df9_4 = df9[df9['CHAIN'] == 'BSC']
df9_fig4 = px.bar(df9_4,
               x='CATEGORY',
               y='TXN_COUNT',
               log_y=True,
               title='Swap $ Distribution by Txn Count on BSC [Log]',)
#               labels={'USER_COUNT': 'User Count'})
df9_fig4.update_layout(hovermode="x unified")

df9_5 = df9[df9['CHAIN'] == 'Optimism']
df9_fig5 = px.bar(df9_5,
               x='CATEGORY',
               y='TXN_COUNT',
               log_y=True,
               title='Swap $ Distribution by Txn Count on Optim [Log]',)
#               labels={'USER_COUNT': 'User Count'})
df9_fig5.update_layout(hovermode="x unified")

df9_6 = df9[df9['CHAIN'] == 'Polygon']
df9_fig6 = px.bar(df9_6,
               x='CATEGORY',
               y='TXN_COUNT',
               log_y=True,
               title='Swap $ Distribution by Txn Count on Poly [Log]',)
#               labels={'USER_COUNT': 'User Count'})
df9_fig6.update_layout(hovermode="x unified")

##########################___________________DF21_____________________######################

df21_1 = df21[df21['CHAIN'] == 'Arbitrum']
df21_1['PCT_SHARE'] = df21_1.groupby('WEEK')['SWAP_VOLUME'].transform(lambda x: x / x.sum() * 100)

df21_fig1 = px.area(df21_1,
              x="WEEK",
              y="PCT_SHARE",
              color="DEX",
              title="Market Share of DEXs on Arbitrum by USD Swap Volume")
df21_fig1.update_layout(hovermode="x unified")


df21_2 = df21[df21['CHAIN'] == 'Avalanche']
df21_2['PCT_SHARE'] = df21_2.groupby('WEEK')['SWAP_VOLUME'].transform(lambda x: x / x.sum() * 100)

df21_fig2 = px.area(df21_2,
              x="WEEK",
              y="PCT_SHARE",
              color="DEX",
              title="Market Share of DEXs on Avalanche by USD Swap Volume")
df21_fig2.update_layout(hovermode="x unified")


df21_3 = df21[df21['CHAIN'] == 'Base']
df21_3['PCT_SHARE'] = df21_3.groupby('WEEK')['SWAP_VOLUME'].transform(lambda x: x / x.sum() * 100)

df21_fig3 = px.area(df21_3,
              x="WEEK",
              y="PCT_SHARE",
              color="DEX",
              title="Market Share of DEXs on Base by USD Swap Volume")
df21_fig3.update_layout(hovermode="x unified")

df21_4 = df21[df21['CHAIN'] == 'BSC']
df21_4['PCT_SHARE'] = df21_4.groupby('WEEK')['SWAP_VOLUME'].transform(lambda x: x / x.sum() * 100)

df21_fig4 = px.area(df21_4,
              x="WEEK",
              y="PCT_SHARE",
              color="DEX",
              title="Market Share of DEXs on BSC by USD Swap Volume")
df21_fig4.update_layout(hovermode="x unified")


df21_5 = df21[df21['CHAIN'] == 'Optimism']
df21_5['PCT_SHARE'] = df21_5.groupby('WEEK')['SWAP_VOLUME'].transform(lambda x: x / x.sum() * 100)

df21_fig5 = px.area(df21_5,
              x="WEEK",
              y="PCT_SHARE",
              color="DEX",
              title="Market Share of DEXs on Optimism by USD Swap Volume")
df21_fig5.update_layout(hovermode="x unified")


df21_6 = df21[df21['CHAIN'] == 'Polygon']
df21_6['PCT_SHARE'] = df21_6.groupby('WEEK')['SWAP_VOLUME'].transform(lambda x: x / x.sum() * 100)

df21_fig6 = px.area(df21_6,
              x="WEEK",
              y="PCT_SHARE",
              color="DEX",
              title="Market Share of DEXs on Polygon by USD Swap Volume")
df21_fig6.update_layout(hovermode="x unified")

##########################___________________DF23_____________________######################

df23_fig1 = px.line(df23,
              x="WEEK_START",
              y="AVG_TIME_DIFF_SECONDS",
              color="CHAIN",
              title="Weekly Average Time Difference (in seconds) Between Swaps On Uniswap",
              labels={'WEEK_START': 'WEEK'})
df23_fig1.update_layout(hovermode="x unified")
df23_fig1.update_layout(
    xaxis_title="WEEK")    

#################################################### LAYOUT ##############################################

st.plotly_chart(df23_fig1, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url23}")

col_1a, col_1b = st.columns([3, 1])
with col_1a:
    tab1, tab2 = st.tabs(["Swap Volume Change [10D]", "Unique Users Change [10D]"])
    with tab1:
        st.subheader("Day-over-Day Changes in Swap Volume Over The Last 10 Days")
        st.dataframe(df4)
        st.link_button("View SQL", f"{url4}")
    with tab2:
        st.subheader("Day-over-Day Changes in Unique Users Over The Last 10 Days")
        st.dataframe(df5)
        st.link_button("View SQL", f"{url5}")

with col_1b:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    insight_1 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 16px;">Uniswap users on Avalanche exhibit a distinctive trading behavior characterized by less frequent transactions in quick succession, notably reflected in the platform\'s high time difference (in seconds) between swaps per week. It\'s worth considering that this pattern may stem from the relatively recent integration of Uniswap on Avalanche. A parallel can be drawn to Arbitrum\'s early phase on Uniswap, where similar intervals were observed, suggesting that the trading dynamics could evolve over time as Uniswap becomes more established on Avalanche.</p>'
    st.markdown(insight_1, unsafe_allow_html=True)

tab3, tab4 = st.tabs(["Swap Volume Distribution on Uniswap by Hour and Weekday [30D]", "User Distribution by Transaction Count [All Time]"])

with tab3:
    col_4a, col_4b = st.columns(2)
    with col_4a:
        st.plotly_chart(df10_fig1, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url10}")
    with col_4b:
        st.plotly_chart(df10_fig2, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url10}")

    col_5a, col_5b, = st.columns(2)
    with col_5a:
        st.plotly_chart(df10_fig3, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url10}")
    with col_5b:
        st.plotly_chart(df10_fig4, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url10}")

    col_6a, col_6b, = st.columns(2)
    with col_6a:
        st.plotly_chart(df10_fig5, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url10}")
    with col_6b:
        st.plotly_chart(df10_fig6, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url10}")

with tab4:
    col_2a, col_2b, col_2c = st.columns(3)
    with col_2a:
        st.plotly_chart(df9_fig1, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url9}")
    with col_2b:
        st.plotly_chart(df9_fig2, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url9}")
    with col_2c:
        st.plotly_chart(df9_fig3, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url9}")

    col_3a, col_3b, col_3c = st.columns(3)
    with col_3a:
        st.plotly_chart(df9_fig4, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url9}")
    with col_3b:
        st.plotly_chart(df9_fig5, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url9}")
    with col_3c:
        st.plotly_chart(df9_fig6, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url9}")

colored_header(
    label="",
    description="",
    color_name="gray-70",
)

insight_2 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">Thursdays, between 13:00 UTC and 17:00 UTC has been the most active time period by swap volume in the last 30 days across all 6 L2s.</p>'
st.markdown(insight_2, unsafe_allow_html=True)

colored_header(
    label="",
    description="",
    color_name="gray-70",
)

col_7a, col_7b = st.columns(2)
with col_7a:
    st.plotly_chart(df21_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url21}")
with col_7b:
    st.plotly_chart(df21_fig2, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url21}")

col_8a, col_8b = st.columns(2)
with col_8a:
    st.plotly_chart(df21_fig3, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url21}")
with col_8b:
    st.plotly_chart(df21_fig4, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url21}")

col_9a, col_9b = st.columns(2)
with col_9a:
    st.plotly_chart(df21_fig5, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url21}")
with col_9b:
    st.plotly_chart(df21_fig6, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url21}")

colored_header(
    label="",
    description="",
    color_name="gray-70",
)

insight_3 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">Except for Avalanche, where Trader Joe holds dominance, and BSC, where Pancakeswap reigns supreme, Uniswap commands the lion\'s share of swap volume among decentralized exchanges (DEXs) across the remaining four chains. Notably, on chains like Base, where Uniswap was initially unavailable, its subsequent launch resulted in a substantial market shift, eroding the market share of existing alternatives like Balancer. This underscores Uniswap\'s status as a household name, with users demonstrating a readiness to transition from other platforms to leverage its services once it becomes accessible.</p>'
st.markdown(insight_3, unsafe_allow_html=True)

colored_header(
    label="",
    description="",
    color_name="gray-70",
)
