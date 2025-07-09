import pandas as pd
import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
import plotly.express as px

# Load data
merged_df = pd.read_csv('../data/processed/final_merged.csv', parse_dates=['timestamp'])

# Initialize the Dash app
app = dash.Dash(__name__)
app.title = "ThreatSight AI – Anomaly Detection Dashboard"

# Layout
app.layout = html.Div([
    html.H1("📊 ThreatSight AI: Anomaly Detection on Web Server Logs", style={"textAlign": "center", "fontWeight": "bold", "marginBottom": "30px"}),

    html.Div([
        html.Label("Select Anomaly Detection Source:", style={"fontWeight": "bold"}),
        dcc.Dropdown(
            id='model-selector',
            options=[
                {'label': 'Isolation Forest', 'value': 'pred_if'},
                {'label': 'Autoencoder', 'value': 'pred_ae'},
                {'label': 'Both Models', 'value': 'both'}
            ],
            value='both',
            style={'fontWeight': 'normal'}
        )
    ], style={'width': '40%', 'margin': 'auto'}),

    html.Div([
        dcc.Graph(id='time-series-anomalies'),
        dcc.Graph(id='recon-error-plot'),
        dcc.Graph(id='url-bar-chart')
    ], style={"marginTop": "40px"}),

    html.H3("🧾 Detailed Anomalous Events", style={"textAlign": "center", "marginTop": "40px"}),

    dash_table.DataTable(
        id='anomaly-table',
        columns=[
            {"name": "Timestamp", "id": "timestamp"},
            {"name": "URL", "id": "url"},
            {"name": "Isolation Forest", "id": "pred_if"},
            {"name": "Autoencoder", "id": "pred_ae"}
        ],
        page_size=10,
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'left', 'fontFamily': 'Arial', 'padding': '8px'},
        style_header={
            'backgroundColor': 'rgb(230, 230, 230)',
            'fontWeight': 'bold'
        }
    )
])

# Callbacks
@app.callback(
    [
        Output('time-series-anomalies', 'figure'),
        Output('recon-error-plot', 'figure'),
        Output('url-bar-chart', 'figure'),
        Output('anomaly-table', 'data')
    ],
    [Input('model-selector', 'value')]
)
def update_dashboard(model_choice):
    if model_choice == 'both':
        df_filtered = merged_df[(merged_df['pred_if'] == 1) | (merged_df['pred_ae'] == 1)]
    else:
        df_filtered = merged_df[merged_df[model_choice] == 1]

    # Time Series Plot
    ts_fig = px.scatter(
        df_filtered,
        x='timestamp', y='url',
        title='🕒 Anomalies Over Time',
        color=model_choice if model_choice != 'both' else None,
        labels={"timestamp": "Timestamp", "url": "URL"}
    )

    # Reconstruction Error Plot
    recon_fig = px.line(
        merged_df,
        x='timestamp',
        y='recon_error',
        title='🔁 Autoencoder Reconstruction Error',
        labels={"timestamp": "Timestamp", "recon_error": "Reconstruction Error"}
    )

    # Top Anomalous URLs Bar Chart
    url_counts = df_filtered['url'].value_counts().nlargest(10).reset_index()
    url_counts.columns = ['url', 'count']
    bar_fig = px.bar(
        url_counts,
        x='url', y='count',
        title='🔗 Top Anomalous URLs',
        labels={"url": "URL", "count": "Anomaly Count"}
    )

    # Data Table
    table_data = df_filtered[['timestamp', 'url', 'pred_if', 'pred_ae']].to_dict('records')

    return ts_fig, recon_fig, bar_fig, table_data

if __name__ == '__main__':
    app.run(debug=True)