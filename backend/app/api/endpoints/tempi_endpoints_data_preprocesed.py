import math
import statistics

class DataDigest:
    
    def __init__(self,data):
        self.data = data


    def validate_data(data):
        try:
            for i in data:
                if isinstance(i,int):
                    i = i*100/1.0*64
        except:
            print("Error on Digest data")

        
    def remove_errors(self, data):
        try:
            for i in data:
                if i < -100 or i > 100:
                    # I is not valid measurement
                    i = self.mean(data)
        except:
            print("Error on remover errors")

    def mean(self):
        return statistics.mean(self.data)
    
    def median(self):
        return statistics.median(self.data)
    
    def mode(self):
        return statistics.mode(self.data)
    
    def variance(self):
        return statistics.variance(self.data)
    
    def standard_deviation(self):
        return statistics.stdev(self.data)
    
    def sum(self):
        return sum(self.data)


