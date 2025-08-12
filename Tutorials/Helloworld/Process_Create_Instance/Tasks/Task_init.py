from msa_sdk.variables import Variables
from msa_sdk.msa_api import MSA_API
from msa_sdk.orchestration import Orchestration
import json

dev_var = Variables()
dev_var.add('name', var_type='String')
context = Variables.task_call(dev_var)


ret = MSA_API.process_content('ENDED', 'Task OK', context, True)
print(ret)

