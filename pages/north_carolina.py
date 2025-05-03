import dash, gatheringInfo
from dash import html, dcc, callback, Input, Output, dash_table

dash.register_page(__name__)

# dropdown menu of buoys in selected region
layout = html.Div([
    html.Div(className='row', children='North Carolina Region Buoy Selection',
             style={'textAlign': 'left', 'color': 'black', 'fontSize': 24}),
    dcc.Dropdown(['none','Frying Pan Shoals','Diamond Shoals','Beaufort','Hatteras','Nags Head','Wilmington Harbor'],
                 'none', id='nc_dropdown'),
    html.Br(),
    html.Div(id='nc_output')
                  ])


@callback(
    Output(component_id='nc_output', component_property='children'),
    Input(component_id='nc_dropdown', component_property='value')
)
def display_data(selected_string):
    """"""
    id_list = ['41013','41025','BFTN7','HCGN7','44086','WLON7']
    if selected_string == "none":
        # display nothing
        return ""
    else:
        # convert selected_string to station ID by selecting from a dictionary

        # dash_table is set up through a dictionary
        table = dash_table.DataTable(
            {'Data Type': 'Wind Speed (m/s)', 'Value': gatheringInfo.gatherWindSpeed(layout[1])})