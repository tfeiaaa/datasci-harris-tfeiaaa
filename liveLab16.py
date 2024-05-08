"""
EXERCISE 1

Consider the following list of best-selling music artists, with a focus
on artist who have sold more than 250 million records:
    
    https://en.wikipedia.org/wiki/List_of_best-selling_music_artists
    
Are we allowed to scrape the data from this page with a program? What should 
we check?
"""
Wikipedia's Terms of Use and Licensing: Wikipedia content is typically licensed under the Creative Commons Attribution-ShareAlike license. This allows you to use, share, and even adapt the content as long as you attribute it properly and share any adapted content under the same terms. For scraping, this generally means it's allowed as long as you follow these licensing requirements.
Robot.txt File: Websites use this file to indicate which parts of the site can be accessed by automated tools like web scrapers. You should check Wikipedia's robots.txt file to see if it disallows scraping for the part of the site you're interested in. Generally, Wikipedia allows scraping as long as it’s done responsibly—that is, without causing excessive load on their servers.
API Use: Instead of scraping, consider using Wikipedia's API, which is designed to allow programmatic access to the content in a more controlled and server-friendly manner. The API also ensures that you receive the data in a structured format, making it easier to handle.
Ethical Considerations: Ensure your scraping activities are ethical, not overly burdensome on Wikipedia's servers, and compliant with any data privacy regulations that might apply.
In summary, while scraping Wikipedia is generally allowed, using their API is often a better, more responsible approach.

Check the Terms of Service: Always review the terms of service or similar legal agreements on the website. Wikipedia generally allows the use of its content under a free license (the Creative Commons Attribution-ShareAlike License), which typically permits scraping for non-commercial and educational purposes, provided you attribute the source and share any adaptations under the same license.
Respect the Robots.txt File: This file on websites specifies what parts of the site can or cannot be scraped by web crawlers. Wikipedia’s robots.txt allows scraping most of its content, but it’s good practice to check this file to ensure compliance.
Server Load Consideration: Avoid putting excessive load on Wikipedia's servers. This means running your scraping program during off-peak hours, limiting the rate of your requests, and ideally, caching results to minimize repeat requests.
Data Use and Redistribution: If you plan to redistribute the scraped data, make sure to do so in accordance with Wikipedia's licensing terms, which will usually require you to distribute your work under the same or a compatible license.
Local Laws and Regulations: Consider the legal implications under your local laws regarding data privacy and digital rights.
For scraping from Wikipedia, if your usage adheres to these guidelines, it should be permissible. Always ensure that your specific use case aligns with these recommendations.



"""
EXERCISE 2

Having verified this, download the page in Python; put it into a soup object
"""
import requests
from bs4 import BeautifulSoup

# URL of the page to be scraped
url = 'https://en.wikipedia.org/wiki/List_of_best-selling_music_artists'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the content of the request with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    print("Page has been successfully downloaded and parsed.")
else:
    print("Failed to retrieve the page. Status code:", response.status_code)


"""
EXERCISE 3

Short: Create a csv file with the table of artists who have sold 250 million 
records or more

Long:
A Find all the tables in this page. How many are there?
B. Create a object with just the first table; does it have the set of artists
who have sold more than 250M records?
C. Extract a object with all the rows in this table.
D. Convert the rows into elements of a list
E. Create a dataframe and export  it as a CSV file
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the page to be scraped
url = 'https://en.wikipedia.org/wiki/List_of_best-selling_music_artists'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    tables = soup.find_all('table')
    print("Total tables found:", len(tables))

    # Assuming the first table is the one we need
    first_table = tables[0]
    rows = first_table.find_all('tr')

    # Extracting data into a list
    data = []
    for row in rows:
        cols = row.find_all('td')
        if cols:
            data.append([col.text.strip() for col in cols])

    # Creating a DataFrame
    if data:
        df = pd.DataFrame(data, columns=["Artist", "Country", "Period active", "Sales range"])
        print(df.head())

        # Exporting to CSV
        csv_path = "Artists_250M_Records.csv"
        df.to_csv(csv_path, index=False)
        print("CSV file created at:", csv_path)
    else:
        print("No data extracted.")
else:
    print("Failed to retrieve the page. Status code:", response.status_code)




