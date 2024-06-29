import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data',color='orange', alpha=0.5)

    # Calculate first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(range(1880, 2051), res.slope * range(1880, 2051) + res.intercept, label='Best Fit 1880-2014')

    # Calculate second line of best fit (since 2000)
    recent_data = df[df['Year'] >= 2000]
    res_recent = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    plt.plot(range(2000, 2051), res_recent.slope * range(2000, 2051) + res_recent.intercept, label='Best Fit 2000-Present')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

