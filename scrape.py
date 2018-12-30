import billboard


def doSomething(chart):
  [print(c.title + ' - ' + c.artist)  for c in chart.entries]

chart = billboard.ChartData('hot-100')
while chart.previousDate:
    doSomething(chart)

    chart = billboard.ChartData('hot-100', chart.previousDate)

