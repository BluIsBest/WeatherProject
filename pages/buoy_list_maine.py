import dash, gatheringInfo
from dash import Dash, html, dcc, callback, Input, Output, dash_table

#app = Dash()

dash.register_page(__name__, name='Maine', path='/maine')

# dropdown menu of buoys in selected region
layout = [html.Div(className='row', children='Maine Region Buoy Selection',
                   style={'textAlign': 'left', 'color': 'black', 'fontSize': 24}),
          dcc.Dropdown(['none','Eastport','Bar Harbor','Portland','Western Maine Shelf','Matinicus Rock','Jonesport'],
                       'none', id='dropdown')]
