from random import *
from tkinter import *
import tkinter
from time import *

# generates a random color.
def rgb(rgb: tuple):
    return "#%02x%02x%02x" %rgb

# generates random numbers to be used to create a hex RGB string
def random_color():
    return rgb((randrange(255),randrange(255),randrange(255)))

def manhattan_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

# The under the hood code for the game.
class game():
    
    def __init__(self, width: int, height: int, num_mobs: int):
        """
        :args width - int that is how wide the map is gonnna be
        :args height - int that is how tall the map is gonna be
        """
        self.world = grid(width, height)
        self.entity_grid = grid(width, height)
        self.width = width
        self.height = height
        self.build_world()
        self.player_pos = (width // 2, height // 2)
        self.entity_list = []
        self.num_mobs = num_mobs
        self.held_object = None
        self.direction = 1
        self.pick_up_able_list = ["rock"]
        for x in range(num_mobs):
            self.entity_list.append(mob(self))
        for x in range(15):
            self.entity_grid.add("rock", self.random_placement())
        self.pass_methods = {mob: self.passable_for_mob}
            
        

    # defines how big the "window" will be that the player will see the map through.
    def window(self, coords: tuple, width: int, height: int):
        """
        :args coords - a tuple giving the x and y for what tile to start from.
        :args width - int that is how wide the window is gonnna be
        :args height - int that is how tall the window is gonna be
        :return - returns how much of the map will be visable
        """
        return (self.world.window(coords, width, height), \
        self.entity_grid.window(coords, width, height))

    # Goes through each cell in the game and decides if its going to be water
    # or grass.
    def build_world(self):
        for x in range(self.width):
            for y in range(self.height):
                if randint(0, 2) < 2:
                    self.world.add("grass", (x, y))
                    if randint(0, 1) == 0:
                        self.world.add("tree", (x, y))
                    if randint(0, 1) == 0:
                        self.world.add("boulder", (x, y))
                else: 
                    self.world.add("water", (x, y))

    # checks if the player can move in the dirction they're inputted.
    def move_checker(self, dir: int, coords: tuple, passable_method):
        """
        :args dir - this is an int we use to reprsent a dirction, with 3 being 
        up, 1 being down, 0 being right and 2 being left.
        :return - returns true if new_pos is within the map and false if its not
        """
        new_pos = self.cell_from(coords, dir)
        # checks to see if new_pos is off the map - if its greater then the 
        # width/height or less then equal to 0 its off the map.
        return new_pos[0] >= 0 and new_pos[0] < self.width and new_pos[1] >= 0 \
            and new_pos[1] < self.height and \
                passable_method( self.entity_grid.get_value(new_pos), self.world.get_value(new_pos))
            
                
                
    # Moves the player if move_checker returns true
    def move_player(self, dir: int):
        """
        :args dir - this is an int we use to reprsent a dirction, with 3 being 
        up, 1 being down, 0 being right and 2 being left.
        :return - returns true if the player did manage to move and false if not
        """
        self.direction = dir
        if not self.move_checker(dir, self.player_pos, self.passable_default):
            return False
        match dir:
            # up
            case 3:
                self.player_pos = (self.player_pos[0], self.player_pos[1] - 1)
            # down
            case 1:
                self.player_pos = (self.player_pos[0], self.player_pos[1] + 1)
            # right
            case 0:
                self.player_pos = (self.player_pos[0] + 1, self.player_pos[1])
            # left
            case 2:
                self.player_pos = (self.player_pos[0] - 1, self.player_pos[1])
        return True

    # returns random coords of a grass tile, used for placing mobs.
    def random_placement(self):
        coords = (randrange(self.width), randrange(self.height))
        while "grass" not in self.world.get_value(coords):
            coords = (randrange(self.width), randrange(self.height))
        return coords

    # Takes a cell and a diriction and returns what cell is in that diriction.
    def cell_from(self, cell: tuple, dir: int):
        match dir:
            # up
            case 0:
                return ((cell[0] +1), cell[1])
            # down
            case 1:
                return ( cell[0], (cell[1] +1))
            # right
            case 2:
                return ((cell[0] -1), cell[1])
            # left
            case 3:
                return ( cell[0], (cell[1] -1))

    # works out what the shortest path is between two points.
    def shortest_path(self, cell_one: tuple, cell_two: tuple, path_so_far: list, max_distance: int, passable_method):
        if manhattan_distance(cell_one, cell_two) > max_distance:
            return None
        if max_distance == 0:
            return None
        if cell_one == cell_two: # checks if its arrived.
            return [cell_two]
        new_path_so_far = path_so_far[:] # creates a copy of the path so far
        new_path_so_far.append(cell_one)
        best_path = None
        paths = []
        dirs = list(range(4))
        while len(dirs) > 0: # while it can still check one of the 4 directions
            dir = dirs.pop(randrange(len(dirs))) # removes the direction once we've tried it
            if not self.move_checker(dir, cell_one, passable_method) \
                or self.cell_from(cell_one, dir) in path_so_far: # checks if the
                # mob can move in that dirction or if it has already gone that 
                # direction, no point rechecking a path.
                continue
            else:
                path = self.shortest_path(self.cell_from(cell_one, dir), \
                    cell_two, new_path_so_far, max_distance - 1, passable_method) # if it can go in that direction 
                    # it calls itself to check if the next cell can go towards
                    # the targeted cell and does this untill it reaches the cell.
                if path != None:
                    paths.append(path)
        if len(paths) == 0:
            return None # incase there isnt a path.
        for path in paths:
            if best_path == None:
                best_path = path 
            else:
                if len(best_path) > len(path): # checks which is the shortest path.
                    best_path = path
        # best_path.insert(0, cell_one)
        return [cell_one] + best_path
    
    def do_stuff(self):
        for x in self.entity_list:
            x.do_something()

    def pick_up(self):
        if self.held_object == None:
            cell_to_check = self.cell_from(self.player_pos, self.direction)
            things = self.entity_grid.get_value(cell_to_check)
            for x in things:
                if self.pick_up_able(x):
                    self.held_object = x
                    things.remove(x)
                    return
    
    def pick_up_able(self, thing):
        if type(thing) == str:
            return thing in self.pick_up_able_list
        else:
            return thing.pick_up_able
    
    def put_down(self):
        if self.held_object == None:
            return
        else:
            cell_to_drop = self.cell_from(self.player_pos, self.direction)
            self.entity_grid.add(self.held_object, cell_to_drop)
            self.held_object = None

    def passable_for_entity(self, entity, entity_cell, world_cell):
        if entity in self.pass_methods: # entity will either be a type or a string.
            return self.pass_methods[entity](entity_cell, world_cell)
        else:
            self.passable_default(entity_cell, world_cell)

    def passable_default(self, entity_cell, world_cell):
        if "water" in world_cell and not "rock" in entity_cell:
            return False
        if not "water" in world_cell:
            return len(entity_cell) == 0
        else:
            return len(set(entity_cell) - {"rock"}) == 0
    
    def passable_for_mob(self, entity_cell, world_cell):
        if len(list(filter(lambda x: type(x) == mob, entity_cell))) > 0: 
            return True
        else:
            return self.passable_default(entity_cell, world_cell)

    def cell_passable_for_entity(self, entity, pos):
        if type(entity) == str:
            return self.passable_for_entity(entity, self.entity_grid.get_value(pos),\
                self.world.get_value(pos))
        else:
            return self.passable_for_entity(type(entity), self.entity_grid.get_value(pos),\
                self.world.get_value(pos))

    def deal_damage(self):
        return randint(5, 10)

    def attack(self):
        mob_list = list(filter(lambda x: type(x) == mob, self.entity_grid.get_value(self.cell_from(self.player_pos, self.direction))))
        if len(mob_list) == 0:
            return
        if mob_list[0].take_damage(self.deal_damage()):
            self.entity_grid.remove(mob_list[0], mob_list[0].pos)
            self.delete_mob(mob_list[0])

    def delete_mob(self, mob):
        self.entity_list.remove(mob)
            
        

                


# The part of the game the user will be interacting with.
class interface():
    
    def __init__(self, game: object, width: int, height: int, cell_size: int):
        """
        :args - copy of the game object that the interface is for
        :args width - int that is how wide the map is gonnna be
        :args height - int that is how tall the map is gonna be
        :args cell_size - how big each tile is gonna be
        """
        self.cell_size = cell_size
        self.width = width
        self.height = height
        self.game = game
        self.window = tkinter.Tk()
        self.boulder_tree_image = PhotoImage(file = "python stuff\games_with_wally\images\\boulder_tree.png")
        self.boulder_image = PhotoImage(file = "python stuff\games_with_wally\images\\boulders.png")
        self.grass_boulder_tree_image = PhotoImage(file = "python stuff\games_with_wally\images\grass_boulder_tree.png")
        self.grass_image = PhotoImage(file = "python stuff\games_with_wally\images\grass.png")
        self.tree_image = PhotoImage(file = "python stuff\games_with_wally\images\\tree.png")
        self.water_image = PhotoImage(file = "python stuff\games_with_wally\images\water.png")
        self.rock_image = PhotoImage(file = "python stuff\games_with_wally\images\\rock_image.png")
        self.water_rock_image = PhotoImage(file = "python stuff\games_with_wally\images\\rock_image_water.png")
        self.player_0 = PhotoImage(file = "python stuff\games_with_wally\images\dude0.png")
        self.player_1 = PhotoImage(file = "python stuff\games_with_wally\images\dude1.png")
        self.player_2 = PhotoImage(file = "python stuff\games_with_wally\images\dude2.png")
        self.player_3 = PhotoImage(file = "python stuff\games_with_wally\images\dude3.png")
        self.player_0_rock = PhotoImage(file = "python stuff\games_with_wally\images\dude_rock_0.png")
        self.player_1_rock = PhotoImage(file = "python stuff\games_with_wally\images\dude_rock_1.png")
        self.player_2_rock = PhotoImage(file = "python stuff\games_with_wally\images\dude_rock_2.png")
        self.player_3_rock = PhotoImage(file = "python stuff\games_with_wally\images\dude_rock_3.png")
        self.player_hit_0 = PhotoImage(file = "python stuff\games_with_wally\images\dudehit0.png")
        self.player_hit_1 = PhotoImage(file = "python stuff\games_with_wally\images\dudehit1.png")
        self.player_hit_2 = PhotoImage(file = "python stuff\games_with_wally\images\dudehit2.png")
        self.player_hit_3 = PhotoImage(file = "python stuff\games_with_wally\images\dudehit3.png")
        # dic of all the possible tiles we can draw.
        self.tile_images = {frozenset(["grass", "boulder", "tree"]): self.grass_boulder_tree_image,\
            frozenset(["grass"]): self.grass_image, frozenset(["water"]): self.water_image,\
                frozenset(["tree", "boulder"]): self.boulder_tree_image, \
                    frozenset(["boulder"]): self.boulder_image, \
                        frozenset(["tree"]): self.tree_image }
        self.canvas = Canvas(bg="white", width = width * cell_size + 3, \
        height = height * cell_size + 3, \
        scrollregion=(-1, -1, width * cell_size + 2, height * cell_size + 2))
        self.canvas.pack()
        self.play_offset = self.cell_size * (1 - 0.7) / 2
        self.entity_offset = self.cell_size * (1 - 0.5) / 2
        self.window.bind("<Key>", self.handle_key)
        self.entity_colors = {} 
        self.player_image = None
        self.draw_methods = {mob: self.draw_mob, str: self.draw_string}
        self.entity_images = {"rock": self.rock_image}
        self.special_string_draw_methods = {"rock": self.draw_rock}
        self.player_images = {"default": [self.player_0,self.player_1,self.player_2,self.player_3],\
             "rock": [self.player_0_rock,self.player_1_rock,self.player_2_rock,self.player_3_rock],
             "attack":[self.player_hit_0, self.player_hit_1, self.player_hit_2, self.player_hit_3]}
        self.attacking = False


    # draws a tile out using the coords given and the key for tile_images.
    def draw_image_tile(self, key, coords: tuple, cell_size: int, canvas: object):
        """
        :args key - a frozen set of the elements to draw.
        :args coords - a tuple giving the x and y for what tile we want to change.
        :args cell_size - the size of each tile
        :args canvas - a tkinter object that everything is displayed on.
        """
        canvas.create_image(coords[0] * cell_size, coords[1] * cell_size, \
            anchor = NW, image = self.tile_images[key] )

    # Draws the section of the map in the interface allowing the user to 
    # see/interact with it.
    def draw_window(self, coord_x, coord_y, window_width: int, window_height: int):
        """
        :args coords - a tuple giving the x and y for what tile we want to change.
        :args window_width - the width for how much of the map is gonna be visable.
        :args window_height - the height for how much of the map is gonna be visable.
        """
        self.canvas.delete("all")
        
        enviroment, entities = self.game.window((coord_x, coord_y), window_width,\
             window_height)

        for i in range(window_width):
            for j in range(window_height):
                self.draw_cell(enviroment.get_value((i, j)), \
                    entities.get_value((i, j)), (i, j))

        self.draw_player()
        self.window.update()

    # Draws a "thing" (tile or mob etc)
    def draw_thing(self, thing, coords: tuple):
        pass
    
    # Draws multiple "things" (tile or mob etc)
    def draw_things(self, things: list, coords: tuple):
        """
        :args things - the type of thing you want to draw (tile or mob)
        :args coords - a tuple giving the x and y for what tile we want to change. 
        """
        if things in self.tile_images:
            self.draw_image_tile(things, coords, self.cell_size, self.canvas)
        
    # Checks if we have a function to draw whatever is desired on the tile and
    # calls it if it is, will also check more then one function can create the 
    # desired tile. 
    def draw_cell(self, world_cell: list, entities_cell: list, coords: tuple):
        """
        :args world_cell - what we want to draw onto the map or background
        :args entities_cell - what mob we want to draw
        :args coords - a tuple giving the x and y for what tile we want to change. 
        """
        # Drawing the tiles
        if world_cell == None: # if world hasnt been generated
            return
        world_set = frozenset(world_cell)
        if world_set in self.tile_images:
            self.draw_image_tile(world_set, coords, \
                self.cell_size, self.canvas)
        else:
            for key in self.tile_images:
                if key <= world_set:
                    self.draw_image_tile(key, coords, \
                        self.cell_size, self.canvas)
                    world_set -= key
        # Drawing the entities
        for x in entities_cell:
            self.draw_methods[type(x)](coords, x, entities_cell, world_cell)


    # Draws the player in the center of the screen with an offset to make them
    # not take up the whole tile.
    def draw_player(self):
        if self.attacking:
            key = "attack"
        elif not self.game.held_object:
            key = "default"
        elif type(self.game.held_object) == str:
            key = self.game.held_object
        else:
            key = type(object)
        self.canvas.create_image((self.width // 2) * self.cell_size, \
            (self.height // 2) * self.cell_size, \
            anchor = NW, image = self.player_images[key][self.game.direction] )

    # allows the user to control the player char by capturing keyboard inputs.
    def handle_key(self, event):
        match event.keysym:
            case "h":
                self.attacking = True
                self.game.attack()
                self.set_player_pos(self.game.player_pos)
                sleep(0.3)
                self.attacking = False
            case "space":
                if not self.game.held_object:
                    self.game.pick_up()
                else:
                    self.game.put_down()
            case "Up":
                self.player_image = self.player_3
                if self.game.direction == 3: 
                    self.game.move_player(3)
                else:
                    self.game.direction = 3
            case "Down":
                self.player_image = self.player_1
                if self.game.direction == 1:
                    self.game.move_player(1)
                else:
                    self.game.direction = 1 
            case "Right":
                self.player_image = self.player_0
                if self.game.direction == 0:
                    self.game.move_player(0)
                else:
                    self.game.direction = 0
            case "Left":
                self.player_image = self.player_2
                if self.game.direction == 2:
                    self.game.move_player(2)
                else:
                    self.game.direction = 2                    
        self.set_player_pos(self.game.player_pos)
        self.game.do_stuff()
        

    # sets the player pos at the center of the screen.
    def set_player_pos(self, pos):
        self.draw_window(pos[0] - self.width // 2, pos[1] - self.height // 2, \
            self.width, self.height)

    def get_entity_color(self, entity):
        if not entity in self.entity_colors:
            self.entity_colors[entity] = random_color()
        return self.entity_colors[entity]

    def draw_mob(self, coords, mob, entiy_cell, world_cell):
        self.shape = self.canvas.create_oval(coords[0] * self.cell_size + self.entity_offset, coords[1] * self.cell_size + self.entity_offset, \
        (coords[0] +1) * self.cell_size - self.entity_offset, (coords[1] +1) * self.cell_size - self.entity_offset, fill = self.get_entity_color(mob) )

    def draw_string(self, coords, string, entity_cell, world_cell):
        if string in self.special_string_draw_methods:
            self.special_string_draw_methods[string](coords, entity_cell, world_cell)
        else:
            self.canvas.create_image(coords[0] * self.cell_size, coords[1] * self.cell_size, \
            anchor = NW, image = self.entity_images[string])

    def draw_rock(self, coords, entity_cell, world_cell):
        if "water" in world_cell:
            self.canvas.create_image(coords[0] * self.cell_size, coords[1] * self.cell_size, \
            anchor = NW, image = self.water_rock_image)
        else:
            self.canvas.create_image(coords[0] * self.cell_size, coords[1] * self.cell_size, \
            anchor = NW, image = self.rock_image)
    


# Where the infomation on the tiles of the game map is kept.
class grid():
    def __init__(self, width: int, height: int):
        """
        :args width - int that is how wide the map is gonnna be
        :args height - int that is how tall the map is gonna be
        """
        self.width = width
        self.height = height
        self.g = []
        for i in range(width):
            self.g.append([])
            for j in range(height):
                self.g[i].append([])

    # Allows you to print out the grid to check whats in it
    def print_self(self):
        print(self.g)

    # Add a tile to the grid
    def add(self, thing, coords: tuple):
        """
        :args thing - what we want to add to the cell
        :args coords - a tuple giving the x and y for what tile we want to change.
        """
        self.g[coords[0]][coords[1]].append(thing)

    # Remove a tile from the grid
    def remove(self, thing, coords: tuple):
        """
        :args thing - what we want to remove from the call
        :args coords - a tuple giving the x and y for what tile we want to change.
        """
        if thing in self.g[coords[0]][coords[1]]:
            self.g[coords[0]][coords[1]].remove(thing)

    # Returns the dimensions of the map.
    def get_dims(self):
        """
        :returns - returns a tuple of the width and height.
        """
        return (self.width, self.height)
    
    # Checks if the tile is unassigned.
    def check_empty(self, coords: tuple):
        """
        :args coords - a tuple giving the x and y for what tile we want to change.
        :reutns - returns true if the cell is empty and false if its not.
        """
        return len(self.g[coords[0]][coords[1]]) == 0

    # Creates the window for the player to view.
    def window(self, coords: tuple, window_width: int, window_height: int):
        """
        :args coords - a tuple giving the x and y for what tile we want to change.
        :args window_width - int that is how wide the window is gonnna be
        :args window_height - int that is how tall the window is gonna be
        :return -
        """
        view = grid(window_width, window_height)
        for i in range(window_width):
            for j in range(window_height):
                view.g[i][j] = self.get_value((i + coords[0], j + coords[1]))
        return view

    # Returns the value of whats in a tile.
    def get_value(self, coords: tuple):
        """
        :args coords - a tuple giving the x and y for what tile we want to change.
        :return - whats inside the cell of the given tuple coords.
        """
        if coords[0] >= self.width or coords[0] < 0 or coords[1] \
        >= self.height or coords[1] < 0:
            return None
        else:
            return self.g[coords[0]][coords[1]]

class entity():
    
    def __init__(self, game):
        self.game = game
        self.pos = game.random_placement()
        self.game.entity_grid.add(self, self.pos)
        pick_up_able = False
        self.mob_health = randint(10,20)

    def set_position(self, pos):
        if not self.game.passable_default(self.game.entity_grid.get_value(pos),self.game.world.get_value(pos) ):
            return
        self.game.entity_grid.remove(self, self.pos)
        self.pos = pos
        self.game.entity_grid.add(self, self.pos)





class player(entity):
    pass

class mob(entity):


    def do_something(self):
        path = self.game.shortest_path(self.pos, self.game.player_pos, [], 10, self.game.passable_for_mob)
        if path != None: # if shortest_path has returned a value
            if len(path) < 3:
                return
            else:
                self.set_position(path[1])
                pass
        else:
            # insert random movement here
            pass

    def take_damage(self, damage):
        self.mob_health -= damage
        if self.mob_health <= 0:
            return True
        return False



windim = 11

game1 = game(40, 40, 10)
playable_game = interface(game1, windim, windim, 100)






playable_game.set_player_pos(game1.player_pos)
playable_game.window.mainloop()


# for i in range(20):
#     playable_game.draw_window(i, 10, windim, windim)
#     sleep(0.1)