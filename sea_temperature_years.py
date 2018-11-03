import numpy as np
from scipy.stats import pearsonr
from matplotlib import pyplot as plt
from matplotlib import ticker
from scipy import stats

my_data = np.genfromtxt('data/sea-surface-temp_fig-1.csv', delimiter=',', encoding="UTF-8")
years = my_data[:,0]
temperature = my_data[:,1]

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(years,temperature, "-o", markersize=3, color="#94c5dd")

ax.set_title('Sea surface temperature anomalies')
ax.set_xlabel("Years")
ax.set_ylabel("Temperature anomalies (°F)")
plt.show()