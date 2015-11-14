from __future__ import print_function, division

import math
import mraa
import time

import plotly.plotly as py

from datetime import datetime
from plotly.graph_objs import Figure, Layout, Scatter

# plot.ly constants
user_name = "USERNAME"
api_key = "API_KEY"
stream_token = "STREAM_TOKEN"

# temperature sensor constants
temp_sensor = mraa.Aio(1)
B = 4275  # B value of the thermistor
R0 = 100000  # default resistance

py.sign_in(user_name, api_key)  # sign into plot.ly
# graph
trace1 = Scatter(
    x=[],
    y=[],
    stream=dict(
        token=stream_token,
        maxpoints=500
    )
)

layout = Layout(title='BafHax Temperature')

fig = Figure(data=[trace1], layout=layout)

print(py.plot(fig, filename='BafHax real-time temperature'))

stream = py.Stream(stream_token)
stream.open()

while True:
    temp = temp_sensor.read()

    R = 1023.0 / float(temp) - 1.0
    R *= R0

    final_temp = 1.0 / (math.log(R / R0) / B + 1 / 298.15) - 273.15
    print("Temperature is:", final_temp)
    stream.write({'x': str(datetime.now()), 'y': final_temp})

    time.sleep(0.05)
