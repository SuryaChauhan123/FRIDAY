from Features.openapp import openapp
from Features.closeapp import closeapp
from Features.tellTimeAndDate import telltime
from Features.tellTimeAndDate import telldate
from Features.searchweb import searchweb
from Features.controlvolume import control_volume
from LLM.chat import chat


def execute(task,user):
    if task['intent'].lower()=='open_app':
        openapp(task['app_name'])
        # speak(openapp(task['app_name']))
    elif task['intent'].lower()=='tell_time':
        telltime()
    elif task['intent'].lower()=='tell_date':
        telldate()
    elif task['intent'].lower()=='chat':
        print(f"FRIDAY: {chat(user)}")
    elif task['intent'].lower()=='search_web':
        searchweb(task['query'])
    elif task['intent'].lower()=='control_volume':
        control_volume(task['value'])
    else:
        print("We are working on that feature yet :<")