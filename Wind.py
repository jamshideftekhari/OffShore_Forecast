
class WindMeasure(object):
    def __init__(self, timeStamp, windSpeed, windDirection):
        self.TimeStamp= timeStamp
        self.WindSpeed = windSpeed
        self.WindDirection = windDirection

    def __repr__(self):
        return str(self.TimeStamp) + " Wind Speed: " + str(self.WindSpeed) + " wind derection: " + str(self.WindDirection) + "\r\n"

    def ToString(self):
        return self.TimeStamp + " Wind Speed: " + str(self.WindSpeed) + " wind derection: " + str(self.WindDirection)