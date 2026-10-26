from aws_cdk import (
    Stack,
    RemovalPolicy,
    aws_s3 as s3,
)
from constructs import Construct


class CdkTaskStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # simple s3 bucket
        bucket = s3.Bucket(
            self,
            "LaxmanDemoBucket",
            bucket_name="laxman-demo-bucket-updated-590852515231",
            versioned=True,
            removal_policy=RemovalPolicy.DESTROY,   
            auto_delete_objects=True,               
            encryption=s3.BucketEncryption.S3_MANAGED,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
        )
