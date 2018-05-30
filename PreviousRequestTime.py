import datetime

class PreviousRequestTime:
    def __init__(self, filename):
        self.filename = filename
    
    def get(self) -> datetime:
        '''Gets the previous date time as a datetime object'''
        try:
            f = open(self.filename, 'r')
            time_str = f.read()
            f.close()
            prev_datetime = datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S.%f')
            return prev_datetime
        except IOError:
            print("Unable to open the previous request time file")
        except ValueError:
            print("Unable to read the time as it is formatted")
    
    def update(self, newTime):
        '''Updates the last request time with the new one'''
        f = open(self.filename, 'w')
        f.write(str(newTime))
        f.close()