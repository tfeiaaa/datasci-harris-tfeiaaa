"""
EXERCISE 1

Short: Open the gdp data and turn it into a CLEAN long-shaped dataframe.
Make sure that the resulting year variable is an int object

Long: Open gdp.csv, and use melt() to convert it into a long-shaped dataframe.
At this point you'll observe that "year" column has ugly entries like
"gdp2021". There are multiple ways you can fix this:
    
    - Don't use melt()! Use wide_to_long() instead, looking up how it works
    online: https://pandas.pydata.org/docs/user_guide/reshaping.html
    - Use map() or apply() to fix this by the application of function, maybe
    even a lambda function
    - Use df["x"].str to "vectorize" the column x in dataframe df. You can now
    apply any string function the way you normally would e.g. df["x"].str.upper()
    The method astype(int) can convert str to int
    
The choice of this is left to you. You can pick one at random by choosing
a random number from 1 to 3 at https://www.random.org
"""
import pandas as pd

# Load the GDP data
gdp_df = pd.read_csv('/Users/feitianyang/Documents/GitHub/datasci-harris-tfeiaaa/gdp.csv')

# Display the first few rows of the data to understand its structure
gdp_df.head()
   state_id   gdp2021   gdp2022   gdp2023
0        17       973      1002      1033
1        18       385       373       396
2        55       289       298       307
# Using wide_to_long to reshape the dataframe and extract the year
gdp_long_df = pd.wide_to_long(gdp_df, stubnames='gdp', i='state_id', j='year', suffix='\d{4}').reset_index()

# Renaming the 'gdp' column to a more meaningful name
gdp_long_df.rename(columns={'gdp': 'gdp_value'}, inplace=True)

# Ensure the 'year' column is an integer
gdp_long_df['year'] = gdp_long_df['year'].astype(int)

gdp_long_df.head()
Empty DataFrame
Columns: [state_id, year,  gdp2021,  gdp2022,  gdp2023, gdp_value]
Index: []
# Strip any whitespace from the column names
gdp_df.columns = gdp_df.columns.str.strip()

# Try the wide_to_long transformation again
gdp_long_df = pd.wide_to_long(gdp_df, stubnames='gdp', i='state_id', j='year', suffix='\d{4}').reset_index()

# Renaming the 'gdp' column to a more meaningful name and ensuring correct data types
gdp_long_df.rename(columns={'gdp': 'gdp_value'}, inplace=True)
gdp_long_df['year'] = gdp_long_df['year'].astype(int)

gdp_long_df.head()
   state_id  year  gdp_value
0        17  2021        973
1        18  2021        385
2        55  2021        289
3        17  2022       1002
4        18  2022        373

"""
EXERCISE 2

Short: Do the same for the population data

Long: This does not require a longer explanation 
"""
# Load the population data
population_df = pd.read_csv('/Users/feitianyang/Documents/GitHub/datasci-harris-tfeiaaa/population.csv')

# Display the first few rows to understand its structure
population_df.head()
  state   pop2021   pop2022   pop2023
0    IL     12.51     12.72     12.83
1    IN      6.71      6.79      6.83
2    WI      5.79      5.85      5.91
# Strip any whitespace from the column names
population_df.columns = population_df.columns.str.strip()

# Use wide_to_long to reshape the dataframe and extract the year
population_long_df = pd.wide_to_long(population_df, stubnames='pop', i='state', j='year', suffix='\d{4}').reset_index()

# Renaming the 'pop' column to a more meaningful name and ensuring correct data types
population_long_df.rename(columns={'pop': 'population'}, inplace=True)
population_long_df['year'] = population_long_df['year'].astype(int)

population_long_df.head()
  state  year  population
0    IL  2021       12.51
1    IN  2021        6.71
2    WI  2021        5.79
3    IL  2022       12.72
4    IN  2022        6.79
"""
EXERCISE 3

Short: Merge the two data frames using the crosswalk provided in L09_data_crosswalk.csv

Long: It appears that the two dataset identify the state using different 
techniques. The population data uses the abbreviation of the state's name. The
GDP data uses a number to identify it - specifically it uses the FIPS
code: https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards

Create a dataframe that merges the gdp dataframe with the crosswalk using "state_id"
in the gdp dataframe and "FIPS" in the crosswalk dataframe. Then merge df with the 
population df using "Abbreviation" in df and "state" in the population dataframe.
"""
# Load the crosswalk data
crosswalk_df = pd.read_csv('/Users/feitianyang/Documents/GitHub/datasci-harris-tfeiaaa/crosswalk.csv')

# Display the first few rows to understand its structure
crosswalk_df.head()
   FIPS   Statename Abbreviation
0     1     ALABAMA           AL
1     2      ALASKA           AK
2     4     ARIZONA           AZ
3     5    ARKANSAS           AR
4     6  CALIFORNIA           CA
# Strip any whitespace from the column names
crosswalk_df.columns = crosswalk_df.columns.str.strip()

# Merge the GDP long dataframe with the crosswalk dataframe
gdp_crosswalk_merged = pd.merge(gdp_long_df, crosswalk_df, left_on='state_id', right_on='FIPS')

# Merge the result with the population long dataframe
final_merged_df = pd.merge(gdp_crosswalk_merged, population_long_df, left_on=['Abbreviation', 'year'], right_on=['state', 'year'])

# Select relevant columns for the final dataframe
final_merged_df = final_merged_df[['state_id', 'Statename', 'Abbreviation', 'year', 'gdp_value', 'population']]

final_merged_df.head()
   state_id  Statename Abbreviation  year  gdp_value  population
0        17   ILLINOIS           IL  2021        973       12.51
1        18    INDIANA           IN  2021        385        6.71
2        55  WISCONSIN           WI  2021        289        5.79
3        17   ILLINOIS           IL  2022       1002       12.72
4        18    INDIANA           IN  2022        373        6.79

"""
EXERCISE 4

Short: Clean the data up, removing extraneous columns and reordering it so that
it goes: state, year, then the two economic indicators

Long: Use .drop to get rid of any columns you no longer want e.g. state_id. 
Reordering is done by passing through a list of column names arranged
in the desired order.
"""
# Drop the 'state_id' column and reorder columns
final_cleaned_df = final_merged_df.drop(columns='state_id')
final_cleaned_df = final_cleaned_df[['Statename', 'Abbreviation', 'year', 'gdp_value', 'population']]

final_cleaned_df.head()
   Statename Abbreviation  year  gdp_value  population
0   ILLINOIS           IL  2021        973       12.51
1    INDIANA           IN  2021        385        6.71
2  WISCONSIN           WI  2021        289        5.79
3   ILLINOIS           IL  2022       1002       12.72
4    INDIANA           IN  2022        373        6.79
"""
BONUS

- Find the GDP per capita. The gdp presented is in billions and the population 
is in millions

- Use the sort_values method to arrange it neatly, first by state and then by 
year
 https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html
"""