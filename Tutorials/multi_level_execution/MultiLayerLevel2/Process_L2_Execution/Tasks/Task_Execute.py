from msa_sdk.variables import Variables
from msa_sdk.msa_api import MSA_API
import time


dev_var = Variables()
context = Variables.task_call(dev_var)

time.sleep(20)

task_success('L2 Execution Task OK', context, True)