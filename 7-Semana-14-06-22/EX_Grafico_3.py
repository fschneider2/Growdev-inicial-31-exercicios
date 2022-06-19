# Mostre a quantidade de homens e mulheres na base de dados.

# import os
# os.system('clear')

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

from funcoes import importar_arquivo, dicionario_e_int

homem = 0
mulher = 0

dados = importar_arquivo()
info = dicionario_e_int(dados)

for i in info:
    if i['sexo'] == 'M':
        homem += 1
    else:
        mulher += 1

valores = [homem, mulher]

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "generos": ["Homem","Mulher"],
    "valores": [homem, mulher]
    
})

fig = px.pie(df, names="generos", values="valores", color="generos")
fig.update_traces(textposition='inside', textinfo='percent+value+label')
app.layout = html.Div(children=[
    html.H1(children='Comparativo de quantidade de Homens e Mulheres'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)