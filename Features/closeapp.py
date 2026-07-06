import psutil

def closeapp(target_name):
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'].lower() == target_name.lower():
                proc.terminate()
                print("terminated ",proc.info['name'])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
