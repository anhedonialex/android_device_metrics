import re
import builtins

import secrets


def batteryInfo(device):
    """
    Returns battery stats
    :param device:
    :return:
    """
    info = {}
    out = device.shell("dumpsys battery")
    parsed = out.split('\n')
    for line in parsed:
        info[line[:line.find(":")].strip()] = line[line.rfind(" "):].strip()
    return info

def RAMInfo(device):
    info = {}
    out = device.shell("cat /proc/meminfo")
    parsed = out.strip().split('\n')
    for line in parsed:
        info[line[:line.find(":")].strip()] = re.search("\d+", line).group(0).strip()
    return info

def uptimeInfo(device):
    info = {}
    out = device.shell("cat /proc/uptime")
    parsed = out.strip().split()
    info["total"] = parsed[0]
    info["idle"] = parsed[1]
    return info

def lookyIsUpInfo(device):
    info = {}
    out = device.shell("ps -A")
    if secrets.APP2MONITOR in out:
        info["appIsUp"] = "true"
    else:
        info["appIsUp"] = "false"
    return info

def wifiInfo(device):
    info = {}
    info["wifi"] = device.shell("dumpsys wifi | grep 'curState=ConnectedState'")
    return info

