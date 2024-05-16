"""
Economic booms and busts have always existed, but are they getting worse? Or
better? In this exercise we'll be looking at the relative variance of US GDP 
over the last few decades. A side benefit: getting to know the groupby method 
in greater detail!
"""

"""
EXERCISE 1
Get GDP data from FRED, from 1950 to 2023. Perform any operations you might
need to in order to "clean" it.
"""
import pandas_datareader.data as web
import datetime

# Define the time period
start_date = datetime.datetime(1950, 1, 1)
end_date = datetime.datetime(2023, 12, 31)

# Fetch GDP data from FRED
gdp_data = web.DataReader('GDP', 'fred', start_date, end_date)

# Display the first few rows of the data
print(gdp_data.head())
DATE               
1950-01-01  280.828
1950-04-01  290.383
1950-07-01  308.153
1950-10-01  319.945
1951-01-01  336.000

import pandas as pd

# Check for missing values
print(gdp_data.isnull().sum())

# Fill missing values with forward fill method
gdp_data.fillna(method='ffill', inplace=True)

# Ensure the date is the index and in datetime format
gdp_data.index = pd.to_datetime(gdp_data.index)

# Display the cleaned data
print(gdp_data.head())
DATE               
1950-01-01  280.828
1950-04-01  290.383
1950-07-01  308.153
1950-10-01  319.945
1951-01-01  336.000

import pandas_datareader.data as web
import datetime
import pandas as pd

# Define the time period
start_date = datetime.datetime(1950, 1, 1)
end_date = datetime.datetime(2023, 12, 31)

# Fetch GDP data from FRED
gdp_data = web.DataReader('GDP', 'fred', start_date, end_date)

# Check for missing values
print(gdp_data.isnull().sum())

# Fill missing values with forward fill method
gdp_data.fillna(method='ffill', inplace=True)

# Ensure the date is the index and in datetime format
gdp_data.index = pd.to_datetime(gdp_data.index)

# Display the cleaned data
print(gdp_data.head())
DATE               
1950-01-01  280.828
1950-04-01  290.383
1950-07-01  308.153
1950-10-01  319.945
1951-01-01  336.000

"""
EXERCISE 2
Normalize the GDP

If we merely look at raw variance, it will obviously be rising over time, as 
GDP is rising over time. First we need to "normalize" the GDP by dividing the
GDP in a particular time period with the average GDP of that decade.

Calculate the mean GDP by decade. Create an "adjusted_gdp" column that is
(GDP/mean_GDP)

Hints: - The // is the "floor division" operator in Python e.g. 1962 // 10 = 196

- The groupby method creates a DataFrame object that can be merged back into 
the original dataframe

- The groupby object creates a dataframe that has a method mean() that will return
the average value of series. So df.groupby('A')['B'].mean() will group by A and 
return the mean value of B
ref: https://pandas.pydata.org/pandas-docs/version/0.25.0/reference/api/pandas.core.groupby.GroupBy.mean.html
"""
import pandas_datareader.data as web
import datetime
import pandas as pd

# Step 1: Fetch the GDP data from FRED
start_date = datetime.datetime(1950, 1, 1)
end_date = datetime.datetime(2023, 12, 31)
gdp_data = web.DataReader('GDP', 'fred', start_date, end_date)

# Clean the data
gdp_data.fillna(method='ffill', inplace=True)
gdp_data.index = pd.to_datetime(gdp_data.index)

# Step 2: Calculate the decade for each entry
gdp_data['Decade'] = (gdp_data.index.year // 10) * 10

# Step 3: Group by decade and calculate the mean GDP for each decade
mean_gdp_by_decade = gdp_data.groupby('Decade')['GDP'].mean().reset_index()
mean_gdp_by_decade.columns = ['Decade', 'Mean_GDP']

# Step 4: Merge the mean GDP back into the original DataFrame
gdp_data = gdp_data.reset_index()
gdp_data = gdp_data.merge(mean_gdp_by_decade, on='Decade')

# Step 5: Create the "adjusted_gdp" column
gdp_data['adjusted_gdp'] = gdp_data['GDP'] / gdp_data['Mean_GDP']

# Display the resulting DataFrame
print(gdp_data.head())
        DATE      GDP  Decade  Mean_GDP  adjusted_gdp
0 1950-01-01  280.828    1950  414.5602      0.677412
1 1950-04-01  290.383    1950  414.5602      0.700460
2 1950-07-01  308.153    1950  414.5602      0.743325
3 1950-10-01  319.945    1950  414.5602      0.771770
4 1951-01-01  336.000    1950  414.5602      0.810497


"""
EXERCISE 3
Get the relative variance by decade, then plot the relative variance over
time.

Hint: - The groupby object is a dataframe with a var() method that works 
similarly to the above

- You don't need to merge it back into the original dataframe for this graph.
"""

import pandas_datareader.data as web
import datetime
import pandas as pd
import matplotlib.pyplot as plt

# Fetch the GDP data from FRED
start_date = datetime.datetime(1950, 1, 1)
end_date = datetime.datetime(2023, 12, 31)
gdp_data = web.DataReader('GDP', 'fred', start_date, end_date)

# Clean the data
gdp_data.fillna(method='ffill', inplace=True)
gdp_data.index = pd.to_datetime(gdp_data.index)

# Calculate the decade for each entry
gdp_data['Decade'] = (gdp_data.index.year // 10) * 10

# Group by decade and calculate the mean GDP for each decade
mean_gdp_by_decade = gdp_data.groupby('Decade')['GDP'].mean().reset_index()
mean_gdp_by_decade.columns = ['Decade', 'Mean_GDP']

# Merge the mean GDP back into the original DataFrame
gdp_data = gdp_data.reset_index()
gdp_data = gdp_data.merge(mean_gdp_by_decade, on='Decade')

# Create the "adjusted_gdp" column
gdp_data['adjusted_gdp'] = gdp_data['GDP'] / gdp_data['Mean_GDP']

# Step 1: Calculate the relative variance by decade
relative_variance_by_decade = gdp_data.groupby('Decade')['adjusted_gdp'].var().reset_index()
relative_variance_by_decade.columns = ['Decade', 'Relative_Variance']

# Step 2: Plot the relative variance over time
plt.figure(figsize=(10, 6))
plt.plot(relative_variance_by_decade['Decade'], relative_variance_by_decade['Relative_Variance'], marker='o')
plt.title('Relative Variance of Adjusted GDP by Decade')
plt.xlabel('Decade')
plt.ylabel('Relative Variance')
plt.grid(True)
plt.show()
