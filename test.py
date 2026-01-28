import asyncio
import time


from bgetech_modbus.client import BGEtechClient
from bgetech_modbus.devices import DS100, TemplateDevice


async def main():

    print("Starting BGEtech Modbus Client Test...\n")
    # DS100 Client
    client_ds100 = BGEtechClient(host="127.0.0.1", port=502, device_id=1)
    await client_ds100.connect()

    config_ds100 = [DS100.serial_number]

    while True:
        time.sleep(3)

        data_ds100 = await client_ds100.read_data(config_ds100)

        print("DS100 Data:")
        for entry in data_ds100:
            print(f"{entry.name}: {entry.value} {entry.unit}")
            print(f"Last received: {entry.last_received}")
            print(f"[{entry.address}, {entry.count}, {entry.data_type.value}]")
            print()

    client_ds100.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nExit!")
