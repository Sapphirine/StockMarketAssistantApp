import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import matplotlib.dates as mdates
import datetime as dt


import tkinter as tk
from tkinter import ttk
from tkinter import StringVar

import numpy as np

from matplotlib import pyplot as plt

from PIL import Image, ImageTk



LARGE_FONT = ('Verdana', 12)
NORM_FONT = ('Verdana', 10)
SMALL_FONT = ('Verdana', 8)

style.use('ggplot')

f = plt.figure()
ax1 = plt.subplot2grid((5,4),(0,0),rowspan=4,colspan=4)
#ax2 = plt.subplot2grid((5,4),(4,0),sharex=ax1,rowspan=1,colspan=4)
#a = f.add_subplot(111)

exchange = 'BTC-e'
DatCounter = 9000
programName = 'btce'

resampleSize = "15Min"
DataPace = "1d"
candleWidth = 0.008

StockName = 'AAPL'


def changeStocks(stock):
    global StockName
    StockName = stock
    
    






def popupmsg(msg):
    popup = tk.Tk()
    
    popup.wm_title('!')
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side='top',fill='x',pady=10)
    B1 = ttk.Button(popup, text='Okay', command=popup.destroy)
    B1.pack()
    popup.mainloop()

def animate(i):
    pullData = open(StockName+'.txt','r').read()
    dataList = pullData.split('\n')
    dateList = []
    closepList = []
    highpList = []
    lowpList = []
    openpList = []
    volumeList = []
    
    for eachLine in dataList:
        if len(eachLine) > 1:
            date, closep, highp, lowp, openp, volume = eachLine.split(',')
            #date = datetime.datetime.fromtimestamp(int(date)).strftime('%Y%m%d')
            #date = dates.num2date(date)
            date = dt.datetime.strptime(date,'%Y%m%d').date()
            dateList.append(date)
            closepList.append(closep)
            highpList.append(highp)
            lowpList.append(lowp)
            openpList.append(openp)
            volumeList.append(volume)
            
                

    ax1.clear()
    #ax2.clear()
    #plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y%m%d'))
    #plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    ax1.plot(dateList, openpList)
    ax1.plot(dateList, closepList)
    ax1.plot(dateList, highpList)
    ax1.plot(dateList, lowpList)
    plt.ylabel('Stock Price')
    #plt.setp(ax1.get_xticklabels(),visible=False)   #set invisible
    
    #ax2.plot(dateList, volumeList)
    #plt.ylabel('Volume')
    plt.xlabel('Date') 
    plt.suptitle(StockName+' Stock Price')
    
   
    #ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    
            

class SeaofBTC(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        
        tk.Tk.wm_title(self, 'Stock Market Assistant Application')
        
        container = tk.Frame(self)
        container.pack(side='top', fill='both',expand=True)
        container.grid_rowconfigure(0, weight=1)

        container.grid_columnconfigure(0, weight=1)

        
        
        menubar = tk.Menu(container)
        
        filemenu = tk.Menu(menubar, tearoff=0)
        #filemenu.add_command(label='Save settings', command=lambda:popupmsg('Not supported yet.'))
        #filemenu.add_separator()
        filemenu.add_command(label='Exit', command=quit)
        menubar.add_cascade(label='File',menu=filemenu)
        
        dataTF = tk.Menu(menubar, tearoff=1)
        dataTF.add_command(label = "AAPL",
                                   command=lambda: changeStocks('AAPL'))
        dataTF.add_command(label = "GOOG",
                                   command=lambda: changeStocks('GOOG'))
        dataTF.add_command(label = "MSFT",
                                   command=lambda: changeStocks('MSFT'))
        dataTF.add_command(label = "AMZN",
                                   command=lambda: changeStocks('AMZN'))
        dataTF.add_command(label = "EBAY",
                                   command=lambda: changeStocks('EBAY'))
        dataTF.add_command(label = "TSLA",
                                   command=lambda: changeStocks('TSLA'))
        menubar.add_cascade(label = "Stocks", menu = dataTF)
        
        
        
        
        
        
        
        
        
        tk.Tk.config(self, menu=menubar)
        
        self.frames = {}
        
        for F in (HomePage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        
        
        self.show_frame(HomePage)
        
    def show_frame(self, cont):
        
        frame = self.frames[cont]
        frame.tkraise()
        
def qf(param):
    print(param)        
        
class HomePage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        
        
        #button1 = tk.Button(self, text='Visit Page 1', command=lambda:qf("aaaa")) 
        button1 = ttk.Button(self, text='Graph Page', command=lambda: controller.show_frame(PageOne))
        button1.pack()
        button2 = ttk.Button(self, text='Information Page', command=lambda: controller.show_frame(PageTwo))
        button2.pack()
        
        label = ttk.Label(self, text='Home Page', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        label = tk.Label(self, text="""Hi, this is my final project-- Stock Market Assistant Application.
        I'm using big data method to provide you with some assistance of Stock Mrket.
        Hope you enjoy.""", font=LARGE_FONT)


        label.pack(side="top", fill="x", pady=10)
        
        
class PageOne(tk.Frame):    #Graph Page
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        
        button1 = tk.Button(self, text='Home Page', command=lambda: controller.show_frame(HomePage))
        button1.pack()
        button2 = tk.Button(self, text='Information Page', command=lambda: controller.show_frame(PageTwo))
        button2.pack()
        
        label = ttk.Label(self, text='Graph Page', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
class PageTwo(tk.Frame):    #Information Page
    
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        
        f = open('RSS.txt', 'r')
        line1 = f.readline()
        line2 = f.readline()
        while line2:
            line1 += line2
            line2 = f.readline()
            
        print(line1)
        
          

        #frame = ttk.Frame(parent)
        #frame['padding'] = (5,10)
        #frame['borderwidth'] = 2
        #frame['relief'] = 'sunken'
        
        
        #button1 = tk.Button(self, text='Visit Page 1', command=lambda:qf("aaaa")) 
        button1 = ttk.Button(self, text='Home Page', command=lambda: controller.show_frame(HomePage))
        button1.pack()
        button2 = ttk.Button(self, text='Graph Page', command=lambda: controller.show_frame(PageOne))
        button2.pack()
        
        #label1 = tk.Label(self, text='Information Page', height=100, font=LARGE_FONT,anchor=tk.NW, width=150, justify='left')
        #label1.pack(pady=10, padx=10)
        
        label1 = tk.Label(self, text=line1, height=100, font=LARGE_FONT,anchor=tk.NW, width=150, justify='left')
        label1.pack(pady=10, padx=10)
        
        #resultsContents = StringVar()
        #resultsContents.set(line1)
        
        #label = ttk.Label(self, text='Full name:')
        #label['textvariable'] = resultsContents
        
        #label.pack(pady=10, padx=10)
        

        
                      
app = SeaofBTC()
app.geometry('1280x720')
ani = animation.FuncAnimation(f, animate, interval=100)    #update after 0.1 sec
app.mainloop()

        
       
       
          
         
         
         
    
