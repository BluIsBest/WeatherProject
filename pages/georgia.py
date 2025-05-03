import dash, gatheringInfo
from dash import html, dcc, callback, Input, Output, dash_table

dash.register_page(__name__)

# dropdown menu of buoys in selected region
layout = html.Div([
    html.Div(className='row', children='South Carolina Region Buoy Selection',
             style={'textAlign': 'left', 'color': 'black', 'fontSize': 24}),
    dcc.Dropdown(['none','Fort Pulaski','Grays Reef','Kings Bay MSF Pier', 'Sapelo Island Reserve'],
                 'none', id='ga_dropdown'),
    html.Br(),
    html.Div(id='ga_output')
])


@callback(
    Output(component_id='ga_output', component_property='children'),
    Input(component_id='ga_dropdown', component_property='value')
)
def display_data(selected_string):
    """"""
    id_list = ['FPKG1','41008','KBMG1','SAQG1']
    if selected_string == "none":
        # display nothing
        return ""
    else:
        # convert selected_string to station ID by selecting from a dictionary

        # dash_table is set up through a dictionary
        table = dash_table.DataTable({'Data Type': 'Wind Speed (m/s)', 'Value': gatheringInfo.gatherWindSpeed(layout[1])})