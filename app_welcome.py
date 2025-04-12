# Import packages
import dash
from dash import Dash, html, dcc, page_registry, page_container

# Initialize the app and css
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, use_pages=True, external_stylesheets=external_stylesheets)

# App layout, containing title for app, a secondary title prompting to choose a region, and buttons that will take user to page with dropdown menu
app.layout = [html.Div(className='row', children='Welcome to Weather Risk Assessment!', style={'textAlign': 'center', 'color': 'blue', 'fontSize': 30}),
              html.Div(className='row', children='Choose a region:', style={'textAlign': 'center', 'color': 'black', 'fontSize': 24}),
              dcc.Link(html.Button(id='region1', children='New York'), href="/pages/buoy_list_new_york.py"),
              dash.page_container
              ]

app.layout = html.Div([
    html.H1(className='row', children='Welcome to Weather Risk Assessment!', style={'textAlign': 'center', 'color': 'blue', 'fontSize': 30}),
    html.Div([
        html.Div(dcc.Link(html.Button(id='region1', children='New York'), href="/pages/buoy_list_new_york.py")
                 ) for page in page_registry.values()
    ]),
    page_container
])

#@callback()

if __name__ == '__main__':
    app.run(debug=True)
