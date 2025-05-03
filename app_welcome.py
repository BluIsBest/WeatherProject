# Author: Joshua Bauer
# Date: May 1, 2025
# Description: updating multipage GUI with a home page

# Import packages
import dash
from dash import Dash, html, dcc

# Initialize the app and css
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, use_pages=True, external_stylesheets=external_stylesheets)

# App layout, containing title for app, a secondary title prompting to choose a region, and buttons that will take user to page with dropdown menu
app.layout = html.Div([
    html.H1(className='row', children='Welcome to Weather Risk Assessment!', style={'textAlign': 'center', 'color': 'blue', 'fontSize': 30}),
    html.Div([
        html.Div([
            html.H3(className='row', children='How To Use:',style={'textAlign': 'left', 'color': 'black', 'fontSize': 24}),
            html.Div([
                html.H4(className='row',children='1. Select a region of the eastern United States using the buttons',style={'textAlign': 'left', 'color': 'black', 'fontSize': 20}),
                html.H4(className='row',children='2. Select a buoy in your selected region',style={'textAlign': 'left', 'color': 'black', 'fontSize': 20}),
                html.H4(className='row',children='3. Average data from the buoy and the selected region will be displayed with a predicted storm strength',style={'textAlign': 'left', 'color': 'black', 'fontSize': 20})])
        ]),

        html.H2(className='row', children='Choose a Region in the Eastern United States:', style={'textAlign': 'left', 'color': 'black', 'fontSize': 24}),
        html.Div([
            dcc.Link(html.Button(page['name']), href=page['path'], style={'width': '5px'}) for page in dash.page_registry.values()

        ])
    ]),

    html.Br(),
    dash.page_container
])

#print(dash.page_registry.values())

#@callback()

if __name__ == '__main__':
    app.run(debug=True)
