#!/usr/bin/env python3
import boto3
import json

def get_running_ec2_instances():
    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

    inventory = {
        '_meta': {'hostvars': {}}
    }

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            private_ip = instance.get('PrivateIpAddress', 'N/A')
            public_ip = instance.get('PublicIpAddress', 'N/A')

            host_entry = {
                'ansible_host': public_ip if public_ip != 'N/A' else private_ip,
                'instance_id': instance_id,
            }

            inventory[instance_id] = host_entry

    return inventory

if __name__ == "__main__":
    inventory_data = get_running_ec2_instances()
    print(json.dumps(inventory_data, indent=2))
