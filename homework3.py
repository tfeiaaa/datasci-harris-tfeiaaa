# Your name here
# Your CNET ID here (this is the part of your uchicago email id before the @)
# Your github user id here

"""
INSTRUCTIONS

Available: May 2nd

Due: May 12th at 11:59PM

Gentle reminder that, among other things, you

(a) Must answer your questions in the homework3.py file
(b) Must homework3.py commit to your clone of the GitHub homework repo
(c) Must link your GitHub repo to GradeScope
(d) Must NOT repeatedly use a hard-coded path for the working directory
(e) Must NOT modify the original data in any way

Failure to do any of these will result in the loss of points
"""

"""
QUESTION 1

In this question, you'll be replicating the graph from Lecture 14, slide 5
which shows the population of Europe from 0 AD to the present day in both
the linear and the log scale. You can find the data in population.csv, and the
variable names are self-explanatory.

Open this data and replicate the graph. 

Clarification: You are not required to replicate the y-axis of the right hand
side graph; leaving it as log values is fine!

Clarification: You are not required to save the figure

Hints: Note that...

- The numpy function .log() can be used to convert a column into logs
- It is a single figure with two subplots, one on the left and the other on
the right
- The graph only covers the period after 0 AD
- The graph only covers Europe
- The figure in the slides is 11 inches by 6 inches
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Load the data
data = pd.read_csv('/Users/feitianyang/Documents/GitHub/datasci-harris-tfeiaaa/population.csv')

# Step 2: Filter the data
# Filter for Europe and years starting from 0 AD
filtered_data = data[(data['Year'] >= 0) & (data['Entity'] == 'Europe')]

# Step 3: Create the plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 6))

# Subplot 1: Linear scale
ax1.plot(filtered_data['Year'], filtered_data['Population (historical estimates)'])
ax1.set_title('Population of Europe (Linear Scale)')
ax1.set_xlabel('Year')
ax1.set_ylabel('Population')

# Subplot 2: Log scale
ax2.plot(filtered_data['Year'], np.log(filtered_data['Population (historical estimates)']))
ax2.set_title('Population of Europe (Log Scale)')
ax1.set_xlabel('Year')
ax1.set_ylabel('Log of Population')

plt.tight_layout()
plt.show()



"""
QUESTION 2

A country's "capital stock" is the value of its' physical capital, which includes the 
stock of equipment, buildings, and other durable goods used in the production 
of goods and services. Macroeconomists seem to conisder it important to have 
public policies that encourage the growth of capital stock. Why is that?

In this exercise we will look at the relationship between capital stock and 
GDP. You can find data from the IMF in "capitalstock.csv" and documentation in
"capitalstock documentation.txt".

In this exercise we will only be using the variables that are demarcated in
thousands of 2017 international dollars to adjust for variation in the value 
of nominal national currency. Hint: These are the the variables that 
end in _rppp.

1. Open the dataset capitalstock.csv and limit the dataframe to only 
observations from 2018

import pandas as pd

# Load the capital stock data
capital_stock_data = pd.read_csv('/Users/feitianyang/Documents/GitHub/datasci-harris-tfeiaaa/capitalstock.csv')

# Filter the data for the year 2018 using the correct column name
capital_stock_2018 = capital_stock_data[capital_stock_data['year'] == 2018]

# Show the first few rows to confirm the filter
print(capital_stock_2018.head())

                 country  year  ...      kppp_n         GDP_n
58           Afghanistan  2018  ...         NaN   1296.559082
118              Albania  2018  ...  206.659638   1635.714600
178              Algeria  2018  ...  572.795227  20452.300780
238               Angola  2018  ...   41.546593  25627.742190
298  Antigua and Barbuda  2018  ...         NaN      4.334450

2. Construct a variable called "capital_stock" that is the sum of the general
government capital stock and private capital stock. Drop 
observations where the value of capital stock is 0 or missing. (We will be 
ignoring public-private partnership capital stock for the purpose of t
his exercise.)

# Step 1: Filter the dataframe for the year 2018
data_2018 = capital_stock_data[capital_stock_data['year'] == 2018]

# Step 2: Create the 'capital_stock' column
data_2018['capital_stock'] = data_2018['kgov_rppp'] + data_2018['kpriv_rppp']

# Drop rows where 'capital_stock' or 'GDP_rppp' is zero or missing
data_2018 = data_2018.dropna(subset=['capital_stock', 'GDP_rppp'])
data_2018 = data_2018[data_2018['capital_stock'] > 0]

# Show the modified data
data_2018[['country', 'year', 'kgov_rppp', 'kpriv_rppp', 'capital_stock', 'GDP_rppp']].head()



3. Create a scatterplot showing the relationship between log GDP and log
capital stock. Put capital stock on the y-axis. Add the line of best 
fit. Add labels where appropriate and make any cosmetic adjustments you want.

(Note: Does this graph suggest that macroeconomists are correct to consider 
 capital stock important? You don't have to answer this question - it's 
 merely for your own edification.)

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

# Calculate the logarithm of GDP and capital stock
data_2018['log_GDP_rppp'] = np.log(data_2018['GDP_rppp'])
data_2018['log_capital_stock'] = np.log(data_2018['capital_stock'])

# Create a scatterplot with a line of best fit
plt.figure(figsize=(10, 6))
sns.scatterplot(x='log_capital_stock', y='log_GDP_rppp', data=data_2018, alpha=0.6)

# Fit a linear regression line
slope, intercept, r_value, p_value, std_err = linregress(data_2018['log_capital_stock'], data_2018['log_GDP_rppp'])
x = np.linspace(min(data_2018['log_capital_stock']), max(data_2018['log_capital_stock']), 100)
y = slope * x + intercept
plt.plot(x, y, 'r', label=f'Line of Best Fit\nSlope: {slope:.4f}')

# Add labels and title
plt.xlabel('Log of Capital Stock')
plt.ylabel('Log of GDP')
plt.title('Relationship between Log of GDP and Log of Capital Stock')
plt.legend()
plt.grid(True)

plt.show()





(Note: Does this graph suggest that macroeconomists are correct to consider 
 capital stock important? You don't have to answer this question - it's 
 merely for your own edification.)

4. Estimate a model of the relationship between the log of GDP 
and the log of capital stock using OLS. GDP is the dependent 
variable. Print a table showing the details of your model and, using comments, 
interpret the coefficient on capital stock. 

import statsmodels.api as sm

# Define the dependent variable (GDP) and the independent variable (capital stock)
X = sm.add_constant(data_2018['log_capital_stock'])  # adding a constant for the intercept term
y = data_2018['log_GDP_rppp']

# Fit the OLS model
model = sm.OLS(y, X).fit()

# Print the summary of the model
model.summary()
"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:           log_GDP_rppp   R-squared:                       0.964
Model:                            OLS   Adj. R-squared:                  0.964
Method:                 Least Squares   F-statistic:                     4345.
Date:                Mon, 06 May 2024   Prob (F-statistic):          2.12e-118
Time:                        17:28:31   Log-Likelihood:                -82.634
No. Observations:                 163   AIC:                             169.3
Df Residuals:                     161   BIC:                             175.5
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
=====================================================================================
                        coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------
const                -0.6456      0.086     -7.481      0.000      -0.816      -0.475
log_capital_stock     0.9758      0.015     65.915      0.000       0.947       1.005
==============================================================================
Omnibus:                       19.090   Durbin-Watson:                   2.275
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               42.892
Skew:                          -0.480   Prob(JB):                     4.85e-10
Kurtosis:                       5.322   Cond. No.                         16.3
==============================================================================

Hint: when using the scatter() method that belongs to axes objects, the alpha
option can be used to make the markers transparent. s is the option that
controls size
"""