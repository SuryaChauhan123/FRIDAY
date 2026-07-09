from LLM.llm import extract_intent
from LLM.command_splitter import command_splitter
from Router.router import execute

while True:
    user = input("You: ")
    if user.lower()=='close':  
        break

    tasks=command_splitter(user)
    print(tasks)
    for task in tasks:
        intent=extract_intent(task)
        print(intent)
        execute(intent,task)

