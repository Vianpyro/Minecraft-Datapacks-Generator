class Predicate():
	def __init__(self, predicate_name: str, entity: str = 'this', condition= 'minecraft:entity_properties'):
		self.name = predicate_name
		self.entity = entity
		self.condition = condition
		self.predicate = {'condition': condition,'entity': entity, 'predicate': None}

	def set_template(self, template: str, needed: bool = True):
		'''
		list of template :

		is_sneaking
		'''

		if template == 'is_sneaking':
			self.predicate['predicate'] = { 'flags': { 'is_sneaking': needed}}
		if template == 'is_sprinting':
			self.predicate['predicate'] = { 'flags': { 'is_sprinting': needed}}

	def set_raw(self, raw: dict):
		self.predicate = raw
