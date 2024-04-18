"""
EXERCISE 1

Open the file diamonds.csv, and explore it using .describe()

Then, use groupby() to create an object df_color which groups by color.
"""
import pandas as pd

# Load the diamonds.csv file
diamonds = pd.read_csv('/Users/feitianyang/Documents/GitHub/datasci-harris-tfeiaaa/diamonds.csv')

# Use describe() to explore the data
data_description = diamonds.describe()

# Use groupby() to group the data by color
df_color = diamonds.groupby('color')

data_description



"""
EXERCISE 2

The color of a diamond is graded from D to Z, though it maxes out at J 
in our data. D is colorless and diamonds get progressively darker as we 
go towards J. Colorless diamonds are the most desirable of diamonds 
and should be the most expensive: 
https://www.lumeradiamonds.com/diamond-education/diamond-color

Using the method mean() check whether D-color diamonds are in fact
more expensive than other categories. Do you seen any trend? Is it in
the right direction?

Hint: Groupby objects can "call" columns e.g. 

    df_color["depth"].describe()

will give you summary statistics for the column named depth across 
groups. Try it out and see.
    
At this point you have to figure out the exact command to get a short
list of prices and your output should looks something like this:

color
D    3169.95
E    3076.75
F    3724.89
G    3999.14
H    4486.67
I    5091.87
J    5323.82
Name: price, dtype: float64

In other words - darker diamonds appear to be *more* expensive
on average! This is in contrast to our expectation that darker 
diamonds should be less expensive
"""
# Using the df_color groupby object to calculate the mean price for each color category
mean_prices_by_color = df_color['price'].mean()
mean_prices_by_color
color
D    3169.954096
E    3076.752475
F    3724.886397
G    3999.135671
H    4486.669196
I    5091.874954
J    5323.818020
Name: price, dtype: float64
"""
EXERCISE 3

Here's a theory for why that's happening: our results are being
confounded by weight. Darker diamonds would usually sell for less.
In our dataset, they are also larger, which pushes up the price.

To check whether this theory is plausible, check how the average 
weight (in carats) varies across groups. If it appears that darker
colors are also larger, that lends support to this theory
"""
# Using the df_color groupby object to calculate the mean carat (weight) for each color category
mean_carats_by_color = df_color['carat'].mean()
mean_carats_by_color
color
D    0.657795
E    0.657867
F    0.736538
G    0.771190
H    0.911799
I    1.026927
J    1.162137
Name: carat, dtype: float64
"""
EXERCISE 4

Short: check if the effect is diminished when we "control" for size

Long: 1. Look up the average weight of diamonds in the dataset

2. Create an indicator variable called "small" that has the value 1 
if the diamond is smaller than the average weight and 0 otherwise

3. Create a groupby object using both color AND this indicator
variable

4. Check the mean price by group for this combination of categories, 
focusing on the price of small diamonds 
"""


# Step 1: Calculate the average weight of diamonds in the dataset
average_carat = diamonds['carat'].mean()

# Step 2: Create an indicator variable 'small' based on whether the diamond is smaller than the average weight
diamonds['small'] = (diamonds['carat'] < average_carat).astype(int)

# Step 3: Create a groupby object using both 'color' and 'small'
df_color_small = diamonds.groupby(['color', 'small'])

# Step 4: Calculate the mean price by group for the combination of color and 'small'
mean_prices_by_color_and_size = df_color_small['price'].mean()
mean_prices_by_color_and_size.loc[:, 1]  # Focusing on small diamonds (small=1)

color
D    1503.577173
E    1430.061563
F    1472.542419
G    1321.974222
H    1222.627030
I    1226.350947
J    1136.629301
Name: price, dtype: float64
