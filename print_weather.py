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
temp_output = format_temperature(150)
print("Formatted temperature:", temp_output)

# Convert a date
date_iso = "2021-07-02T07:00:00+08:00"
date_output = convert_date(date_iso)
print("Converted date:", date_output)

# Convert f to c
fahrenheit_temp = 100
celsius_output = convert_f_to_c(fahrenheit_temp)
print(f"{fahrenheit_temp}°F in Celsius is:", celsius_output)

# Calculate mean
temperatures = [49, 57, 56, 55, 53]
mean_output = calculate_mean(temperatures)
print("Mean temperature:", mean_output)

# Load data from a csv
csv_file = "tests/data/example_one.csv"
weather_data = load_data_from_csv(csv_file)
print("Loaded weather data:", weather_data)

# Find min
low_temps = [i[1] for i in weather_data]  
min_value, min_index = find_min(low_temps)
print("Min:", (min_value, min_index))

# Find max
high_temps = [i[2] for i in weather_data]
max_value, max_index = find_max(high_temps)
print("Max:", (max_value, max_index))

# Generate summary
summary = generate_summary(weather_data)
print("\nWeekly Summary:\n", summary)

# Generate daily summary
daily_summary = generate_daily_summary(weather_data)
print("\nDaily Summary:\n", daily_summary)