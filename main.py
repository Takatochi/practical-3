# Проведений аналіз даних "The_Data.txt"" кореляцій “рівень освіти за регіонами”
    # Location - Місцезнаходження
    # Total - Сумарана кількі в регіонів різних типів освіти
    # Higher - містить загальну кількість людей з вищою освітою в певному регіоні
    # Doctors - містить кількість людей з рівнем освіти доктор наук
    # PhD  - містить кількість людей з рівнем освіти доктор філософії
    # Master_of_Science - містить кількість людей з рівнем освіти магістер
    # Bachelors - - містить кількість людей з рівнем освіти бакалавр
    # Others - містить кількість людей з іншим рівнем освіти
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Reading data from the file
brainFile = 'The_Data.txt' 
brainFrame = pd.read_csv(brainFile)

# Displaying the first few rows of the DataFrame
print(brainFrame.head())

# Displaying summary statistics of the DataFrame
print(brainFrame.describe())

# Calculate the average level of education for each region
avg_education = brainFrame.groupby('Location')['Total'].mean()
print(avg_education)

# Creating a bar chart to show the average level of education in each region
plt.bar(avg_education.index, avg_education.values)
plt.xlabel('Location')
plt.ylabel('Average level of education')
plt.title('Average level of education by region in Ukraine')
plt.xticks(rotation=90)
plt.show()

# Calculate the percentage of people with a bachelor's degree in each region
pct_bachelors = (brainFrame['Bachelors'] / brainFrame['PhD']) * 100

# Group the data by 'Location' and calculate the mean percentage for each location
mean_pct_bachelors = pct_bachelors.groupby(brainFrame['Location']).mean()

# Create a bar chart to show the mean percentage of people with a bachelor's degree in each region
plt.bar(mean_pct_bachelors.index, mean_pct_bachelors.values)
plt.xlabel("Location")
plt.ylabel("Mean Percentage of People with a Bachelor's Degree")
plt.title("Mean Percentage of People with a Bachelor's Degree by Region in Ukraine")
plt.xticks(rotation=90)

# Adjusting the spacing between x-axis labels for better readability
n = 1
plt.xticks(range(0, len(mean_pct_bachelors.index), n), mean_pct_bachelors.index[::n])
plt.show()

# Calculating and printing the average level of education
average_level_of_education = brainFrame['Total'].mean()
print(f'The average level of education is {average_level_of_education:.2f} years.')

# Filtering data for people with a bachelor's degree
CtUaDFB = brainFrame[(brainFrame.Bachelors >= 50.0)] 
print(CtUaDFB)

# Calculating and plotting the smart score for people with a bachelor's degree
sscoreSmart = CtUaDFB[["Bachelors"]].mean(axis=1) 
print(sscoreSmart)
plt.scatter(sscoreSmart, CtUaDFB["Location"])
plt.show()

# Removing the 'Location' column for correlation analysis
CtUaDFB = CtUaDFB.drop(columns=['Location'])
corrB = CtUaDFB.corr()

# Similar analysis for people with a PhD
CtUaDF = brainFrame[(brainFrame.PhD >= 50.0)] 
print(CtUaDF)
sscoreSmart = CtUaDF[["PhD"]].mean(axis=1) 
print(sscoreSmart)
plt.scatter(sscoreSmart, CtUaDF["Location"])
plt.show()

# Removing the 'Location' column for correlation analysis
CtUaDF = CtUaDF.drop(columns=['Location'])
corr = CtUaDF.corr()

# Calculating and printing correlations
print("(############brainFrame############)")
def Correlation(a, b):
    corr = brainFrame[a].corr(brainFrame[b])
    print(f'Correlation between {a} and {b}: {corr}')

Correlation('Total', 'Bachelors')
Correlation('Total', 'PhD')
Correlation('Bachelors', 'PhD')
Correlation('Bachelors', 'Master_of_Science')
Correlation('PhD', 'Master_of_Science')

# Creating heatmaps for correlation matrices
sns.heatmap(corr, annot=True, cmap='viridis')
plt.show()

print(corrB)
sns.heatmap(corrB, annot=True, cmap='viridis')
plt.show()
#//////////

# Creating a heatmap of the mean 'Total' values by location
mean_total_by_location = brainFrame.groupby('Location')['Bachelors'].mean().reset_index()
sns.heatmap(mean_total_by_location.pivot_table(index='Location', values='Bachelors', aggfunc='mean'), annot=True, cmap='viridis')
plt.xlabel('Location')
plt.ylabel('Mean Total')
plt.title('Mean Total by Location in Ukraine')
plt.show()