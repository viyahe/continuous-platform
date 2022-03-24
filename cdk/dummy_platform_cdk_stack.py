from aws_cdk import core
from aws_cdk.aws_dynamodb import Attribute, AttributeType, StreamViewType, Table
from aws_cdk.aws_lambda import StartingPosition
from aws_cdk.aws_lambda_event_sources import DynamoEventSource

from viyahe_platform import BaseDynamoDbCdkStack, PlatformCdkStack


class DummyDynamoDbCdkStack(BaseDynamoDbCdkStack):
    """DynamoDB Stack for dummy platform."""

    def __init__(self, scope: core.Construct, **kwargs) -> None:
        super().__init__(scope, **kwargs)
        pkAttribute = Attribute(name='PK', type=AttributeType.STRING)
        skAttribute = Attribute(name='SK', type=AttributeType.STRING)
        self.table = Table(
            self,
            'table',
            table_name=self.table_name,
            partition_key=pkAttribute,
            sort_key=skAttribute,
            stream=StreamViewType.NEW_AND_OLD_IMAGES,
        )

class DummyPlatformCdkStack(PlatformCdkStack):
    def __init__(self, scope: core.Construct, dynamodb_stack: DummyDynamoDbCdkStack, **kwargs) -> None:
        super().__init__(scope, dynamodb_stack=dynamodb_stack, **kwargs)

        ddb_stream_event_source = DynamoEventSource(
            self.dynamodb_stack.table, starting_position=StartingPosition.TRIM_HORIZON
        )