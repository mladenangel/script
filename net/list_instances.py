#!/usr/bin/env pythonimport boto3ec2 = boto3.resource('ec2') for instance
# delwin
print(instance.id, instance.state)

