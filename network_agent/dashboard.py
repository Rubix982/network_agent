import streamlit as st
from streamlit_autorefresh import st_autorefresh
import pandas as pd
import constants
import tests

st_autorefresh(interval=2000, key="network_agent")

st.title("Network Statistics")
names: list[str] = [v["display_name"] for v in tests.get_tests().values()]
df: pd.DataFrame = pd.read_csv(constants.NETWORK_AGENT_STATS_FILE, names=names)
st.dataframe(df)
df = tests.normalize_df(dataframe=df)
st.line_chart(df)
