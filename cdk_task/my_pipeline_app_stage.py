import aws_cdk as cdk
from constructs import Construct
from cdk_task.my_pipeline_lambda_stack import MyLambdaStack
from cdk_task.cdk_task_stack import CdkTaskStack


class MyPipelineAppStage(cdk.Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambdaStack = MyLambdaStack(self, "LambdaStack")
        s3Stack = CdkTaskStack(self, "S3Stack")