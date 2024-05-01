"""
INTRODUCTION

In today's exercise, we'll study one of the great failures of macroeconomics -
the Phillips Curve. Originally, this was the theory that unemployment and 
inflation were inversely related, so central banks could lower unemployment 
by increasing inflation (and vice-versa.) However, in the 1970s, this 
relationship broke down and the USA suffered both acute inflation
AND unemployment.
"""

"""
DOCUMENTATION

Below is the documentation for macrodata.csv; you don't have to read it 
thoroughly, merely consult it when the need arises or curiosity strikes.

Compiled by Skipper Seabold. All data are from the Federal Reserve Bank of St.
Louis [1] except the unemployment rate which was taken from the National
Bureau of Labor Statistics [2]. ::

    [1] Data Source: FRED, Federal Reserve Economic Data, Federal Reserve Bank of
        St. Louis; http://research.stlouisfed.org/fred2/; accessed December 15,
        2009.

    [2] Data Source: Bureau of Labor Statistics, U.S. Department of Labor;
        http://www.bls.gov/data/; accessed December 15, 2009.

    Number of Observations - 203

    Number of Variables - 14

    Variable name definitions::

        year      - 1959q1 - 2009q3
        quarter   - 1-4
        realgdp   - Real gross domestic product (Bil. of chained 2005 US$,
                    seasonally adjusted annual rate)
        realcons  - Real personal consumption expenditures (Bil. of chained
                    2005 US$, seasonally adjusted annual rate)
        realinv   - Real gross private domestic investment (Bil. of chained
                    2005 US$, seasonally adjusted annual rate)
        realgovt  - Real federal consumption expenditures & gross investment
                    (Bil. of chained 2005 US$, seasonally adjusted annual rate)
        realdpi   - Real private disposable income (Bil. of chained 2005
                    US$, seasonally adjusted annual rate)
        cpi       - End of the quarter consumer price index for all urban
                    consumers: all items (1982-84 = 100, seasonally adjusted).
        m1        - End of the quarter M1 nominal money stock (Seasonally
                    adjusted)
        tbilrate  - Quarterly monthly average of the monthly 3-month
                    treasury bill: secondary market rate
        unemp     - Seasonally adjusted unemployment rate (%)
        pop       - End of the quarter total population: all ages incl. armed
                    forces over seas
        infl      - Inflation rate (ln(cpi_{t}/cpi_{t-1}) * 400)
        realint   - Real interest rate (tbilrate - infl)
"""

"""
EXERCISE 1

Question: In the 1960s, was there an inverse relationship between unemployment
and inflation?

Long: Open macrodata.csv. What is the unit of observation?

Restrict your analysis to macroeconomics data between 1960-69 by creating a
smaller dataframe consisting entirely of data from this time period.

Using whatever package you prefer, perform a linear regression using Ordinary
Least Squares. Use umemployment as the dependant variable and inflation as the
independant variable. Was there a statistically significant relationship 
between these two variables? Is the coefficient positive or negative?
"""
import pandas as pd

# Load the dataset
file_path = '/Users/feitianyang/Documents/GitHub/datasci-harris-tfeiaaa/macrodata.csv'
macrodata = pd.read_csv(file_path)

# Display the first few rows of the dataframe and its columns
macrodata.head(), macrodata.columns
(   year  quarter   realgdp  realcons  ...  unemp      pop  infl  realint
 0  1959        1  2710.349    1707.4  ...    5.8  177.146  0.00     0.00
 1  1959        2  2778.801    1733.7  ...    5.1  177.830  2.34     0.74
 2  1959        3  2775.488    1751.8  ...    5.3  178.657  2.74     1.09
 3  1959        4  2785.204    1753.7  ...    5.6  179.386  0.27     4.06
 4  1960        1  2847.699    1770.5  ...    5.2  180.007  2.31     1.19

import numpy as np

# Getting X and y values
X = data_1960s['infl'].values
y = data_1960s['unemp'].values

# Adding the intercept term manually
X_with_intercept = np.column_stack((np.ones(X.shape[0]), X))

# Computing the coefficients using the Normal Equation
beta = np.linalg.inv(X_with_intercept.T @ X_with_intercept) @ X_with_intercept.T @ y

# Coefficients
intercept_manual = beta[0]
coefficient_manual = beta[1]

# Compute R-squared manually
y_pred = X_with_intercept @ beta
ss_res = np.sum((y - y_pred) ** 2)
ss_tot = np.sum((y - np.mean(y)) ** 2)
r_squared_manual = 1 - ss_res / ss_tot

intercept_manual, coefficient_manual, r_squared_manual
(5.848975969554865, -0.4181848718968205, 0.5534491599415935)










"""
EXERCISE 2

Question: Did this relationship persist into the 1970s?

Long: Repeat Exercise 1 but with data from the period 1970-79. What is the
magnitude of the coefficient? How does it compare to the same coefficient from
the sixties? 

Hint: You don't have to use functions here - copy pasting code from Exercise 1 
is fine!
"""
# Filter the dataset for the 1970s
data_1970s = macrodata[(macrodata['year'] >= 1970) & (macrodata['year'] < 1980)]

# Getting X and y values for the 1970s
X_1970s = data_1970s['infl'].values
y_1970s = data_1970s['unemp'].values

# Adding the intercept term manually for the 1970s
X_1970s_with_intercept = np.column_stack((np.ones(X_1970s.shape[0]), X_1970s))

# Computing the coefficients using the Normal Equation for the 1970s
beta_1970s = np.linalg.inv(X_1970s_with_intercept.T @ X_1970s_with_intercept) @ X_1970s_with_intercept.T @ y_1970s

# Coefficients for the 1970s
intercept_1970s = beta_1970s[0]
coefficient_1970s = beta_1970s[1]

# Compute R-squared manually for the 1970s
y_pred_1970s = X_1970s_with_intercept @ beta_1970s
ss_res_1970s = np.sum((y_1970s - y_pred_1970s) ** 2)
ss_tot_1970s = np.sum((y_1970s - np.mean(y_1970s)) ** 2)
r_squared_1970s = 1 - ss_res_1970s / ss_tot_1970s

(intercept_1970s, coefficient_1970s, r_squared_1970s)
Out[105]: (6.6620334874656635, -0.06194173305607096, 0.033529874788211234)

"""
EXERCISE 3

Question: In the 1970s, what was the relationship between the annual CHANGE in 
inflation and unemployment?

Long: In your original dataframe, create a change in inflation column, subtracting
inflation in the current quarter with inflation from a year ago. (Be careful and
keep in mind the unit of observation of this data!) Then repeat Exercise 2 
using change in inflation instead of inflation.

Hint: For this exercise, you will have to use the shift() function. Run the 
following bit of code and explore the dataframe to get a sense of 
what shift() does:
    
    df["newvar"] = df["realint"].shift(1)
    
"""
macrodata['infl_shifted'] = macrodata['infl'].shift(1)  # shift by one quarter for demonstration

# Show the changes to see how shift() works
macrodata[['year', 'quarter', 'infl', 'infl_shifted']].head(10)
   year  quarter  infl  infl_shifted
0  1959        1  0.00           NaN
1  1959        2  2.34          0.00
2  1959        3  2.74          2.34
3  1959        4  0.27          2.74
4  1960        1  2.31          0.27
5  1960        2  0.14          2.31
6  1960        3  2.70          0.14
7  1960        4  1.21          2.70
8  1961        1 -0.40          1.21
9  1961        2  1.47         -0.40
# Calculate the annual change in inflation
macrodata['change_in_infl'] = macrodata['infl'] - macrodata['infl'].shift(4)

# Filter the dataset for the 1970s again, including the new variable
data_1970s_change = macrodata[(macrodata['year'] >= 1970) & (macrodata['year'] < 1980)]

# Getting X and y values for the change in inflation analysis
X_1970s_change = data_1970s_change['change_in_infl'].values
y_1970s_change = data_1970s_change['unemp'].values

# Adding the intercept term manually for the 1970s change analysis
X_1970s_change_with_intercept = np.column_stack((np.ones(X_1970s_change.shape[0]), X_1970s_change))

# Computing the coefficients using the Normal Equation for the 1970s change analysis
beta_1970s_change = np.linalg.inv(X_1970s_change_with_intercept.T @ X_1970s_change_with_intercept) @ X_1970s_change_with_intercept.T @ y_1970s_change

# Coefficients for the 1970s change analysis
intercept_1970s_change = beta_1970s_change[0]
coefficient_1970s_change = beta_1970s_change[1]

# Compute R-squared manually for the 1970s change analysis
y_pred_1970s_change = X_1970s_change_with_intercept @ beta_1970s_change
ss_res_1970s_change = np.sum((y_1970s_change - y_pred_1970s_change) ** 2)
ss_tot_1970s_change = np.sum((y_1970s_change - np.mean(y_1970s_change)) ** 2)
r_squared_1970s_change = 1 - ss_res_1970s_change / ss_tot_1970s_change

(intercept_1970s_change, coefficient_1970s_change, r_squared_1970s_change)
Out[127]: (6.336867947388466, -0.17391073476769844, 0.2789908010872024)
