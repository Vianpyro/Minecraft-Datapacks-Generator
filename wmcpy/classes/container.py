from .block_nbt import Block_nbt
from .item import Item

containers = {'chest': 26, 'trapped_chest': 26, 'dispenser': 8, 'furnace': 2, 'brewing_stand': 4, 'hopper': 4, 'dropper': 8, 'shulker_box': 26, 'barrel': 26, 'smoker': 2, 'blast_furnace':  2, 'campfire': 3, 'soul_campfire': 3, 'lectern': 0}

class Container():
    def __init__(self, block: Block_nbt) -> None:
        if not block.block_type in containers:
            raise NameError('this block type is not suported')
        else:
            self.block = block
            self.items = {}
            self.new_nbt = block.nbt

    def add_item(self, item: Item, slot: int):
        if slot >= containers[self.block.block_type] + 1: raise ValueError('this item slot is to big, see in minecraft the numbers of them (from 0)')
        self.new_nbt['Items'].append(item.data_form)

    @property
    def block_form(self):
        return self.block.block_type + str(self.new_nbt)

    @property
    def give_form(self):
        new_nbt = self.new_nbt
        new_nbt['id'] = 'minecraft:' + self.item_name
        return self.block.block_type + {'BlockEntityTag': new_nbt}