from Model.square import Square


class Maze:
    def __init__(self, size):
        self.size = size
        self.grid = [Square(k) for k in range(size**2)]
        self.player = None
        self.ia = None

    def init_grid(self):
        for i in range(self.size):
            for j in range(self.size):
                if i != 0:
                    self.grid[self.size * i + j].set_up(self.size * (i-1) + j)
                if i != self.size -1 :
                    self.grid[self.size * i + j].set_down(self.size * (i + 1) + j)
                if j != 0 :
                    self.grid[self.size * i + j].set_up(self.size * i + j - 1)
                if j != self.size - 1 :
                    self.grid[self.size * i + j].set_up(self.size * i + j+1)

    def get_grid(self):
        return self.grid

    def get_neighbours(self, square):
        return(self.grid[square].get_up())
