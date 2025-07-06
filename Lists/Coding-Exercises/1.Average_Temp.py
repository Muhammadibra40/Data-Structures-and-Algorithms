num_of_days = int(input("How many day's temperature: "))

# Calculate Average Temperature
temps = []
for i in range((num_of_days)):
    temps.append(float(input(f"Day {i + 1}'s high temp: ")))

avg_temp = round(sum(temps)/ num_of_days, 2)
days_above_count = 0


# Get the days above the average temperature
for i in range(num_of_days):
    if temps[i] > avg_temp:
        days_above_count += 1

print(f"Average = {avg_temp}")
print(f"{days_above_count} day(s) above average")