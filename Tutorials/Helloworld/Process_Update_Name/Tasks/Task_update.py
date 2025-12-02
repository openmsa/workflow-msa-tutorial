from msa_sdk.variables import Variables
from msa_sdk.msa_api import MSA_API

dev_var = Variables()
dev_var.add('name', var_type='String')
context = Variables.task_call(dev_var)

ubiqube_id = context['UBIQUBEID']
name = context.get('name')

context.update(name=name)

MSA_API.task_success('Task OK', context)
