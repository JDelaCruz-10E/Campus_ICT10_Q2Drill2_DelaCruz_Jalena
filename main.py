from pyscript import display

weather_today = {
    "location" : "Manila",
    "temperature_c" : 32,
    "humidity" : 78,
    "condition" : "Sunny"
}

display(weather_today, 'temperature_c: 32', target='output')

weather_today['condition'] = 'Cloudy'
weather_today['heat_index'] = '38'
display(f'{weather_today}', target='output')