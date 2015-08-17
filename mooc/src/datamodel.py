from gen_utils import *

import csv
import sys
import statistics as stat


class DataModel:
    """Class that parses raw data"""
    def __init__(self):
        self.data_file = '../data/data.csv'


    def read_data(self, to_read_count=-1):
        self.data = []
        """Reads data file"""
        read_count = 0
        with open(self.data_file,'r') as data_f:
            reader = csv.DictReader(data_f)
            for row in reader:
                self.data.append(lowercase(row))
                read_count += 1
                if to_read_count > 0 and read_count >= to_read_count:
                    break
        return None


    def write_data(self, output_file):
        with open(output_file,'w') as output_f:
            data_writer = csv.DictWriter(output_f, fieldnames=sorted(list(self.data[0].keys())))
            data_writer.writeheader()
            for row in self.data:
                data_writer.writerow(row)
        return None


