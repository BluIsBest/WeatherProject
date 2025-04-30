import dash, gatheringInfo
from dash import Dash, html, dcc, callback, Input, Output, dash_table

#app = Dash()

dash.register_page(__name__, name='Maryland', path='/maryland')

# dropdown menu of buoys in selected region
layout = [html.Div(className='row', children='Maryland Region Buoy Selection',
                   style={'textAlign': 'left', 'color': 'black', 'fontSize': 24}),
          dcc.Dropdown(['none','Baltimore','Chesapeake Bay','Annapolis','Washington D.C.','Cambridge','Cooperative Oxford Laboratory'],
                       'none', id='dropdown')]

#@callback(
#    Output(component_id='value', component_property='children'),
#    Input(component_id=layout[1],component_property='value')
#)
#def display_data(selected_string):
#    """"""
#    app.layout = dash_table.DataTable({'Data Type': 'Wind Speed (m/s)','Value': gatheringInfo.gatherWindSpeed(layout[2])})