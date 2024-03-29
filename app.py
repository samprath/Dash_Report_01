import dash
import dash_core_components as dcc
import dash_html_components as html
app = dash.Dash()
colors = {
    'background': None,
    'text': '#7FDBFF'
}
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='This is Dash sample report',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    dcc.Graph(
        id='Graph1',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montr'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': None,
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])
if __name__ == '__main__':
    app.run_server()
