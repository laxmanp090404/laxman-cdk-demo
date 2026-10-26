import aws_cdk as cdk
from constructs import Construct
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep

class MyPipelineStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipeline =  CodePipeline(self, "Pipeline",
                        pipeline_name="LaxmanDemoPipeline",
                        synth=ShellStep("Synth",
                            input=CodePipelineSource.git_hub("laxmanp090404/laxman-cdk-demo", "main",
                                                             authentication=cdk.SecretValue.secrets_manager("laxman-github-token")),
                            commands=["npm install -g aws-cdk",
                                "python -m pip install -r requirements.txt",
                                "cdk synth"]
                        )
                    )