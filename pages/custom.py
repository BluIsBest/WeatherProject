import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(__name__)

# layout for the user inserting a custom
layout = html.Div([
    html.H5("Input a custom location to access weather data and SSI"),
    html.Div([
        html.H6('Latitude: ')
        dcc.Input(id='lat-custom-input', value='none', type='text'),
        html.H6('Longitude: '),
        dcc.Input(id='long-custom-input', value='none', type='text'),
        id='custom-input'=['lat-custom-input','long-custom-input']
    ]),
    html.Br(),
    html.Div(id='lat-custom-output')
])

# callback decorator to display weather data based on input, using radial search
@callback(
    Output(component_id='custom-output', component_property='children'),
    Input(component_id='custom-input', component_property='value')
)
def custom_data_display(custom_string):
    """

    :param custom_string: custom string user inputs in GUI
    :return: strings of data separated by html line breaks
    """

    return [
        f'',
        html.Br(),
        f''
    ]
