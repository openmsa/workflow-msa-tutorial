from msa_sdk.variables import Variables
from msa_sdk.msa_api import MSA_API

dev_var = Variables()
context = Variables.task_call()

MSA_API.task_success(f'Firewall service deleted', context)
