import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Step 3: Load and Process the Data
df = pd.read_csv('formatted_data.csv')

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Sort data by date
df = df.sort_values('date')

# Step 4: Create the Dash app
app = dash.Dash(__name__)

# Step 5: Layout the Dash app
app.layout = html.Div(children=[
    html.H1(children='sales Data Visualizer for Pink Morsels'),

    dcc.Graph(
        id='sales-line-chart',
        figure=px.line(
            df,
            x='date',
            y='sales',
            title='sales Over Time',
            labels={'date': 'Date', 'sales': 'Total sales ($)'},
            markers=True,
            line_shape='linear'
        ).update_layout(
            xaxis=dict(title='Date'),
            yaxis=dict(title='sales ($)'),
            shapes=[{
                'type': 'line',
                'x0': '2021-01-15', 'x1': '2021-01-15',
                'y0': 0, 'y1': df['sales'].max(),
                'line': {'color': 'red', 'width': 2},
            }],
            annotations=[{
                'x': '2021-01-15', 'y': df['sales'].max(),
                'xref': 'x', 'yref': 'y',
                'text': 'Price Increase',
                'showarrow': True,
                'arrowhead': 2, 'ax': 0, 'ay': -40
            }]
        )
    )
])

# Step 6: Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
