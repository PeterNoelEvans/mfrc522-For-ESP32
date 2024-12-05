### Changes Made:

1. Simplified the constructor to only require the SPI object, chip select, and reset pin as arguments. The SPI object should be configured outside the class to provide flexibility in using different pins and settings.
2. Removed platform-specific checks and SPI setup inside the constructor, assuming that the SPI setup will be handled externally based on the board (ESP32 or otherwise).

For the ESP32, you might find that the pin numbering and capabilities are different from the ESP8266. Here’s a generic guide to help you configure the GPIOs for the ESP32:

1. **SCK (Serial Clock)**: Typically, you can use any available GPIO that supports output. Common choices are GPIO 18 or GPIO 5.
2. **MOSI (Master Out Slave In)**: GPIO 23 is a standard choice for MOSI on the ESP32.
3. **MISO (Master In Slave Out)**: GPIO 19 is commonly used for MISO.
4. **RST (Reset)**: Any general GPIO can be used; GPIO 22 or GPIO 5 are typical choices.
5. **CS (Chip Select)**: GPIO 5 or GPIO 17 are often used for chip select.


### Running the Code:
1. Save the code in a file (e.g., `main.py`) and upload it to your ESP32.
2. Open the serial monitor to view the output.
3. Place an RFID tag near the RC522 reader, and you should see the UID of the tag printed in the serial monitor.

### Troubleshooting Tips:
- Ensure that your connections are correct and secure.
- Check the power supply; the RC522 should be powered with 3.3V.
- If you encounter issues, try using different GPIO pins for the connections.