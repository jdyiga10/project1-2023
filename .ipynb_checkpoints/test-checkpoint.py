import billboard
import pandas as pd
import matplotlib as plt

#If this runs for you and shows the top 50 alternative songs of 2022, then your import and pip install work successfully
#and we should be good to go as far as manipulating the data and extrapolating some interesting conclusions.
chart = billboard.ChartData('hot-100')
print(chart.title)

testchart1 = billboard.ChartData('alternative-songs', year=2022)
print(testchart1)

testchart2 = billboard.ChartData('rap-songs', year=2022)
print(testchart2)

testchart3 = billboard.ChartData('pop-songs', year=2022)
print(testchart3)

#testchart4 = billboard.ChartData('indie-songs', year=2022) INDIE DOES NOT SEEM TO BE A CATEGORY OFFICIALLY
#print(testchart4)

testchart5 = billboard.ChartData('hot-country-songs', year=2022)
print(testchart5)

testchart6 = billboard.ChartData('latin-pop-songs', year=2022)
print(testchart6)