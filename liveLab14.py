"""
INTRODUCTION

This exercise asks you to play around with multiple models by using a dataset
containing the rates of violent crime per 100,000 residents for various US 
states. We will construct 4 different models and then use a new tool called
summary_col to show them all in a single compact table.
"""

"""
DOCUMENTATION

Title: Statewide Crime Data 2009

Notes: All data is for 2009 and was obtained from the American Statistical 
    Abstracts except as indicated below.
    
    
    Number of observations: 51
    Number of variables: 8
    Variable name definitions:

    state
        All 50 states plus DC.
    violent
        Rate of violent crimes / 100,000 population. Includes murder, forcible
        rape, robbery, and aggravated assault. Numbers for Illinois and
        Minnesota do not include forcible rapes. Footnote included with the
        American Statistical Abstract table reads:
        "The data collection methodology for the offense of forcible
        rape used by the Illinois and the Minnesota state Uniform Crime
        Reporting (UCR) Programs (with the exception of Rockford, Illinois,
        and Minneapolis and St. Paul, Minnesota) does not comply with
        national UCR guidelines. Consequently, their state figures for
        forcible rape and violent crime (of which forcible rape is a part)
        are not published in this table."
    murder
        Rate of murders / 100,000 population.
    hs_grad
        Percent of population having graduated from high school or higher.
    poverty
        % of individuals below the poverty line
    white
        Percent of population that is one race - white only. From 2009 American
        Community Survey
    single
        Calculated from 2009 1-year American Community Survey obtained
        from Census. Variable is Male householder, no wife present, family
        household combined with Female householder, no husband present, family
        household, divided by the total number of Family households.
    urban
        % of population in Urbanized Areas as of 2010 Census. Urbanized
        Areas are area of 50,000 or more people.
"""

"""
EXERCISE 1

One theory posits that a lack of education is responsible for violent crime.

Open the file statecrime.csv Create and estimate a linear model where violent 
crime per 100,000 residents is the endogenous variable and high school 
graduation rate is the exogenous variable.

Name this model "model1".

Use the OLS method from statsmodels:

    from statsmodels.regression.linear_model import OLS

Hint: in the example below, .fit() is immediately applied, and the variable 
named model is now storing the results of this model!

    model = OLS(<content>).fit()

"""
import pandas as pd

# Load the data
data = pd.read_csv('/Users/feitianyang/Documents/GitHub/datasci-harris-tfeiaaa/statecrime.csv')

# Display the first few rows and the columns to understand the structure
data.head(), data.columns
import statsmodels.api as sm

# Define the predictor (X) and response variable (y)
X = sm.add_constant(data['hs_grad'])  # adding a constant to include the intercept in the model
y = data['violent']

# Create the OLS model
model1 = sm.OLS(y, X).fit()

# Summary of the model
model1.summary()
"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                violent   R-squared:                       0.147
Model:                            OLS   Adj. R-squared:                  0.129
Method:                 Least Squares   F-statistic:                     8.433
Date:                Wed, 01 May 2024   Prob (F-statistic):            0.00551
Time:                        18:32:03   Log-Likelihood:                -340.03
No. Observations:                  51   AIC:                             684.1
Df Residuals:                      49   BIC:                             687.9
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const       2461.6710    706.516      3.484      0.001    1041.873    3881.469
hs_grad      -23.5984      8.126     -2.904      0.006     -39.929      -7.268
==============================================================================
Omnibus:                       48.213   Durbin-Watson:                   1.839
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              240.170
Skew:                           2.417   Prob(JB):                     7.04e-53
Kurtosis:                      12.468   Cond. No.                     2.26e+03
==============================================================================





"""
EXERCISE 2

Create model2 and model3, which are similar to model1 except that they look at
the poverty rate and urbanization rates respectively.

Create a model4 which includes all three factors as exogenous variables.
"""

# Creating model2 with poverty rate as the exogenous variable
X2 = sm.add_constant(data['poverty'])
model2 = OLS(Y, X2).fit()

# Creating model3 with urbanization rate as the exogenous variable
X3 = sm.add_constant(data['urban'])
model3 = OLS(Y, X3).fit()

# Creating model4 with all three factors as exogenous variables
X4 = sm.add_constant(data[['hs_grad', 'poverty', 'urban']])
model4 = OLS(Y, X4).fit()

# Output summaries of all new models
model2_summary = model2.summary()
model3_summary = model3.summary()
model4_summary = model4.summary()

model2_summary, model3_summary, model4_summary
"""
                             OLS Regression Results                            
 ==============================================================================
 Dep. Variable:                violent   R-squared:                       0.132
 Model:                            OLS   Adj. R-squared:                  0.114
 Method:                 Least Squares   F-statistic:                     7.422
 Date:                Wed, 01 May 2024   Prob (F-statistic):            0.00891
 Time:                        19:25:42   Log-Likelihood:                -340.48
 No. Observations:                  51   AIC:                             685.0
 Df Residuals:                      49   BIC:                             688.8
 Df Model:                           1                                         
 Covariance Type:            nonrobust                                         
 ==============================================================================
                  coef    std err          t      P>|t|      [0.025      0.975]
 ------------------------------------------------------------------------------
 const         75.4439    126.361      0.597      0.553    -178.488     329.376
 poverty       24.2541      8.903      2.724      0.009       6.363      42.145
 ==============================================================================
 Omnibus:                       30.845   Durbin-Watson:                   1.812
 Prob(Omnibus):                  0.000   Jarque-Bera (JB):               74.375
 Skew:                           1.704   Prob(JB):                     7.07e-17
 Kurtosis:                       7.836   Cond. No.                         65.7
 ==============================================================================
 
 Notes:
 [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
 """,
 <class 'statsmodels.iolib.summary.Summary'>
 """
                             OLS Regression Results                            
 ==============================================================================
 Dep. Variable:                violent   R-squared:                       0.183
 Model:                            OLS   Adj. R-squared:                  0.166
 Method:                 Least Squares   F-statistic:                     10.98
 Date:                Wed, 01 May 2024   Prob (F-statistic):            0.00174
 Time:                        19:25:42   Log-Likelihood:                -338.92
 No. Observations:                  51   AIC:                             681.8
 Df Residuals:                      49   BIC:                             685.7
 Df Model:                           1                                         
 Covariance Type:            nonrobust                                         
 ==============================================================================
                  coef    std err          t      P>|t|      [0.025      0.975]
 ------------------------------------------------------------------------------
 const        151.8880     82.725      1.836      0.072     -14.354     318.130
 urban          4.2788      1.291      3.314      0.002       1.684       6.873
 ==============================================================================
 Omnibus:                       24.274   Durbin-Watson:                   2.049
 Prob(Omnibus):                  0.000   Jarque-Bera (JB):               46.142
 Skew:                           1.418   Prob(JB):                     9.56e-11
 Kurtosis:                       6.697   Cond. No.                         199.
 ==============================================================================
 
 Notes:
 [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
 """,
 <class 'statsmodels.iolib.summary.Summary'>
 """
                             OLS Regression Results                            
 ==============================================================================
 Dep. Variable:                violent   R-squared:                       0.397
 Model:                            OLS   Adj. R-squared:                  0.358
 Method:                 Least Squares   F-statistic:                     10.31
 Date:                Wed, 01 May 2024   Prob (F-statistic):           2.48e-05
 Time:                        19:25:42   Log-Likelihood:                -331.18
 No. Observations:                  51   AIC:                             670.4
 Df Residuals:                      47   BIC:                             678.1
 Df Model:                           3                                         
 Covariance Type:            nonrobust                                         
 ==============================================================================
                  coef    std err          t      P>|t|      [0.025      0.975]
 ------------------------------------------------------------------------------
 const      -1224.7347   1220.551     -1.003      0.321   -3680.167    1230.697
 hs_grad        8.7255     11.860      0.736      0.466     -15.133      32.585
 poverty       38.6569     12.941      2.987      0.004      12.623      64.691
 urban          5.6464      1.315      4.294      0.000       3.001       8.292
 ==============================================================================
 Omnibus:                       16.593   Durbin-Watson:                   2.142
 Prob(Omnibus):                  0.000   Jarque-Bera (JB):               19.926
 Skew:                           1.244   Prob(JB):                     4.71e-05
 Kurtosis:                       4.786   Cond. No.                     5.62e+03
 ==============================================================================

"""
EXERCISE 3

Let's create a single table to show all the resulting coefficients, using the 
summary_col method:

    from statsmodels.iolib.summary2 import summary_col

summary_col has only one positional argument: a list of fitted models to be
shown. Pass a list of all the models we've constructed into this method to
create a table.

Hint: Use the option stars = True to flag all statistically significant 
coefficients.

Hint: You can read more about summary_cols here:
https://tedboy.github.io/statsmodels_doc/generated/statsmodels.iolib.summary2.summary_col.html
"""

from statsmodels.iolib.summary2 import summary_col

# Create a table with all model summaries using summary_col
results_table = summary_col([model1, model2, model3, model4], stars=True)

# Display the results table
results_table
"""

===============================================================
                violent I   violent II violent III violent IIII
---------------------------------------------------------------
R-squared      0.1468       0.1315     0.1831      0.3970      
R-squared Adj. 0.1294       0.1138     0.1664      0.3585      
const          2461.6710*** 75.4439    151.8880*   -1224.7347  
               (706.5164)   (126.3609) (82.7252)   (1220.5510) 
hs_grad        -23.5984***                         8.7255      
               (8.1262)                            (11.8599)   
poverty                     24.2541***             38.6569***  
                            (8.9030)               (12.9412)   
urban                                  4.2788***   5.6464***   
                                       (1.2911)    (1.3151)    
===============================================================
Standard errors in parentheses.
* p<.1, ** p<.05, ***p<.01
"""

"""
EXERCISE 4 (BONUS)

Let's use our fine grained control over the parameters. Change the column
names to something more conventional such as (1), (2) ... and so on. Make it so
that coefficients only round to 2 decimal points.
"""