import argparse
from dataclasses import dataclass
from enum import Enum


class Model(Enum):
    GPT_4 = "gpt-4-turbo-preview"
    GPT_35_TURBO = "gpt-3.5-turbo"


def argparse_model_type(model_str):
    try:
        return Model[model_str.upper().replace("-", "_")]
    except KeyError:
        raise argparse.ArgumentTypeError(f"Invalid model: {model_str} .")


@dataclass
class Conversation:
    messages: list[dict]
    model: Model
