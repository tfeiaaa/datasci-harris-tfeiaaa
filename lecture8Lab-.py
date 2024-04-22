
"""
EXCERCISE 1

Short: Open the data.

Long: In this repo is a file named "L08 LabData.csv". Use pandas to create a
datafrane named df. Explore it.
"""
import pandas as pd


df = pd.read_csv('/Users/feitianyang/Documents/GitHub/datasci-harris-tfeiaaa/L08 LabData.csv')


df.head()
  DATEOFRECORDING  GDPRAWEST  POPULATIONINMILLION  UNEMPLOYMENTRATE
0     31DCMBR1947     2490.0                144.0               4.9
1     31DCMBR1948     2564.7                145.4               4.1
2     31DCMBR1949     2641.6                146.9               4.2
3     31DCMBR1950     2720.9                148.4               4.4
4     31DCMBR1951     2802.5                149.8               4.7

"""
EXCERCISE 2

Short: Rename the variables to something sensible

Long: You will notice that the column names are IN ALLCAPS AS IF THEY WERE SHOUTING
AT YOU making them hard to read. Change their names into something easier to use.
Use a standalone dictionary object to ensure that you can easily make changes in
the future. Make sure that you use the Python naming conventions for variables
e.g. all lower case. You can look up the what each variable means in the 
associated Codebook which every dataset should come with. In this case it is a
 plain text file.

Hint: the following variable names are suggested: date, gdp, population, 
unemployment
"""


column_names = {
    'DATEOFRECORDING': 'date',
    'GDPRAWEST': 'gdp',
    'POPULATIONINMILLION': 'population',
    'UNEMPLOYMENTRATE': 'unemployment'
}


df.rename(columns=column_names, inplace=True)


df.head()
          date     gdp  population  unemployment
0  31DCMBR1947  2490.0       144.0           4.9
1  31DCMBR1948  2564.7       145.4           4.1
2  31DCMBR1949  2641.6       146.9           4.2
3  31DCMBR1950  2720.9       148.4           4.4
4  31DCMBR1951  2802.5       149.8           4.7

"""
EXCERCISE 3

Short: Make a GDP per capita column

Long: Create a new column called gdp_per_capita which is equal to the total GDP
divided by the population. The end result should be in dollars. 
Recall that GDP is in billions of dollars while population is in millions of
people.

Hint: the GDP per capita in 1947 should be around 17,000 dollars
"""

df['gdp_per_capita'] = (df['gdp'] * 1e9) / (df['population'] * 1e6)


df.head()
          date     gdp  population  unemployment  gdp_per_capita
0  31DCMBR1947  2490.0       144.0           4.9    17291.666667
1  31DCMBR1948  2564.7       145.4           4.1    17638.927098
2  31DCMBR1949  2641.6       146.9           4.2    17982.300885
3  31DCMBR1950  2720.9       148.4           4.4    18334.905660
4  31DCMBR1951  2802.5       149.8           4.7    18708.277704

"""
EXCERCISE 4

Short: Fix the date column

Long: Whatever monster created this dataset seems to have used their own esoteric 
naming convention, truncating December to DCMBR. Awful! Panda's to_dateime module
cannot parse this. Create a function that will replace all instances of "31DCMBR"
in a string something that can be parsed by to_datetime such as "12-31-" and use
the map method to fix this column. Then use the to_datetime method to turn 
this column into a datetime object.
"""
def fix_date(date_str):
    """
    Replace '31DCMBR' with '12-31-' in the date string to make it parseable by to_datetime.

    :param date_str: The original date string.
    :return: The fixed date string.
    """
    return date_str.replace('31DCMBR', '12-31-')


df['date'] = df['date'].map(fix_date)


df['date'] = pd.to_datetime(df['date'], format='%m-%d-%Y')


df.head()
        date     gdp  population  unemployment  gdp_per_capita
0 1947-12-31  2490.0       144.0           4.9    17291.666667
1 1948-12-31  2564.7       145.4           4.1    17638.927098
2 1949-12-31  2641.6       146.9           4.2    17982.300885
3 1950-12-31  2720.9       148.4           4.4    18334.905660
4 1951-12-31  2802.5       149.8           4.7    18708.277704

"""
EXCERCISE 5

Short: Filter the dataset, so as to find all the 'good' years i.e. the years where the
rate of unemployment was less than 4.5%. How many were there?

Long: Create a dataframe called df_filtered that contains the rows for which 
the rate of unemployement is less than 4.5. Use df.shape to view the number of
rows remaining.

Hint: The answer should be 26
"""

df_filtered = df[df['unemployment'] < 4.5]


filtered_shape = df_filtered.shape

filtered_shape
(26, 5)
"""
BONUS

Short: Find the rate of growth of GDP per capita. You may assume that it grows
exponentially, and that the rate of growth is constant.

Long: Recall that the model of exponential growth looks something like this:
    
    y_2023 = y_1947 * (R^t)
    
where y_1947 is the value in 1947, y_2023 is the value in 2023, R is the rate of
growth (or 1 + rate of growth) and t is the number of years since 1947. Here t = 76

Using logs and rearranging, we have 

log(R) = (log(y_2023) - log(y_1947)) / t

Hint: Note that the math package has a function log that can generate the log
of various numbers. So log(2,10) will give you log 2 to the base 10.

More: https://www.w3schools.com/python/ref_math_log.asp

To get the antilog of x, you can use then use 10 ** x

Hint: Find y_2023 and y_1947 by using the .loc method. You can look up the indexes
using .head() and .tail()
"""
