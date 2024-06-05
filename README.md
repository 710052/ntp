# Raspberry NTP Server Atomic Clock
NTP Server for Raspberry Pi and Waveshare e-paper e-ink display

![display](docs/display.jpg)

## Hardware

### Platform

* Raspberry Pi Zero W
* Raspberry Pi 3b+
* Raspberry Pi 4
* Any other modern RPi

### Supported displays

* Waveshare eInk types:
  * epd2in13v2
  * epd2in13v3
  * epd2in13bv3
  * epd2in7
  * epd3in7
* Virtual (picture)

## Installation

1. Turn on SPI via `sudo raspi-config`
    ```
    Interfacing Options -> SPI
   ```
2. Install dependencies
    ```
    sudo apt update
    sudo apt-get install python3-pip python3-pil python3-numpy git
    pip3 install RPi.GPIO spidev
    ```

3. Install drivers for your display
    1. If you have a Waveshare display
    ```
    git clone https://github.com/waveshare/e-Paper.git ~/e-Paper
    pip3 install ~/e-Paper/RaspberryPi_JetsonNano/python/
    ```
4. Download NTP Atomic Clock
    ```
    git clone https://github.com/710052/ntp.git ~/ntp
    ```
5. Run it
    ```
    python3 ~/ntp/main.py
    ```
