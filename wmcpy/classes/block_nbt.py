class Block_nbt():
	'''
	this feature will enable you to return the nbt of an tile entity / block with an nbt
	'''

	def __init__(self, block_type: str = 'chest', **opts):
		block_type = block_type.replace('minecraft:', '')
		self.block_type = block_type
		block_type_opt = {'chest':{'Items': [], 'id': 'minecraft:chest'}}
		new_opts = {}
		try:
			placeholder = block_type_opt[block_type]
			del placeholder
		except:
			print(block_type + ' is an unkwown block type, so we can\'t help you to get the block nbt')
		for opt_key in block_type_opt[block_type]:
			new_opts[opt_key] = block_type_opt[block_type][opt_key]
		for opt_key in opts:
			new_opts[opt_key] = opts[opt_key]
		self.nbt = new_opts
		self.modifyed = False

	def set_value(self, json_value: dict):
		self.nbt = json_value
		self.modifyed = True

	def __str__(self) -> str:
		if not self.modifyed: return self.block_type
		else: tr = self.block_type + str(self.nbt); return tr