import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(__name__)

# layout for the user inserting a custom
layout = html.Div([
    html.H5("Input a custom location to access weather data and SSI"),
    html.Div([
        dcc.Input(id='custom-input', value='none', type='text')
    ]),
    html.Br(),
    html.Div(id='custom-output')
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