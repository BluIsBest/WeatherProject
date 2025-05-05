import dash, gatheringInfo
from dash import html, dcc, callback, Input, Output

dash.register_page(__name__)

# layout for the user inserting a custom
layout = html.Div([
    html.H5("Input a custom location to access weather data and SSI"),
    html.Div([
        html.H6('Latitude: '),
        dcc.Input(id='lat-custom-input', value='none', type='text'),
        html.H6('Longitude: '),
        dcc.Input(id='long-custom-input', value='none', type='text')
    ]),
    html.Br(),
    html.Div(id='lat-custom-output')
])

# callback decorator to display weather data based on input, using radial search
@callback(
    Output(component_id='custom-output', component_property='children'),
    Input(component_id='lat-custom-input', component_property='value'),
    Input(component_id='long-custom-input',component_property='value')
)
def custom_data_display(cust_lat, cust_long):
    """
    :param cust_lat: string from first input GUI
    :param cust_long: string from second input GUI
    :return: strings of data separated by html line breaks
    """

    # define new object through Add_New_Location(lat, long) function from gatheringInfo class file
    new_loc_buoy = gatheringInfo.Add_New_Location(float(cust_lat), float(cust_long))

    # obtain average weather data of the new, user-defined location
    avg_wind_speed = new_loc_buoy.get_SSI_WSPD()
    avg_wave_height = new_loc_buoy.get_SSI_WVHT()
    avg_pressure = new_loc_buoy.get_SSI_PRES()

    # determines storm strength
    SSI = (0.5 * ((avg_wind_speed / 60) ** 2) +
           0.3 * (930 / avg_pressure) +
           0.2 * avg_wave_height / 12)

    if SSI < 0.2:
        storm_strength = f"The expected storm should be a minimal storm"
    if 0.21 < SSI < 0.4:
        storm_strength = f"The expected storm should be a moderate storm"
    if 0.41 < SSI < 0.6:
        storm_strength = f"The expected storm should be a strong storm"
    if 0.61 < SSI < 0.8:
        storm_strength = f"The expected storm should be a severe storm"
    if 0.81 < SSI:
        storm_strength = f"The expected storm should be an extreme storm"

    return [f'Weather conditions at location: ',
            html.Br(),
            f'Average Wind Speed: {avg_wind_speed} m/s',
            html.Br(),
            f'Average Wave Height: {avg_wave_height} m',
            html.Br(),
            f'Average Pressure: {avg_pressure} millibars',
            storm_strength
            ]