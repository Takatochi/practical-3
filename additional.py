# Аналіз даних "BrainSieze.txt" між жіночою та чоловічою статтю с такими параметрами 
#   1.Стать: чоловіча або жіноча
#   2.FSIQ: Повномасштабні показники IQ на основі чотирьох субтестів Векслера (1981)
#   3.VIQ: Вербальні показники IQ на основі чотирьох субтестів Векслера (1981)
#   4.PIQ: Показники продуктивності IQ на основі чотири підтести Векслера (1981)
#   5.Weight: вага тіла в фунтах
#   6.Height: зріст у дюймах
#   7.MRI_Count: загальна кількість пікселів за 18 скануваннями МРТ
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the BrainSieze.txt file into a Pandas DataFrame
brainFile = 'BrainSieze.txt' 
brainFrame = pd.read_csv(brainFile)
print(brainFrame.head()) 

# Calculate the mean Smarts for males and females
menDf = brainFrame[(brainFrame.Gender =='Male')] 
womenDf = brainFrame[(brainFrame.Gender =='Female')]
#This code is also good, but you may want to add a comment 
# explaining how you are splitting the DataFrame into two DataFrames.
womenDf = womenDf.drop(columns=['Gender'])
print(womenDf)
menDf = menDf.drop(columns=['Gender'])
print(menDf)


# Plot the mean Smarts against the MRI_Count for each group
menMeanSmarts = menDf[["PIQ","FSIQ","VIQ"]].mean(axis=1) 
print(menMeanSmarts)
plt.scatter(menMeanSmarts, menDf["MRI_Count"])
plt.show()

# Plot to the mean Smarts against the MRI_Count for each group
womenMeanSmarts = womenDf[["PIQ","FSIQ","VIQ"]].mean(axis=1) 
print(womenMeanSmarts)
plt.scatter(womenMeanSmarts, womenDf["MRI_Count"])
plt.show()

# Calculate the correlation between MRI_Count and mean Smarts for males and females
menCorrelation = np.corrcoef(menMeanSmarts, menDf["MRI_Count"])[0, 1]
womenCorrelation = np.corrcoef(womenMeanSmarts, womenDf["MRI_Count"])[0, 1]
# Print the correlation coefficients
print("Correlation between MRI_Count and mean Smarts for males:", menCorrelation)
print("Correlation between MRI_Count and mean Smarts for females:", womenCorrelation)

# Calculate the correlation matrix for each group
wcorr = womenDf.corr()
sns.heatmap(wcorr)
plt.show()
mcorr =menDf.corr() 
sns.heatmap(mcorr)
plt.show()