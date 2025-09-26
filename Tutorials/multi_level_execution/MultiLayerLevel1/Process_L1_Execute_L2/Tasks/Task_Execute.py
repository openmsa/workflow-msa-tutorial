import time
from msa_sdk.variables import Variables
from msa_sdk.msa_api import MSA_API
from msa_sdk.orchestration import Orchestration
from msa_sdk import util
import json

dev_var = Variables()
context = Variables.task_call(dev_var)

ubiqube_id = context['UBIQUBEID']
async_update_list = (context['PROCESSINSTANCEID'], context['TASKID'], context['EXECNUMBER'])
header = context["input1"]

SERVICE_NAME = 'Process/Tutorials/multi_level_execution/MultiLayerLevel2/MultiLayerLevel2'
CREATE_PROCESS_NAME = 'Process/Tutorials/multi_level_execution/MultiLayerLevel2/Process_L2_Execution'

orch = Orchestration(ubiqube_id)
processes = {}
nb = int(context['nb_l2'])

for i in range(nb):
    data = dict()
    data["input1"] = f"{header}, Process L2 instance {i+1}"
    orch.execute_service(SERVICE_NAME, CREATE_PROCESS_NAME, data)
    response = json.loads(orch.content)
    process_id = response.get('processId').get('id')
    processes[process_id] = "RUNNING"
    orch.update_asynchronous_task_details(*async_update_list, f'{i} L2 running process')   

total_process = len(processes)
still_running = total_process
while processes:
  for process_id in list(processes):
    status = orch.get_process_status_by_id(process_id)
    if status != "RUNNING":  # process completed
        del processes[process_id]
  still_running = len(processes)
  orch.update_asynchronous_task_details(*async_update_list, f'{still_running} / {total_process} L1 running process')
  time.sleep(1)  # wait before next poll

MSA_API.task_success('L1 Execution Task OK', context, True)
