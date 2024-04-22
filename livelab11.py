import pandas as pd
import matplotlib.pyplot as plt

"""
Today we will be graphing weather data for a fictional city using 
weather_data.csv. It contains the following variables:

Date: The date for each recorded weather observation. Formatted as YYYY-MM-DD.
Max Temperature: The maximum temperature recorded on a given day, measured in 
    degrees Celsius
Min Temperature: The minimum temperature recorded on a given day, measured in 
    degrees Celsius
Precipitation: The amount of precipitation recorded on a given day, measured 
    in millimeters
Wind Speed: The average wind speed recorded on a given day, measured in 
    kilometers per hour
Humidity: The average humidity percentage recorded on a given day

The data covers the period of a single year.
"""

"""
EXERCISE 1

Open the weather data, and convert the dates into a date time object. Plot the
Maximum temperature and the minimum temperature in a single plot. Give them 
different colors and linestyles.

Remember to...
- Label the lines and create a legend
- Add a title
- Label the x-axis and y-axis
- Create a title

Save the figure as 'temperature.png' with high resolution 
"""
import pandas as pd
import matplotlib.pyplot as plt

# Load the weather data
file_path = '/Users/feitianyang/Documents/GitHub/datasci-harris-tfeiaaa/weather_data.csv'
weather_data = pd.read_csv(file_path)

# Convert the 'Date' column to datetime
weather_data['Date'] = pd.to_datetime(weather_data['Date'])

# Plotting Max Temperature and Min Temperature
plt.figure(figsize=(10, 6))
plt.plot(weather_data['Date'], weather_data['Max Temperature'], label='Max Temperature (°C)', color='red', linestyle='-')
plt.plot(weather_data['Date'], weather_data['Min Temperature'], label='Min Temperature (°C)', color='blue', linestyle='--')

# Adding labels, title, and legend
plt.title('Daily Maximum and Minimum Temperatures')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend()

# Saving the figure with high resolution
plt.savefig('/Users/feitianyang/Documents/GitHub/datasci-harris-tfeiaaa/temperature.png', dpi=300)

# Show the plot
plt.show()


"""
EXERCISE 2

Create a fig object with three axes, one below the other.

On the first, plot the precipitation; on the second, plot the wind speed; and 
on the third, plot the humidity.. Ensure that all three have different colors, though
you can use the same solid lines.

For each, remember to add a title and labels for the x-axis and y-axis.

Save the entire graph as weather.png

Hint: the matplotlib method tight_layout() can be used to prevent overlap 
"""
# Creating a fig object with three axes
fig, axes = plt.subplots(3, 1, figsize=(10, 12))

# Plotting precipitation on the first axis
axes[0].plot(weather_data['Date'], weather_data['Precipitation'], color='navy', linestyle='-', linewidth=1)
axes[0].set_title('Daily Precipitation')
axes[0].set_xlabel('Date')
axes[0].set_ylabel('Precipitation (mm)')

# Plotting wind speed on the second axis
axes[1].plot(weather_data['Date'], weather_data['Wind Speed'], color='forestgreen', linestyle='-', linewidth=1)
axes[1].set_title('Daily Wind Speed')
axes[1].set_xlabel('Date')
axes[1].set_ylabel('Wind Speed (km/h)')

# Plotting humidity on the third axis
axes[2].plot(weather_data['Date'], weather_data['Humidity'], color='purple', linestyle='-', linewidth=1)
axes[2].set_title('Daily Humidity')
axes[2].set_xlabel('Date')
axes[2].set_ylabel('Humidity (%)')

# Adjusting layout to prevent overlap
plt.tight_layout()

# Saving the entire graph as weather.png
plt.savefig('/Users/feitianyang/Documents/GitHub/datasci-harris-tfeiaaa/weather.png', dpi=300)

# Show the plot
plt.show()


