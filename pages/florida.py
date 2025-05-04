import dash, gatheringInfo
from dash import html, dcc, callback, Input, Output


dash.register_page(__name__)

options = ['none','Port Everglades','Virginia Key','Little Madeira', 'Murray Key', 'Watson Place', 'Fort Myers']

# dropdown menu of buoys in selected region
layout = html.Div([
    html.Div(className='row', children='Southern Florida Buoy Selection',
                   style={'textAlign': 'left', 'color': 'black', 'fontSize': 24}),
    dcc.Dropdown(options,'none', id='fl_dropdown'),
    html.Br(),
    html.Div(id='fl_output')
    ])


@callback(
    Output(component_id='ny_output', component_property='children', allow_duplicate=True),
    Input(component_id='ny_dropdown', component_property='value'),
    prevent_initial_call='initial_duplicate'

)
def display_single_buoy_data(selected_string):
    """
    :param selected_string: this is the selection from the dropdown menu
    :return: nothing is displayed if the selection is 'none' or displays the weather data from the selection
    """
    id_list = ['PEGF1', 'VAKF1', 'LMDF1', 'MUKF1', 'WPLF1', 'FMRF1']

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

        return (f'Weather conditions at {buoy_name} buoy:\n'
                f'Wind Speed: {wind_speed} m/s\n'
                f'Wave Height: {wave_height} m\n'
                f'Pressure: {pressure} millibars\n'
                f'New York Metropolitan Region Weather Data:\n'
                f'Average Wind Speed: {avg_wind_speed} m/s\n'
                f'Average Wave Height: {avg_wave_height} m\n'
                f'Average Pressure: {avg_pressure} millibars\n'
                f'{storm_strength}'
                )
