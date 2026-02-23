# Name: Yuvaraj
# Roll number: iitp_aimltn_2602801
# Assignment: Python Loops & Automation - Subjective Question

print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]

highest_temp = temperatures[0]
lowest_temp = temperatures[0]

for temp in temperatures:
    if temp > highest_temp:
        highest_temp = temp
    if temp < lowest_temp:
        lowest_temp = temp

print(f"Highest temperature: {highest_temp}")
print(f"Lowest temperature: {lowest_temp}")


print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
hot_days_count = 0
for temp in temperatures:
    if temp <= 30:
        continue
    if temp > 30:
        hot_days_count += 1
print(f"Number of hot days (temperature > 30°C): {hot_days_count}")    


print("\n===== Task 3: Alert System =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]
hot_days_before_alert = 0

for day, temp in enumerate(temperatures, start=1):
     if temp >= 40:
        alert_message = f"Alert! Extreme temperature {temp}°C detected on Day {day}"
        break
     elif temp > 30:
        hot_days_before_alert += 1

print(f"Hot days before alert: {hot_days_before_alert}")

if alert_message:
    print(alert_message)
