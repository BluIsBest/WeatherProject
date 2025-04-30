import dash
from dash import Dash, html, dcc

#app = Dash()

dash.register_page(__name__, name='Florida', path='/south-florida')

# dropdown menu of buoys in selected region
layout = [html.Div(className='row', children='Southern Florida Buoy Selection',
                   style={'textAlign': 'left', 'color': 'black', 'fontSize': 24}),
          dcc.Dropdown(['none','Everglades','Virginia Key','Little Madeira', 'Murray Key', 'Watson Place', 'Fort Myers'],
                       'none', id='dropdown')]