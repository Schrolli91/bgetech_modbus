"""
TemplateDevice: Copy this file to create a new device.

Steps to add a new device:
1. Copy this file to `bgetech_modbus/devices/<your_device>.py`
2. Rename the class to match your device (e.g., `class PM100:`)
3. Adjust register addresses, scales, and units as needed
4. Add your device to `bgetech_modbus/devices/__init__.py`
5. Import and use in your code: `from bgetech_modbus.devices import PM100`

Example usage:
    config = [PM100.active_energy_import, PM100.voltage_l1_n]
    data = await client.read_data(config)
"""

from bgetech_modbus.devices.base import BaseDevice
from . import DataType, ModbusRegister


class TemplateDevice(BaseDevice):
    """
    Template for a new Modbus device.
    Copy this file and rename the class to create a new device.
    """

    # Example register: Serial Number (BCD format)
    serial_number = ModbusRegister(
        name="Serial Number",
        address=0x1000,  # <-- Adjust this address for your device
        count=3,
        data_type=DataType.BCD,
    )

    # Example register: Software Revision (UINT16)
    sw_rev = ModbusRegister(
        name="Software Revision",
        address=0x1004,  # <-- Adjust this address for your device
        count=1,
        data_type=DataType.UINT16,
    )

    # Example register: Voltage L1/N (INT32, scaled)
    voltage_l1_n = ModbusRegister(
        name="Voltage L1/N",
        address=0x0400,  # <-- Adjust this address for your device
        count=2,
        data_type=DataType.INT32,
        scale=0.001,
        unit="V",
    )

    # Example register: Active Energy Import (INT32, scaled)
    active_energy_import = ModbusRegister(
        name="Active Energy Import",
        address=0x010E,  # <-- Adjust this address for your device
        count=2,
        data_type=DataType.INT32,
        scale=0.01,
        unit="kWh",
    )

    # Add more registers as needed for your device
    # Example: active_energy_export, current_l1, etc.

    # Note: Ensure all addresses are unique and match your device's Modbus map.
