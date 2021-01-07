## Schedule Patching Across Multiple Accounts Using AWS Systems Manager Automation

Watch this video on YouTube: [Schedule Patching Across Multiple Accounts Using AWS Systems Manager Automation](https://www.youtube.com/watch?v=dcJDvoUfboA&list=PLhr1KZpdzukcaA06WloeNmGlnM_f1LrdP)

Timestamp | File Name  | Description
------------- | ------------- | -------------
[2:54](https://youtu.be/dcJDvoUfboA?list=PLhr1KZpdzukcaA06WloeNmGlnM_f1LrdP&t=174) | [```example-multi-account-automation-patching-document.yaml```](https://github.com/aws-samples/aws-management-and-governance-samples-youtube/blob/main/schedule-patching-across-multiple-accounts-using-aws-systems-manager-automation/example-multi-account-automation-patching-document.yaml) | An example Automation document that initiates a Run Command task for ```AWS-RunPatchBaseline``` against the targeted resource group.
[3:36](https://youtu.be/dcJDvoUfboA?list=PLhr1KZpdzukcaA06WloeNmGlnM_f1LrdP&t=216) | [```example-lambda-iam-policy.json```](https://github.com/aws-samples/aws-management-and-governance-samples-youtube/blob/main/schedule-patching-across-multiple-accounts-using-aws-systems-manager-automation/example-lambda-iam-policy.json) | An example IAM policy for the AWS Lambda function that grants permissions to intiate the multi-account and multi-Region Automation patching operation.
[5:17](https://youtu.be/dcJDvoUfboA?list=PLhr1KZpdzukcaA06WloeNmGlnM_f1LrdP&t=317) | [```example-lambda-function.py```](https://github.com/aws-samples/aws-management-and-governance-samples-youtube/blob/main/schedule-patching-across-multiple-accounts-using-aws-systems-manager-automation/example-lambda-function.py) | An example Lambda function that starts the multi-account and multi-Region Automation patching operation.

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

