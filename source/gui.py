import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
import plot_categorical, plot_torn, plot_hail, plot_wind, plot_severe, plot_days48

day1plots = {
    'categorical': plot_categorical,
    'tornado': plot_torn,
    'hail': plot_hail,
    'wind': plot_wind
}

day2plots = {
    'categorical': plot_categorical,
    'severe': plot_severe
}

day48plots = {
    'severe': plot_days48
}


class GUI(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.forecast = tk.IntVar()
        self.event = tk.StringVar()
        self.grid()
        self.createForecastWidget()
        self.createForecastTypeWidget()
        self.createWidgets()
        self.createLabels()

    def createLabels(self):
        self.dayLabel = tk.Label(self, text='Day: ')
        self.forecastLabel = tk.Label(self, text='Event: ')
        self.dayLabel.grid(row=1, column=0)
        self.forecastLabel.grid(row=2, column=0)

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.submitButton = tk.Button(self, text='Submit', command=self.plot)
        self.submitButton.grid(columnspan=6)
        self.quitButton.grid(columnspan=6)

    def createForecastWidget(self):
        self.dayOne = tk.Radiobutton(self, text='Day 1', variable=self.forecast, command=self.day1button, value=1)
        self.dayTwo = tk.Radiobutton(self, text='Day 2', variable=self.forecast, command=self.days23button, value=2)
        self.dayThree = tk.Radiobutton(self, text='Day 3', variable=self.forecast, command=self.days23button, value=3)
        self.dayFourEight = tk.Radiobutton(self, text='Days 4-8', variable=self.forecast, command=self.days48button, value=48)

        self.dayOne.grid(row=1, column=1)
        self.dayTwo.grid(row=1, column=2)
        self.dayThree.grid(row=1, column=3)
        self.dayFourEight.grid(row=1, column=4, columnspan=2)

    def createForecastTypeWidget(self):
        self.categoricalButton = tk.Radiobutton(self, text='Categorical', variable=self.event, value='categorical')
        self.tornButton = tk.Radiobutton(self, text='Tornado', variable=self.event, value='tornado')
        self.hailButton = tk.Radiobutton(self, text='Hail', variable=self.event, value='hail')
        self.windButton = tk.Radiobutton(self, text='Wind', variable=self.event, value='wind')
        self.severeButton = tk.Radiobutton(self, text='Severe', variable=self.event, value='severe')

        self.categoricalButton.grid(row=2, column=1)
        self.tornButton.grid(row=2, column=2)
        self.hailButton.grid(row=2, column=3)
        self.windButton.grid(row=2, column=4)
        self.severeButton.grid(row=2, column=5)

    def plot(self):
        forecast = self.forecast.get()
        event = self.event.get()

        if forecast == 1:
            if event in day1plots.keys():
                day1plots[event].main(forecast)
        elif forecast == 2 or forecast == 3:
            if event in day2plots.keys():
                day2plots[event].main(forecast)
        else:
            day48plots[event].main(forecast)

    def day1button(self):
        self.categoricalButton.configure(state=tk.NORMAL)
        self.tornButton.configure(state=tk.NORMAL)
        self.windButton.configure(state=tk.NORMAL)
        self.hailButton.configure(state=tk.NORMAL)
        self.severeButton.configure(state=tk.DISABLED)
        self.categoricalButton.select()

    def days23button(self):
        self.categoricalButton.configure(state=tk.NORMAL)
        self.tornButton.configure(state=tk.DISABLED)
        self.windButton.configure(state=tk.DISABLED)
        self.hailButton.configure(state=tk.DISABLED)
        self.severeButton.configure(state=tk.NORMAL)
        self.categoricalButton.select()

    def days48button(self):
        self.categoricalButton.configure(state=tk.DISABLED)
        self.tornButton.configure(state=tk.DISABLED)
        self.windButton.configure(state=tk.DISABLED)
        self.hailButton.configure(state=tk.DISABLED)
        self.severeButton.configure(state=tk.NORMAL)
        self.severeButton.select()


app = GUI()
app.master.title('SPC Convective Outlook GUI')
app.mainloop()
