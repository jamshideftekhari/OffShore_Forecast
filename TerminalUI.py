from DataDraw import DataDraw
from MeasurementCatalog import MeasureCatalog
print("*********** Site Forecast *********")
#draw = DataDraw()
#draw.AverageDirection()
WD = MeasureCatalog()   #Measurement catalog object
#for W in WD.GetWindData():
 #   print (W.ToString())

#print("wind Max Value: "+ str(WD.GetWinMaxValue()))    
#print("Max and min date time: "+ str(WD.GetMeasureTimeInterval(0,0)))

#for MWD in WD.SortList():
#print(WD.SortList())
WD.GroupAndMax()