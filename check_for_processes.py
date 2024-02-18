import json

processes2monitor = []
with open('processes2monitor.json') as f:
    processes2monitor = json.load(f)
def isAllUp(processes):
    global processes2monitor
    for process in processes2monitor:
        #Тут используется списковая сборка и сравнение строк
        if not any([process in p for p in processes]):
            return False
    return True

