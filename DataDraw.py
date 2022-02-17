import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from MeasurementCatalog import MeasureCatalog

class DataDraw(object):

    def __init__(self):
        print("MatPlotlib Version: " + matplotlib.__version__)
        mc=MeasureCatalog()
        self.WindData = mc.GetWindData()

    def BarGarph(self):
        x = np.array(["A", "B", "C", "D"])
        y = np.array([3, 8, 1, 10])

        plt.bar(x,y)
        plt.show()  
   
    def CountDirection(self, direction):
        count=0
        for r in self.WindData:
            if r.WindDirection == direction:
                count+=1
        return count        

    def AverageDirection(self):
        x = np.array(["North", "East", "South", "West"])
        nc = 0
        ec = 0
        sc = 0
        wc = 0

        nc = self.CountDirection("North")
        ec = self.CountDirection("East")
        sc = self.CountDirection("south")
        wc = self.CountDirection("West")

        y = np.array([nc, ec, sc, wc])

        plt.bar(x,y)
        plt.show()     