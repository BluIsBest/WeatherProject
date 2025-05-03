import dash, gatheringInfo
from dash import html, dcc, callback, Input, Output, dash_table

dash.register_page(__name__)

# dropdown menu of buoys in selected region
layout = html.Div([
    html.Div(className='row', children='Maine Region Buoy Selection',
             style={'textAlign': 'left', 'color': 'black', 'fontSize': 24}),
    dcc.Dropdown(['none','Eastport','Bar Harbor','Portland','Western Maine Shelf','Matinicus Rock','Jonesport'],
                 'none', id='me_dropdown'),
    html.Br(),
    html.Div(id='me_output')
])


@callback(
    Output(component_id='me_output', component_property='children'),
    Input(component_id='me_dropdown', component_property='value')
)
def display_data(selected_string):
    """"""
    id_list = ['PSBM1','ATGM1','CASM1','44030','MISM1','44027']
    if selected_string == "none":
        # display nothing
        return ""
    else:
        # convert selected_string to station ID by selecting from a dictionary

        # dash_table is set up through a dictionary
        table = dash_table.DataTable(
            {'Data Type': 'Wind Speed (m/s)', 'Value': gatheringInfo.gatherWindSpeed(layout[1])})