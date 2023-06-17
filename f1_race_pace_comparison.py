import fastf1 as ff1
from fastf1 import plotting
from fastf1 import utils
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
import pandas as pd
import math

ff1.plotting.setup_mpl(misc_mpl_mods=False)

year1, grand_prix1, session1 = 2023, 8, 'FP2'
year2, grand_prix2, session2 = 2023, 8, 'FP2'

session1 = ff1.get_session(year1, grand_prix1, session1)
session1.load()

session2 = ff1.get_session(year2, grand_prix2, session2)
session2.load()

driver_1, driver_2 = 'HAM', 'RUS'
subplot_bgcolor = '#FAFAFA'
chart_subtitle = ''
color_1 = '#CC0000'
color_2 = '#0000CC'
label_1 = f"{driver_1} - {session1.name}"
label_2 = f"{driver_2} - {session2.name}"

driver_laps_1 = session1.laps.pick_driver(driver_1).pick_quicklaps().reset_index()
driver_laps_2 = session2.laps.pick_driver(driver_2).pick_quicklaps().reset_index()

driver_laps_1['time_float_1'] = driver_laps_1['LapTime'] / np.timedelta64(1, 's')
driver_laps_2['time_float_2'] = driver_laps_2['LapTime'] / np.timedelta64(1, 's')

if driver_laps_1['time_float_1'].min() < driver_laps_2['time_float_2'].min():
    time_min = driver_laps_1['time_float_1'].min()
else:
    time_min = driver_laps_2['time_float_2'].min()

if driver_laps_1['time_float_1'].max() > driver_laps_2['time_float_2'].max():
    time_max = driver_laps_1['time_float_1'].max()
else:
    time_max = driver_laps_2['time_float_2'].max()

time_min_round = math.floor(time_min)
time_max_round = math.ceil(time_max)

fig, ax = plt.subplots(figsize=(22, 15), ncols=2)

sns.scatterplot(data=driver_laps_1, x="LapNumber", y="time_float_1", hue="Compound", palette=ff1.plotting.COMPOUND_COLORS, s=40, linewidth=0, ax=ax[0])
sns.scatterplot(data=driver_laps_2, x="LapNumber", y="time_float_2", hue="Compound", palette=ff1.plotting.COMPOUND_COLORS, s=40, linewidth=0, ax=ax[1])

ax[0].set_title(driver_1, color='gold')
ax[0].set_xlabel("Lap Number", fontsize=14)
ax[0].set_ylabel("Lap Time (s)", fontsize=14)
ax[0].xaxis.label.set_color('white')
ax[0].yaxis.label.set_color('white')
ax[0].legend(frameon=False, labelcolor='w')
ax[0].set(ylim=(time_min_round, time_max_round))
ax[0].tick_params(labelsize=14)
# ax[0].invert_yaxis()

ax[1].set_title(driver_2, color='gold')
ax[1].set_xlabel("Lap Number", fontsize=14)
ax[1].set_ylabel("Lap Time (s)", fontsize=14)
ax[1].xaxis.label.set_color('white')
ax[1].yaxis.label.set_color('white')
ax[1].legend(frameon=False, labelcolor='w')
ax[1].set(ylim=(time_min_round, time_max_round))
ax[1].tick_params(labelsize=14)

sns.set(rc={'axes.facecolor':'r', 'figure.facecolor':'white'})
sns.despine(left=True, bottom=True)

ax[0].grid(which='major', color='white', linewidth=0.2)
ax[1].grid(which='major', color='white', linewidth=0.2)

plot_title = f"{session1.event.year} {session1.event.EventName} - {session1.name}"

fig.suptitle(plot_title+'\n'+chart_subtitle, y='0.96', color='gold')

plt.show()