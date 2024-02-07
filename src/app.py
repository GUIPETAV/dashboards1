from dash import Dash, html, dcc, Input, Output
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime, timedelta

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css']


app = Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)
server = app.server

def side_header():
    return html.Div([
        html.Img(src='/assets/logo.jpeg', style={'height':'200px', 'width':'200px', 'display': 'block', 'margin': 'auto'}),
        html.H2("Captação", style={"text-align": "center", "color": "white"}),
        html.Ul([
            html.Li([html.I(className="fas fa-home", style={"padding-right": "10px"}), html.A("Visão Geral", href='/pag1')], style={"padding-left": "40px", "color": "white"}),
            html.Li([html.I(className="fas fa-font", style={"padding-right": "10px"}), html.A("Fontes", href='/pag2')], style={"padding-left": "40px", "color": "white"}),
            html.Li([html.I(className="fas fa-project-diagram", style={"padding-right": "10px"}), html.A("Projetos", href='/pag3')], style={"padding-left": "40px", "color": "white"}),
        ], style={"list-style-type": "none"})
    ], style={"width": "15%", "float": "left", "background-color": "#002244", "height": "100vh", "color": "white", "padding": "0px", "margin": "0px"})



def layout_pag1():
    return html.Div([
        side_header(),
        html.Div([
            html.Div([
                html.Img(src='/assets/cap.png', 
                         style={'height': '700px', 'width': '700px'}),
            ], style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'height': '100%'}),
            # Outros elementos do conteúdo principal aqui
        ], style={"width": "80%", "float": "left"})
    ])


def layout_pag2():
    return html.Div([
        side_header(),
        html.Div([], style={"width": "80%", "float": "left"})
    ])

def layout_pag3():
    return html.Div([
        side_header(),
        html.Div([], style={"width": "80%", "float": "left"})
    ])

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/pag1' or pathname == '/':
        return layout_pag1()
    elif pathname == '/pag2':
        return layout_pag2()
    elif pathname == '/pag3':
        return layout_pag3()
    else:
        return "Página não encontrada"

if __name__ == '__main__':
    app.run_server(debug=True)
