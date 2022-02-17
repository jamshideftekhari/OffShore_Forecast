import pandas as pd
import Persistance
from Wind import WindMeasure
from datetime import datetime,timedelta
from operator import attrgetter
from itertools import groupby


class MeasureCatalog(object):
    Measurements=[]
    WindMeasurements=[]
    def __init__(self):
        self.Measurements = Persistance.GetFromCSV()
        self.WindMeasurements.clear()
        for m in self.Measurements:
            wm = WindMeasure(m.TimeStamp, float(m.WindSpeed.replace(",",".")), Persistance.ConverDegreeToText(int(m.WindDirection)))
            self.WindMeasurements.append(wm)
        

    def GetWindData(self):
        return self.WindMeasurements

    def GetMeasureTimeInterval(self,stime, etime):
        wd= self.WindMeasurements
        dailymax=[]
        maxDate = max(m.TimeStamp for m in wd)
        minDate = min(m.TimeStamp for m in wd)
        print(maxDate)
        print(minDate)
        print(datetime.strptime(maxDate,"%d-%m-%Y %H:%M").date())
        print(datetime.strptime(minDate,"%d-%m-%Y %H:%M").date())
        print(datetime.strptime(minDate,"%d-%m-%Y %H:%M").date()+timedelta(days=1))

        dailymax.append([maxDate, 9.1])
        dailymax.append([minDate, 6.2])

        tempList=[]
        for d in range(1,2):
            dateList = list(filter(lambda x:(x.TimeStamp==maxDate),wd))
            print(dateList)
            maxWind = max(mw.WindSpeed for mw in dateList)
            tempList.append(maxWind)
            print(tempList)
            
        for d in dailymax:
            print(d)

    def GetWinMaxValue(self):
        wd= self.WindMeasurements
        return max(m.WindSpeed for m in wd)

    def GetWinMaxValueEachDay(self):
        dailymax=[]
        index = 0
        for m in self.WindMeasurements:
           date = datetime.strptime(m.TimeStamp,"%d-%m-%Y %H:%M").date()
           maxwind = m.WindSpeed
           index +=1 
           if index<len(self.WindMeasurements):
               dateInNext = datetime.strptime(self.WindMeasurements[index].TimeStamp,"%d-%m-%Y %H:%M").date()
               if date == dateInNext:
                 if maxwind <= self.WindMeasurements[index].WindSpeed:
                    maxwind = self.WindMeasurements[index].WindSpeed
                    print(maxwind)
                    print(dateInNext)
               else:     
                 dailymax.append(m) 
        
        return dailymax    

    def SortList(self):
        print(self.WindMeasurements)
       # print(self.WindMeasurements.sort(key=attrgetter("WindSpeed")))
        s = sorted(self.WindMeasurements,key=lambda x: x.WindSpeed)
        return s # sorted(s,key=lambda x: x.TimeStamp)
        
    def GroupAndMax(self):
        listByDate=self.WindMeasurements
        print("********before*******")
        for m in listByDate:
            print(m)
        for item in listByDate:
            item.TimeStamp = datetime.strptime(item.TimeStamp,"%d-%m-%Y %H:%M").date()
        print("********after*******")
        for m in listByDate:
            print(m)

        groups = groupby(listByDate, lambda x: (x.TimeStamp, x.WindDirection))
        for key,gr in groups:
            print(key)
            ln = len(list(gr))
            print("group length is: " + str(ln))
            
            
        groups1 = groupby(listByDate, lambda x: (x.TimeStamp))
        st=0
        for key, gr in groups1:
           print(key)
           ln = len(list(gr))
           print("group length is: " + str(ln)) 
           print("group starts and stop in indexes: " + str(st) + " " + str(st+ln))
           print(listByDate[st:ln+st]) 
           print("Max daily wind direction: ")
           print(max(m.WindSpeed for m in listByDate[st:ln+st]))
           st = ln   

    def MaxUsingIterator(self):
        myIter = iter(self.WindMeasurements)
        
