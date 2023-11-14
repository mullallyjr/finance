import yfinance as yf
import plotly.graph_objects as go
import pandas as pd

l = ['AAPL', 'MMM']

df_list = []

for t in l:
    df_list.append(pd.DataFrame([yf.Ticker(t).info]))

df = pd.concat(df_list)

print(df)