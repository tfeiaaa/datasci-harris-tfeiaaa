"""
Write your answers in the space between the questions, and commit/push only
this file (homework2.py) and countries.csv to your repo. Note that there can 
be a difference between giving a "minimally" right answer, 
and a really good answer, so it can pay to put thought into your work. 

This is a much longer project than those you've done in class - remember to use
comments to help readers navigate your work!

To answer these questions, you will use the two csv files provided in the repo.
The file named gdp.csv contains the per capita GDP of many countries in and 
around Europe in 2023 US dollars. The file named population.csv contains 
estimates of the population of many countries.
"""

"""
QUESTION 1

Short: Open the data

Long: Load the GDP data into a dataframe. Specify an absolute path using the Python 
os library to join filenames, so that anyone who clones your homework repo 
only needs to update one string for all loading to work.
"""
import pandas as pd
import os

# Define the base directory where the files are located.
base_dir = '/Users/feitianyang/Documents/GitHub/datasci-harris-tfeiaaa'

# Construct the path to the GDP data file using os.path.join
gdp_file_path = os.path.join(base_dir, 'gdp.csv')

# Load the GDP data into a DataFrame
gdp_data = pd.read_csv(gdp_file_path)

# Display the first few rows of the dataframe to confirm it's loaded correctly
print(gdp_data.head())
                                       TIME GDP2012  ... GDP2022 GDP2023
0  European Union - 27 countries (from 2020)   25770  ...   35460   37610
1       Euro area – 20 countries (from 2023)   29000  ...   38760   40990
2      Euro area - 19 countries  (2015-2022)   29230  ...   39000   41220
3                                    Belgium   34770  ...   47440   49540
4                                   Bulgaria    5780  ...   13270   14580


"""
QUESTION 2

Short: Clean the data

Long: There are numerous issues with the data, on account of it having been 
haphazardly assembled from an online table. To start with, the column containing
country names has been labeled TIME. Fix this.

Next, trim this down to only member states of the European Union. To do this, 
find a list of members states (hint: there are 27 as of Apr 2024) and manually 
create your own CSV file with this list. Name this file countries.csv. Load it 
into a dataframe. Merge the two dataframes and keep only those rows with a 
match.

(Hint: This process should also flag the two errors in naming in gdp.csv. One 
 country has a dated name. Another is simply misspelt. Correct these.)
"""


import pandas as pd
import os

# Assume the base path is already defined and correct.
# Load the GDP data
gdp_file_path = os.path.join(base_path, 'gdp.csv')
gdp_data = pd.read_csv(gdp_file_path)

# Fix the incorrect column label
gdp_data.rename(columns={'TIME': 'Country'}, inplace=True)

# Load the list of EU countries from the manually created CSV
countries_file_path = os.path.join(base_path, 'countries.csv')
eu_countries = pd.read_csv(countries_file_path)

# Merge the dataframes to focus only on EU countries
eu_gdp_data = pd.merge(gdp_data, eu_countries, on='Country', how='inner')

# Identify and correct naming errors in the gdp.csv
# Suppose "Czechia" is labeled as "Czech Republic" and "Slovakia" as "Slovkia"
eu_gdp_data['Country'].replace({'Czech Republic': 'Czechia', 'Slovkia': 'Slovakia'}, inplace=True)

# Print the cleaned data
print(eu_gdp_data.head())
    Country GDP2012 GDP2013  ... Unnamed: 4 Unnamed: 5 Unnamed: 6
0   Belgium   34770   35210  ...        NaN        NaN        NaN
1  Bulgaria    5780    5790  ...        NaN        NaN        NaN
2   Denmark   45530   46100  ...        NaN        NaN        NaN
3   Germany   34130   34860  ...        NaN        NaN        NaN
4   Estonia   13520   14320  ...        NaN        NaN        NaN





"""
QUESTION 3

Short: Reshape the data

Long: Convert this wide data into long data with columns named year and gdp.
The year column should contain int datatype objects.

Remember to convert GDP from string to float. (Hint: the data uses ":" instead
of NaN to denote missing values. You will have to fix this first.) 
"""

import pandas as pd
import os

# Assuming previous steps are done and eu_gdp_data is ready and correct
# Replace ":" with NaN
eu_gdp_data.replace(':', pd.NA, inplace=True)

# Reshape the data to long format
id_vars = ['Country']  # This assumes 'Country' is the only non-year column.
value_vars = [col for col in eu_gdp_data.columns if col not in id_vars]  # Year columns.

long_format_data = pd.melt(eu_gdp_data, id_vars=id_vars, value_vars=value_vars, var_name='year', value_name='gdp')

# Convert 'year' to int (strip out non-numeric parts first)
long_format_data['year'] = long_format_data['year'].str.extract('(\d+)').astype(int)

# Ensure 'gdp' is properly converted to float, handling NA values
long_format_data['gdp'] = pd.to_numeric(long_format_data['gdp'], errors='coerce')

# Print the first few rows of the reshaped DataFrame
print(long_format_data.head())
    Country  year      gdp
0   Belgium  2012  34770.0
1  Bulgaria  2012   5780.0
2   Denmark  2012  45530.0
3   Germany  2012  34130.0
4   Estonia  2012  13520.0


"""
QUESTION 4

Short: Repeat this process for the population data.

Long: Load population.csv into a dataframe. Rename the TIME columns. 
Merge it with the dataframe loaded from countries.csv. Make it long, naming
the resulting columns year and population. Convert population and year into int.
"""
import pandas as pd
import os


# Load the population data
population_file_path = os.path.join(base_path, 'population.csv')
population_data = pd.read_csv(population_file_path)

# Fix the incorrect column label
population_data.rename(columns={'TIME': 'Country'}, inplace=True)

# Merge the dataframes to focus only on EU countries
eu_population_data = pd.merge(population_data, eu_countries, on='Country', how='inner')

# Reshape the data to long format
id_vars = ['Country']  # This assumes 'Country' is the only non-year column.
value_vars = [col for col in eu_population_data.columns if col not in id_vars]  # Year columns.

long_format_population = pd.melt(eu_population_data, id_vars=id_vars, value_vars=value_vars, var_name='year', value_name='population')

# Convert 'year' to int (strip out non-numeric parts first)
long_format_population['year'] = long_format_population['year'].str.extract('(\d+)').astype(int)

# Convert 'population' to int, handling NA values
long_format_population['population'] = pd.to_numeric(long_format_population['population'], errors='coerce').astype('Int64')

# Print the first few rows of the reshaped DataFrame
print(long_format_population.head())
          Country  year  population
0         Belgium  2012    11075889
1        Bulgaria  2012     7327224
2  Czech Republic  2012    10505445
3         Denmark  2012     5580516
4         Germany  2012    80327900

"""
QUESTION 5

Short: Merge the two dataframe, find the total GDP

Long: Merge the two dataframes. Total GDP is per capita GDP times the 
population.
"""
import pandas as pd
import os


# Merge the GDP and Population dataframes on 'Country' and 'year'
combined_data = pd.merge(long_format_data, long_format_population, on=['Country', 'year'])

# Calculate the total GDP
combined_data['total_gdp'] = combined_data['gdp'] * combined_data['population']

# Print the first few rows of the merged DataFrame with the total GDP
print(combined_data.head())
    Country  year      gdp  population        total_gdp
0   Belgium  2012  34770.0    11075889   385108660530.0
1  Bulgaria  2012   5780.0     7327224    42351354720.0
2   Denmark  2012  45530.0     5580516   254080893480.0
3   Germany  2012  34130.0    80327900  2741591227000.0
4   Estonia  2012  13520.0     1325217    17916933840.0

"""
QUESTION 6

Short: For each country, find the annual GDP growth rate in percentage points.
Round down to 2 digits.

Long: Sort the data by name, and then year. You can now use a variety of methods
to get the gdp growth rate, and we'll suggest one here: 

1. Use groupby and shift(1) to create a column containing total GDP from the
previous year. We haven't covered shift in class, so you'll need to look
this method up. Using groupby has the benefit of automatically generating a
missing value for 2012; if you don't do this, you'll need to ensure that you
replace all 2012 values with missing values.



2. Use the following arithematic operation to get the growth rate:
    gdp_growth = (total_gdp - total_gdp_previous_year) * 100 / total_gdp
"""
import pandas as pd
import os



# Step 1: Sort the data by 'Country' and 'year'
combined_data = combined_data.sort_values(by=['Country', 'year'])

# Step 2: Calculate the total GDP from the previous year for each country
combined_data['total_gdp_previous_year'] = combined_data.groupby('Country')['total_gdp'].shift(1)

# Step 3: Compute the GDP growth rate
# Ensure to handle divisions by zero or missing previous year GDP values appropriately
combined_data['gdp_growth'] = (combined_data['total_gdp'] - combined_data['total_gdp_previous_year']) / combined_data['total_gdp_previous_year'] * 100

# Handling missing values for the year 2012 and other potential missing data
combined_data['gdp_growth'] = combined_data['gdp_growth'].fillna(0)  # Optional: fill with 0 or some other logic

# Round the GDP growth rate to 2 decimal places
combined_data['gdp_growth'] = combined_data['gdp_growth'].apply(lambda x: round(x, 2))

# Print some of the data to check
print(combined_data[['Country', 'year', 'total_gdp', 'total_gdp_previous_year', 'gdp_growth']].head())


import pandas as pd
import os



# Step 1: Sort the data by 'Country' and 'year'
combined_data = combined_data.sort_values(by=['Country', 'year'])

# Step 2: Calculate the total GDP from the previous year for each country
combined_data['total_gdp_previous_year'] = combined_data.groupby('Country')['total_gdp'].shift(1)

# Step 3: Compute the GDP growth rate using the corrected formula
# Handling potential division by zero errors with a small number if required
combined_data['gdp_growth'] = ((combined_data['total_gdp'] - combined_data['total_gdp_previous_year']) * 100) / combined_data['total_gdp'].replace(0, pd.NA)

# Handling missing values for the year 2012 and other potential missing data
combined_data['gdp_growth'] = combined_data['gdp_growth'].fillna(0)  # Optional: fill with 0 or some other logic

# Round the GDP growth rate to 2 decimal places
combined_data['gdp_growth'] = combined_data['gdp_growth'].apply(lambda x: round(x, 2) if pd.notna(x) else x)

# Print some of the data to check
print(combined_data[['Country', 'year', 'total_gdp', 'total_gdp_previous_year', 'gdp_growth']].head())



"""
QUESTION 7

Short: Which country has the highest total gdp (for the any year) in the EU? 

Long: Do not hardcode your answer! You will have to put the automate putting 
the name of the country into a string called country_name and using the following
format string to display it:

print(f"The largest country in the EU is {country_name}")
"""
import pandas as pd
import os


# Find the row with the highest total GDP
max_gdp_row = combined_data[combined_data['total_gdp'] == combined_data['total_gdp'].max()]

# Get the country name with the highest total GDP
country_name = max_gdp_row['Country'].values[0]  # Taking the first value in case there are multiple entries

# Print the country with the highest total GDP
print(f"The largest country in the EU is {country_name}")
The largest country in the EU is Germany

"""
QUESTION 8

Create a dataframe that consists only of the country you found in Question 7

In which year did this country have the most growth in the period 2012-23?

In which year did this country have the least growth in the peroid 2012-23?

Do not hardcode your answer. You will have to use the following format strings 
to show your answer:

print(f"Their best year was {best_year}")
print(f"Their worst year was {worst_year}")
"""

import pandas as pd
import os


# Filter the DataFrame for the specific country
country_data = combined_data[combined_data['Country'] == country_name]

# Filter for the years between 2012 and 2023
country_data = country_data[(country_data['year'] >= 2012) & (country_data['year'] <= 2023)]

# Identify the year with the most growth
best_year_row = country_data[country_data['gdp_growth'] == country_data['gdp_growth'].max()]
best_year = best_year_row['year'].values[0]  # Assuming there's a unique max; handle duplicates as needed

# Identify the year with the least growth
worst_year_row = country_data[country_data['gdp_growth'] == country_data['gdp_growth'].min()]
worst_year = worst_year_row['year'].values[0]  # Assuming there's a unique min; handle duplicates as needed

# Print the results
print(f"Their best year was {best_year}")
Their best year was 2023
print(f"Their worst year was {worst_year}")
Their worst year was 2020