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
        print('Début de la génération du labyrinthe')
        not_visited = [k for k in range(self.size ** 2)]
        while not_visited:
            position = not_visited[0]
            beginning = position
            current_way = []
            turns = []
            while position in not_visited and position not in current_way:  # Elaboration d'itinéraire
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
                    if position in not_visited:
                        not_visited.remove(position)
                    direction = turns.pop(0)
                    if direction == 0:  # Mettre les 4 directions dans maze
                        position = self.grid[position].get_up()
                        if position != -1:
                            self.grid[position].give_up_access()
                    elif direction == 1:
                        position = self.grid[position].get_right()
                        if position != -1:
                            self.grid[position].give_right_access()
                    elif direction == 2:
                        position = self.grid[position].get_down()
                        if position != -1:
                            self.grid[position].give_down_access()
                    else:
                        position = self.grid[position].get_left()
                        if position != -1:
                            self.grid[position].give_left_access()
            print(len(not_visited))
        return None