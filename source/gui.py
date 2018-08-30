import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
import geturl
import get_forecast_object
import plot_forecast
import datetime

import logging

format = '%(asctime)-15s %(filename)s %(funcName)s %(message)s'
logging.basicConfig(filename='guilog.log', level=logging.DEBUG, format=format)


class GUI(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        self.forecast = tk.IntVar()
        self.event = tk.StringVar()
        self.year = tk.IntVar()
        self.month = tk.IntVar()
        self.day = tk.IntVar()
        self.time = tk.StringVar()

        self.year.set(datetime.date.today().year)
        self.month.set(datetime.date.today().month)
        self.day.set(datetime.date.today().day)

        self.grid()

        self.createForecastWidget()
        self.createForecastTimeWidget()
        self.createForecastTypeWidget()
        self.createWidgets()
        self.createLabels()


    def createLabels(self):
        self.dateLabel = tk.Label(self, text='Date: ')
        self.dayLabel = tk.Label(self, text='Day: ')
        self.timeLabel = tk.Label(self, text='Outlook Time: ')
        self.forecastLabel = tk.Label(self, text='Event: ')

        self.dateLabel.grid(row=0, column=0)
        self.dayLabel.grid(row=1, column=0)
        self.timeLabel.grid(row=3, column=0)
        self.forecastLabel.grid(row=8, column=0)


    def createWidgets(self):
        self.yearMenu = tk.OptionMenu(self, self.year, *list(range(2015, 2019)))
        self.monthMenu = tk.OptionMenu(self, self.month, *list(range(1, 13)))
        self.dayMenu = tk.OptionMenu(self, self.day, *list(range(1, 32)))

        self.yearMenu.grid(row=0, column=1, columnspan=2)
        self.monthMenu.grid(row=0, column=3)
        self.dayMenu.grid(row=0, column=4)

        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.submitButton = tk.Button(self, text='Submit', command=self.plot)

        self.submitButton.grid(columnspan=6)
        self.quitButton.grid(columnspan=6)

    def createForecastWidget(self):
        self.dayOne = tk.Radiobutton(self, text='Day 1', variable=self.forecast, command=self.day1button, value=1)
        self.dayTwo = tk.Radiobutton(self, text='Day 2', variable=self.forecast, command=self.day2button, value=2)
        self.dayThree = tk.Radiobutton(self, text='Day 3', variable=self.forecast, command=self.day3button, value=3)
        self.dayFourEight = tk.Radiobutton(self, text='Days 4-8', variable=self.forecast, command=self.days48button, value=48)

        self.dayOne.grid(row=1, column=1)
        self.dayTwo.grid(row=1, column=2)
        self.dayThree.grid(row=1, column=3)
        self.dayFourEight.grid(row=1, column=4, columnspan=2)

    def createForecastTimeWidget(self):
        self.day1outlook1 = tk.Radiobutton(self, text='0100', variable=self.time, value='0100')
        self.day1outlook2 = tk.Radiobutton(self, text='1200', variable=self.time, value='1200')
        self.day1outlook3 = tk.Radiobutton(self, text='1300', variable=self.time, value='1300')
        self.day1outlook4 = tk.Radiobutton(self, text='1630', variable=self.time, value='1630')
        self.day1outlook5 = tk.Radiobutton(self, text='2000', variable=self.time, value='2000')
        self.day2outlook1 = tk.Radiobutton(self, text='0600', variable=self.time, value='0600')
        self.day2outlook2 = tk.Radiobutton(self, text='1730', variable=self.time, value='1730')
        self.day3outlook1 = tk.Radiobutton(self, text='0730', variable=self.time, value='0730')

        self.day1outlook1.grid(row=3, column=1)
        self.day1outlook2.grid(row=4, column=1)
        self.day1outlook3.grid(row=5, column=1)
        self.day1outlook4.grid(row=6, column=1)
        self.day1outlook5.grid(row=7, column=1)
        self.day2outlook1.grid(row=3, column=2)
        self.day2outlook2.grid(row=4, column=2)
        self.day3outlook1.grid(row=3, column=3)

    def createForecastTypeWidget(self):
        self.categoricalButton = tk.Radiobutton(self, text='Categorical', variable=self.event, value='categorical')
        self.tornButton = tk.Radiobutton(self, text='Tornado', variable=self.event, value='tornado')
        self.hailButton = tk.Radiobutton(self, text='Hail', variable=self.event, value='hail')
        self.windButton = tk.Radiobutton(self, text='Wind', variable=self.event, value='wind')
        self.severeButton = tk.Radiobutton(self, text='Severe', variable=self.event, value='severe')

        self.categoricalButton.grid(row=8, column=1)
        self.tornButton.grid(row=8, column=2)
        self.hailButton.grid(row=8, column=3)
        self.windButton.grid(row=8, column=4)
        self.severeButton.grid(row=8, column=5)


    def day1button(self):
        self.categoricalButton.configure(state=tk.NORMAL)
        self.tornButton.configure(state=tk.NORMAL)
        self.windButton.configure(state=tk.NORMAL)
        self.hailButton.configure(state=tk.NORMAL)
        self.severeButton.configure(state=tk.DISABLED)
        self.day1outlook1.configure(state=tk.NORMAL)
        self.day1outlook2.configure(state=tk.NORMAL)
        self.day1outlook3.configure(state=tk.NORMAL)
        self.day1outlook4.configure(state=tk.NORMAL)
        self.day1outlook5.configure(state=tk.NORMAL)
        self.day2outlook1.configure(state=tk.DISABLED)
        self.day2outlook2.configure(state=tk.DISABLED)
        self.day3outlook1.configure(state=tk.DISABLED)

        self.categoricalButton.select()
        self.day1outlook1.select()

    def day2button(self):
        self.categoricalButton.configure(state=tk.NORMAL)
        self.tornButton.configure(state=tk.DISABLED)
        self.windButton.configure(state=tk.DISABLED)
        self.hailButton.configure(state=tk.DISABLED)
        self.severeButton.configure(state=tk.NORMAL)
        self.day1outlook1.configure(state=tk.DISABLED)
        self.day1outlook2.configure(state=tk.DISABLED)
        self.day1outlook3.configure(state=tk.DISABLED)
        self.day1outlook4.configure(state=tk.DISABLED)
        self.day1outlook5.configure(state=tk.DISABLED)
        self.day2outlook1.configure(state=tk.NORMAL)
        self.day2outlook2.configure(state=tk.NORMAL)
        self.day3outlook1.configure(state=tk.DISABLED)

        self.categoricalButton.select()
        self.day2outlook1.select()

    def day3button(self):
        self.categoricalButton.configure(state=tk.NORMAL)
        self.tornButton.configure(state=tk.DISABLED)
        self.windButton.configure(state=tk.DISABLED)
        self.hailButton.configure(state=tk.DISABLED)
        self.severeButton.configure(state=tk.NORMAL)
        self.day1outlook1.configure(state=tk.DISABLED)
        self.day1outlook2.configure(state=tk.DISABLED)
        self.day1outlook3.configure(state=tk.DISABLED)
        self.day1outlook4.configure(state=tk.DISABLED)
        self.day1outlook5.configure(state=tk.DISABLED)
        self.day2outlook1.configure(state=tk.DISABLED)
        self.day2outlook2.configure(state=tk.DISABLED)
        self.day3outlook1.configure(state=tk.NORMAL)

        self.categoricalButton.select()
        self.day3outlook1.select()

    def days48button(self):
        self.categoricalButton.configure(state=tk.DISABLED)
        self.tornButton.configure(state=tk.DISABLED)
        self.windButton.configure(state=tk.DISABLED)
        self.hailButton.configure(state=tk.DISABLED)
        self.severeButton.configure(state=tk.NORMAL)
        self.day1outlook1.configure(state=tk.DISABLED)
        self.day1outlook2.configure(state=tk.DISABLED)
        self.day1outlook3.configure(state=tk.DISABLED)
        self.day1outlook4.configure(state=tk.DISABLED)
        self.day1outlook5.configure(state=tk.DISABLED)
        self.day2outlook1.configure(state=tk.DISABLED)
        self.day2outlook2.configure(state=tk.DISABLED)
        self.day3outlook1.configure(state=tk.DISABLED)

        self.severeButton.select()
        self.day3outlook1.select()
        self.day3outlook1.deselect()


    def plot(self):
        date = datetime.date(self.year.get(), self.month.get(), self.day.get())
        url = geturl.lookup_url(date, self.forecast.get(), self.time.get())
        forecast = self.forecast.get()
        event = self.event.get()
        forecast_object = get_forecast_object.main(forecast, url)
        plot_forecast.main(forecast_object, event)



app = GUI()
app.master.title('SPC Convective Outlook GUI')
app.mainloop()
