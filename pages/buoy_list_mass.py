import dash, gatheringInfo
from dash import Dash, html, dcc, callback, Input, Output, dash_table

#app = Dash()

dash.register_page(__name__, name='Massachusetts', path='/massachusetts')

# dropdown menu of buoys in selected region
layout = [html.Div(className='row', children='Massachusetts Region Buoy Selection',
                   style={'textAlign': 'left', 'color': 'black', 'fontSize': 24}),
          dcc.Dropdown(['none','Boston','Cape Cod Bay','Nantucket Sound','Massachusetts Bay','New Bedford','Buzzards Bay'],
                       'none', id='dropdown')]

#@callback(
#    Output(component_id='value', component_property='children'),
#    Input(component_id=layout[1],component_property='value')
#)
#def display_data(selected_string):
#    """"""
#    app.layout = dash_table.DataTable({'Data Type': 'Wind Speed (m/s)','Value': gatheringInfo.gatherWindSpeed(layout[2])})