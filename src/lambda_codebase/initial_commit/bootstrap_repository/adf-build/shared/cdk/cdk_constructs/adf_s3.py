# Copyright Amazon.com Inc. or its affiliates.
# SPDX-License-Identifier: MIT-0

"""Construct related to S3 Codepipeline Input
"""

import os

from aws_cdk import (
    aws_codepipeline as _codepipeline,
)
from constructs import Construct

from cdk_constructs.adf_codepipeline import Action

ADF_DEPLOYMENT_REGION = os.environ["AWS_REGION"]
ADF_DEPLOYMENT_ACCOUNT_ID = os.environ["ACCOUNT_ID"]
ADF_DEFAULT_BUILD_TIMEOUT = 20


class S3(Construct):
    def __init__(self, scope: Construct, id: str, map_params: dict, **kwargs): #pylint: disable=W0622
        super().__init__(scope, id, **kwargs)
        self.source = _codepipeline.CfnPipeline.StageDeclarationProperty(
            name="Source-S3",
            actions=[
                Action(
                    name="source",
                    provider="S3",
                    owner="AWS",
                    category="Source",
                    run_order=1,
                    map_params=map_params,
                    action_name="source"
                ).config
            ]
        )
