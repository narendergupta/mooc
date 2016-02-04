from mooc.config.strings import *
from datamodel import DataModel
from gen_utils import *

import statistics as stats


class Experimenter:
    """Execute and manage machine learning experiments"""
    def __init__(self, dm):
        self.dm = dm

    def set_datamodel(self, dm):
        self.dm = dm
        return None

    def perform_dummy_experiment(self):
        print("Dummy Experiment")
        print("Size of data: " + str(len(self.dm.data)))

