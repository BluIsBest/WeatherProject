import dash, gatheringInfo
from dash import html, dcc, callback, Input, Output, dash_table

dash.register_page(__name__)

# dropdown menu of buoys in selected region
layout = html.Div([
    html.Div('New York Region Buoy Selection',
                   style={'textAlign': 'left', 'color': 'black', 'fontSize': 24}),

    dcc.Dropdown(
        ['none','Islip, NY','Breezy Point, NY','Sandy Hook, NJ','Kings Point, NY','Mariners Harbor, NY','Robbins Reef, NJ','The Battery, NY'],
                 'none', id='ny_dropdown'),
    html.Br(),
    html.Div(id='ny_output')
])


@callback(
    Output(component_id='ny_output', component_property='children'),
    Input(component_id='ny_dropdown', component_property='value')
)
def display_data(selected_string):
    """"""
    id_list = ['44025', '44065', 'SDNH4', 'KPTN6', 'MHRN6', 'ROBN4', 'BATN6']
    if selected_string == 'none':
        # display nothing
        return ''
    else:
        # convert selected_string to station ID by selecting from a dictionary

        # dash_table is set up through a dictionary
        table = dash_table.DataTable(
            {'Data Type': 'Wind Speed (m/s)', 'Value': gatheringInfo.gatherWindSpeed(layout[1])})