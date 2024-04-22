"""
Imagine that you are running a bookstrore. Below is a list of dictionaries
that contains the title, author, genre, quantity sold in the last year, and the
price sold. You will use this data to create a dataframe, then perform various
analysis to decide what to restock etc.

Reminder: Import pandas before you start!
"""

books_data = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Classic", "quantity_sold": 30, "price": 8.99},
    {"title": "1984", "author": "George Orwell", "genre": "Dystopian", "quantity_sold": 42, "price": 9.99},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Classic", "quantity_sold": 25, "price": 7.99},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "genre": "Classic", "quantity_sold": 34, "price": 8.49},
    {"title": "Brave New World", "author": "Aldous Huxley", "genre": "Dystopian", "quantity_sold": 18, "price": 9.49}
]

"""
EXCERCISE 1

Use the data provided to create a dataframe. This is not the only dataframe that
you will be creating so call it df_books.
"""
import pandas as pd

# Data provided
books_data = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Classic", "quantity_sold": 30, "price": 8.99},
    {"title": "1984", "author": "George Orwell", "genre": "Dystopian", "quantity_sold": 42, "price": 9.99},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Classic", "quantity_sold": 25, "price": 7.99},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "genre": "Classic", "quantity_sold": 34, "price": 8.49},
    {"title": "Brave New World", "author": "Aldous Huxley", "genre": "Dystopian", "quantity_sold": 18, "price": 9.49}
]

# Creating a dataframe
df_books = pd.DataFrame(books_data)
df_books
                    title               author      genre  quantity_sold  price
0   To Kill a Mockingbird           Harper Lee    Classic             30   8.99
1                    1984        George Orwell  Dystopian             42   9.99
2        The Great Gatsby  F. Scott Fitzgerald    Classic             25   7.99
3  The Catcher in the Rye        J.D. Salinger    Classic             34   8.49
4         Brave New World        Aldous Huxley  Dystopian             18   9.49
"""
EXCERCISE 2

We want to create a subset of this data that contains infromation that we can
share with the public e.g. it excludes variables such as quantity sold. 
We want this part of the code to be as flexible as possible so...
 
1. Create a list named "excluded_variables" - it contains only "quantity_sold"
2. Create a dataset named df_public that excludes all variable names in quantity_sold

It is not necessary that df_public be a copy of this list.

Hint: Suppose x is a string and y is a list of strings. Recall that the condition

if x not in y:

will be True if string x is not list y
"""
# Create a list named "excluded_variables" containing "quantity_sold"
excluded_variables = ["quantity_sold"]
excluded_variables
# Create a dataset named df_public that excludes the variables in the excluded_variables list
df_public = df_books.drop(columns=excluded_variables)
df_public
                    title               author      genre  price
0   To Kill a Mockingbird           Harper Lee    Classic   8.99
1                    1984        George Orwell  Dystopian   9.99
2        The Great Gatsby  F. Scott Fitzgerald    Classic   7.99
3  The Catcher in the Rye        J.D. Salinger    Classic   8.49
4         Brave New World        Aldous Huxley  Dystopian   9.49
"""
EXCERCISE 3

Create a new column called revenue that is the product of the quantity and
price. 

Hint: Creating a new series is easy! Let df be the name of your dataframe.
The 'x' and 'y' be the names of two columns that contain integers. 
Then the sum of those can be generated in a series named 'sum' using 

df['sum'] = df['x'] + df['y']
"""
# Create a new column called 'revenue' that is the product of quantity_sold and price
df_books['revenue'] = df_books['quantity_sold'] * df_books['price']
df_books
                    title               author  ... price  revenue
0   To Kill a Mockingbird           Harper Lee  ...  8.99   269.70
1                    1984        George Orwell  ...  9.99   419.58
2        The Great Gatsby  F. Scott Fitzgerald  ...  7.99   199.75
3  The Catcher in the Rye        J.D. Salinger  ...  8.49   288.66
4         Brave New World        Aldous Huxley  ...  9.49   170.82
"""
EXCERCISE 4

Find the three most lucrative titles sold and copy those titles and that
list into a new dataframe called df_bestsellers. 

To do so, you can try to figure it out on your own or follow the instructions
below...

1. Sort the dataframe by revenue. Makes sure that the it is in descending order.
Store this in a new dataset called df_books_sorted. Print this to take a look at it

Hint: Each dataframe has a method named sort_values(). So if wanted to sort
the books by cheapest first:

df_books_sorted = df_books.sort_values(by="price", ascending=True)
# Sort the dataframe by revenue in descending order
df_books_sorted = df_books.sort_values(by="revenue", ascending=False)
df_books_sorted
                    title               author  ... price  revenue
1                    1984        George Orwell  ...  9.99   419.58
3  The Catcher in the Rye        J.D. Salinger  ...  8.49   288.66
0   To Kill a Mockingbird           Harper Lee  ...  8.99   269.70
2        The Great Gatsby  F. Scott Fitzgerald  ...  7.99   199.75
4         Brave New World        Aldous Huxley  ...  9.49   170.82

2. Note that this does NOT change the index numbers! To do that, create a list
of integers and renumber use it to renumber df_books_sorted using df.index = [list_name]

Hint: [x for x in range(3)] generates [0, 1, 2]
# Reset the index of df_books_sorted
df_books_sorted.index = [x for x in range(len(df_books_sorted))]
df_books_sorted
                    title               author  ... price  revenue
0                    1984        George Orwell  ...  9.99   419.58
1  The Catcher in the Rye        J.D. Salinger  ...  8.49   288.66
2   To Kill a Mockingbird           Harper Lee  ...  8.99   269.70
3        The Great Gatsby  F. Scott Fitzgerald  ...  7.99   199.75
4         Brave New World        Aldous Huxley  ...  9.49   170.82


3. Create a new dataframe named df_bestsellers using loc that contains 
only the top 3 rows and the columns named title and revenue. Use .copy() to ensure
that this is copy, not a view of the original df_books
# Create a new dataframe df_bestsellers that contains only the top 3 rows and the columns 'title' and 'revenue'
df_bestsellers = df_books_sorted.loc[:2, ['title', 'revenue']].copy()
df_bestsellers
                    title  revenue
0                    1984   419.58
1  The Catcher in the Rye   288.66
2   To Kill a Mockingbird   269.70
"""