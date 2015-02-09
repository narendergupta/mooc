import csv
import sys
import statistics as stat


class DataModel:
  """Class that parses raw data"""
  def __init__(self):
    self.data_files = ['data/data1.csv', 'data/data2.csv']
    self.readers = (
        csv.reader(open('data/data1.csv', 'r'), delimiter=','),\
        csv.reader(open('data/data2.csv', 'r'), delimiter=','),
        )
    self.data = []
    self.headers = next(self.readers[0])


  def get_header_index(self, header_name):
    for i in range(len(self.headers)):
      if self.headers[i] == header_name.lower().strip():
        return i;
    return -1


  def get_header_name(self, header_index):
    if header_index in range(len(self.headers)):
      return self.headers[header_index]
    return None


  def get_data(self, num):
    req_num = num
    data_count = len(self.data)
    if data_count < num:
      ri = 0
      while ri in range(len(self.readers)):
        if num <= 0:
          break
        num = num + 1 - self.readers[ri].line_num
        while num > 0:
          try:
            row = next(self.readers[ri])
            self.data.append(row)
            num = num - 1
          except StopIteration as e:
            ri = ri + 1
            break
    return self.data[:req_num]
