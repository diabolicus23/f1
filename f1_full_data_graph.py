import fastf1 as ff1
from fastf1 import plotting
from fastf1 import utils
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
import pandas as pd
import math

year1, grand_prix1, session1 = 2023, 8, 'FP2'
year2, grand_prix2, session2 = 2023, 8, 'FP2'

session1 = ff1.get_session(year1, grand_prix1, session1)
session1.load()

session2 = ff1.get_session(year2, grand_prix2, session2)
session2.load()

driver_1 = 'HAM'
driver_2 = 'RUS'
subplot_bgcolor = '#FAFAFA'
chart_subtitle = 'Telemetry Data'
color_1 = '#CC0000'
color_2 = '#0000CC'
label_1 = f"{driver_1} - {session1.name}"
label_2 = f"{driver_2} - {session2.name}"

# Laps can now be accessed through the .laps object coming from the session
laps_driver_1 = session1.laps.pick_driver(driver_1)
laps_driver_2 = session2.laps.pick_driver(driver_2)

# Select the fastest lap or the single lap
fastest_driver_1 = laps_driver_1.pick_fastest()
fastest_driver_2 = laps_driver_2.pick_fastest()
# fastest_driver_1 = laps_driver_1.pick_lap(54)
# fastest_driver_2 = laps_driver_2.pick_lap(54)

# Retrieve the telemetry and add the distance column
telemetry_driver_1 = fastest_driver_1.get_telemetry().add_distance()
telemetry_driver_2 = fastest_driver_2.get_telemetry().add_distance()

# Teams color in case we need them
team_driver_1 = fastest_driver_1['Team']
team_driver_2 = fastest_driver_2['Team']


plot_size = [22, 30]
plot_title = f"{session1.event.year} {session1.event.EventName} - {session1.name} - {driver_1} vs {driver_2}"

# Make plot a bit bigger
plt.rcParams['figure.figsize'] = plot_size

# Create subplots with different sizes
fig, ax = plt.subplots(5, height_ratios=[3, 2, 1, 1, 3])

ax[0].set_facecolor(subplot_bgcolor)
ax[1].set_facecolor(subplot_bgcolor)
ax[2].set_facecolor(subplot_bgcolor)
ax[3].set_facecolor(subplot_bgcolor)
ax[4].set_facecolor(subplot_bgcolor)

# Speed
ax[0].plot(telemetry_driver_1['Distance'], telemetry_driver_1['Speed'], label=label_1, color=color_1, linewidth=1)
ax[0].plot(telemetry_driver_2['Distance'], telemetry_driver_2['Speed'], label=label_2, color=color_2, linewidth=1)
ax[0].set(ylabel=f"Speed (km/h)")

ax[0].grid(which='major', color='#CCCCCC', linewidth=0.8)
ax[0].grid(which='minor', color='#DDDDDD', linestyle=':', linewidth=0.5)
ax[0].minorticks_on()

ax[0].title.set_text('Speed')

Subjects = {10 : 1,
            12 : 1,
            14 : 1,
            0 : 0,
            1 : 0,
            2 : 0,
            3 : 0,
            4 : 0,
            8 : 0}

telemetry_driver_1["DRS_Status"] = telemetry_driver_1["DRS"].map(Subjects)
telemetry_driver_2["DRS_Status"] = telemetry_driver_2["DRS"].map(Subjects)
# telemetry_driver_1["DRS_Status"] = telemetry_driver_1["DRS"]
# telemetry_driver_2["DRS_Status"] = telemetry_driver_2["DRS"]

# Throttle
ax[1].grid(which='major', axis='x', color='#CCCCCC', linewidth=0.8)
ax[1].grid(which='minor', axis='x', color='#DDDDDD', linestyle=':', linewidth=0.5)
ax[1].minorticks_on()
ax[1].axes.get_yaxis().set_ticks([])
ax[1].title.set_text('DRS Usage')
ax[1].plot(telemetry_driver_1['Distance'], telemetry_driver_1['Throttle'], label=label_1, color=color_1, linewidth=1)
ax[1].plot(telemetry_driver_2['Distance'], telemetry_driver_2['Throttle'], label=label_2, color=color_2, linewidth=1)
ax[1].set(ylabel=f"Throttle (%)")
ax[1].grid(which='major', color='#CCCCCC', linewidth=0.8)
ax[1].grid(which='minor', color='#DDDDDD', linestyle=':', linewidth=0.5)
ax[1].minorticks_on()
pos = ax[1].get_position()
ax[1].set_position([pos.x0, pos.y0, pos.width, pos.height * 0.85])
ax[1].title.set_text('Throttle')

# Brake
ax[2].grid(which='major', axis='x', color='#CCCCCC', linewidth=0.8)
ax[2].grid(which='minor', axis='x', color='#DDDDDD', linestyle=':', linewidth=0.5)
ax[2].minorticks_on()
ax[2].axes.get_yaxis().set_ticks([])
ax[2].title.set_text('DRS Usage')
ax[2].plot(telemetry_driver_1['Distance'], telemetry_driver_1['Brake'], label=label_1, color=color_1, linewidth=1)
ax[2].plot(telemetry_driver_2['Distance'], telemetry_driver_2['Brake'], label=label_2, color=color_2, linewidth=1)
ax[2].set(ylabel=f"Brake (%)")
ax[2].grid(which='major', color='#CCCCCC', linewidth=0.8)
ax[2].grid(which='minor', color='#DDDDDD', linestyle=':', linewidth=0.5)
ax[2].minorticks_on()
pos = ax[2].get_position()
ax[2].set_position([pos.x0, pos.y0, pos.width, pos.height * 0.85])
ax[2].title.set_text('Brake')

# DRS
ax[3].plot(telemetry_driver_1['Distance'], telemetry_driver_1['DRS_Status'], label=label_1, color=color_1, linewidth=1)
ax[3].plot(telemetry_driver_2['Distance'], telemetry_driver_2['DRS_Status'], label=label_2, color=color_2, linewidth=1)
ax[3].set(ylabel=f"DRS Usage")

# RPM
ax[4].plot(telemetry_driver_1['Distance'], telemetry_driver_1['RPM'], label=label_1, color=color_1, linewidth=1)
ax[4].plot(telemetry_driver_2['Distance'], telemetry_driver_2['RPM'], label=label_2, color=color_2, linewidth=1)
ax[4].set(ylabel=f"RPM")

ax[4].grid(which='major', color='#CCCCCC', linewidth=0.8)
ax[4].grid(which='minor', color='#DDDDDD', linestyle=':', linewidth=0.5)
ax[4].minorticks_on()
ax[4].title.set_text('RPM')

ax[4].legend(
    loc='lower center',
    bbox_to_anchor=(0.5, -0.3),
    ncol=2,
)

plt.suptitle(plot_title+'\n'+chart_subtitle, y='0.96')

plt.subplots_adjust(hspace=0.5)

plt.show()