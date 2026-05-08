import dash
from dash import dcc, html, Input, Output, dash_table
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# ─────────────────────────────────────────
# CONFIGURACIONES
# ─────────────────────────────────────────

COLORES = {
    "Meji":  "#D85A30",
    "Txato":  "#1D9E75",
    "Turko": "#378ADD",
    "Iñigo":  "#993556",
    "Txikito":   "#BA7517",
    "Tuflo": "#3b3b3b",
    "Gordo": "#b3b3b3",
    "Lozanías": "#dddddd",
    "Txaki":"#cccccc",
    "Triki": "#888888", 
     "Pulido": "#444444"

}

FONDO   = "#ffffff"#0d1117"
CARD_BG = "#F4F5F6"#161b22"
BORDE   = "#F4F5F6"#30363d"
TEXTO   = "#ff286e"#e6edf3"
MUTED   = "#8b949e"
ROSA    = "#ff286e"



# ─────────────────────────────────────────
# DATOS
# ─────────────────────────────────────────

jugadores= [
"Gordo","Lozanías","Txaki","Triki", "Txikito","Txato","Meji","Turko","Pulido","Iñigo","Tuflo"
]

excel_corredores="./data/startlist_giro_2026.xlsx"
corredores = pd.read_excel(excel_corredores, index_col=0)

equipos = [
{'id': 1, 'nombre': 'Alpecin-Premier Tech',  'jugador':'Gordo'},
{'id': 11, 'nombre': 'Bahrain Victorious',  'jugador':'Triki'},
{'id': 21, 'nombre': 'Bardiani-CSF 7 Saber',  'jugador':'Lozanías'},
{'id': 31, 'nombre': 'Decathlon CMA CGM Team',  'jugador':'Txaki'},
{'id': 41, 'nombre': 'EF Education-EasyPost',  'jugador':'Iñigo'},
{'id': 51, 'nombre': 'Groupama-FDJ United',  'jugador':'Iñigo'},
{'id': 61, 'nombre': 'Lidl-Trek',  'jugador':'Txikito'},
{'id': 71, 'nombre': 'Lotto-Intermarché',  'jugador':'Txaki'},
{'id': 81, 'nombre': 'Movistar Team',  'jugador':'Turko'},
{'id': 91, 'nombre': 'INEOS Grenadiers',  'jugador':'Meji'},
{'id': 101, 'nombre': 'NSN Cycling Team',  'jugador':'Pulido'},
{'id': 111, 'nombre': 'Pinarello-Q36.5 Pro Cycling Team',  'jugador':'Pulido'},
{'id': 121, 'nombre': 'Red Bull-BORA-hansgrohe',  'jugador':'Lozanías'},
{'id': 131, 'nombre': 'Soudal Quick-Step',  'jugador':'Txato'},
{'id': 141, 'nombre': 'Team Jayco-AlUla',  'jugador':'Lozanías'},
{'id': 151, 'nombre': 'Team Picnic PostNL',  'jugador':'Txato'},
{'id': 161, 'nombre': 'Team Polti VisitMalta',  'jugador':'Tuflo'},
{'id': 171, 'nombre': 'Team Visma | Lease a Bike',  'jugador':'Triki'},
{'id': 181, 'nombre': 'Tudor Pro Cycling Team',  'jugador':'Turko'},
{'id': 191, 'nombre': 'UAE Team Emirates-XRG',  'jugador':'Meji'},
{'id': 201, 'nombre': 'Unibet Rose Rockets',  'jugador':'Txikito'},
{'id': 211, 'nombre': 'Uno-X Mobility',  'jugador':'Gordo'},
{'id': 221, 'nombre': 'XDS Astana Team',  'jugador':'Tuflo'},
]

etapas = [
 {'num': 1, 'fecha': '08/05',  'nombre': 'Nesebăr - Burgas',  'km':'147 kms' ,    'tipo': 'llana',        'podio': ['BARTHE Cyril','BAX Sjoerd','LEMMEN Bart']},
{'num': 2, 'fecha': '09/05',  'nombre': 'Burgas - Veliko Tarnovo',  'km':'221 kms' ,    'tipo': 'ondulada',        'podio': []},
{'num': 3, 'fecha': '10/05',  'nombre': 'Plovdiv - Sofia',  'km':'175 kms' ,    'tipo': 'llana',        'podio': []},
{'num': 4, 'fecha': '12/05',  'nombre': 'Catanzaro - Cosenza',  'km':'138 kms' ,    'tipo': 'ondulada',        'podio': []},
{'num': 5, 'fecha': '13/05',  'nombre': 'Praia a Mare - Potenza',  'km':'203 kms' ,    'tipo': 'ondulada',        'podio': []},
{'num': 6, 'fecha': '14/05',  'nombre': 'Paestum - Napels',  'km':'142 kms' ,    'tipo': 'llana',        'podio': []},
{'num': 7, 'fecha': '15/05',  'nombre': 'Formia - Blockhaus',  'km':'244 kms' ,    'tipo': 'montaña',        'podio': []},
{'num': 8, 'fecha': '16/05',  'nombre': 'Chieti - Fermo',  'km':'156 kms' ,    'tipo': 'ondulada',        'podio': []},
{'num': 9, 'fecha': '17/05',  'nombre': 'Cervia - Corno alle Scale',  'km':'184 kms' ,    'tipo': 'montaña',        'podio': []},
{'num': 10, 'fecha': '19/05',  'nombre': 'Viareggio - Massa',  'km':'42 kms' ,    'tipo': 'crono',        'podio': []},
{'num': 11, 'fecha': '20/05',  'nombre': 'Porcari - Chiavari',  'km':'195 kms' ,    'tipo': 'ondulada',        'podio': []},
{'num': 12, 'fecha': '21/05',  'nombre': 'Imperia - Novi Ligure',  'km':'175 kms' ,    'tipo': 'llana',        'podio': []},
{'num': 13, 'fecha': '22/05',  'nombre': 'Alessandria - Verbania',  'km':'189 kms' ,    'tipo': 'ondulada',        'podio': []},
{'num': 14, 'fecha': '23/05',  'nombre': 'Aosta - Pila',  'km':'133 kms' ,    'tipo': 'montaña',        'podio': []},
{'num': 15, 'fecha': '24/05',  'nombre': 'Voghera - Milan',  'km':'157 kms' ,    'tipo': 'llana',        'podio': []},
{'num': 16, 'fecha': '26/05',  'nombre': 'Bellinzona - Carì',  'km':'113 kms' ,    'tipo': 'montaña',        'podio': []},
{'num': 17, 'fecha': '27/05',  'nombre': 'Cassana d`Adda - Andalo',  'km':'202 kms' ,    'tipo': 'ondulada',        'podio': []},
{'num': 18, 'fecha': '28/05',  'nombre': 'Fai della Paganelle - Pieve di Soligo',  'km':'171 kms' ,    'tipo': 'ondulada',        'podio': []},
{'num': 19, 'fecha': '29/05',  'nombre': 'Feltre - Piani di Pezzè',  'km':'151 kms' ,    'tipo': 'montaña',        'podio': []},
{'num': 20, 'fecha': '30/05',  'nombre': 'Gemona del Friuli - Piancavallo',  'km':'200 kms' ,    'tipo': 'montaña',        'podio': []},
{'num': 21, 'fecha': '31/05',  'nombre': 'Rome - Rome',  'km':'131 kms' ,    'tipo': 'llana',        'podio': []},
]

general = pd.DataFrame([
    {"pos": 1,  "corredor": "GROVES Kaden",   "equipo": "Alpecin-Premier Tech",    "dif": "Líder",    "jugador": "Meji"},
    {"pos": 2,  "corredor": "BAYER Tobias",  "equipo": "Alpecin-Premier Tech",  "dif": "+26s",     "jugador": "Txato"},
    {"pos": 3,  "corredor": "BUSATTO Francesco",     "equipo": "Alpecin-Premier Tech",    "dif": "+1m 11s",  "jugador": "Turko"},
    {"pos": 4,  "corredor": "GEENS Jonas",    "equipo": "Alpecin-Premier Tech",   "dif": "+1m 29s",  "jugador": "Meji"},
    {"pos": 5,  "corredor": "PLANCKAERT Edward",     "equipo": "Alpecin-Premier Tech",   "dif": "+1m 42s",  "jugador": "Iñigo"},
    {"pos": 6,  "corredor": "PLOWRIGHT Jensen",    "equipo": "Alpecin-Premier Tech",  "dif": "+2m 50s",  "jugador": "Meji"},
    {"pos": 7,  "corredor": "PRICE-PEJTERSEN Johan", "equipo": "Alpecin-Premier Tech",   "dif": "+3m 43s",  "jugador": "Turko"},
    {"pos": 8,  "corredor": "VERGALLITO Luca",     "equipo": "Alpecin-Premier Tech",  "dif": "+5m 00s",  "jugador": "Tuflo"},
    {"pos": 9,  "corredor": "BUITRAGO Santiago",  "equipo": "Bahrain Victorious",   "dif": "+6m 56s",  "jugador": "Tuflo"},
    {"pos": 10, "corredor": "CARUSO Damiano",    "equipo": "Bahrain Victorious",  "dif": "+1h 4m",   "jugador": "Txikito"},
])

maillots = {
    "🟣 Rosa":        {"corredor": "GROVES Kaden",   "detalle": "+26s sobre 2º"},
    "🟢 Regularidad": {"corredor": "BAYER Tobias",  "detalle": "312 pts"},
    "🔴 Montaña":     {"corredor": "BUSATTO Francesco",    "detalle": "78 pts"},
    "🔵 Equipos":     {"corredor": "Alpecin-Premier Tech","detalle": "3h 42m 08s"},
    "⚫ Farolillo":   {"corredor": "HARPER Chris",    "detalle": "+1h 04m"},
}

puntos_etapa  = {1: 10, 2: 6, 3: 4}
puntos_general = {1: 15, 2: 10, 3: 7, 4: 5, 5: 4, 6: 3, 7: 2, 8: 2, 9: 1, 10: 1}

puntos_maillots_jugador = {"Meji": 20, "Txato": 8, "Turko": 8, "Txikito":8 , "Iñigo":5}  # rosa: 20 / mon: 8 / regular 8  / equip 8 /farol 5



# ─────────────────────────────────────────
# LÓGICA DE PUNTOS
# ─────────────────────────────────────────

def puntos_de_jugador(jugador):
    pts = 0
    for e in etapas:
        for i, corredor in enumerate(e["podio"], 1):
            if corredores.loc[corredores["nombre"] == corredor, "jugador"].values[0] == jugador:
                pts += puntos_etapa.get(i, 0)
    for _, row in general.iterrows():
        if row["jugador"] == jugador:
            pts += puntos_general.get(row["pos"], 0)
    pts += puntos_maillots_jugador.get(jugador, 0)
    return pts

ranking = pd.DataFrame([
    {"jugador": j, "puntos": puntos_de_jugador(j)} for j in jugadores
]).sort_values("puntos", ascending=False).reset_index(drop=True)

# ─────────────────────────────────────────
# APP
# ─────────────────────────────────────────

app = dash.Dash(__name__, title="Quiniela Giro de Italia 🚴")


def card(children, extra_style=None):
    style = {
        "background": CARD_BG,
        "border": f"1px solid {BORDE}",
        "borderRadius": "10px",
        "padding": "16px 20px",
    }
    if extra_style:
        style.update(extra_style)
    return html.Div(children, style=style)

def metric_card(label, value, sub=""):
    return card([
        html.P(label, style={"color": MUTED, "fontSize": "12px", "margin": "0 0 4px"}),
        html.P(value, style={"color": TEXTO, "fontSize": "26px", "fontWeight": "600", "margin": "0"}),
        html.P(sub,   style={"color": MUTED, "fontSize": "11px", "margin": "4px 0 0"}) if sub else None,
    ])

# Layout
app.layout = html.Div(style={"background": FONDO, "minHeight": "100vh", "fontFamily": "system-ui, sans-serif", "color": TEXTO, "padding": "24px"}, children=[

    # Título
    html.Div([
        html.H1("🚴 Quiniela — Giro de Italia", style={"margin": "0", "fontSize": "24px", "fontWeight": "700"}),
        html.P("Dashboard de seguimiento de la bolilla", style={"color": MUTED, "margin": "4px 0 0", "fontSize": "14px"}),
    ], style={"marginBottom": "24px"}),

    # Métricas
    html.Div([
        metric_card("Etapas jugadas", "8", "de 21 totales"),
        metric_card("Líder quiniela", ranking.iloc[0]["jugador"], f"{ranking.iloc[0]['puntos']} pts"),
        metric_card("Corredores activos", str(len(corredores[corredores.estado == "activo"])), f"{len(corredores[corredores.estado == 'retirado'])} retirados"),
        metric_card("Próxima etapa", "E9", "Nápoles → Roma"),
    ], style={"display": "grid", "gridTemplateColumns": "repeat(4, 1fr)", "gap": "12px", "marginBottom": "24px"}),

    # Maillots
    card([
        html.H3("Maillots especiales", style={"margin": "0 0 14px", "fontSize": "14px", "color": MUTED, "fontWeight": "500", "textTransform": "uppercase", "letterSpacing": "0.08em"}),
        html.Div([
            html.Div([
                html.P(maillot, style={"fontSize": "13px", "fontWeight": "600", "margin": "0 0 2px", "color": ROSA}),
                html.P(info["corredor"], style={"fontSize": "13px", "color": TEXTO, "margin": "0"}),
                html.P(info["detalle"],  style={"fontSize": "11px", "color": MUTED, "margin": "2px 0 0"}),
            ], style={"flex": "1", "minWidth": "120px", "borderRight": f"1px solid {BORDE}", "paddingRight": "16px", "marginRight": "16px"})
            for maillot, info in maillots.items()
        ], style={"display": "flex", "flexWrap": "wrap", "gap": "0"}),
    ], {"marginBottom": "24px"}),

    # Tabs
    dcc.Tabs(id="tabs", value="ranking", style={"marginBottom": "16px"}, children=[
        dcc.Tab(label="Clasificación quiniela", value="ranking",    style={"color": MUTED}, selected_style={"color": TEXTO, "background": CARD_BG, "borderTop": f"2px solid {ROSA}"}),
        dcc.Tab(label="Resultados por etapa",   value="etapas",     style={"color": MUTED}, selected_style={"color": TEXTO, "background": CARD_BG, "borderTop": f"2px solid {ROSA}"}),
        dcc.Tab(label="Top 10 general",         value="general",    style={"color": MUTED}, selected_style={"color": TEXTO, "background": CARD_BG, "borderTop": f"2px solid {ROSA}"}),
        dcc.Tab(label="Corredores",             value="corredores", style={"color": MUTED}, selected_style={"color": TEXTO, "background": CARD_BG, "borderTop": f"2px solid {ROSA}"}),
    ]),

    html.Div(id="tab-content"),
])

# ─────────────────────────────────────────
# CALLBACKS
# ─────────────────────────────────────────

@app.callback(Output("tab-content", "children"), Input("tabs", "value"))
def render_tab(tab):

    # ── RANKING ──────────────────────────
    if tab == "ranking":
        fig = go.Figure(go.Bar(
            x=ranking["puntos"],
            y=ranking["jugador"],
            orientation="h",
            marker_color=[COLORES[j] for j in ranking["jugador"]],
            text=ranking["puntos"].astype(str) + " pts",
            textposition="outside",
        ))
        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            font_color=TEXTO, margin=dict(l=0, r=60, t=20, b=20),
            xaxis=dict(showgrid=False, showticklabels=False),
            yaxis=dict(autorange="reversed", tickfont=dict(size=14, color=TEXTO)),
            height=280, showlegend=False,
        )
        medallas = ["🥇", "🥈", "🥉", "", ""]
        
        tabla = html.Table([
            html.Thead(html.Tr([html.Th(c) for c in ["#", "Jugador", "Pts etapas", "Bonus", "Total"]], style={"color": MUTED, "fontSize": "12px"})),
            html.Tbody([
                html.Tr([
                     
                    html.Td({1:"🥇", 2:"🥈", 3:"🥉"}.get(i+1, str(i+1))),
                    html.Td(row["jugador"], style={"fontWeight": "600", "color": COLORES[row["jugador"]]}),
                    html.Td(puntos_de_jugador(row["jugador"]) - puntos_maillots_jugador.get(row["jugador"], 0)),
                    html.Td(puntos_maillots_jugador.get(row["jugador"], 0)),
                    html.Td(row["puntos"], style={"fontWeight": "700"}),
                ], style={"borderBottom": f"1px solid {BORDE}", "fontSize": "14px"})
                for i, (_, row) in enumerate(ranking.iterrows())
            ])
        ], style={"width": "100%", "borderCollapse": "collapse"})
        return card([dcc.Graph(figure=fig, config={"displayModeBar": False}), html.Hr(style={"borderColor": BORDE}), tabla])

    # ── ETAPAS ───────────────────────────
    elif tab == "etapas":
        opciones = [{"label": f"E{e['num']} — {e['nombre']}", "value": e["num"]} for e in etapas]
        return card([
            html.Div([
                dcc.Dropdown(id="etapa-sel", options=opciones, value=1,
                    style={"background": CARD_BG, "color": "#000", "width": "340px"},
                    clearable=False),
            ], style={"marginBottom": "16px"}),
            html.Div(id="etapa-detalle"),
        ])

    # ── GENERAL ──────────────────────────
    elif tab == "general":
        rows = []
        for _, row in general.iterrows():
            medalla = {1:"🥇", 2:"🥈", 3:"🥉"}.get(row["pos"], str(row["pos"]))
            pts = puntos_general.get(row["pos"], 0)
            rows.append(html.Tr([
                html.Td(medalla),
                html.Td(row["corredor"], style={"fontWeight": "500"}),
                html.Td(row["equipo"], style={"color": MUTED}),
                html.Td(row["dif"]),
                html.Td(row["jugador"], style={"color": COLORES.get(row["jugador"], TEXTO), "fontWeight": "600"}),
                html.Td(f"+{pts} pts" if pts else "—", style={"color": "#3fb950"}),
            ], style={"borderBottom": f"1px solid {BORDE}", "fontSize": "14px"}))

        tabla = html.Table([
            html.Thead(html.Tr([html.Th(c) for c in ["Pos", "Corredor", "Equipo", "Dif", "Jugador", "Puntos quiniela"]], style={"color": MUTED, "fontSize": "12px"})),
            html.Tbody(rows),
        ], style={"width": "100%", "borderCollapse": "collapse"})

        # gráfico puntos por jugador desde general
        pts_general = {j: sum(puntos_general.get(r["pos"], 0) for _, r in general.iterrows() if r["jugador"] == j) for j in jugadores}
        fig = go.Figure(go.Bar(
            x=list(pts_general.keys()), y=list(pts_general.values()),
            marker_color=[COLORES[j] for j in pts_general],
            text=[f"{v} pts" for v in pts_general.values()], textposition="outside",
        ))
        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            font_color=TEXTO, margin=dict(l=0, r=0, t=20, b=20),
            yaxis=dict(showgrid=False, showticklabels=False),
            xaxis=dict(tickfont=dict(size=13)),
            height=200, showlegend=False,
            title=dict(text="Puntos acumulados del top 10 por jugador", font=dict(size=13, color=MUTED)),
        )
        return card([dcc.Graph(figure=fig, config={"displayModeBar": False}), html.Hr(style={"borderColor": BORDE}), tabla])

    # ── CORREDORES ───────────────────────
    elif tab == "corredores":
        opts = [{"label": "Todos", "value": "Todos"}] + [{"label": j, "value": j} for j in jugadores]
        return card([
            dcc.Dropdown(id="corredor-filtro", options=opts, value="Todos", clearable=False,
                style={"background": CARD_BG, "color": "#000", "width": "220px", "marginBottom": "16px"}),
            html.Div(id="corredores-tabla"),
        ])

    return html.Div()


@app.callback(Output("etapa-detalle", "children"), Input("etapa-sel", "value"))
def render_etapa(num):
    if num is None:
        return html.Div()
    e = next(et for et in etapas if et["num"] == num)
    tipo_color = {"llana": "#1D9E75", "crono": "#378ADD", "ondulada": "#BA7517", "montaña": "#D85A30"}
    color = tipo_color.get(e["tipo"], MUTED)
    filas = []
    for i, corredor in enumerate(e["podio"], 1):
        jugador = corredores.loc[corredores["nombre"] == corredor, "jugador"].values[0]
        pts = puntos_etapa[i]
        filas.append(html.Tr([
            html.Td({1:"🥇", 2:"🥈", 3:"🥉"}[i], style={"fontSize": "18px"}),
            html.Td(corredor, style={"fontWeight": "500"}),
            html.Td(jugador, style={"color": COLORES.get(jugador, TEXTO), "fontWeight": "600"}),
            html.Td(f"+{pts} pts", style={"color": "#3fb950", "fontWeight": "600"}),
        ], style={"borderBottom": f"1px solid {BORDE}", "fontSize": "14px", "padding": "10px 0"}))
    return html.Div([
        
        html.Span(e["fecha"], style={"background": color + "33", "color": color, "borderRadius": "6px",
            "padding": "3px 10px", "fontSize": "12px", "fontWeight": "600", "marginBottom": "14px", "display": "inline-block"}),
        html.Span("  "),
        html.Span(e["tipo"], style={"background": color + "33", "color": color, "borderRadius": "6px",
            "padding": "3px 10px", "fontSize": "12px", "fontWeight": "600", "marginBottom": "14px", "display": "inline-block"}),
        html.Span("  "),
        html.Span(e["km"], style={"background": color + "33", "color": color, "borderRadius": "6px",
            "padding": "3px 10px", "fontSize": "12px", "fontWeight": "600", "marginBottom": "14px", "display": "inline-block"}),
        html.Table([
            html.Thead(html.Tr([html.Th(c) for c in ["Pos", "Corredor", "Jugador", "Puntos"]], style={"color": MUTED, "fontSize": "12px"})),
            html.Tbody(filas),
        ], style={"width": "100%", "borderCollapse": "collapse", "marginTop": "12px"}),
    ])


@app.callback(Output("corredores-tabla", "children"), Input("corredor-filtro", "value"))
def render_corredores(filtro):
    df = corredores if filtro == "Todos" else corredores[corredores["jugador"] == filtro]
    filas = []
    for _, row in df.iterrows():
        estado_color = "#3fb950" if row["estado"] == "activo" else MUTED
        filas.append(html.Tr([
            html.Td(row["nombre"], style={"fontWeight": "500"}),
            html.Td(row["equipo"], style={"color": MUTED}),
            html.Td(row["pais"],   style={"color": MUTED}),
            html.Td(row["jugador"], style={"color": COLORES.get(row["jugador"], TEXTO), "fontWeight": "600"}),
            html.Td(row["estado"], style={"color": estado_color}),
        ], style={"borderBottom": f"1px solid {BORDE}", "fontSize": "14px"}))
    return html.Table([
        html.Thead(html.Tr([html.Th(c) for c in ["Corredor", "Equipo", "País", "Jugador", "Estado"]], style={"color": MUTED, "fontSize": "12px"})),
        html.Tbody(filas),
    ], style={"width": "100%", "borderCollapse": "collapse"})


if __name__ == "__main__":
    app.run(debug=True, suppress_callback_exceptions=True)
