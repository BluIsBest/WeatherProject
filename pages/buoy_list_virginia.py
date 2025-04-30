import dash, gatheringInfo
from dash import Dash, html, dcc, callback, Input, Output, dash_table

#app = Dash()

dash.register_page(__name__, name='Virginia', path='/virginia')

# dropdown menu of buoys in selected region
layout = [html.Div(className='row', children='New York Region Buoy Selection',
                   style={'textAlign': 'left', 'color': 'black', 'fontSize': 24}),
          dcc.Dropdown(['none','Virginia Beach','Cape Henry','York Spit','Rappahannock Light','Dahlgren','South Craney Island'],
                       'none', id='dropdown')]

# callback decorator allows a table of the weather data to be displayed based on the selection from the dropdown menu.
# callback Output still needs a component_id string.
#@callback(
#    Output(component_id='', component_property='children'),
#    Input(component_id=layout[1],component_property='value')
#)
#def display_data(selected_string): # attempting to create table by making a dictionary in gui code
#    layout = dash_table.DataTable({'Data Type': 'Wind Speed','Value': gatheringInfo.gatherWindSpeed(layout[2])})
