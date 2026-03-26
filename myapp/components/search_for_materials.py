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
    
    def search(self):
        item_det = randint(0, 4)  # Determine rarity of found item
        if item_det < 4:
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
