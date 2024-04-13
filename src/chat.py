import argparse
import glob
import time
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

def delete_assistant(name):
    assistants = client.beta.assistants.list()
    for assistant in assistants.data:
        if assistant.name == name:
            print(f"Deleting assistant {name}...")
            client.beta.assistants.delete(assistant_id=assistant.id)
            print(f"Assistant {name} deleted.")
            break

def create_assistant(name):
    assistant = None
    assistants = client.beta.assistants.list()
    for assistant in assistants.data:
        if assistant.name == name:
            print(f"Assistant {name} already exists.")
            return assistant

    # Step 1. Upload Knowledge
    md_files = glob.glob('knowledge/**/*.md', recursive=True)

    for file_path in md_files:
        with open(file_path, "rb") as file:
            print(f"Loading knowledge file {file.name} ...")
            response = client.files.create(file=file, purpose="assistants")

    # Step 2. Create the Assistant
    with open('behaviors/default.txt', 'r') as file:
        instructions = file.read()

    print(f"Creating assistant {name}...")
    assistant = client.beta.assistants.create(
        instructions=instructions,
        name=name,
        tools=[{"type": "code_interpreter"}, {"type": "retrieval"}],
        model="gpt-4-turbo-preview",
    )
    print(f"Assistant {name} created.")

    return assistant

def main():
    parser = argparse.ArgumentParser(description="Manage OpenAI Assistant")
    parser.add_argument('command', type=str, help='Command to execute: create, recreate')
    args = parser.parse_args()

    if args.command == 'recreate':
        delete_assistant("AI-ChatFlask-GPT")
        create_assistant("AI-ChatFlask-GPT")
    elif args.command == 'create':
        create_assistant("AI-ChatFlask-GPT")
    else:
        print("Unknown command. Use 'create' or 'recreate'.")


assistant = create_assistant("AI-ChatFlask-GPT")

def create_message(thread_id, content):
    client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=content
    )

    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant.id
    )

    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run.id,
        )
        time.sleep(0.5)

    messages = client.beta.threads.messages.list(
        thread_id=thread_id
    )

    return messages.data[0].content[0].text.value

def get_thread():
     return client.beta.threads.create()

if __name__ == "__main__":
    main()
