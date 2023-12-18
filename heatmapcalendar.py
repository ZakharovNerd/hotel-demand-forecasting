import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def create_calendar_array(days_of_month, values):
    """
    Transforms a list of values and their corresponding days into a 5x7 calendar array.
    
    :param days_of_month: List of day numbers.
    :param values: List of values for each day.
    :return: 5x7 numpy array representing the calendar.
    """
    calendar_array = np.full((5, 7), np.nan)  # Initialize with NaNs

    for day, value in zip(days_of_month, values):
        week, day_of_week = divmod(day - 1, 7)
        calendar_array[week, day_of_week] = value

    return calendar_array

def plot_calendar_heatmap(calendar_array, days_of_month):
    """
    Plots a calendar heatmap from the calendar array.
    
    :param calendar_array: 5x7 numpy array representing the calendar.
    :param days_of_month: List of day numbers.
    """
    fig, ax = plt.subplots(figsize=(12, 7))
    cmap = plt.get_cmap('coolwarm')
    min_val, max_val = np.nanmin(calendar_array), np.nanmax(calendar_array)

    for week in range(5):
        for day in range(7):
            day_val = calendar_array[week, day]
            if not np.isnan(day_val):
                color = cmap((day_val - min_val) / (max_val - min_val))
                rect = Rectangle([day, week], 1, 1, color=color)
                ax.add_patch(rect)
                ax.text(day + 0.5, week + 0.3, f"{day_val:.1f}", ha='center', va='center', fontsize=12, color='white')
                ax.text(day + 0.5, week + 0.5, str(days_of_month[week * 7 + day]), ha='right', va='bottom', fontsize=6, color='black')

    ax.set_xlim(0, 7)
    ax.set_ylim(0, 5)
    ax.axis('off')

    sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=min_val, vmax=max_val))
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax, orientation='horizontal', shrink=0.5, pad=0.02)
    cbar.ax.set_xlabel('Sales Value')
    plt.gca().invert_yaxis()
    plt.show()

    return fig, ax

def create_calendar_heatmap(values, days_of_month):
    """
    Creates a calendar heatmap for a list of values corresponding to days of a month.

    :param values: List of values for each day.
    :param days_of_month: List of day numbers corresponding to the values.
    """
    calendar_array = create_calendar_array(days_of_month, values)
    fig, ax = plot_calendar_heatmap(calendar_array, days_of_month)
    return fig, ax