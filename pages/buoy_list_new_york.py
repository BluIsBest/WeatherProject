import dash
from dash import html, dcc

dash.page_registry(__name__, name='New York', path='/new-york')

# dropdown menu of buoys in selected region
layout = [html.Div(className='row', children='New York Region Buoy Selection',
                   style={'textAlign': 'left', 'color': 'black', 'fontSize': 24}),
          dcc.Dropdown(['Islip, NY','Breezy Point, NY','Sandy Hook, NJ','Kings Point, NY','Mariners Harbor, NY','Robbins Reef, NJ','The Battery, NY'],
                       'Islip, NY', id='dropdown')]
