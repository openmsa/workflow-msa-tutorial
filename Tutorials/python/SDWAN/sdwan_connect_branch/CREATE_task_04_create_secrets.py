from msa_sdk.variables import Variables
from msa_sdk.msa_api import MSA_API
from msa_sdk.order import Order


dev_var = Variables()
context = Variables.task_call()

# (2) secrets
try:
    order = Order(context["left_device_id"])
    order.command_execute("CREATE", context["sdwan_ipsec_secret_left"])
except Exception as e:
    MSA_API.task_error(f'ERROR: {str(e)}', context)

try:
    order = Order(context["right_device_id"])
    order.command_execute('CREATE', context["sdwan_ipsec_secret_right"])
except Exception as e:
    MSA_API.task_error(f'ERROR: {str(e)}', context)


MSA_API.task_success(f'Secrets Created.', context)
