#!/usr/bin/env python3

from aws_cdk import core
from cdk import DummyDynamoDbCdkStack, DummyPlatformCdkStack


app = core.App()
dynamodb_stack = DummyDynamoDbCdkStack(app)
DummyPlatformCdkStack(app, dynamodb_stack=dynamodb_stack)
app.synth()
