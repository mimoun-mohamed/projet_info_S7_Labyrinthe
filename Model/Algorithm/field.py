from Model.Algorithm.algorithm import Algorithm
import random


class Field(Algorithm):
    def __init__(self, name, description, code, maze):
        super.__init__(name, description)
        self.code = code
        self.maze = maze

    def add_way(self, way):
        return None

    def get_next(self,square):
        return None


