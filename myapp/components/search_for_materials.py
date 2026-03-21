from django_unicorn.components import UnicornView
from random import randint

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

    item_det = randint(0, 5)  # Determine rarity of found item
    if item_det < 4:
        common_item_id = randint(0, 4)
        if common_item_id == 0:

    else:
    
