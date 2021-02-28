class Custom():
    '''
    everything not implemented (like snapshot features) can be created with this class

    if you need to add the workspace name in the content, set `${WORKSPACE}` to replace this to the workspace

    if you need to create a new workspace, give this class to the datapack, if not give this class to the workspace

    example :
    {'folders_to_add':[
        '${WORKSPACE}/mysupercustomfeature'
    ], 'files_to_modify':[
        '${WORKSPACE}/mysupercustomfeature/mysupercustomfile.json': [{'supercode': 'you can see, this is a super code !'}]
    ]}
    '''
    def __init__(self, content: dict):
        self.content = content
