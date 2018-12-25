class Square:
    def __init__(self, id):
        self.id = id
        self.up = -1
        self.right = -1
        self.down = -1
        self.left = -1
        self.up_access = False
        self.right_access = False
        self.down_access = False
        self.left_access = False
        self.object = None

    def set_up(self, square):
        self.up = square

    def set_right(self, square):
        self.right = square

    def set_down(self, square):
        self.down = square

    def set_left(self, square):
        self.left = square

    def give_up_access(self):
        self.up_access = True

    def give_right_access(self):
        self.right_access = True

    def give_down_access(self):
        self.down_access = True

    def give_left_access(self):
        self.left_access = True

    def get_up(self, square):
        self.up = square

    def get_right(self, square):
        self.right = square

    def get_down(self, square):
        self.down = square

    def get_left(self, square):
        self.left = square
