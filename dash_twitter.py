import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque
import sqlite3
import pandas as pd
import time
#popular topics: google, olympics, trump, gun, usa

app = dash.Dash(__name__)
app.layout = html.Div(
    [   html.H1('Live Twitter Sentiment'),
        dcc.Input(id='sentiment_term', value='', type='text'),
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(
            id='graph-update',
            interval=1*1000
        ),

    ]
)

@app.callback(
            Output('live-graph', 'figure'),
            [Input('sentiment_term', 'value'),
            Input('graph-update', 'n_intervals')]
            )


def update_graph_scatter(sentiment_term, n):
    try:
        conn = sqlite3.connect('twitter.db')

        c = conn.cursor()
        df = pd.read_sql("SELECT * FROM twitter WHERE tweet LIKE ? ORDER BY unix DESC LIMIT 1000", conn, params=('%' + sentiment_term + '%',))
        sentiment_df = df[['unix', 'tweet', 'sentiment']]
        sentiment_df.sort_values('unix', inplace=True)
        sentiment_df['sentiment_smoothed'] = sentiment_df['sentiment'].rolling(int(len(df)/5)).mean()
        # print(sentiment_df.head())
        
        sentiment_df['date'] = pd.to_datetime(sentiment_df['unix'], unit='ms')
        sentiment_df.set_index('date', inplace=True)

        sentiment_df.dropna(inplace=True)
        # print(sentiment_df.head(10))
        # X = df.unix.values[-100:]
        # Y = df.sentiment_smoothed.values[-100:]

        X = sentiment_df.index
        Y = sentiment_df.sentiment_smoothed
        # print('2')
        data = plotly.graph_objs.Scatter(
                x=X,
                y=Y,
                name='Scatter',
                mode= 'lines+markers'
                )
        

        return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(X), max(X)]),
                                                    yaxis=dict(range=[min(Y), max(Y)]),
                                                    title='Term: {}'.format(sentiment_term))}
        # print(data)

    except Exception as e:
        with open('errors.txt','a') as f:
            f.write(str(e))
            f.write('\n')

if __name__ == '__main__':
    app.run_server(debug=True)