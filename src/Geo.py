# Taylor Pool
# March 14, 2017
#AUVSI Project
#

##############################
#Function toGPS takes NED and converts into GPS format using the geopy library


from geographiclib.geodesic import Geodesic
import math 

class Geobase:
    #Initializer Function
    def __init__(self, originLat, originLong, originHeight=0):
        self.origin = [originLat, originLong, originHeight]

    #Instance Variable Modifier
    def change_origin(self, originLat, originLong, originHeight=0):
        self.origin = [originLat, originLong, originHeight]

    #GPS to NED
    #Pre: lat2 and long2 are in long decimal format or DD-MM-SS
    #Post: Returns a list containing location in [north, east, down]
    def gps_to_ned(self, lat2, long2, height=0):
        #Conversion to Long Decimal Format from DD-MM-SS
        values = [str(lat2), str(long2)]
        newValues = []
        for value in values:
            if ("N" in value) or ("S" in value) or ("E" in value) or ("W" in value) == True:
                newValues.append(decimal_degrees(value))
            else:
                newValues.append(float(value))
        diction = Geodesic.WGS84.Inverse(self.origin[0], self.origin[1], newValues[0], newValues[1])
        solution = [diction['s12']*math.cos(math.radians(diction['azi1'])), diction['s12']*math.sin(math.radians(diction['azi1'])), -height]
        return solution

    #NED to GPS
    #Pre: north, east ,down are in meters
    #Post: Returns a list containing GPS [latitude, longitude, altitude]
    def ned_to_gps(self, north, east, down = 0):
        s_12 = math.sqrt(north**2+east**2)
        azi_1 = math.degrees(math.asin(east/s_12))
        diction = Geodesic.WGS84.Direct(self.origin[0], self.origin[1], azi_1, s_12)
        solution = [diction['lat2'], diction['lon2'], -down]
        return solution

