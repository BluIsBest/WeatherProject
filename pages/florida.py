import dash, gatheringInfo
from dash import html, dcc, callback, Input, Output, dash_table


dash.register_page(__name__)

# dropdown menu of buoys in selected region
layout = html.Div([
    html.Div(className='row', children='Southern Florida Buoy Selection',
                   style={'textAlign': 'left', 'color': 'black', 'fontSize': 24}),
    dcc.Dropdown(['none','Port Everglades','Virginia Key','Little Madeira', 'Murray Key', 'Watson Place', 'Fort Myers'],
                 'none', id='fl_dropdown'),
    html.Br(),
    html.Div(id='fl_output')
                  ])


@callback(
    Output(component_id='fl_output', component_property='children'),
    Input(component_id='fl_dropdown', component_property='value')
)
def display_data(selected_string):
    """"""
    id_list = ['PEGF1','VAKF1','LMDF1','MUKF1','WPLF1','FMRF1']
    if selected_string == "none":
        # display nothing
        return ""
    else:
        # convert selected_string to station ID by selecting from a dictionary

        # dash_table is set up through a dictionary
        table = dash_table.DataTable(
            {'Data Type': 'Wind Speed (m/s)', 'Value': gatheringInfo.gatherWindSpeed(layout[1])})