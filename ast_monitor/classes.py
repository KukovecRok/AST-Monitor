class SensorData():
    def __init__(self, hr, lon, lat, alt, curr_time):
        self.hr = hr
        self.lon = lon
        self.lat = lat
        self.alt = alt
        self.curr_time = curr_time

class Intervals():
    def __init__(self, avhr, td):
        self.avhr = avhr
        self.td = td        
