
import numpy as np
from scipy.stats import pearsonr
from matplotlib import pyplot as plt
from matplotlib import ticker
from scipy import stats

from pearson import pearsonr_ci

my_data = np.genfromtxt('data/ocean-acidity_fig-1.csv', delimiter=',', encoding="UTF-8")
years = my_data[:,0]
ph = my_data[:,1]
co2 = my_data[:,2]

#years = np.array([np.rint(year) for year in years if not np.isnan(year)])
tmp = []
for year in years:
  if not np.isnan(year):
    tmp.append(np.rint(year))
years = np.array(tmp)
#print(years)

# Get the index of the elements that are nan and compare them with OR
# This means that if one of the two index is nan, we will mark it to not use it.
nas = np.logical_or(np.isnan(ph), np.isnan(co2))

# Now we access all the elements of the arrays
# but no the index from where we encounter nan
x = ph[~nas]
y = co2[~nas]
r, p = pearsonr(x, y)
print("Correlation", r, p)

a, b, c, d = pearsonr_ci(x, y, alpha = 0.01)
print("CorrelationFisher", a,b,c,d)

fit = np.polyfit(x, y, 1)
fit_fn = np.poly1d(fit)
print("Linear Regression", fit, fit_fn)


# years, x (ph), y (co2)
list_mean_ph = []
list_mean_co2 = []
list_std_ph = []
list_std_co2 = []
control_year = years[0]
list_ph = []
list_co2 = []
for year, value_ph, value_co2 in zip(years, ph, co2):
  #print(year, value_ph, value_co2)
  if year == control_year:
    #print(year, value_ph, value_co2)
    list_ph.append(value_ph)
    list_co2.append(value_co2)
  else:
    mean_ph = np.mean(list_ph)
    std_ph = np.std(list_ph)
    mean_co2 = np.mean(list_co2)
    std_co2 = np.std(list_co2)

    list_mean_ph.append(mean_ph)
    list_mean_co2.append(mean_co2)
    list_std_ph.append(std_ph)
    list_std_co2.append(std_co2)

    control_year = year
    list_ph = []
    list_co2 = []


fig = plt.figure()
ax = fig.add_subplot(111)


error_ph = list_std_ph/np.sqrt(len(list_mean_ph))
error_co2 = list_std_co2/np.sqrt(len(list_mean_co2))

a, b, c, d = pearsonr_ci(np.array(list_mean_ph), np.array(list_mean_co2), alpha = 0.01)
r, p = pearsonr(np.array(list_mean_ph), np.array(list_mean_co2))
print("::::::", a, r)

ax.errorbar(list_mean_ph, list_mean_co2, yerr=error_co2, xerr=error_ph,
    fmt='o', ecolor="green", color="#d46051", ms=4, lw=0.7)
ax.plot(x, fit_fn(x), color="black", label = "r={:.3f}".format(a))


ax.set_xlim(8.06,8.13)
ax.set_ylim(300,400)
ax.set_title('Ocean acidity (Hawaii)')
ax.set_xlabel("pH")
ax.set_ylabel(r"$CO_2$ (ppm)")
ax.legend()
plt.show()




