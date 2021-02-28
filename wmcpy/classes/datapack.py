from os import mkdir
from shutil import rmtree
from json import dump


class Datapack_json():
	'''
	example:
```py
datapack = Datapack_json({'ref':{
	'name':'mysuperdatapack',
	'description':'mysuperdatapack',
	'version': 6
    },
	'content':{
		'mysuperworkspace':{
			'functions':{
				'mysuperfunction.mcfunction':[
					'execute run execute run execute run execute run execute run say hey it\\'s me, the super code!'
				]
			},
			'predicates':{
				'sneak.json':{
					'condition': 'minecraft:entity_properties',
					'entity': 'this', 'predicate': {'flags':{'is_sneaking': True}}
				}
			
			}
		}
	}
})
	'''
	def __init__(self, data: dict):
		self.data = data
		self.name = data['ref']['name']
		self.description = data['ref']['description']
		self.version = data['ref']['version']

	def build(self, force, path):
		try:
			mkdir(path + '/' + self.name)
		except FileExistsError:
			if force:
				rmtree(path + '/' + self.name)
				mkdir(path + '/' + self.name)
			else:
				raise FileExistsError('dir early exist with this path, add force=True to the function to ignore this error and to delete the dir to re-create it')
		mkdir(path + '/' + self.name + '/data')
		data_path = path + '/' + self.name + '/data/'
		for workspace in self.data['content']:
			mkdir(data_path + workspace)
			for dir in self.data['content'][workspace]:
				mkdir(data_path + workspace + '/' + dir)
				for file in self.data['content'][workspace][dir]:
					if isinstance(self.data['content'][workspace][dir][file], dict):
						dump(self.data['content'][workspace][dir][file], open(data_path + workspace + '/' + dir, 'w+'), indent=4)
					elif isinstance(self.data['content'][workspace][dir][file], list):
						f = open(data_path + workspace + '/' + dir, 'w+')
						for line in self.data['content'][workspace][dir][file]:
							f.write(self.data['content'][workspace][dir][file][line])
						f.close()
					else:
						open(data_path + workspace + '/' + dir, 'w+').write(self.data['content'][workspace][dir][file])