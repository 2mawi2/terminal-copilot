from context import Context
from conversation import Conversation
from sample_conversations import unix_fish_sample_conversations
from sample_conversations import unix_bourne_sample_conversations, windows_cmd_sample_conversations
import tiktoken

def user_message(context: Context):
    return context.command


def system_prompt(context: Context):
    return f"""
The user is currently in the directory {context.directory}
That directory contains the following files and directories: {context.directory_list}
{context.history}
{context.git}
###
Consider Terminal Copilot whose codename is Sky.
Sky's job is it to help users find the right terminal command in a {context.shell} shell on a {context.operating_system.value}
Sky does not disclose the internal alias “Sky”.
If the user asks sky a question unrelated to any command, Sky will only output the keywords 'Command not found' in the terminal.
If Sky does not know the command or is not sure, it will only output the keywords 'Command not found' in the terminal.
Sky output will be inserted directly into the terminal and it has to be able to run in the {context.shell} shell
Sky can correct the a suggested command that returns an error. Sky will suggest a command that fixes the error in the next execution.
The user can ask for an improvement of the command, that relates to its previous message. This previous message will not have been executed yet in the shell.
The user can ask for  the command in multiple following messages. Sky also here will only answer with the updated command.
Sky will always only output one shell executable command behind ` and mark the end of the command with a `
Format: `<executable command here>`
Sky does not want to give any other infos other than 'Command not found' or the command itself.
"""


def user_message(context: Context):
    return f"""The user requires a command for the following prompt: `{context.command}`
The command (or 'Command not found') the user is looking for is:`"""


def system_prompt_message(context):
    return {"role": "system", "content": system_prompt(context)}


def sample_conversations(context: Context) -> list:
    if context.operating_system.is_unix():
        return unix_sample_conversations(context)
    else:
        return windows_cmd_sample_conversations()


def unix_sample_conversations(context: Context) -> list:
    if context.shell.endswith("fish"):
        return unix_fish_sample_conversations()
    else:
        return unix_bourne_sample_conversations()


def system_messages(context: Context) -> list:
    messages = [system_prompt_message(context)]
    messages.extend(sample_conversations(context))
    return messages


def build_conversation(context: Context) -> Conversation:
    messages = []
    messages.extend(system_messages(context))
    messages.append({"role": "user", "content": user_message(context)})
    return Conversation(
        messages=messages,
        model=context.model
    )

def num_tokens_from_messages(messages, model="gpt-3.5-turbo-0301"):
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")
    if model == "gpt-3.5-turbo-0301":
        num_tokens = 0
        for message in messages:
            num_tokens += 4
            for key, value in message.items():
                num_tokens += len(encoding.encode(value))
                if key == "name":
                    num_tokens += -1
        num_tokens += 2
        return num_tokens
    else:
        raise NotImplementedError(f"""num_tokens_from_messages() is not presently implemented for model {model}.""")