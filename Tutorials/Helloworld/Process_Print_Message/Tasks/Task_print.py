from msa_sdk.variables import Variables
from msa_sdk.msa_api import MSA_API

dev_var = Variables()
context = Variables.task_call(dev_var)


name= context.get('name')
ret = MSA_API.process_content('ENDED', f'Task OK:{name}', context, True)
print(ret)

