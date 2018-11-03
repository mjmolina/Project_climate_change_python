import numpy as np
from scipy.stats import pearsonr
from matplotlib import pyplot as plt
from matplotlib import ticker
from scipy import stats
import matplotlib.patches as mpatches

temp_data = np.genfromtxt('data/sea-surface-temp_fig-1.csv', delimiter=',', encoding="UTF-8")
years = temp_data[:,0]
temperature = temp_data[:,1]
ids = np.argsort(years)
years = years[ids]
temperature = temperature[ids]

bleaching_data = np.genfromtxt('data/CoralBleachingHawaii.csv', delimiter=',', encoding="UTF-8")
bleaching_years = bleaching_data[:,8]
bleaching_severities = bleaching_data[:,10]

ids = np.argsort(bleaching_years)
bleaching_years = bleaching_years[ids]
bleaching_severities = bleaching_severities[ids]

list_years=[]
list_severities=[]
list_severity_years=[]
current_year=bleaching_years[0]

for year,severity in zip(bleaching_years,bleaching_severities):
    if severity != -1:
        if current_year == year:
            list_severity_years.append(severity)
        else:
            list_years.append(current_year)
            list_severities.append(list_severity_years)

            list_severity_years=[]
            list_severity_years.append(severity)
            current_year=year    

print(list_years)
print(list_severities)


list_temperature = []
for i in list_years:
    for j, z in zip(years, temperature):
        if i == j:
            list_temperature.append(z)

fig = plt.figure()
ax = fig.add_subplot(111)

for i, (y, sev) in enumerate(zip(list_years, list_severities)):                                                  
    y_value = list_temperature[i]                                                                                
    mk = 16                                                                                            
    for s in sev:                                                                                      
        print(y, s, y_value)                                                                           
        if s == 0:                                                                                     
            cl = "white"                                                                               
        elif s == 1:                                                                                   
            cl = "yellow"                                                                              
        elif s == 2:                                                                                   
            cl = "orange"                                                                              
        elif s == 3:                                                                                   
            cl = "red"                                                                                 
        ax.plot(y, y_value, 'o' ,markersize=mk, color=cl, markeredgecolor="black", markeredgewidth=0.5)
        mk -= 4

ax.plot(years,temperature, "-o", markersize=3, color="#94c5dd")


red_patch = mpatches.Patch(facecolor='red',edgecolor="black", linewidth=0.5, label="Bleaching severity: High" )                       
orange_patch = mpatches.Patch(facecolor='orange',edgecolor="black", linewidth=0.5, label='Bleaching severity: Medium')              
white_patch = mpatches.Patch(facecolor='white',edgecolor="black", linewidth=0.5, label='Bleaching severity: None')                 
plt.legend(handles=[red_patch, orange_patch, white_patch])

ax.set_title('Sea surface temperature anomalies and bleaching effect in Hawaii')
ax.set_xlabel("Years")
ax.set_ylabel("Temperature anomalies (°F)")
plt.show()