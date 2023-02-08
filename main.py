import csv
import pandas

"""
with open("./weather_data.csv") as data:
    raw = csv.reader(data)
    temperature = []
    for row in raw:
        temperature.append(row[1])
    temperature = temperature[1:]

    for i in range(len(temperature)):
        temperature[i] = int(temperature[i])
    print(temperature)
"""

data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
#
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp_F = monday.temp * 9 / 5 + 32
print(monday_temp_F)
