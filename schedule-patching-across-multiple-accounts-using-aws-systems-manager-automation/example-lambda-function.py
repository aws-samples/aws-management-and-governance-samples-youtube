import boto3
import os
import uuid

client = boto3.client('ssm')

def lambda_handler(event,context):
    response = client.start_automation_execution(
        DocumentName='<AUTOMATION-DOCUMENT-NAME>',
            
        Parameters={
            'AutomationAssumeRole':['arn:aws:iam::<ACCOUNT-ID>:role/AWS-SystemsManager-AutomationAdministrationRole'],
            'ResourceGroupName' : ['<RESOURCE-GROUP-NAME'],
            'Operation' : ['Scan'] ,
            'RebootOption' : ['NoReboot'] ,
            #'InstallOverrideList' : [''] ,
            'SnapshotId' : [str(uuid.uuid4())]
        },
        TargetLocations=[
            {
                'Accounts': ['<ACCOUNT-ID-1>','<ACCOUNT-ID-2>','<ACCOUNT-ID-3>'],
                'Regions': ['<REGION-1>','<REGION-2>'],
                'TargetLocationMaxConcurrency': '10%',
                'TargetLocationMaxErrors': '10%',
                'ExecutionRoleName': 'AWS-SystemsManager-AutomationExecutionRole'
            }
        ]
    )
    print(response)