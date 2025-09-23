import json
from msa_sdk.variables import Variables
from msa_sdk.msa_api import MSA_API
from msa_sdk.order import Order
from msa_sdk import util


# List all the parameters required by the task
dev_var = Variables()
dev_var.add('id')
dev_var.add('icmp')
dev_var.add('src_ip')
dev_var.add('dst_port')
context = Variables.task_call(dev_var)
process_id = context['SERVICEINSTANCEID']

devices = context['devices']
for device in devices:  
  # extract the database ID
  device_db_id = device['id'][3:]

  if context['icmp'] == 'true':
    context['dst_port'] = 'null'
  else:
    dst_port = context['dst_port']
    if not util.is_valid_port(dst_port):
      MSA_API.task_failure(f'Invalid port number {dst_port}', context)

  # build the Microservice JSON params for the CREATE
  micro_service_vars_array = {"object_id": context['id'],
                              "src_ip": context['src_ip'],
                              "dst_port": context['dst_port']
                              }
  object_id = context['id']

  simple_firewall = {"simple_firewall": {object_id: micro_service_vars_array}}

  # call the CREATE for simple_firewall MS for each device
  order = Order(device_db_id)
  order.command_execute('CREATE', simple_firewall)

  # convert dict object into json
  content = json.loads(order.content)

  # check if the response is OK
  if order.response.ok:
    if 'rules' in context.keys():
      num = len(context['rules'])
    else:
      context['rules'] = {}
      num = 0

    context['rules'][num] = {}
    context['rules'][num]['delete'] = False
    context['rules'][num]['id'] = context['id']
    context['rules'][num]['src_ip'] = context['src_ip']
    context['rules'][num]['dst_port'] = context['dst_port']

    MSA_API.task_success(f'STATUS: {content["status"]}, MESSAGE: {content["message"]}', context)
  else:
    MSA_API.task_failure(f'Policy update failed - {order.content}', context)
