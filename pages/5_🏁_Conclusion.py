import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from millify import millify
from streamlit_extras.colored_header import colored_header

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

st.markdown(f'<h1 style="color:#434346;font-size:60px;text-align:center;">{"Conclusion"}</h1>', unsafe_allow_html=True)
st.info("This page encapsulates the essential takeaways from our exploration, providing a holistic understanding of the state of Uniswap on L2s.", icon="ℹ️")


insight_1 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">As we conclude our examination of Uniswap\'s presence on L2s, certain patterns come into focus. Arbitrum emerges as a dominant force, commanding a significant share of both users and total swap volume, underscoring its appeal for active and high-value trading. Polygon\'s gas fee efficiency and expansive token listings position it as a noteworthy contender, showcasing the importance of cost considerations in user preferences.</p>'
st.markdown(insight_1, unsafe_allow_html=True)


insight_2 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">The influence of airdrop events on user engagement, as exemplified by Optimism\'s case, highlights the potential impact of strategic initiatives on Uniswap\'s adoption. The consistent preference for WETH and USDC in token swaps, reflects the enduring dominance of certain tokens within the Uniswap ecosystem.</p>'
st.markdown(insight_2, unsafe_allow_html=True)


insight_3 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">As Uniswap continues to evolve and adapt to different L2s, understanding these nuanced patterns and user behaviors becomes crucial. Strategies to enhance retention on chains with lower engagement, such as Avalanche and BSC, could further strengthen Uniswap\'s position in the broader DEX landscape.</p>'
st.markdown(insight_3, unsafe_allow_html=True)
