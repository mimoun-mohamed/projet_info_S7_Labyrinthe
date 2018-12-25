from Model.Algorithm.algorithm import Algorithm
import random


class Field(Algorithm):
    def __init__(self, name, description, code, maze):
        super.__init__(name, description)
        self.code = code
        self.maze = maze

    def add_way(self, way):
        return (None)

    def wilson_algorithm(self, size):
        not_visited = [k for k in range(size ** 2)]
        current_way = []
        while not_visited:
            position = not_visited[0]
            while position in not_visited and position not in current_way:
                current_way.append(position)
                direction = random.randint(0,3)
                next = self.maze.get_grid()[position].set_     #mettre les 4 directions dans maze
            if position not in not_visited:
                self.add_way(current_way)
