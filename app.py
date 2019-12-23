#!/usr/bin/env python3

from aws_cdk import core

from learn_cdk.learn_cdk_stack import LearnCdkStack


app = core.App()
LearnCdkStack(app, "learn-cdk")

app.synth()
