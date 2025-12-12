# Import all the functions we need
from weather import (
    format_temperature,
    convert_date,
    convert_f_to_c,
    calculate_mean,
    load_data_from_csv,
    find_min,
    find_max,
    generate_summary,
    generate_daily_summary
)

# Format temperature
temp_output = format_temperature(150)  # Pass a number
print("Formatted temperature:", temp_output)

# Convert a date
date_iso = "2021-07-02T07:00:00+08:00"
date_output = convert_date(date_iso)
print("Converted date:", date_output)

# Convert Fahrenheit to Celsius
fahrenheit_temp = 100
celsius_output = convert_f_to_c(fahrenheit_temp)
print(f"{fahrenheit_temp}°F in Celsius is:", celsius_output)

# Calculate mean of a list
temperatures = [50, 60, 70, 80]
mean_output = calculate_mean(temperatures)
print("Mean temperature:", mean_output)

# Load data from a CSV
csv_file = "tests/data/example_one.csv"
weather_data = load_data_from_csv(csv_file)
print("Loaded weather data:", weather_data)

# Find min and max
low_temps = [day[1] for day in weather_data]  # Extract all low temps
high_temps = [day[2] for day in weather_data] # Extract all high temps

min_value, min_index = find_min(low_temps)
max_value, max_index = find_max(high_temps)
print("Min:", (min_value, min_index))
print("Max:", (max_value, max_index))

# Generate weekly summary
summary = generate_summary(weather_data)
print("\nWeekly Summary:\n", summary)

# Generate daily summary
daily_summary = generate_daily_summary(weather_data)
print("\nDaily Summary:\n", daily_summary)