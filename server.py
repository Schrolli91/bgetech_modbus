#!/usr/bin/env python3
"""
Einfacher Modbus-Server für Testzwecke.
Dieser Server simuliert ein Modbus-Gerät mit einem Register für die Seriennummer.
"""

from pyModbusTCP.server import ModbusServer, DataBank
import time

# Modbus-Server-Konfiguration
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 502

# Seriennummer als BCD-Wert (3 Register, 6 Bytes)
# Beispiel: Seriennummer "123456"
SERIAL_NUMBER_BCD = [0x0012, 0x3456, 0x0000]  # 3 Register, jeweils 16 Bit

def setup_server():
    """Konfiguriert den Modbus-Server mit den erforderlichen Registern."""
    # Server erstellen
    server = ModbusServer(host=SERVER_HOST, port=SERVER_PORT, no_block=True)
    
    # Datenbank-Instanz erstellen
    db = DataBank()
    
    # Seriennummer in die Register schreiben
    # Adresse 0x1000 (4096 in dezimal)
    db.set_holding_registers(4096, SERIAL_NUMBER_BCD)
    
    print(f"Modbus-Server läuft auf {SERVER_HOST}:{SERVER_PORT}")
    print(f"Seriennummer (BCD): {SERIAL_NUMBER_BCD}")
    print("Register-Adresse: 0x1000 (4096)")
    
    return server

def main():
    """Startet den Modbus-Server."""
    try:
        server = setup_server()
        server.start()
        
        print("Server gestartet. Drücke STRG+C, um zu beenden.")
        
        # Endlosschleife, um den Server am Laufen zu halten
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nServer wird beendet...")
        server.stop()
        print("Server beendet.")

if __name__ == "__main__":
    main()