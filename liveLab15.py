"""
In this assignment we're going to plot the US debt to GDP ratio
using data we programmatically download via the FRED API.
"""

"""
EXERCISE 1

Short: Download the GDP time series for 1970-2023

Long: Find the FRED data series called "Gross Domestic Product" and look up the
abbreviation.(Note that this is NOT the real GDP, which is adjusted for 
inflation.) Download it using DataReader.

(Note that there are some "clean up" steps that you will have to do. You'll need 
to create a year variable for the purpose of merging later but the DATE variable 
will become the index. Hint: look up the reset_index() function.

Renaming the columns so they are more descriptive would be of benefit to you.)
"""
import pandas as pd
from pandas_datareader import data as pdr

# Fetch the GDP data from FRED
gdp_data = pdr.DataReader('GDP', 'fred', start='1970-01-01', end='2023-12-31')

# Reset the index to make 'DATE' a column
gdp_data.reset_index(inplace=True)

# Create a new column for the year
gdp_data['Year'] = gdp_data['DATE'].dt.year

# Rename the columns for clarity
gdp_data.rename(columns={'DATE': 'Date', 'GDP': 'GDP (in millions)'}, inplace=True)

# Display the first few rows of the dataframe
print(gdp_data.head())

        Date  GDP (in millions)  Year
0 1970-01-01           1051.200  1970
1 1970-04-01           1067.375  1970
2 1970-07-01           1086.059  1970
3 1970-10-01           1088.608  1970
4 1971-01-01           1135.156  1971


"""
EXERCISE 2

Short: Download the debt time series for 1970-2023

Long: Find the series called "Federal Debt: Total Public Debt" and download it
via DataReader.

(Similar clean up steps are involved, except that this is quarterly data, ao there 
are 4 entries per year. You'll have to get rid of the duplicates for a year 
using drop_duplicates().)
"""


import pandas as pd
from pandas_datareader import data as pdr

# Fetch the Federal Debt data from FRED
debt_data = pdr.DataReader('GFDEBTN', 'fred', start='1970-01-01', end='2023-12-31')

# Reset the index to make 'DATE' a column
debt_data.reset_index(inplace=True)

# Create a new column for the year
debt_data['Year'] = debt_data['DATE'].dt.year

# Drop duplicate entries for each year, keeping the last entry (you could choose to keep the first)
debt_data.drop_duplicates(subset='Year', keep='last', inplace=True)

# Rename the columns for clarity
debt_data.rename(columns={'DATE': 'Date', 'GFDEBTN': 'Total Public Debt (in millions)'}, inplace=True)

# Display the first few rows of the dataframe
print(debt_data.head())

         Date  Total Public Debt (in millions)  Year
3  1970-10-01                         389158.0  1970
7  1971-10-01                         424131.0  1971
11 1972-10-01                         448473.0  1972
15 1973-10-01                         469073.0  1973
19 1974-10-01                         492664.0  1974

"""
EXERCISE 3

Short: Merge the two datasets and create a debt-to-gdp time series.

Long: This is just debt/gdp for each year. Note that debt and GDP are recorded 
using different units and remember to adjust for that!
"""

import pandas as pd
from pandas_datareader import data as pdr

# Fetch GDP data
gdp_data = pdr.DataReader('GDP', 'fred', start='1970-01-01', end='2023-12-31')
gdp_data.reset_index(inplace=True)
gdp_data['Year'] = gdp_data['DATE'].dt.year
gdp_data.rename(columns={'DATE': 'Date', 'GDP': 'GDP (in billions)'}, inplace=True)

# Fetch Federal Debt data
debt_data = pdr.DataReader('GFDEBTN', 'fred', start='1970-01-01', end='2023-12-31')
debt_data.reset_index(inplace=True)
debt_data['Year'] = debt_data['DATE'].dt.year
debt_data.drop_duplicates(subset='Year', keep='last', inplace=True)
debt_data.rename(columns={'DATE': 'Date', 'GFDEBTN': 'Total Public Debt (in millions)'}, inplace=True)

# Merge the datasets on the 'Year' column
merged_data = pd.merge(gdp_data, debt_data, on='Year')

# Convert Debt to billions to match the GDP units
merged_data['Total Public Debt (in billions)'] = merged_data['Total Public Debt (in millions)'] / 1000

# Calculate the debt-to-GDP ratio
merged_data['Debt-to-GDP Ratio'] = merged_data['Total Public Debt (in billions)'] / merged_data['GDP (in billions)']

# Display the resulting DataFrame
print(merged_data[['Year', 'GDP (in billions)', 'Total Public Debt (in billions)', 'Debt-to-GDP Ratio']])


     Year  ...  Debt-to-GDP Ratio
0    1970  ...           0.370204
1    1970  ...           0.364594
2    1970  ...           0.358321
3    1970  ...           0.357482
4    1971  ...           0.373632
..    ...  ...                ...
211  2022  ...           1.189761
212  2023  ...           1.268069
213  2023  ...           1.256382
214  2023  ...           1.231486
215  2023  ...           1.216207

"""
EXERCISE 4 (BONUS)

Plot the debt-to-gdp ratio over time. Include a red line for when the
ratio crossed 1.00
"""
import matplotlib.pyplot as plt

# Assuming 'merged_data' is already prepared from the previous steps

# Plotting the debt-to-GDP ratio
plt.figure(figsize=(12, 6))
plt.plot(merged_data['Year'], merged_data['Debt-to-GDP Ratio'], label='Debt-to-GDP Ratio', marker='o')

# Drawing a red horizontal line at ratio 1.00
plt.axhline(y=1.00, color='r', linestyle='--', label='Debt = 100% of GDP')

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Debt-to-GDP Ratio')
plt.title('US Debt-to-GDP Ratio Over Time')
plt.legend()

# Displaying the plot
plt.grid(True)
plt.show()
