import dash, gatheringInfo
from dash import html, dcc, callback, Input, Output, dash_table

dash.register_page(__name__)

# dropdown menu of buoys in selected region
layout = html.Div([
    html.Div('Massachusetts Region Buoy Selection',
                   style={'textAlign': 'left', 'color': 'black', 'fontSize': 24}),
    dcc.Dropdown(['none','Boston','Cape Cod Bay','Nantucket Sound','Massachusetts Bay','New Bedford','Buzzards Bay'],
                 'none', id='mass_dropdown'),
    html.Br(),
    html.Div(id='mass_output')
                  ])

@callback(
    Output(component_id='mass_output', component_property='children'),
    Input(component_id='mass_dropdown', component_property='value')
)
def display_data(selected_string):
    """"""
    id_list = ['BHBM3','44090','44020','44029','NBGM3','BUZM3']
    if selected_string == "none":
        # display nothing
        return ""
    else:
        # convert selected_string to station ID by selecting from a dictionary

        # dash_table is set up through a dictionary
        table = dash_table.DataTable({'Data Type': 'Wind Speed (m/s)', 'Value': gatheringInfo.gatherWindSpeed(layout[1])})