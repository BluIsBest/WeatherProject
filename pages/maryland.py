import dash, gatheringInfo
from dash import html, dcc, callback, Input, Output, dash_table

dash.register_page(__name__)

# dropdown menu of buoys in selected region
layout = html.Div([
    html.Div(className='row', children='Maryland Region Buoy Selection',
                   style={'textAlign': 'left', 'color': 'black', 'fontSize': 24}),
    dcc.Dropdown(['none','Baltimore','Chesapeake Bay','Annapolis','Washington D.C.','Cambridge','Cooperative Oxford Laboratory'],
                 'none', id='md_dropdown'),
    html.Br(),
    html.Div(id='md_output')
                  ])

@callback(
    Output(component_id='md_output', component_property='children'),
    Input(component_id='md_dropdown',component_property='value')
)
def display_data(selected_string):
    """"""
    id_list = ['BLTM2', 'CPVM2', 'APAM2', 'WASD2', 'CAMM2', 'CXLM2']
    if selected_string == "none":
        #display nothing
        return ""
    else:
        table = dash_table.DataTable({'Data Type': 'Wind Speed (m/s)','Value': gatheringInfo.gatherWindSpeed(layout[1])})