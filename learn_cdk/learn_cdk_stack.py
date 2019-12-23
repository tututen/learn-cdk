from aws_cdk import core
from aws_cdk.core import Duration
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_apigateway as _apigw


class LearnCdkStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        handler = _lambda.Function(
            self,
            "demo_func",
            runtime=_lambda.Runtime.PYTHON_3_7,
            handler="demo_func.handler",
            timeout=Duration.minutes(1),  # pylint: disable=E1120
            code=_lambda.Code.asset("lambda_code/demo_func"),  # pylint: disable=E1120
        )

        api_gw = _apigw.RestApi(
            self, "ApiGatewayForSlack", rest_api_name="gw_for_slack"
        )

        exam_entity = api_gw.root.add_resource("test")
        exam_entity_lambda_integration = _apigw.LambdaIntegration(
            handler, proxy=False, integration_responses=[{"statusCode": "200"}],
        )
        exam_entity.add_method(
            "GET",
            exam_entity_lambda_integration,
            method_responses=[{"statusCode": "200"}],
        )

