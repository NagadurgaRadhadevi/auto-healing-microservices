import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    instance_id = 'i-xxxxxxxxxxxxxxxx'  # Replace with your EC2 instance ID
    ec2.reboot_instances(InstanceIds=[instance_id])
    return 'Instance reboot triggered'
