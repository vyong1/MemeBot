import datetime

class PreviousRequestTime:
    def __init__(self, filename):
        self.filename = filename
    
    def get(self) -> datetime:
        '''Gets the previous date time as a datetime object'''
        try:
            # Read in the file
            f = open(self.filename, 'r')
            time_str = f.read()
            f.close()
            #Read in the string time
            prev_datetime = datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S.%f')
            return prev_datetime
        except IOError:
            print("Unable to open the file")
        except ValueError:
            print("Unable to read the time as it is formatted")
    
    def update(newTime):
        '''Updates the last request time with the new one'''
        f = open(self.filename, 'w')
        f.write(str(newTime))
        f.close()