import pandas as pd
from dash import Dash, html, dcc
from dash.dependencies import Output, Input
from src.fresadora import Fresadora

app = Dash(__name__)
app.title = "Monitoreo de Fresadoras CNC"

fresadoras = [Fresadora(i) for i in range(1, 9)]  # 8 fresadoras

app.layout = html.Div([
    html.H1("Sala de Fresadoras CNC", style={'textAlign': 'center'}),
    dcc.Interval(id='actualizador', interval=5000, n_intervals=0),
    html.Div(id='panel-fresadoras')
])

@app.callback(
    Output('panel-fresadoras', 'children'),
    Input('actualizador', 'n_intervals')
)
def actualizar_panel(n):
    panel = []
    for f in fresadoras:
        datos = f.generar_lecturas()
        bloque = html.Div([
            html.H4(f"Fresadora {f.id} - Estado: {f.estado}", style={'color': f.color}),
            html.P(f"Temperatura: {datos['temperatura']} K"),
            html.P(f"Torque: {datos['torque']} Nm"),
            html.P(f"Velocidad: {datos['velocidad']} rpm"),
            html.P(f"Recomendación: {f.recomendacion}")
        ], style={
            'border': f'3px solid {f.color}',
            'borderRadius': '10px',
            'padding': '10px',
            'margin': '10px',
            'width': '45%',
            'display': 'inline-block'
        })
        panel.append(bloque)
    return panel

def iniciar():
    app.run_server(debug=True)
