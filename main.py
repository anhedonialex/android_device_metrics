from ppadb.client import Client as AdbClient

import secrets


def dump_logcat(connection):
    while True:
        data = connection.read(1024)
        if not data:
            break
        print(data.decode('utf-8'))

    connection.close()

def dump_logcat_by_line(connect):
    file_obj = connect.socket.makefile()
    for index in range(0, 10):
        print("Line {}: {}".format(index, file_obj.readline().strip()))


def main():
    client = AdbClient(host="127.0.0.1", port=5037)
    print("client version", client.version())
    device = client.device(secrets.DEVICE_SERIAL)
    print(device.serial)
    print(device.shell("dumpsys battery"))




if __name__ == "__main__":
    main()