import dash
from dash import html, dcc

dash.register_page(__name__, name='Florida', path='/south-florida')

# dropdown menu of buoys in selected region
layout = [html.Div(className='row', children='Southern Florida Buoy Selection',
                   style={'textAlign': 'left', 'color': 'black', 'fontSize': 24}),
          dcc.Dropdown(['Everglades, FL','Virginia Key, FL','Little Madeira, FL', 'Murray Key, FL', 'Watson Place, FL', 'Fort Myers, FL'],
                       'Lake Worth Pier, FL', id='dropdown')]