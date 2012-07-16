from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/stop_instance", methods=["GET"])
def stop_instance():
    if request.args['api_key'] != 'testkey':
        return "BAD ARG"

    instances = {
        "instances": [{}],
        "exception_name": ""
    }

    return json.dumps(instances)


@app.route("/list_instances", methods=["GET"])
def list_instances():
    if request.args['api_key'] != 'testkey':
        return "BAD ARG"

    instances = {
        "instances": [
        {
            "instance_id": "inst_CP2WrQi2WIS4iheyAVkQYw",
            "vm_num_logical_cores": 8,
            "vm_num_physical_cores": 4,
            "winning_bid_id": "bid_X5xhotGYiGUk7_RmIqVafA",
            "vm_ram": 1429436743,
            "start_state_time": 1342108905,
            "vm_ssh_wan_ip_endpoint": "69.4.239.74:62394",
            "current_state": "Running",
            "ended_state_time": "null",
            "running_state_time": 1342108989
        }
        ],
        "exception_name": ""
    }

    return json.dumps(instances)

if __name__ == "__main__":
    app.debug = True
    app.run()
