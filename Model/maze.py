from Model.square import Square
import random

class Maze:
    def __init__(self, size):
        self.size = size
        self.grid = [Square(k) for k in range(size**2)]
        self.player = None
        self.ia = None
        self.init_grid()

    def init_grid(self):
        for i in range(self.size):
            for j in range(self.size):
                if i != 0:
                    self.grid[self.size * i + j].set_up(self.size * (i-1) + j)
                if i != self.size - 1:
                    self.grid[self.size * i + j].set_down(self.size * (i + 1) + j)
                if j != 0:
                    self.grid[self.size * i + j].set_up(self.size * i + j - 1)
                if j != self.size - 1:
                    self.grid[self.size * i + j].set_up(self.size * i + j+1)

    def get_grid(self):
        return self.grid

    def add_way(self,way):
        return None

    def wilson_algorithm(self):
        not_visited = [k for k in range(self.size ** 2)]
        current_way = []
        turns = [] 
        while not_visited:
            position = not_visited[0]
            beginning = position
            while position in not_visited and position not in current_way: # Elaboration d'itinéraire
                current_way.append(position)
                direction = random.randint(0, 3)
                turns.append(direction)
                if direction == 0:    # Mettre les 4 directions dans maze
                    position = self.grid[position].get_up()
                elif direction == 1:
                    position = self.grid[position].get_right()
                elif direction == 2:
                    position = self.grid[position].get_down()
                else:
                    position = self.grid[position].get_left()
            if position not in current_way:                              #Implémentation de l'itinéraire
                position = beginning
                while turns:
                    not_visited.remove(position)
                    if direction == 0:  # Mettre les 4 directions dans maze
                        self.grid[position].give_up_access()
                        position = self.grid[position].get_up()
                    elif direction == 1:
                        self.grid[position].give_right_access()
                        position = self.grid[position].get_right()
                    elif direction == 2:
                        self.grid[position].give_down_access()
                        position = self.grid[position].get_down()
                    else:
                        self.grid[position].give_left_access()
                        position = self.grid[position].get_left()
        return None