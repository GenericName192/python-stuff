from random import *
from tkinter import *
import tkinter
from time import *

def rgb(rgb):
    return "#%02x%02x%02x" %rgb

def random_color():
    return rgb((randrange(255),randrange(255),randrange(255)))

class graph_mover:
    def __init__(self, mover, game):
        self.mover = mover
        self.game = game
        self.shape = game.canvas.create_oval(mover.x * game.cell_size, mover.y * game.cell_size, \
        (mover.x +1) * game.cell_size, (mover.y +1) * game.cell_size, fill = random_color() )

    def move(self):
        self.mover.move()
        self.game.canvas.coords(self.shape, (self.mover.x * self.game.cell_size, self.mover.y * self.game.cell_size, \
        (self.mover.x +1) * self.game.cell_size, (self.mover.y +1) * self.game.cell_size))

    def reset(self):
        self.mover.reset()
        self.game.canvas.delete(self.shape)
        self.shape = self.game.canvas.create_oval(self.mover.x * self.game.cell_size, self.mover.y * self.game.cell_size, \
        (self.mover.x +1) * self.game.cell_size, (self.mover.y +1) * self.game.cell_size, fill = random_color() )

class mover:
    def __init__(self, x, y, game):
        self.last_move = randrange(4)
        self.x = x
        self.y = y
        self.map = game.grid
        self.game = game
        dims = self.map.get_dims()
        self.map_width = dims[0]
        self.map_height = dims[1]
        self.map.add(self, x, y)

    def print_self(self):
        print("I am at: " + str(self.x) + " " + str(self.y))
        pass

    def move(self):
        if (self.x, self.y) == self.game.player_pos:
            self.game.finish_game()
            return
        path = self.game.shortest_path((self.x, self.y), self.game.player_pos, [])
        if self.map.check_empty(path[1][0], path[1][1]):
            self.map.remove(self, self.x, self.y)
            self.x = path[1][0]
            self.y = path[1][1]
            self.map.add(self, self.x, self.y)
        # dirs = [0, 1, 2, 3]
        # dirs.remove(self.last_move)
        # while len(dirs) > 0:
        #     dir = dirs.pop(randrange(len(dirs)))
        #     if self.move_dir(dir):
        #         self.last_move = (dir + 2) % 4
        #         return
        # dir = self.last_move 
        # self.last_move = (dir + 2) % 4
        # self.move_dir(dir)
    
    def reset(self):
        self.map.remove(self, self.x, self.y)
        self.x = randrange(self.map_width)
        self.y = randrange(self.map_height)
        self.map.add(self, self.x, self.y)

    def move_dir(self, dir):
        if not self.game.move_checker(self.x, self.y, dir):
            return False
        self.map.remove(self, self.x, self.y) 
        match dir:
            case 0:
                self.x = (self.x +1) % self.map_width
            case 1:
                self.y = (self.y +1) % self.map_height
            case 2:
                self.x = (self.x -1) % self.map_width
            case 3:
                self.y = (self.y -1) % self.map_height
        self.map.add(self, self.x, self.y)
        return True
               

    def __repr__(self):
        return "mover"

class grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.g = []
        for i in range(width):
            self.g.append([])
            for j in range(height):
                self.g[i].append([])

    def print_self(self):
        print(self.g)

    def add(self, thing, x, y):
        self.g[x][y].append(thing)

    def remove(self, thing, x, y):
        if thing in self.g[x][y]:
            self.g[x][y].remove(thing)

    def get_dims(self):
        return (self.width, self.height)
    
    def check_empty(self, x, y):
        return len(self.g[x][y]) == 0

class game:
    def __init__(self, width, height, cell_size, num_movers, density):
        self.num_movers = num_movers
        self.density = density
        self.cell_size = cell_size
        self.width = width
        self.height = height
        self.num_movers = num_movers
        self.window = tkinter.Tk()
        self.canvas = Canvas(bg="white", width = width * cell_size + 3, height = height * cell_size + 3, scrollregion=(-1, -1, width * cell_size + 2, height * cell_size + 2))
        self.canvas.pack()
        self.grid = grid(width, height)
        self.make_walls(density)
        self.join_domains()
        self.draw_walls()
        self.gmovers = []
        self.play_offset = self.cell_size * (1 - 0.7) / 2
        self.set_player_pos((self.width // 2 ,self.height // 2))
        self.window.bind("<Key>", self.handle_key)
        self.end_game = False
        for i in range(num_movers):
            self.gmovers.append(graph_mover(mover(randrange(width), randrange(height), self), self ))

    def handle_key(self, event):
        if self.end_game:
            match event.keysym:
                case "y":
                    self.reset()
                case "n":
                    self.window.destroy()
                    global running
                    running = False
        match event.keysym:
            case "Up":
                self.move_player(3)
            case "Down":
                self.move_player(1)
            case "Right":
                self.move_player(0)
            case "Left":
                self.move_player(2)


    def step(self):
        for m in self.gmovers:
            m.move()
        self.window.update()

    def move_checker(self, x, y, dir, mobs = True):
        if mobs and hasattr(self, "player_pos") and self.cell_from((x, y), dir) == self.player_pos:
            return False
        match dir:
            case 0:
                if self.vwalls[y][(x + 1) % self.width]:
                    return False
                x = (x + 1) % self.width
            case 1:
                if self.hwalls[x][(y + 1) % self.height]:
                    return False
                y = (y + 1) % self.height
            case 2:
                if self.vwalls[y][x]:
                    return False
                x = (x - 1) % self.width
            case 3:
                if self.hwalls[x][y]:
                    return False
                y = (y - 1) % self.height
        if mobs:
            return self.grid.check_empty(x, y)
        else: 
            return True

    def draw_walls(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.vwalls[i][j]:
                    self.canvas.create_line(j * self.cell_size, i * self.cell_size, j * self.cell_size, (i + 1) * self.cell_size, fill="black", width=1)
            if self.vwalls[i][0]:
                self.canvas.create_line(self.width * self.cell_size, i * self.cell_size, self.width * self.cell_size, (i + 1) * self.cell_size, fill="black", width=1)
        for i in range(self.width):
            for j in range(self.height):
                if self.hwalls[i][j]:
                    self.canvas.create_line(i * self.cell_size, j * self.cell_size, (i + 1) * self.cell_size, j * self.cell_size, fill="black", width=1)
            if self.hwalls[i][0]:
                self.canvas.create_line(i * self.cell_size, self.height * self.cell_size, (i + 1) * self.cell_size, self.height * self.cell_size, fill="black", width=1)



    def make_walls(self, density):
        hwalls = []
        vwalls = []

        for i in range(self.width):
            tempt_walls = []
            for j in range(self.height):
                test = random() < density
                tempt_walls.append(test)
                #if test: self.canvas.create_line(i * self.cell_size, j * self.cell_size, (i + 1) * self.cell_size, j * self.cell_size, fill="black", width=1)
            hwalls.append(tempt_walls)

        for i in range(self.height):
            tempt_walls = []
            for j in range(self.width):
                test = random() < density
                tempt_walls.append(test)
                #if test: self.canvas.create_line(j * self.cell_size, i * self.cell_size, j * self.cell_size, (i + 1) * self.cell_size, fill="black", width=1)
            vwalls.append(tempt_walls)

        self.hwalls = hwalls
        self.vwalls = vwalls
    
    def find_connecting_cells(self, start_cell, found_cells):
        if start_cell in found_cells:
            return
        found_cells.append(start_cell)
        for d in range(4):
            if self.move_checker(start_cell[0], start_cell[1], d):
                self.find_connecting_cells(self.cell_from(start_cell, d), found_cells)

    def cell_from(self, cell, dir):
        match dir:
            case 0:
                return ((cell[0] +1) % self.width, cell[1])
            case 1:
                return ( cell[0], (cell[1] +1) % self.height)
            case 2:
                return ((cell[0] -1) % self.width, cell[1])
            case 3:
                return ( cell[0], (cell[1] -1) % self.height)
    
    def find_domains(self):
        domains = []
        for x in range(self.width):
            for y in range(self.height):
                if self.is_in_domains((x,y), domains):
                    continue
                new_domain = []
                self.find_connecting_cells((x,y), new_domain)
                domains.append(new_domain)
        return domains

    def is_in_domains(self, cell, domains):
        for dom in domains:
            if cell in dom:
                return True
        return False
    
    def is_border_cell(self, cell, domain):
        dirs = list(range(4))
        while len(dirs) > 0:
            d = dirs.pop(randrange(len(dirs)))
            c = self.cell_from(cell, d)
            if not c in domain:
                return d
        return None

    def break_wall(self, cell, dir):
            match dir:
                case 0:
                    # right
                    self.vwalls[cell[1]][(cell[0] + 1 ) % self.width] = False
                case 1:
                    # down
                    self.hwalls[cell[0]][(cell[1] + 1 ) % self.height ] = False
                case 2:
                    # left
                    self.vwalls[cell[1]][cell[0]] = False
                case 3:
                    # up
                    self.hwalls[cell[0]][cell[1]] = False

    def join_domains(self):
        domains = self.find_domains()
        while len(domains) > 1:
            self.blend_domain(domains[randrange(len(domains))], domains)


    def blend_domain(self, domain, domains):
        copy = domain[:]
        while len(copy) > 0:
            cell = copy.pop(randrange(len(copy)))
            dir = self.is_border_cell(cell, domain)
            if dir == None:
                continue
            else:
                self.break_wall(cell, dir)
                second_domain = self.find_domain(self.cell_from(cell, dir), domains)
                domain += second_domain
                domains.remove(second_domain)


    def find_domain(self, cell, domains):
        for domain in domains:
            if cell in domain:
                return domain

    def set_player_pos(self, pos):
        self.player_pos = pos
        if not hasattr(self, "player_shape"):
            self.player_shape = self.canvas.create_rectangle(pos[0] * self.cell_size + self.play_offset, pos[1] * self.cell_size + self.play_offset, (pos[0] + 1) * self.cell_size - self.play_offset, (pos[1] + 1) * self.cell_size - self.play_offset, fill = "purple")
        else:
            self.canvas.coords(self.player_shape, pos[0] * self.cell_size + self.play_offset, pos[1] * self.cell_size + self.play_offset, (pos[0] + 1) * self.cell_size - self.play_offset, (pos[1] + 1) * self.cell_size - self.play_offset)

    def move_player(self, dir):
        if not self.move_checker(self.player_pos[0], self.player_pos[1], dir):
            return
        self.set_player_pos(self.cell_from(self.player_pos, dir))

    def shortest_path(self, cell_one, cell_two, path_so_far):
        if cell_one == cell_two:
            return [cell_two]
        new_path_so_far = path_so_far[:]
        new_path_so_far.append(cell_one)
        best_path = None
        paths = []
        dirs = list(range(4))
        while len(dirs) > 0:
            dir = dirs.pop(randrange(len(dirs)))
            if not self.move_checker(cell_one[0], cell_one[1], dir, mobs = False) or self.cell_from(cell_one, dir) in path_so_far:
                continue
            else:
                path = self.shortest_path(self.cell_from(cell_one, dir), cell_two, new_path_so_far)
                if path != None:
                    paths.append(path)
        if len(paths) == 0:
            return None
        for path in paths:
            if best_path == None:
                best_path = path
            else:
                if len(best_path) > len(path):
                    best_path = path
        # best_path.insert(0, cell_one)
        return [cell_one] + best_path



    def draw_path(self, cell_list):
        for i in range(len(cell_list) - 1):
            self.draw_line_between(cell_list[i], cell_list[i + 1])
        self.window.update()

    def draw_line_between(self, cell_one, cell_two):
        if (cell_one[0] == 0 and cell_two[0] == self.width - 1) or (cell_one[0] == self.width - 1 and cell_two[0] == 0):
            self.canvas.create_line(self.cell_size * 0.5, (cell_one[1]+ 0.5) * self.cell_size, 0, (cell_one[1]+ 0.5) * self.cell_size, fill = "blue", tag = "path")
            self.canvas.create_line((self.width - 0.5) * self.cell_size, (cell_one[1]+ 0.5) * self.cell_size, self.width * self.cell_size, \
                 (cell_one[1]+ 0.5) * self.cell_size, fill = "blue", tag = "path")
            return

        elif ((cell_one[1] == 0 and cell_two[1] == self.height - 1) or (cell_one[1] == self.height - 1 and cell_two[1] == 0)):
            self.canvas.create_line( (cell_one[0] + 0.5) * self.cell_size, self.cell_size * 0.5, (cell_one[0]+ 0.5) * self.cell_size, 0, fill = "blue", tag = "path")
            self.canvas.create_line((cell_one[0]+ 0.5) * self.cell_size, (self.width - 0.5) * self.cell_size, \
                 (cell_one[1]+ 0.5) * self.cell_size, self.height * self.cell_size, fill = "blue", tag = "path")

        else: 
            self.canvas.create_line((cell_one[0] + 0.5) * self.cell_size, (cell_one[1] + 0.5) * self.cell_size, \
            (cell_two[0] + 0.5) * self.cell_size, (cell_two[1] + 0.5) * self.cell_size, fill = "blue", tag = "path")


    def clear_path(self):
        self.canvas.delete("path")

    def finish_game(self):
        self.canvas.create_text((self.width / 2) * self.cell_size ,(self.height / 2) * self.cell_size, text="You Lose! \n Continue? Y/N", font=("Times New Roman", "40", "bold"))
        self.end_game = True

    def reset(self):
        self.canvas.delete("all")
        self.make_walls(self.density)
        self.join_domains()
        self.draw_walls()
        self.set_player_pos((self.width // 2 ,self.height // 2))
        self.player_shape = self.canvas.create_rectangle(self.player_pos[0] * self.cell_size + self.play_offset, self.player_pos[1] * self.cell_size + self.play_offset, (self.player_pos[0] + 1) * self.cell_size - self.play_offset, (self.player_pos[1] + 1) * self.cell_size - self.play_offset, fill = "purple")
        self.end_game = False
        for mob in self.gmovers:
            mob.reset()


                
                

width = 20
height = 20

print(rgb((154, 182, 52)))
round_one = game(width, height, 50, 5, 0.8)
running = True
# round_one.draw_path(round_one.shortest_path((2, 2), (9, 9), []))
while running: 
    round_one.step()
    sleep(0.3)



# gr = grid(width, height)
# cell_size = 50
# window = tkinter.Tk()
# c = Canvas(bg="white", width = width * cell_size, height = height * cell_size)
# c.pack()
# rpos = (5, 7)
# c.create_oval(rpos[0] * cell_size, rpos[1] * cell_size, (rpos[0] +1) * cell_size, (rpos[1] +1) * cell_size, fill="purple" )
# input()


# movers = []
# for i in range(1):
#     movers.append(mover(randrange(width), randrange(height), gr))

# for a in movers:
#     gr.print_self()
# print("")
# for a in movers:
#     a.move()

# for a in movers:
#     gr.print_self()