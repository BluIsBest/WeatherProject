import dash
from dash import html, dcc

dash.page_registry(__name__, name='New York', path='/new-york')

# dropdown menu of buoys in selected region
layout = [html.Div(className='row', children='New York Region Buoy Selection',
                   style={'textAlign': 'left', 'color': 'black', 'fontSize': 24}),
          dcc.Dropdown(['Kings Point, NY','The Battery, NY','Robbins Reef, NJ', 'Mariners Harbor, NY', 'Sandy Hook, NJ', 'Breezy Point, NY'],
                       'Kings Point, NY', id='dropdown')]
