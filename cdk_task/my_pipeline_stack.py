import aws_cdk as cdk
from constructs import Construct
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
from cdk_task.my_pipeline_app_stage import MyPipelineAppStage
class MyPipelineStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipeline =  CodePipeline(self, "Pipeline",
                        pipeline_name="LaxmanDemoPipeline",
                        synth=ShellStep("Synth",
                            input=CodePipelineSource.connection("laxmanp090404/laxman-cdk-demo", "main",
                                                          connection_arn="arn:aws:codeconnections:us-east-1:590852515231:connection/0ea19336-ff8b-49aa-92e7-11dfcc1c60d1" ),
                            commands=["npm install -g aws-cdk",
                                "python -m pip install -r requirements.txt",
                                "cdk synth"]
                        )
                    )
        pipeline.add_stage(MyPipelineAppStage(self, "test",
            env=cdk.Environment(account="590852515231", region="us-east-1")))