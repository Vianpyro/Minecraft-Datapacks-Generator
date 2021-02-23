class Item():
    def __init__(self, item_name:str, tag: dict = None, count= 64):
        self.item_name = item_name.replace('minecraft:', '', 1)
        self.tag = tag
        self.count = count
    
    @property
    def data_form(self) -> dict:
        return {'id': 'minecraft:' + self.item_name, 'Count': self.count, 'tag': self.tag}
    
    @property
    def give_form(self) -> str:
        return self.item_name + str(self.tag) + ' ' + self.count