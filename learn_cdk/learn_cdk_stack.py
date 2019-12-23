from aws_cdk import core
from aws_cdk import aws_lambda as _lambda


class LearnCdkStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        _lambda.Function(
            self,
            "demo_func",
            runtime=_lambda.Runtime.PYTHON_3_7,
            handler="demo_func.handler",
            code=_lambda.Code.asset("lambda_code/demo_func"),  # pylint: disable=E1120
        )

