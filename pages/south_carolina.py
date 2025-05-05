import dash, gatheringInfo
from dash import html, dcc, callback, Input, Output

dash.register_page(__name__)

options = ['none','Charleston','Winyah Bay Reserve','Springmaid Pier','Bennett\'s Point','Capers Nearshore','Fort Johnson']

# dropdown menu of buoys in selected region
layout = html.Div([
    html.Div(className='row', children='South Carolina Region Buoy Selection',
             style={'textAlign': 'left', 'color': 'black', 'fontSize': 24}),
    dcc.Dropdown(options,'none', id='sc_dropdown'),
    html.Br(),
    html.Div(id='sc_output')
])


@callback(
    Output(component_id='mass_output', component_property='children'),
    Input(component_id='mass_dropdown', component_property='value')
)
def display_single_buoy_data(selected_string):
    """
    :param selected_string: this is the selection from the dropdown menu
    :return: nothing is displayed if the selection is 'none' or displays the weather data from the selection
    """
    id_list = ['CHTS1','WYSS1','MROS1','ACXS1','41029','FMNS1']

    # display individual buoy data
    if selected_string == 'none':
        # display nothing
        return ''
    else:
        # convert selected_string to station ID using id_list
        selection_index = options.index(selected_string)
        selected_station_id = id_list[selection_index - 1]
        single_buoy = gatheringInfo.Buoy(selected_station_id)

        buoy_name = single_buoy.getNAME()
        wind_speed = single_buoy.getWSPD()
        wave_height = single_buoy.getWVHT()
        pressure = single_buoy.getPRES()

        region = gatheringInfo.BB(id_list)

        avg_wind_speed = region.get_SSI_WSPD()
        avg_wave_height = region.get_SSI_WVHT()
        avg_pressure = region.get_SSI_PRES()

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

        return [f'Weather conditions at {buoy_name} buoy:',
                html.Br(),
                f'Wind Speed: {wind_speed} m/s',
                html.Br(),
                f'Wave Height: {wave_height} m',
                html.Br(),
                f'Pressure: {pressure} millibars',
                html.Br(),
                f'New York Metropolitan Region Weather Data:',
                html.Br(),
                f'Average Wind Speed: {avg_wind_speed} m/s',
                html.Br(),
                f'Average Wave Height: {avg_wave_height} m',
                html.Br(),
                f'Average Pressure: {avg_pressure} millibars',
                storm_strength
                ]
