from json import loads

class Predicate():
	def __init__(self, predicate_name: str, entity: str = 'this', condition= 'minecraft:entity_properties'):
		self.name = predicate_name
		self.predicate = {'condition': condition,'entity': entity, 'predicate': None}

	def set_raw(self, raw: dict):
		self.predicate = raw
		return self
