# generate_chart.py
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("files/precos_btc.csv", parse_dates=["timestamp"])

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df['timestamp'],
    y=df['preco'],
    mode='lines+markers',
    name='BTC/USD'
))

fig.update_layout(
    title='Variação do preço do Bitcoin (Coinbase)',
    xaxis_title='Horário',
    yaxis_title='Preço em USD',
)

fig.write_html("files/grafico_btc.html", auto_open=False)
