from datetime import datetime
from gen_utils import *
from mooc.config.strings import *

import csv
import sys
import statistics as stat


class DataModel:
    """Class that parses raw data"""
    def __init__(self):
        self.data_file = '../data/data.csv'


    def read_data(self, to_read_count=-1, normalize_data=False):
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
        # Normalize various features of datapoints
        if normalize_data is True:
            self.normalize_data()
        return None


    def write_data(self, output_file):
        with open(output_file,'w') as output_f:
            data_writer = csv.DictWriter(\
                    output_f, fieldnames=sorted(list(self.data[0].keys())))
            data_writer.writeheader()
            for row in self.data:
                data_writer.writerow(row)
        return None


    def normalize_data(self):
        norm_data = []
        for row in self.data:
            (row[INSTITUTE], row[COURSE_NAME], row[SEM_YEAR], row[SEM_TERM]) = \
                    self.__normalize_course_id(row[COURSE_ID])
            (row[START_TIME_MONTH],row[START_TIME_DAY],row[START_TIME_YEAR]) = \
                    self.__normalize_date(row[START_TIME_DI])
            row[LAST_EVENT_DI] = row[LAST_EVENT_DI] if row[LAST_EVENT_DI] != '' \
                    else row[START_TIME_DI]
            (row[LAST_EVENT_MONTH],row[LAST_EVENT_DAY],row[LAST_EVENT_YEAR]) = \
                    self.__normalize_date(row[LAST_EVENT_DI])
            row[DAYS_BETWEEN] = self.__days_between(\
                    row[START_TIME_DI], row[LAST_EVENT_DI])
            norm_data.append(row)
        self.data = norm_data
        return None


    def __normalize_course_id(self, course_id):
        parts = course_id.split('/')
        institute = parts[0]
        course_name = parts[1]
        sem_parts = parts[2].split('_')
        sem_year = sem_parts[0]
        sem_term = sem_parts[1] if len(sem_parts) > 1 else ''
        return (institute, course_name, sem_year, sem_term)


    def __normalize_date(self, value):
        if value == '':
            return ('','','')
        value = datetime.strptime(value, '%Y-%m-%d')
        return (value.month, value.day, value.year)


    def __days_between(self, d1, d2):
        d1 = datetime.strptime(d1, '%Y-%m-%d')
        d2 = datetime.strptime(d2, '%Y-%m-%d')
        return abs((d2-d1).days)


