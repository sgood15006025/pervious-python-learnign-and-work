

import matplotlib.pyplot as plt
from sitka_highs_lows import highs as sitka_highs
from death_valley_highs_lows import highs as deathvalley_highs
from sitka_highs_lows import dates

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, deathvalley_highs, c='red', alpha=0.5)
ax.plot(dates, sitka_highs, c='blue', alpha=0.5)
plt.fill_between(dates, deathvalley_highs, sitka_highs, facecolor='blue', alpha=0.1)

# Format plot.
plt.title("Daily high temperature comparison, 2018\nDeath Valley, CA and Sitka", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()