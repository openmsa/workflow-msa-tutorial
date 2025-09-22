from msa_sdk.variables import Variables
from msa_sdk.msa_api import MSA_API
import time
from msa_sdk import util


dev_var = Variables()
context = Variables.task_call(dev_var)

time.sleep(20)

MSA_API.task_success('L2 Execution Task OK', context, True)