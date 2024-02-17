from ppadb.client import Client as AdbClient
import getmetrics_phone
import secrets


def dump_logcat(connection):
    while True:
        data = connection.read(1024)
        if not data:
            break
        print(data.decode('utf-8'))

    connection.close()



def main():
    client = AdbClient(host="127.0.0.1", port=5037)
    print("client version", client.version())
    device = client.device(secrets.DEVICE_SERIAL)
    print(getmetrics_phone.batteryInfo(device))
    print(getmetrics_phone.RAMInfo(device))
    print(getmetrics_phone.uptimeInfo(device))
    print(getmetrics_phone.lookyIsUpInfo(device))



if __name__ == "__main__":
    main()