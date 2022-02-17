class WeatherMeasure(object):
    def __init__(self, ts, rh, temp, wd, ws):
        self.TimeStamp = ts
        self.Humidity=rh
        self.Temperature=temp
        self.WindDirection = wd
        self.WindSpeed = ws

    def __repr__(self):
        return str(self.TimeStamp) + " " +str(self.Humidity) + " " +str(self.Temperature)+ " " +str(self.WindSpeed)+ " " +str(self.WindDirection)  
    
    def ToString(self):
        return str(self.TimeStamp) + " " +str(self.Humidity) + " " +str(self.Temperature)+ " " +str(self.WindSpeed)+ " " +str(self.WindDirection)  

