# MODULES #

import qrcode

from time import sleep

import os



# COLORS #

red = "\u001b[31;1m"

reset = "\u001b[0;1m"

green = "\u001b[32;1m"

cyan = "\u001b[36;1m"

yellow = "\u001b[33;1m"


# MAIN #
def main():
	
	# VARIABLES #

	os.system("clear")

	qr = qrcode.QRCode(version = 1, box_size = 30, border = 3)

	data = input(red + "  Link Destination(ex: www.google.com): ")

	print("\n")

	name = input(green + "  File name(without the extension): ")

	print("\n")

	qr.add_data(data)

	qr.make(fit = True)

	image = qr.make_image(fill = "black", back_color = "white")



	# PROCESS #

	image.save(name + ".png")

	print(cyan + "  The image will be saved in the " + green + "coder " + cyan + "folder")

	print("\n")

	print(yellow + "  Thank you for using " + green + "coder" + yellow + "!" + reset)

	print("\n")


# START #

try:
    if __name__ == "__main__":
        main()
except KeyboardInterrupt:
    print(red + "  Exiting..." + reset)
    print("\n")
    exit(1)