import re
import builtins
import secrets
import psutil

def appiumInfo():
    processes = [proc.name() for proc in psutil.process_iter()]
    return processes