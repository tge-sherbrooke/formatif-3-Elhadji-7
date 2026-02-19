# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "adafruit-circuitpython-ahtx0",
#     "adafruit-circuitpython-vcnl4200",
#     "adafruit-blinka",
#     "rpi-gpio",
# ]
# ///
"""Lecture multi-capteurs AHT20 + VCNL4200 via I2C."""

import board
import adafruit_ahtx0
import adafruit_vcnl4200
import time

def main():
    try:
        # Initialisation unique du bus I2C partagé
        i2c = board.I2C()
        
        # Création des objets capteurs
        aht = adafruit_ahtx0.AHTx0(i2c)
        vcnl = adafruit_vcnl4200.Adafruit_VCNL4200(i2c)

        print("=== Station IoT Multi-Capteurs ===")
        # Lecture AHT20
        print(f"Température : {aht.temperature:.1f} C")
        print(f"Humidité    : {aht.relative_humidity:.1f} %RH")
        
        # Lecture VCNL4200
        print(f"Proximité   : {vcnl.proximity}")
        print(f"Lumière     : {vcnl.lux:.1f} lux")
        print("================================")

    except Exception as e:
        print(f"Erreur lors de la lecture : {e}")

if __name__ == "__main__":
    main()
