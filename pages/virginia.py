import dash, gatheringInfo
from dash import html, dcc, callback, Input, Output, dash_table

dash.register_page(__name__)

# dropdown menu of buoys in selected region
layout = html.Div([
    html.Div(className='row', children='New York Region Buoy Selection',
                   style={'textAlign': 'left', 'color': 'black', 'fontSize': 24}),
    dcc.Dropdown(['none','Virginia Beach','Cape Henry','York Spit','Rappahannock Light','Dahlgren','South Craney Island'],
                 'none', id='va_dropdown'),
    html.Br(),
    html.Div(id='va_output')
                  ])

@callback(
    Output(component_id='va_output', component_property='children'),
    Input(component_id='va_dropdown',component_property='value')
)
def display_data(selected_string):
    """"""
    id_list = ['44088','44099','44072','RPLV2','NCDV2','CRYV2']
    if selected_string == "none":
        #display nothing
        return ""
    else:
        # convert selected_string to station ID by selecting from a dictionary

        # dash_table is set up through a dictionary
        table = dash_table.DataTable({'Data Type': 'Wind Speed (m/s)','Value': gatheringInfo.gatherWindSpeed(layout[1])})