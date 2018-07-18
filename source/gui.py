import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
import plot_categorical

class GUI(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.forecast = tk.IntVar()
		self.grid()
		self.createForecastWidget()
		self.createForecastTypeWidget()
		self.createWidgets()

	def createWidgets(self):
		self.quitButton = tk.Button(self, text='Quit', command=self.quit)
		self.submitButton = tk.Button(self, text='Submit', command=lambda day=self.forecast: plot_categorical.main(day.get()))
#		self.submitButton = tk.Button(self, text='Submit', command=lambda day=self.forecast: print(day.get()))
		self.quitButton.grid()
		self.submitButton.grid()

	def createForecastWidget(self):
		self.dayOne = tk.Radiobutton(self, text='Day 1', variable=self.forecast, value=1)
		self.dayTwo = tk.Radiobutton(self, text='Day 2', variable=self.forecast, value=2)
		self.dayThree = tk.Radiobutton(self, text='Day 3', variable=self.forecast, value=3)
		self.dayFourEight = tk.Radiobutton(self, text='Days 4-8', variable=self.forecast, value=48)

		self.dayOne.grid(row=1, column=0)
		self.dayTwo.grid(row=1, column=1)
		self.dayThree.grid(row=1, column=2)
		self.dayFourEight.grid(row=1, column=3)

	def createForecastTypeWidget(self):
		self.forecastList = ['categorical', 'severe', 'tornado', 'hail', 'wind']
		self.forecastType = tk.Listbox(self)
		for item in self.forecastList:
			self.forecastType.insert(tk.END, item)
		self.forecastType.grid(row=2, column=0, columnspan=4)


#	tk.radioButton
#


app = GUI()
app.master.title('Sample App')
app.mainloop()
