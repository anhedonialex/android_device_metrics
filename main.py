from ppadb.client import Client as AdbClient

import check_for_processes
import getmetrics_pc
import getmetrics_phone
import secrets
import telegram


def dump_logcat(connection):
    while True:
        data = connection.read(1024)
        if not data:
            break
        print(data.decode('utf-8'))

    connection.close()



def main():
    try:
        client = AdbClient(host="127.0.0.1", port=5037)
        print("client version", client.version())
        device = client.device(secrets.DEVICE_SERIAL)
    except AttributeError as e:
        telegram.bot_sendtext(f"<МОНИТОР>\nНе конектит adb\n{e}")
    try:
        battery = getmetrics_phone.batteryInfo(device)
        if battery["USB powered"] != 'true':
            telegram.bot_sendtext(f"<МОНИТОР>\nНе заряжается\n")
        if int(battery["level"]) <= 80:
            telegram.bot_sendtext(f"<МОНИТОР>\nБатарея разряжается\n{battery['level']}%")
    except:
        pass
    try:
        if "curState=ConnectedState" not in getmetrics_phone.wifiInfo(device)["wifi"]:
            telegram.bot_sendtext(f"<МОНИТОР>\nОтвалился Wifi")
    except:
        pass
    try:
        if not check_for_processes.isAllUp(getmetrics_pc.processesInfo()):
            telegram.bot_sendtext(f"<МОНИТОР>\nНа компе не запущены нужные процессы")
    except Exception as e2:
        print(e2)


if __name__ == "__main__":
    main()