from LLM.llm import extract_intent
from Router.router import execute
while True:
    user = input("You: ")
    if user.lower()=='close':  
        break

    tasks=extract_intent(user)
    print(tasks)
    for task in tasks:
        execute(task,user)

