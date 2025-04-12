# Import packages
import dash
from dash import Dash, html, dcc

# Initialize the app and css
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, use_pages=True, external_stylesheets=external_stylesheets)

# App layout, containing title for app, a secondary title prompting to choose a region, and buttons that will take user to page with dropdown menu
app.layout = html.Div([
    html.H1(className='row', children='Welcome to Weather Risk Assessment!', style={'textAlign': 'center', 'color': 'blue', 'fontSize': 30}),
    html.H2(className='row', children='Choose a Region in the United States:', style={'textAlign': 'left', 'color': 'black', 'fontSize': 24}),
    html.Div([
        html.Div(dcc.Link(html.Button(page['name']), href=page['path'])
                 ) for page in dash.page_registry.values()
    ]),
    dash.page_container
])

#@callback()

if __name__ == '__main__':
    app.run(debug=True)
