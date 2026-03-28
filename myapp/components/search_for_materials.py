from django_unicorn.components import UnicornView
from random import randint

# Useful comments to remember
# git commit -am "comment"
# git push origin master

class SearchForMaterialsView(UnicornView):

    rocks = 0  # Declare all materials, sorted in common, rare, and the berry
    leaves = 0
    twigs = 0
    bird_eggs = 0
    antlers = 0

    beetles = 0
    quartz = 0
    frog_legs = 0

    the_berry = 0
    
    potion_crafted = False

    elixir_crafted = False
    
    def search(self):
        item_det = randint(0, 5)  # Determine rarity of found item
        if item_det < 5:
            common_item_id = randint(0, 4)  # Determine which common item
            if common_item_id == 0:
                self.rocks += 1
            elif common_item_id == 1:
                self.leaves += 1
            elif common_item_id == 2:
                self.twigs += 1
            elif common_item_id == 3:
                self.bird_eggs += 1
            else:
                self.antlers += 1
        else:
            rare_item_id = randint(0, 2)  # Determine which rare item
            if rare_item_id == 0:
                self.beetles += 1
            elif rare_item_id == 1:
                self.quartz += 1
            else:
                self.frog_legs += 1

    def craft_potion(self):   # Craft potion needed for the berry
        if self.rocks != 0 and self.leaves != 0 and self.twigs != 0 and self.bird_eggs != 0 and self.antlers != 0 and self.beetles != 0 and self.quartz != 0 and self.frog_legs != 0: 
            self.rocks -= 1
            self.leaves -= 1
            self.twigs -= 1
            self.bird_eggs -= 1
            self.antlers -= 1

            self.beetles -= 1
            self.quartz -= 1
            self.frog_legs -= 1

            self.potion_crafted = True

    def include_berry(self):
        if self.potion_crafted == True:
            item_det = randint(0, 19)  # Determine rarity of found item
            if item_det < 15:
                common_item_id = randint(0, 4)  # Determine which common item
                if common_item_id == 0:
                    self.rocks += 1
                elif common_item_id == 1:
                    self.leaves += 1
                elif common_item_id == 2:
                    self.twigs += 1
                elif common_item_id == 3:
                    self.bird_eggs += 1
                else:
                    self.antlers += 1
            elif item_det >= 15 and item_det < 19:
                rare_item_id = randint(0, 2)  # Determine which rare item
                if rare_item_id == 0:
                    self.beetles += 1
                elif rare_item_id == 1:
                    self.quartz += 1
                else:
                    self.frog_legs += 1
            else:  # Include The Berry in the pool of discoverable items
                self.the_berry += 1

    def craft_elixir(self):   # Remove required amount of ingredients and finish the game
        if self.rocks >= 3 and self.leaves >= 3 and self.twigs >= 3 and self.bird_eggs >= 3 and self.antlers >= 3 and self.beetles >= 3 and self.quartz >= 3 and self.frog_legs >=3 and self.beetles >= 3 and self.quartz >= 3 and self.frog_legs >= 3 and self.the_berry != 0:
            self.rocks -= 3
            self.leaves -= 3
            self.twigs -= 3
            self.bird_eggs -= 3
            self.antlers -= 3

            self.beetles -= 3
            self.quartz -= 3
            self.frog_legs -= 3

            self.the_berry -= 1

            self.elixir_crafted = True