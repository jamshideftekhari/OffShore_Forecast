import csv
from WeatherMeasure import WeatherMeasure

WeatherMeasures = []

def ReadPrintCSV():
 with open('WeatherData.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for col in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(col)}')
            line_count += 1
        else:
            print(f'\t{col[0]}     {col[1]}                 {col[2]}           {col[3]}           {col[4]}            {col[5]}')
            line_count += 1
    print(f'Processed {line_count} lines.')

def ConverDegreeToText(degree):
    direction = ""
    if 45<=degree<=135:
        direction = "East"
    elif 135<=degree<=225:
        direction = "south"
    elif 225<=degree<=315:
        direction = "West"    
    elif 315<=degree:
        direction = "North"
    elif degree<=45:
        direction = "North"    
    return direction    



def WMListFromCSV():
 with open('WeatherData.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for col in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(col)}')
            line_count += 1
        else:
            measure=WeatherMeasure(col[0],col[2],col[3],ConverDegreeToText(int(col[4])),col[5])
            WeatherMeasures.append(measure)
            print(f'\t Processed {line_count} lines.')
            line_count += 1
    print(f'Processed {line_count} lines.')

def PrintWeatherData():
    for measure in WeatherMeasures:
        print(measure.ToString())

def GetFromCSV():
 with open('WeatherData.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for col in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(col)}')
            line_count += 1
        else:
            measure=WeatherMeasure(col[0],col[2],col[3],(col[4]),col[5])
            WeatherMeasures.append(measure)
            line_count += 1
    return WeatherMeasures

def GetFromDatabase():
    pass
def GetFromApi():
    pass



#ReadPrintCSV()  
#WMListFromCSV()
#PrintWeatherData()  