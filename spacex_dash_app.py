import dash
from dash import dcc, html
app = dash.Dash(__name__)
import plotly.express as px
import pandas as pd

# ------------------------------------------------------------------ data
spacex_df = pd.read_csv("data/spacex_launch_dash.csv")
max_payload = int(spacex_df["PayloadMass"].max())
min_payload = int(spacex_df["PayloadMass"].min())

site_options = [{"label": "All Sites", "value": "ALL"}] + [
    {"label": s, "value": s} for s in spacex_df["LaunchSite"].unique()
]

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1("SpaceX Launch Records Dashboard",
            style={"textAlign": "center", "color": "#503D36", "font-size": 40}),

    # TASK 1: launch site dropdown
    dcc.Dropdown(id="site-dropdown", options=site_options,
                 value="ALL", placeholder="Select a Launch Site",
                 searchable=True, style={"width": "80%", "padding": "3px", "font-size": 20}),
    html.Br(),

    # TASK 2: success pie chart
    html.Div(dcc.Graph(id="success-pie-chart")),
    html.Br(),

    html.P("Payload range (Kg):"),
    # TASK 3: payload range slider
    dcc.RangeSlider(id="payload-slider", min=0, max=10000, step=1000,
                    marks={i: str(i) for i in range(0, 10001, 2500)},
                    value=[min_payload, max_payload]),

    # TASK 4: payload vs outcome scatter
    html.Div(dcc.Graph(id="success-payload-scatter-chart")),
])


# TASK 2 callback: pie chart of landing success
@app.callback(dash.dependencies.Output("success-pie-chart", "figure"),
              [dash.dependencies.Input("site-dropdown", "value")])
def get_pie_chart(entered_site):
    data = spacex_df[spacex_df["LaunchSite"] == entered_site] \
        if entered_site != "ALL" else spacex_df
    if entered_site == "ALL":
        fig = px.pie(data, names="LaunchSite", values="Class",
                     title="Total Successful Landings by Site")
    else:
        fig = px.pie(data, names="Class",
                     title=f"Success vs. Failure for site {entered_site}")
    return fig


# TASK 4 callback: payload vs outcome scatter
@app.callback(dash.dependencies.Output("success-payload-scatter-chart", "figure"),
              [dash.dependencies.Input("site-dropdown", "value"),
               dash.dependencies.Input("payload-slider", "value")])
def get_scatter(entered_site, payload_range):
    low, high = payload_range
    data = spacex_df[(spacex_df["PayloadMass"] >= low) &
                     (spacex_df["PayloadMass"] <= high)]
    if entered_site != "ALL":
        data = data[data["LaunchSite"] == entered_site]
    return px.scatter(data, x="PayloadMass", y="Class", color="Booster Version Category"
                      if "Booster Version Category" in data.columns else "Class",
                      title="Payload vs. Launch Outcome")


if __name__ == "__main__":
    app.run_server(debug=True)
