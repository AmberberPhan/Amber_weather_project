import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    return f"{temp}{DEGREE_SYMBOL}"

"""Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
"""


def convert_date(iso_string):
    dt = datetime.fromisoformat(iso_string)
    new_format = dt.strftime("%A %d %B %Y")
    return new_format

"""Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
"""

def convert_f_to_c(temp_in_fahrenheit):
    tem_in_celcius = (float(temp_in_fahrenheit) - 32) * 5 / 9
    rounded_up_ceclcius = round(tem_in_celcius, 1)
    return rounded_up_ceclcius

"""Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
"""


def calculate_mean(weather_data):
    new_weather_list = [float(i) for i in weather_data]
    total_sum = sum(new_weather_list)
    mean_temp = total_sum/len(weather_data)
    return mean_temp

"""Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
"""


def load_data_from_csv(csv_file):
    new_data_list = []

    with open(csv_file) as my_file:
        my_file_reader = csv.reader(my_file)

        next(my_file_reader)  # skip header

        for row in my_file_reader:
            # Skip empty rows
            if not row:
                continue

            # Skip rows where any field is empty
            if row[0] == "" or row[1] == "" or row[2] == "":
                continue

            date = row[0]
            low = int(row[1])
            high = int(row[2])

            new_data_list.append([date, low, high])   # <-- LIST, NOT TUPLE

    return new_data_list

"""Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
"""



def find_min(weather_data):
    # Handle empty list
    if not weather_data:
        return ()

    # Convert all values to float
    new_weather_list = [float(i) for i in weather_data]

    # Find the minimum value
    min_value = min(new_weather_list)

    # Find the last index where min_value appears
    min_position = len(new_weather_list) - 1 - new_weather_list[::-1].index(min_value)

    return min_value, min_position


"""Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
"""


def find_max(weather_data):
    # Handle empty list
    if not weather_data:
        return ()

    # Convert all values to float
    new_weather_list = [float(i) for i in weather_data]

    # Find the maximum value
    max_value = max(new_weather_list)

    # Find the last index where max_value appears
    max_position = len(new_weather_list) - 1 - new_weather_list[::-1].index(max_value)

    return max_value, max_position


"""Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
"""


def generate_summary(weather_data):   
    if not weather_data:
        return ""

    # Start by using the first day's values
    first_date, first_low, first_high = weather_data[0]

    # For tracking min and max
    min_temp_f = first_low
    max_temp_f = first_high
    min_date = first_date
    max_date = first_date

    # For calculating averages
    total_low = 0
    total_high = 0

    # Loop through every row
    for date, low, high in weather_data:
        # Update total for mean
        total_low += low
        total_high += high

        # Check for new min
        if low <= min_temp_f:
            min_temp_f = low
            min_date = date

        # Check for new max
        if high >= max_temp_f:
            max_temp_f = high
            max_date = date

    # Calculate averages
    avg_low_f = total_low / len(weather_data)
    avg_high_f = total_high / len(weather_data)

    # Convert everything to required format
    min_temp = format_temperature(convert_f_to_c(min_temp_f))
    max_temp = format_temperature(convert_f_to_c(max_temp_f))
    avg_low = format_temperature(convert_f_to_c(avg_low_f))
    avg_high = format_temperature(convert_f_to_c(avg_high_f))
    min_date_fmt = convert_date(min_date)
    max_date_fmt = convert_date(max_date)

    # Build summary
    summary = (
        f"{len(weather_data)} Day Overview\n"
        f"  The lowest temperature will be {min_temp}, and will occur on {min_date_fmt}.\n"
        f"  The highest temperature will be {max_temp}, and will occur on {max_date_fmt}.\n"
        f"  The average low this week is {avg_low}.\n"
        f"  The average high this week is {avg_high}.\n"
    )

    return summary


"""Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
"""


def generate_daily_summary(weather_data):
    # If the input list is empty, we return an empty string
    if not weather_data:
        return ""

    # This will store each day's formatted summary
    daily_summary_list = []

    # Loop through each day's data
    # Each row contains: date, low temperature, high temperature
    for date_raw, low_temp_f, high_temp_f in weather_data:

        # Convert the raw ISO date into a readable format
        # Example: "2021-07-02T07:00:00+08:00" -> "Friday 02 July 2021"
        date_formatted = convert_date(date_raw)

        # Convert Fahrenheit temperatures to Celsius
        # Using separate variable names so we don't overwrite Python's min/max functions
        low_temp_c = convert_f_to_c(low_temp_f)
        high_temp_c = convert_f_to_c(high_temp_f)

        # Format the temperatures with degree symbol
        low_temp_str = format_temperature(low_temp_c)
        high_temp_str = format_temperature(high_temp_c)

        # Create the daily summary string for this day
        daily_template = (
            f"---- {date_formatted} ----\n"
            f"  Minimum Temperature: {low_temp_str}\n"
            f"  Maximum Temperature: {high_temp_str}\n"
        )

        # Add this day's summary to the list of all summaries
        daily_summary_list.append(daily_template)

    # Join all daily summaries into a single string
    # The "\n" ensures each day's summary is separated by a blank line
    full_daily_summary = "\n".join(daily_summary_list) + "\n"

    return full_daily_summary

    
"""Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
"""

