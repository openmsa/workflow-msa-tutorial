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

SERVICE_NAME = 'Process/Tutorials/multi_level_execution/MultiLayerLevel1/MultiLayerLevel1'
CREATE_PROCESS_NAME = 'Process/Tutorials/multi_level_execution/MultiLayerLevel1/Process_L1_Execute_L2'
processes = []

for i in range(1):
    orch = Orchestration(ubiqube_id)
    data = dict()
    data["input1"] = f"Process L1 instance {i+1}"
    orch.execute_service(SERVICE_NAME, CREATE_PROCESS_NAME, data)
    response = json.loads(orch.content)
    service_id = response.get('serviceId').get('id')
    process_id = response.get('processId').get('id')
   
    orch.update_asynchronous_task_details(*async_update_list, str(processes))   
    processes.append({"process_id": process_id, "status": "RUNNING"})

    orch.execute_service(SERVICE_NAME, CREATE_PROCESS_NAME, data)
    response = json.loads(orch.content)

still_running = True
while still_running:
    still_running = False
    for p in processes:
        if p["status"] == "RUNNING":
            orch = Orchestration(ubiqube_id)
            status = orch.get_process_status_by_id(p["process_id"])
            if status not in ["ENDED", "FAIL"]:  # process completed
                still_running = True  # at least one still running
    orch.update_asynchronous_task_details(*async_update_list, str(processes))
    time.sleep(5)  # wait before next poll

ret = MSA_API.process_content('ENDED', 'Task OK', context, True)
print(ret)

