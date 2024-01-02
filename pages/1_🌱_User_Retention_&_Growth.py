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

st.markdown(f'<h1 style="color:#434346;font-size:60px;text-align:center;">{"User Retention & Growth"}</h1>', unsafe_allow_html=True)
st.info("This page dissects user retention rates and growth patterns across Uniswap on Layer 2s. Understanding how users persist on different L2s.", icon="ℹ️")

############################# cache datasets ########################################

url1 = "https://flipsidecrypto.xyz/edit/queries/9eb769df-c80d-40af-81e9-2a9f3d00d95f"
@st.cache_data
def load_df1():
    req = Request(f"https://api.flipsidecrypto.com/api/v2/queries/{url1.split('/')[-1]}/data/latest", headers={"User-Agent": "Mozilla/5.0"})
    response = urlopen(req).read()
    df1 = pd.read_json(response.decode('utf-8'))
    return df1

url6 = "https://flipsidecrypto.xyz/edit/queries/ddca2c5e-2626-4303-bb77-3b7a44152587"
@st.cache_data
def load_df6():
    req = Request(f"https://api.flipsidecrypto.com/api/v2/queries/{url6.split('/')[-1]}/data/latest", headers={"User-Agent": "Mozilla/5.0"})
    response = urlopen(req).read()
    df6 = pd.read_json(response.decode('utf-8'))
    return df6

url16 = "https://flipsidecrypto.xyz/edit/queries/510159c8-01fb-4cfb-8945-532f510bc75c"
@st.cache_data
def load_df16():
    req = Request(f"https://api.flipsidecrypto.com/api/v2/queries/{url16.split('/')[-1]}/data/latest", headers={"User-Agent": "Mozilla/5.0"})
    response = urlopen(req).read()
    df16 = pd.read_json(response.decode('utf-8'))
    return df16

url17 = "https://flipsidecrypto.xyz/edit/queries/87050e70-1b02-4012-973d-6524766ce87b"
@st.cache_data
def load_df17():
    req = Request(f"https://api.flipsidecrypto.com/api/v2/queries/{url17.split('/')[-1]}/data/latest", headers={"User-Agent": "Mozilla/5.0"})
    response = urlopen(req).read()
    df17 = pd.read_json(response.decode('utf-8'))
    return df17

url26 = "https://flipsidecrypto.xyz/edit/queries/fddcceb6-6ee6-4220-8e6f-7b14cf8db853"
@st.cache_data
def load_df26():
    req = Request(f"https://api.flipsidecrypto.com/api/v2/queries/{url26.split('/')[-1]}/data/latest", headers={"User-Agent": "Mozilla/5.0"})
    response = urlopen(req).read()
    df26 = pd.read_json(response.decode('utf-8'))
    return df26

############################### load datasets ###########################################

df1 = load_df1()
df6 = load_df6()
df16 = load_df16()
df17 = load_df17()
df26 = load_df26()

################################   charts   ##############################################


###############################___________________DF1_____________________#############################

df1['PERCENTAGE'] = df1.groupby('CHAIN')['NUM_WALLETS'].transform(lambda x: x / x.sum() * 100)

df1_fig1 = px.bar(df1, x='CHAIN', y='PERCENTAGE', color='TRANSACTION_CATEGORY',
             labels={'PERCENTAGE': 'Percentage of Total Wallets'},
             custom_data=['NUM_WALLETS'], 
             title='Repeating Uniswap Users')

df1_fig1.update_layout(xaxis_title='Chain',
                  yaxis_title='Percentage')
df1_fig1.update_traces(hovertemplate='%{y:.2f}%<br>Number of Wallets: %{customdata[0]:,.0f}')
df1_fig1.update_layout(hovermode="x unified")
df1_fig1.update_layout(legend_title="User Category")

###############################___________________DF6_____________________#############################

df_retail = df6[df6['CATEGORY'] == 'Retail User']
df_whale = df6[df6['CATEGORY'] == 'Whale']

# Bar chart for Retail Users count
df6_fig1 = px.bar(df_retail, x='CHAIN', y='USER_COUNT', color='CHAIN',
                    title='Retail Users Count',
                    labels={'USER_COUNT': 'User Count'})
df6_fig1.update_layout(hovermode="x unified")

# Bar chart for Whales count
df6_fig2 = px.bar(df_whale, x='CHAIN', y='USER_COUNT', color='CHAIN',
                   title='Whales Count [Logarithmic Scale]',
                   log_y=True,
                   labels={'USER_COUNT': 'User Count'})
df6_fig2.update_layout(hovermode="x unified")

# Bar chart for Retail Users txn per user
df6_fig3 = px.bar(df_retail, x='CHAIN', y='TXN_PER_USER', color='CHAIN',
                    title='Transactions per Retail User',
                    labels={'TXN_PER_USER': 'Transactions per User'})
df6_fig3.update_layout(hovermode="x unified")

# Bar chart for Whales txn per user
df6_fig4 = px.bar(df_whale, x='CHAIN', y='TXN_PER_USER', color='CHAIN',
                   title='Transactions per Whale',
                   labels={'TXN_PER_USER': 'Transactions per User'})
df6_fig4.update_layout(hovermode="x unified")

# Bar chart for Retail Users avg swap size
df6_fig5 = px.bar(df_retail, x='CHAIN', y='AVG_SWAP_SIZE', color='CHAIN',
                    title='Retail Users Average Swap Amount ($)',
                    labels={'AVG_SWAP_SIZE': 'Average Swap Amount'})
df6_fig5.update_layout(
    xaxis_title="CHAIN", yaxis_title="AVG_SWAP_AMOUNT")
df6_fig5.update_layout(hovermode="x unified")

# Bar chart for Whales avg swap size
df6_fig6 = px.bar(df_whale, x='CHAIN', y='AVG_SWAP_SIZE', color='CHAIN',
                   title='Whales Average Swap Amount ($)',
                   labels={'AVG_SWAP_SIZE': 'Average Swap Amount'})
df6_fig6.update_layout(
    xaxis_title="CHAIN", yaxis_title="AVG_SWAP_AMOUNT")
df6_fig6.update_layout(hovermode="x unified")

###############################___________________DF16_____________________#############################

df16_fig1 = px.histogram(df16,
                   x="CHAIN",
                   y="TXN_COUNT",
                   color="LABEL_SUBTYPE",
                   title="Top 5 Contract Types Used By Uniswap Users per Chain [Logarithmic Scale]",
                   log_y=True,
                   color_discrete_sequence=px.colors.qualitative.Dark24)
df16_fig1.update_layout(
    xaxis_title="CHAIN",
    yaxis_title="TXN_COUNT",
    legend_title="Contract Type")

df16_fig1.update_layout(hovermode="x unified")

###############################___________________DF17_____________________#############################

df17_fig1 = px.histogram(df17,
                   x="CHAIN",
                   y="TXN_COUNT",
                   color="PROJECT_NAME",
                   title="Top 5 Projects Used By Uniswap Users per Chain [Logarithmic Scale]",
                   log_y=True,
                   color_discrete_sequence=px.colors.qualitative.Dark24)
df17_fig1.update_layout(
    xaxis_title="CHAIN",
    yaxis_title="TXN_COUNT",
    legend_title="Project Name")
df17_fig1.update_layout(hovermode="x unified")

##########################___________________DF26_____________________######################
df26_fig1 = px.line(df26,
              x="WEEK",
              y="NEW_USERS",
              color="CHAIN",
              title="Weekly New Users On Uniswap")
df26_fig1.update_layout(hovermode="x unified")

############################################ ADDED ############################################

url22 = "https://flipsidecrypto.xyz/edit/queries/95beab6d-99e4-4133-ae87-f3f000c46258"
@st.cache_data
def load_df22():
    req = Request(f"https://api.flipsidecrypto.com/api/v2/queries/{url22.split('/')[-1]}/data/latest", headers={"User-Agent": "Mozilla/5.0"})
    response = urlopen(req).read()
    df22 = pd.read_json(response.decode('utf-8'))
    return df22

df22 = load_df22()

df22_fig3 = px.line(df22,
              x="WEEK",
              y="TXN_PER_USER",
              color="CHAIN",
              title="Weekly Uniswap Transactions per User")
df22_fig3.update_layout(hovermode="x unified")


#################################################### LAYOUT ##############################################

st.plotly_chart(df26_fig1, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url26}")

col_1a, col_1b = st.columns([2, 1.2])
with col_1a:
    st.plotly_chart(df22_fig3, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url22}")
with col_1b:
    st.plotly_chart(df1_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url1}")

st.info("Users with an average swap amount of less than 100,000 USD are classified as 'Retail Users', while those with 100,000 USD or more are 'Whales'.", icon="ℹ️")

col_2a, col_2b = st.columns(2)
with col_2a:
    st.plotly_chart(df6_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url6}")
with col_2b:
    st.plotly_chart(df6_fig2, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url6}")

col_3a, col_3b = st.columns(2)
with col_3a:
    st.plotly_chart(df6_fig3, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url6}")
with col_3b:
    st.plotly_chart(df6_fig4, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url6}")

col_4a, col_4b = st.columns(2)
with col_4a:
    st.plotly_chart(df6_fig5, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url6}")
with col_4b:
    st.plotly_chart(df6_fig6, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url6}")

col_5a, col_5b = st.columns(2)
with col_5a:
    st.plotly_chart(df16_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url16}")
with col_5b:
    st.plotly_chart(df17_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url17}")


colored_header(
    label="",
    description="",
    color_name="gray-70",
)

insight_1 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">The influx of new users on Uniswap has witnessed an upward trajectory, particularly during Arbitrum\'s inaugural airdrop. Intriguingly, despite the airdrop being specific to Arbitrum, there was a concurrent rise in new Uniswap users across other L2s during that period. This suggests that initiatives boosting activity on one chain can have a spillover effect on other chains as well.</p>'
st.markdown(insight_1, unsafe_allow_html=True)

insight_2 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">While Optimism may not be the largest player in the broader landscape, Uniswap users on this chain exhibit noteworthy resilience and engagement. They claimed the highest transactions per user on Uniswap from January to May 2022, a surge likely propelled by airdrop enthusiasts eagerly anticipating the much-anticipated first Optimism (OP) airdrop, officially announced in April of the same year.</p>'
st.markdown(insight_2, unsafe_allow_html=True)

insight_3 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">Avalanche stands out for having the lowest retention rate among L2s, with only 18% of Uniswap users engaging in swaps on different days. In contrast, Arbitrum stands as the only L2 where more users swapped on multiple days - 52%, with the remaining 48% swapping on a single-day only.</p>'
st.markdown(insight_3, unsafe_allow_html=True)

insight_4 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">Arbitrum emerges as the haven for whales, boasting an impressive 591, nearly five times greater than Polygon\'s 119. In the realm of retail users, Arbitrum and Polygon share parity, each hosting approximately 2.6 million. However, the average swap amount for retail users on Arbitrum is the highest at around $2,500, a significant leap compared to Polygon\'s $1,000, securing Arbitrum\'s position as the preferred L2 for substantial retail swaps.</p>'
st.markdown(insight_4, unsafe_allow_html=True)

insight_5 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">A closer examination of the types of contracts Uniswap users engage with reveals that bridging takes the lead across all the L2s under scrutiny, excluding Base and BSC. Hop protocol, a token bridging dApp, enjoys particular popularity, especially on Arbitrum and Polygon, underscoring the significance of interoperability in the Uniswap ecosystem.</p>'
st.markdown(insight_5, unsafe_allow_html=True)

colored_header(
    label="",
    description="",
    color_name="gray-70",
)
