# Created by inc0gnit0 #

# You may change the code however you want but make sure to give me credit #

# MODULES #

import qrcode

import time

import os

import random



# COLORS #

red = "\u001b[31;1m"

reset = "\u001b[0;1m"

green = "\u001b[32;1m"

cyan = "\u001b[36;1m"

yellow = "\u001b[33;1m"

magenta = "\u001b[35;1m"

blue = "\u001b[34;1m"

white = "\u001b[37;1m"

list = ["\u001b[31;1m", "\u001b[32;1m", "\u001b[36;1m", "\u001b[33;1m", "\u001b[35;1m", "\u001b[34;1m", "\u001b[37;1m"]


# MAIN #

def main():

	os.system("clear")

	# BANNER #

	time.sleep(0.1)
	print(random.choice(list) + "                                                888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                              888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                            888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                          888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                        88888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                      888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                    88888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                  888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                88888888")
	time.sleep(0.1)
	print(random.choice(list) + "    888888888888              888888888                  8888888888888")
	time.sleep(0.1)
	print(random.choice(list) + "    888888888888            888888888                    8888888888888")
	time.sleep(0.1)
	print(random.choice(list) + "    888888888888              888888888                  8888888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                  888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                    888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                      88888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                        888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                          888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                            888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                              888888888")
	time.sleep(0.1)
	print(random.choice(list) + "          88                    888888                    88   88    888888")
	time.sleep(0.1)
	print(random.choice(list) + "                               88   888                        88   88   888")
	time.sleep(0.1)
	print(random.choice(list) + "          88 88888888  888888  88  8 88  888888  88888888 88 888888 88  8 88")
	time.sleep(0.1)
	print(random.choice(list) + "          88 88    88 8        88 8  88 88    88 88    88 88   88   88 8  88")
	time.sleep(0.1)
	print(random.choice(list) + "          88 88    88 88    88 888  888 88    88 88    88 88   88   888   88")
	time.sleep(0.1)
	print(random.choice(list) + "          88 88    88  888888   888888   8888888 88    88 88   88    888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                             888")
	time.sleep(0.1)
	print(random.choice(list) + "                                         888888" + red + "                           v2.2")
	print("\033[0m")



	# VARIABLES #

	qr = qrcode.QRCode(version = 1, box_size = 30, border = 3)

	data = input(red + "                         Link Destination(ex: www.google.com): ")

	print("\n")

	name = input(green + "                         File name(without the extension): ")

	print("\n")

	qr.add_data(data)

	qr.make(fit = True)

	image = qr.make_image(fill = "black", back_color = "white")



	# PROCESS #

	image.save(name + ".png")

	print(cyan + "                         The image will be saved in the " + green + "coder " + cyan + "folder")

	print("\n")

	print(yellow + "                         Thank you for using " + green + "coder" + yellow + "!" + reset)

	print("\n")


# START #

try:
    if __name__ == "__main__":
        main()
except KeyboardInterrupt:
    print(red + "                         Exiting..." + reset)
    print("\n")
    exit(1)