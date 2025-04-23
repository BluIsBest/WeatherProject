import dash, gatheringInfo
from dash import Dash, html, dcc, callback, Input, Output, dash_table

dash.register_page(__name__, name='New York', path='/new-york')

app = Dash()

# dropdown menu of buoys in selected region
layout = [html.Div(className='row', children='New York Region Buoy Selection',
                   style={'textAlign': 'left', 'color': 'black', 'fontSize': 24}),
          dcc.Dropdown(['Islip, NY','Breezy Point, NY','Sandy Hook, NJ','Kings Point, NY','Mariners Harbor, NY','Robbins Reef, NJ','The Battery, NY'],
                       'Islip, NY', id='dropdown')]

@callback(
    Output(component_id='', component_property='children'),
    Input(component_id=layout[1],component_property='value')
)
def display_data(selected_string):
    app.layout = dash_table.DataTable({'Data Type': 'Wind Speed','Value': gatheringInfo.gatherWindSpeed(layout[2])})