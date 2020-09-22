import logging
import os

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("skill")


def evaluate(payload: dict, context: dict) -> dict:
    """
    Uses an environment variable to choose which manipulation method should be used.
    :param payload:
    :param context:
    :return:
    """

    # properties can be accessed from the context or from the system environment
    manipulation_method = os.environ.get("MANIPULATION_METHOD")

    request = payload["request"]

    if manipulation_method == "UPPER":
        return {'response': StringManipulator.upper(request)}
    elif manipulation_method == "LOWER":
        return {'response': StringManipulator.lower(request)}
    elif manipulation_method == "CAPITALIZE":
        return {'response': StringManipulator.capitalize(request)}
    raise Exception(f"'{manipulation_method}' is not a valid MANIPULATION_METHOD")


def on_started(context):
    log.info("on_started triggered with environment")
    for k, v in os.environ.items():
        print(k, v, sep="=")


class StringManipulator:
    @staticmethod
    def upper(value: str) -> str:
        if value is None:
            raise Exception("Value can not be None")
        return value.upper()

    @staticmethod
    def lower(value: str) -> str:
        if value is None:
            raise Exception("Value can not be None")
        return value.lower()

    @staticmethod
    def capitalize(value: str) -> str:
        if value is None:
            raise Exception("Value can not be None")
        return value.capitalize()
