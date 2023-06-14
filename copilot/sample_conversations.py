def requirement_template(prompt):
    return prompt
    return f"""The user requires a command for the following prompt: `{prompt}`. The executable command (or 'Command not found') the user is looking for is:`"""


def improvement_template(prompt):
    return prompt
    return f"""The user requires and improvement of the last suggested and not yet executed command with the following prompt: `{prompt}`. The executable command the user is looking for is:`"""


def unix_sample_conversations():
    return [
        {"role": "system", "name": "example_user", "content": requirement_template("list files in directory")},
        {"role": "system", "name": "example_assistant", "content": "ls -la"},
        {"role": "system", "name": "example_user", "content": requirement_template("list all branches")},
        {"role": "system", "name": "example_assistant", "content": "git branch -a"},
        {"role": "system", "name": "example_user",
         "content": requirement_template("find all txt and wav files in the home directory")},
        {"role": "system", "name": "example_assistant", "content": "find . -name \"*.txt\" -o -name \"*.wav\""},
        {"role": "system", "name": "example_user", "content": improvement_template("I meant mp4 files not wav files")},
        {"role": "system", "name": "example_assistant", "content": "find . -name \"*.txt\" -o -name \"*.mp4\""},
        {"role": "system", "name": "example_user",
         "content": requirement_template("google GPT and write the results into Excel")},
        {"role": "system", "name": "example_assistant", "content": "Command not found"},
    ]


def unix_bourne_sample_conversations():
    shared_conversations = unix_sample_conversations()
    specific_conversations = [
        {"role": "system", "name": "example_user", "content": requirement_template("update [yyyy] [name of owner]")},
        {"role": "system", "name": "example_assistant",
         "content": """sed -i '' 's/\[yyyy\] \[name of owner\]/2023 Copilot/g'"""},
        {"role": "system", "name": "example_user",
         "content": requirement_template("update [yyyy] [name of owner]")},
        {"role": "system", "name": "example_assistant",
         "content": """sed -i '' 's/\[yyyy\] \[name of owner\]/2023 Copilot/g' LICENSE"""},
        {"role": "system", "name": "example_user",
         "content": requirement_template("output in a loop all numbers from 1 to 5")},
        {"role": "system", "name": "example_assistant", "content": "for i in {1..5}; do echo $i; done"},
    ]

    return shared_conversations + specific_conversations


def unix_fish_sample_conversations():
    shared_conversations = unix_sample_conversations()
    specific_conversations = [
        {"role": "system", "name": "example_user",
         "content": requirement_template("update Copyright [yyyy] [name of copyright owner]")},
        {"role": "system", "name": "example_assistant",
         "content": "sed -i '' 's/\[yyyy\] \[name of owner\]/2023 Copilot/g'`"},
        {"role": "system", "name": "example_user",
         "content": requirement_template("sed: -I or -i may not be used with stdin")},
        {"role": "system", "name": "example_assistant",
         "content": "sed -i '' 's/\[yyyy\] \[name of owner\]/2023 Copilot/g' LICENSE`"},
        {"role": "system", "name": "example_user",
         "content": requirement_template("set and export an environment variable in Fish shell")},
        {"role": "system", "name": "example_assistant",
         "content": "set -gx MY_VARIABLE \"example_value\"`"},
        {"role": "system", "name": "example_user",
         "content": requirement_template("output in a loop all numbers from 1 to 5")},
        {"role": "system", "name": "example_assistant",
         "content": "for i in (seq 1 5); echo $i; end`"},
    ]

    return shared_conversations + specific_conversations


def windows_cmd_sample_conversations():
    return [
        {"role": "system", "name": "example_user", "content": "list files in directory"},
        {"role": "system", "name": "example_assistant", "content": "dir"},
        {"role": "system", "name": "example_user", "content": "list all branches"},
        {"role": "system", "name": "example_assistant", "content": "git branch -a"},
        {"role": "system", "name": "example_user", "content": "find all txt and wav files in the current directory"},
        {"role": "system", "name": "example_assistant", "content": "dir /b /s *.txt *.wav"},
        {"role": "system", "name": "example_user", "content": "I meant mp4 files not wav files"},
        {"role": "system", "name": "example_assistant", "content": "dir /b /s *.txt *.mp4"},
        {"role": "system", "name": "example_user", "content": "google GPT and write the results into Excel"},
        {"role": "system", "name": "example_assistant", "content": "Command not found"},
        {"role": "system", "name": "example_user", "content": "update Copyright [yyyy] [name of copyright owner]"},
        {"role": "system", "name": "example_assistant", "content": "Command not found"},
        {"role": "system", "name": "example_user", "content": "FILENAME: No such file or directory"},
        {"role": "system", "name": "example_assistant", "content": "Command not found"}
    ]


def windows_cmd_sample_conversations_with_template():
    return [
        {"role": "system", "name": "example_user", "content": requirement_template("list files in directory")},
        {"role": "system", "name": "example_assistant", "content": "dir"},
        {"role": "system", "name": "example_user", "content": requirement_template("list all branches")},
        {"role": "system", "name": "example_assistant", "content": "git branch -a"},
        {"role": "system", "name": "example_user",
         "content": requirement_template("find all txt and wav files in the current directory")},
        {"role": "system", "name": "example_assistant", "content": "dir /b /s *.txt *.wav"},
        {"role": "system", "name": "example_user", "content": improvement_template("I meant mp4 files not wav files")},
        {"role": "system", "name": "example_assistant", "content": "dir /b /s *.txt *.mp4"},
        {"role": "system", "name": "example_user",
         "content": requirement_template("google GPT and write the results into Excel")},
        {"role": "system", "name": "example_assistant", "content": "Command not found"},
        {"role": "system", "name": "example_user", "content": requirement_template("update [yyyy] [name of owner]")},
        {"role": "system", "name": "example_assistant", "content": "Command not found"},
        {"role": "system", "name": "example_user",
         "content": requirement_template("FILENAME: No such file or directory")},
        {"role": "system", "name": "example_assistant", "content": "Command not found"}
    ]
