## Schedule Patching Across Multiple Accounts Using AWS Systems Manager Automation

Watch this video on YouTube: [Schedule Patching Across Multiple Accounts Using AWS Systems Manager Automation](https://www.youtube.com/watch?v=dcJDvoUfboA&list=PLhr1KZpdzukcaA06WloeNmGlnM_f1LrdP)

This video contains three sample files.

* example-multi-account-automation-patching-document.json
* example-lambda-iam-policy.json
* example-lambda-function.py

The first file, ```example-multi-account-automation-patching-document.yaml```, is shown in the video at [2:54](https://youtu.be/dcJDvoUfboA?list=PLhr1KZpdzukcaA06WloeNmGlnM_f1LrdP&t=174). This is an example Automation document that initiates a Run Command task for ```AWS-RunPatchBaseline``` against the targeted resource group.

The second file, ```example-lambda-iam-policy.json```, is shown in the video at [3:36]https://youtu.be/dcJDvoUfboA?list=PLhr1KZpdzukcaA06WloeNmGlnM_f1LrdP&t=216). This is an example IAM policy for the AWS Lambda function that grants permissions to intiate the multi-account and multi-Region Automation patching operation.

The third file, ```example-lambda-function.py```, is shown in the video at [5:17](https://youtu.be/dcJDvoUfboA?list=PLhr1KZpdzukcaA06WloeNmGlnM_f1LrdP&t=317). This is an example Lambda function that starts the multi-account and multi-Region Automation patching operation.

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

