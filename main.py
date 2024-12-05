from machine import Pin, SPI
import mfrc522

sck = Pin(18, Pin.OUT)
mosi = Pin(23, Pin.OUT)
miso = Pin(19, Pin.IN)
rst = Pin(22, Pin.OUT)
cs = Pin(5, Pin.OUT)

spi = SPI(baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)
rdr = mfrc522.MFRC522(spi, cs, rst)

def do_read():
    print("Place card before reader to read")
    try:
        while True:
            (stat, tag_type) = rdr.request(rdr.REQIDL)
            if stat == rdr.OK:
                (stat, raw_uid) = rdr.anticoll()
                if stat == rdr.OK:
                    print("Card detected %s" % raw_uid)
                    if rdr.select_tag(raw_uid) == rdr.OK:
                        key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
                        if rdr.auth(rdr.AUTHENT1A, 8, key, raw_uid) == rdr.OK:
                            print("Address 8 data: %s" % rdr.read(8))
                            rdr.stop_crypto1()
                        else:
                            print("Authentication error")
                    else:
                        print("Failed to select tag")
    except KeyboardInterrupt:
        print("Bye")

def do_write():
    print("Place card before reader to write")
    try:
        while True:
            (stat, tag_type) = rdr.request(rdr.REQIDL)
            if stat == rdr.OK:
                (stat, raw_uid) = rdr.anticoll()
                if stat == rdr.OK:
                    print("Card detected %s" % raw_uid)
                    if rdr.select_tag(raw_uid) == rdr.OK:
                        key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
                        if rdr.auth(rdr.AUTHENT1A, 8, key, raw_uid) == rdr.OK:
                            data = bytearray([0xFF] * 16)
                            rdr.write(8, data)
                            print("Data written to card")
                            rdr.stop_crypto1()
                        else:
                            print("Authentication error")
                    else:
                        print("Failed to select tag")
    except KeyboardInterrupt:
        print("Bye")
