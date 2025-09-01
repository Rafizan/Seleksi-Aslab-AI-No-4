class WumpusWorld:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[' ' for _ in range(width)] for _ in range(height)]
        self.agent_position = (0, 0)
        self.grid[2][0] = 'W'  # Wumpus
        self.grid[2][0] = 'P'  # Pit
        self.grid[2][2] = 'P'
        self.grid[3][3] = 'P'
        self.grid[2][1] = 'G'  # Gold
        self.agent_direction = 'N'  # N, E, S, W
        self.score = 0
        self.has_gold = False
        self.game_over = False

    def reset(self):
        self.__init__(self.width, self.height)

    def is_valid_move(self, position):
        x, y = position
        return 0 <= x < self.width and 0 <= y < self.height

    def move_forward(self):
        x, y = self.agent_position
        if self.agent_direction == 'N':
            new_position = (x, y - 1)
        elif self.agent_direction == 'E':
            new_position = (x + 1, y)
        elif self.agent_direction == 'S':
            new_position = (x, y + 1)
        elif self.agent_direction == 'W':
            new_position = (x - 1, y)

        if self.is_valid_move(new_position):
            self.agent_position = new_position

        if self.grid[self.agent_position[1]][self.agent_position[0]] in ['W', 'P']:
            self.game_over = True
            self.score -= 1001
            return -1001
        else:
            self.score -= 1
            return -1

    def turn_left(self):
        directions = ['N', 'W', 'S', 'E']
        current_index = directions.index(self.agent_direction)
        self.agent_direction = directions[(current_index + 1) % 4]
        self.score -= 1
        return -1

    def turn_right(self):
        directions = ['N', 'E', 'S', 'W']
        current_index = directions.index(self.agent_direction)
        self.agent_direction = directions[(current_index + 1) % 4]
        self.score -= 1
        return -1

    def grab(self):
        x, y = self.agent_position
        if self.grid[y][x] == 'G':
            self.has_gold = True
            self.grid[y][x] = ' '
            self.score += 999
            return 999
        else:
            return -1
    
    def climb(self):
        if self.agent_position == (0, 0):
            self.game_over = True

        return -1
    
    def sense(self):
        x, y = self.agent_position
        perceptions = {
            'breeze': False,
            'stench': False,
            'glitter': False,
        }

        # Check for breeze (pit in adjacent cells)
        if (y > 0 and self.grid[y - 1][x] == 'P') or \
           (y < self.height - 1 and self.grid[y + 1][x] == 'P') or \
           (x > 0 and self.grid[y][x - 1] == 'P') or \
           (x < self.width - 1 and self.grid[y][x + 1] == 'P'):
            perceptions['breeze'] = True

        # Check for stench (Wumpus in adjacent cells)
        if (y > 0 and self.grid[y - 1][x] == 'W') or \
           (y < self.height - 1 and self.grid[y + 1][x] == 'W') or \
           (x > 0 and self.grid[y][x - 1] == 'W') or \
           (x < self.width - 1 and self.grid[y][x + 1] == 'W'):
            perceptions['stench'] = True

        # Check for glitter (gold in current cell)
        if self.grid[y][x] == 'G':
            perceptions['glitter'] = True

        return perceptions