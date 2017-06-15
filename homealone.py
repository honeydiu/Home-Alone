user_input = '> '
prompt = "[ENTER]"

class Scene(object):
    def enter(self):
        pass

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.begin()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Item(object):
    def __init__(self,name,description):
        self.name = name
        self.description = description
    def __str__(self):
        return "%s: %s" %(self.name, self.description)

class Inventory(object):
    def __init__(self):
        self.inventory = []
        self.items = {'key': Key(),'apple': Apple(), 'lantern': Lantern(False)}
    def add_item(self, item):
        self.inventory.append(item)
        print ("Item added to inventory:")
        print (item)
    def use_item(self,item):
        item.action()
    def check_inventory(self):
        print ("Inventory:")
        for item in self.inventory:
            print (item)
        if not self.inventory:
            print ("Your inventory is empty")
        if len(self.inventory) > 0:
            print ("Choose an ITEM to use or CLOSE INVENTORY")
            choice = input("> ")
            if choice in self.items:
                item_chosen = self.items.get(choice)
                self.use_item(item_chosen)
            elif "close" in choice:
                print ("Inventory closed")
            else:
                print ("You don't have that")

class Key(Item):
    def __init__(self):
        self.name = "KEY"
        self.description = "A mysterious old skeleton key"
    def action(self):
        if scene.name == "lobby":
        #if a_map.next_scene == "lobby":
            print ("Open the door")
    # this doesn't work
        else:
            print ("It needs a lock")

key = Key()

class Apple(Item):
    def __init__(self):
        self.name = "APPLE"
        self.description = "A shiny red apple"
    def action(self):
        print ("Do you want to eat the apple?")
        choice = input("> ")
        if choice == "yes":
            print ("You ate the apple")
            inventory.inventory.remove(apple)
        else:
            print ("Never mind")

apple = Apple()

class Lantern(Item):
    def __init__(self, is_lit):
        self.name = "LANTERN"
        self.description = "An oil-based light source"
        global lantern_is_lit
        lantern_is_lit = is_lit
    def action(self):
        print ("Light the lantern?")
        choice = input("> ")
        if "light" in choice or "yes" in choice:
            global lantern_is_lit
            lantern_is_lit = True
            print ("The lantern is lit")
        else:
            print ("Never mind")

lantern = Lantern(False)

inventory = Inventory()


class Opening(Scene):
    def enter(self):
        print ("Welcome Home, honey.")
        input(prompt)
        print ("What would you like us to call you?")
        player_name = input(user_input)
        print (("Okay, %s. Please, make yourself at home.") % player_name)
        input(prompt)
        return "lobby_intro"

class Lobby_Intro(Scene):
    def enter(self):
        print ("You are in the LOBBY.")
        print ("The door closes behind you and locks from the outside.")
        input(prompt)
        return "lobby"

class Lobby(Scene):
    def enter(self):
        print ("To your left is the KITCHEN.")
        print ("To your right is the DINING ROOM.")
        print ("Straight down is the LIVING ROOM.")
        choice = input(user_input)

        if choice.lower() == "open door":
            if key in inventory.inventory:
                print ("You've opened the front door.")
                input(prompt)
                print ("You run into out of the house")
                input(prompt)
                print ("...into the woods")
                input(prompt)
                print ("...")
                input(prompt)
                print ("...never looking back.")
                input(prompt)
                print ("THE END")
                quit()
            else:
                print ("The door is locked. I'm so sorry.")
                return "lobby"
        elif choice.lower() == "go left" or choice.lower() == "kitchen":
            return "kitchen"
        #elif choice.lower() == "go right" or choice.lower() == "dining room":
            #return "dining_room"
        elif choice.lower() == "go straight" or choice.lower() == "living room":
            return "living_room"
        elif "inventory" in choice:
            inventory.check_inventory()
            return "lobby"
        else:
            print ("I don't know what that means.")
            return "lobby"


class Shelf(Scene):
    def enter(self):
        print ("There is Kafka anthology on the shelf. Look inside?")
        shelf = input(user_input)
        if shelf == "yes":
            print ("You found a KEY!")
            inventory.add_item(key)
            input(prompt)
            return "living_room"
        else:
            return "living_room"

class Living_Room(Scene):
    def enter(self):
        if lantern_is_lit == True:
            print ("You are in the LIVING ROOM")
            input(prompt)
            print ("In the room hang lavish portraits of the dead tenants.")
            print ("You ask yourself, 'how did they die?'")
            input(prompt)
            print ("You look around and see a sparse SHELF, a robust BEAR RUG, ")
            print ("and a mahoghany COFFEE TABLE.")
            print ("It feels lonely here...")
        else:
            print ("It's dark in here...")
        choice = input(user_input)
        if lantern_is_lit == True:
            if "shelf".lower() in choice:
                return "shelf"
            elif "lobby".lower() in choice:
                return "lobby"
            elif "bear" in choice or "rug" in choice:
                print ("There is NOTHING under the rug.")
                return "living_room"
            elif "coffee" in choice or "table" in choice:
                print ("There is a copy of a newspaper from 1993.")
                news = input(user_input)
                if news == "read newspaper".lower():
                    print ("The headline reads: ")
                    print ("'FAMILY MURDER SUICIDE IN LIGHT OF SCANDAL'")
                    return "living_room"
                else:
                    return "living_room"
            else:
                return "living_room"
        if "inventory" in choice:
            inventory.check_inventory()
            return "living_room"
        elif "lobby" in choice:
            return "lobby"
        else:
            return "living_room"
class Kitchen(Scene):
    def enter(self):
        print ("You are in the KITCHEN")
        if not lantern in inventory.inventory:
            print ("On the kitchen counter is a LANTERN. Take it?")
        choice = input(user_input)
        #if not apple in inventory.inventory:
            #print ("On the kitchen counter is an APPLE. Take it?")
        if "take" in choice and not lantern in inventory.inventory:
                #inventory.add_item(apple)
                inventory.add_item(lantern)
                return "kitchen"
        elif "lobby" in choice:
            return "lobby"
        else:
            return "kitchen"


class Map(object):
    def enter(self):
        pass

    scenes = {
        'opening': Opening(),
        'lobby_intro': Lobby_Intro(),
        'lobby': Lobby(),
        'living_room': Living_Room(),
        'shelf': Shelf(),
        'kitchen': Kitchen()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def begin(self):
        return self.next_scene(self.start_scene)

a_map = Map('opening')
a_game = Engine(a_map)
a_game.play()
