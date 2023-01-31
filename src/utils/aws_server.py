import asyncio
import datetime
import json
import os

import boto3
from botocore.exceptions import ClientError

file = os.path.join(".devcontainer", "config.json")
with open(file) as f:
    aws_config = json.load(f)["aws"]

INSTANCE_ID = aws_config["server_instance_id"]

async def instances_switch(action):
    action = action.upper()
    ec2 = boto3.client('ec2')

    if action == 'ON':
        # Do a dryrun first to verify permissions
        try:
            ec2.start_instances(InstanceIds=[INSTANCE_ID], DryRun=True)

        except ClientError as e:
            if 'DryRunOperation' not in str(e):
                raise
        # Dry run succeeded, run start_instances without dryrun
        try:
            waiter = ec2.get_waiter('instance_running')
            ec2.start_instances(InstanceIds=[INSTANCE_ID], DryRun=False)

            print(F"{datetime.datetime.now()}: Instance Starting...")
            waiter.wait(InstanceIds=[INSTANCE_ID])
            message = "Ready"
            print(F"{datetime.datetime.now()}: Instance {message}")

            response = ec2.describe_instances(InstanceIds=[INSTANCE_ID])
            public_ip = response["Reservations"][0]["Instances"][0]["PublicIpAddress"]

            return message, public_ip

        except ClientError as e:
            print(e)

    elif action == 'OFF':
        # Do a dryrun first to verify permissions
        try:
            ec2.stop_instances(InstanceIds=[INSTANCE_ID], DryRun=True)

        except ClientError as e:
            if 'DryRunOperation' not in str(e):
                raise

        # Dry run succeeded, call stop_instances without dryrun
        try:
            waiter = ec2.get_waiter('instance_stopped')
            ec2.stop_instances(InstanceIds=[INSTANCE_ID], DryRun=False)

            print(F"{datetime.datetime.now()}: Instance Stoping...")
            waiter.wait(InstanceIds=[INSTANCE_ID])
            message = "Stopped"
            print(F"{datetime.datetime.now()}: Instance {message}")

            return message

        except ClientError as e:
            print(e)

if __name__ == "__main__":
    async def main():
        print(await instances_switch("off"))

    asyncio.run(main())  

# Refer
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/ec2-example-managing-instances.html
# https://docs.python.org/ja/3.8/library/asyncio-task.html