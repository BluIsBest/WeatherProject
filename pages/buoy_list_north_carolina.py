import dash, gatheringInfo
from dash import Dash, html, dcc, callback, Input, Output, dash_table

#app = Dash()

dash.register_page(__name__, name='North Carolina', path='/north-carolina')

# dropdown menu of buoys in selected region
layout = [html.Div(className='row', children='North Carolina Region Buoy Selection',
                   style={'textAlign': 'left', 'color': 'black', 'fontSize': 24}),
          dcc.Dropdown(['none','Frying Pan Shoals','Diamond Shoals','Beaufort','Hatteras','Nags Head','Wilmington Harbor'],
                       'none', id='dropdown')]
