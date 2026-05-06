import dash


from dash import dcc, html, Input, Output, dash_table
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# ─────────────────────────────────────────
# DATOS
# ─────────────────────────────────────────

jugadores = ["Marco", "Sofia", "Carlos", "Elena", "Javi"]

corredores = pd.DataFrame([
    {"nombre": "Tadej Pogacar",    "equipo": "UAE Team Emirates",  "pais": "SVN", "jugador": "Marco",  "estado": "activo"},
    {"nombre": "Geraint Thomas",   "equipo": "INEOS Grenadiers",   "pais": "GBR", "jugador": "Sofia",  "estado": "activo"},
    {"nombre": "Jonathan Milan",   "equipo": "Lidl-Trek",          "pais": "ITA", "jugador": "Carlos", "estado": "activo"},
    {"nombre": "Ben O'Connor",     "equipo": "Decathlon AG2R",     "pais": "AUS", "jugador": "Marco",  "estado": "activo"},
    {"nombre": "Filippo Ganna",    "equipo": "INEOS Grenadiers",   "pais": "ITA", "jugador": "Elena",  "estado": "activo"},
    {"nombre": "Tim Merlier",      "equipo": "Soudal Quick-Step",  "pais": "BEL", "jugador": "Javi",   "estado": "activo"},
    {"nombre": "Andrea Vendrame",  "equipo": "Decathlon AG2R",     "pais": "ITA", "jugador": "Sofia",  "estado": "activo"},
    {"nombre": "Einer Rubio",      "equipo": "Movistar",           "pais": "COL", "jugador": "Carlos", "estado": "activo"},
    {"nombre": "Koen Bouwman",     "equipo": "Visma-LAB",          "pais": "NED", "jugador": "Elena",  "estado": "activo"},
    {"nombre": "Jai Hindley",      "equipo": "BORA-hansgrohe",     "pais": "AUS", "jugador": "Javi",   "estado": "activo"},
    {"nombre": "Magnus Cort",      "equipo": "Uno-X",              "pais": "DEN", "jugador": "Marco",  "estado": "activo"},
    {"nombre": "Filippo Zana",     "equipo": "Jayco AlUla",        "pais": "ITA", "jugador": "Elena",  "estado": "activo"},
    {"nombre": "Vincenzo Nibali",  "equipo": "Astana",             "pais": "ITA", "jugador": "Sofia",  "estado": "retirado"},
    {"nombre": "Mikel Landa",      "equipo": "Soudal Quick-Step",  "pais": "ESP", "jugador": "Carlos", "estado": "retirado"},
    {"nombre": "Romain Bardet",    "equipo": "dsm-firmenich",      "pais": "FRA", "jugador": "Elena",  "estado": "retirado"},
    {"nombre": "Tom Pidcock",      "equipo": "INEOS Grenadiers",   "pais": "GBR", "jugador": "Javi",   "estado": "retirado"},
])

etapas = [
    {"num": 1,  "nombre": "Venecia → Trieste",       "tipo": "llana",        "podio": ["Tim Merlier", "Jonathan Milan", "Filippo Ganna"]},
    {"num": 2,  "nombre": "Cesenatico → Bolonia",    "tipo": "media montaña","podio": ["Tadej Pogacar", "Geraint Thomas", "Einer Rubio"]},
    {"num": 3,  "nombre": "Módena → Viadana",        "tipo": "llana",        "podio": ["Tim Merlier", "Jonathan Milan", "Andrea Vendrame"]},
    {"num": 4,  "nombre": "Acqui Terme → Andora",    "tipo": "media montaña","podio": ["Ben O'Connor", "Andrea Vendrame", "Koen Bouwman"]},
    {"num": 5,  "nombre": "Genova → Lucca",          "tipo": "llana",        "podio": ["Jonathan Milan", "Tim Merlier", "Filippo Ganna"]},
    {"num": 6,  "nombre": "Viareggio → Rapolano",    "tipo": "media montaña","podio": ["Tadej Pogacar", "Ben O'Connor", "Geraint Thomas"]},
    {"num": 7,  "nombre": "Foligno → Perugia",       "tipo": "montaña",      "podio": ["Tadej Pogacar", "Einer Rubio", "Jai Hindley"]},
    {"num": 8,  "nombre": "Spoleto → Prati di Tivo", "tipo": "alta montaña", "podio": ["Ben O'Connor", "Tadej Pogacar", "Geraint Thomas"]},
]

general = pd.DataFrame([
    {"pos": 1,  "corredor": "Tadej Pogacar",   "equipo": "UAE",    "dif": "Líder",    "jugador": "Marco"},
    {"pos": 2,  "corredor": "Geraint Thomas",  "equipo": "INEOS",  "dif": "+26s",     "jugador": "Sofia"},
    {"pos": 3,  "corredor": "Einer Rubio",     "equipo": "MOV",    "dif": "+1m 11s",  "jugador": "Carlos"},
    {"pos": 4,  "corredor": "Ben O'Connor",    "equipo": "AG2R",   "dif": "+1m 29s",  "jugador": "Marco"},
    {"pos": 5,  "corredor": "Jai Hindley",     "equipo": "BORA",   "dif": "+1m 42s",  "jugador": "Javi"},
    {"pos": 6,  "corredor": "Koen Bouwman",    "equipo": "Visma",  "dif": "+2m 50s",  "jugador": "Elena"},
    {"pos": 7,  "corredor": "Andrea Vendrame", "equipo": "AG2R",   "dif": "+3m 43s",  "jugador": "Sofia"},
    {"pos": 8,  "corredor": "Magnus Cort",     "equipo": "Uno-X",  "dif": "+5m 00s",  "jugador": "Marco"},
    {"pos": 9,  "corredor": "Jonathan Milan",  "equipo": "Trek",   "dif": "+6m 56s",  "jugador": "Carlos"},
    {"pos": 10, "corredor": "Filippo Zana",    "equipo": "Jayco",  "dif": "+1h 4m",   "jugador": "Elena"},
])

maillots = {
    "🟣 Rosa":        {"corredor": "Tadej Pogacar",   "detalle": "+26s sobre 2º"},
    "🟢 Regularidad": {"corredor": "Jonathan Milan",  "detalle": "312 pts"},
    "🔴 Montaña":     {"corredor": "Ben O'Connor",    "detalle": "78 pts"},
    "🔵 Equipos":     {"corredor": "UAE Team Emirates","detalle": "3h 42m 08s"},
    "⚫ Farolillo":   {"corredor": "Filippo Zana",    "detalle": "+1h 04m"},
}

puntos_etapa  = {1: 10, 2: 6, 3: 4}
puntos_general = {1: 15, 2: 10, 3: 7, 4: 5, 5: 4, 6: 3, 7: 2, 8: 2, 9: 1, 10: 1}
puntos_maillots_jugador = {"Marco": 20+8, "Carlos": 8, "Elena": 8+5}  # rosa+mont / regular / equip+farol

COLORES = {
    "Marco":  "#D85A30",
    "Sofia":  "#1D9E75",
    "Carlos": "#378ADD",
    "Elena":  "#993556",
    "Javi":   "#BA7517",
}

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

app = dash.Dash(__name__, title="Txikigiro de Italia 🚴")

server = app.server  # 🔴 obligatorio para Render

FONDO   = "#0d1117"
CARD_BG = "#161b22"
BORDE   = "#30363d"
TEXTO   = "#e6edf3"
MUTED   = "#8b949e"
ROSA    = "#E91E8C"

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
                    html.Td(f"{medallas[i]} {i+1}"),
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
    tipo_color = {"llana": "#1D9E75", "media montaña": "#378ADD", "montaña": "#BA7517", "alta montaña": "#D85A30"}
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
        html.Span(e["tipo"], style={"background": color + "33", "color": color, "borderRadius": "6px",
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
    app.run(debug=True)
