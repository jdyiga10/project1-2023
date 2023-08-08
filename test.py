import billboard

#If this runs for you and shows the top 50 alternative songs of 2022, then your import and pip install work successfully
#and we should be good to go as far as manipulating the data and extrapolating some interesting conclusions.
chart = billboard.ChartData('hot-100')
print(chart.title)

testchart = billboard.ChartData('alternative-songs', year=2022)
print(testchart)