# Created by inc0gnit0 #

# You may change the code however you have to give me credit #

# MODULES #

try:

	import qrcode

	import time

	import os

	import random

except ImportError:

	print("\u001b[31;1m" + "  You did not follow the instructions on GitHub")

	print("\n")

	print("Please run the following command: chmod +x * && sudo ./install.sh")



# COLORS #

red = "\u001b[31;1m"

reset = "\u001b[0;1m"

green = "\u001b[32;1m"

cyan = "\u001b[36;1m"

yellow = "\u001b[33;1m"

magenta = "\u001b[35;1m"

blue = "\u001b[34;1m"

white = "\u001b[37;1m"

list = ["\u001b[31;1m", "\u001b[32;1m", "\u001b[36;1m", "\u001b[33;1m", "\u001b[35;1m", "\u001b[34;1m", "\u001b[37;1m"] # List of colors to chose from #



# MAIN #

def main():

	for x in range(5): # Loading Effect #

		print(random.choice(list) + "|")

		time.sleep(0.1)

		os.system("clear")

		print(random.choice(list) + "/")

		time.sleep(0.1)

		os.system("clear")

		print(random.choice(list) + "-")

		time.sleep(0.1)

		os.system("clear")

		print(random.choice(list) + "\\")

		time.sleep(0.1)


	os.system("clear") # Clear the terminal #

	# BANNER #

	print("\n")
	print(random.choice(list) + "                                https://github.com/iinc0gnit0/coder")
	print("\n")
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
	print(random.choice(list) + "                                         888888" + red + "                           v2.8")
	time.sleep(0.1)
	print("\n")
	print(random.choice(list) + "                                     Created by: inc0gnit0")
	time.sleep(0.1)
	print("\n")
	print(random.choice(list) + "                                     GitHub: iinc0gnit0")
	time.sleep(0.1)
	print("\n")
	print(random.choice(list) + "                                     Email: iinc0gnit0@pm.me")
	time.sleep(0.1)
	print("\n")
	print(random.choice(list) + "                                     Instagram: i.nc0gnit0")
	time.sleep(0.1)
	print("\n\033[0m")



	# VARIABLES #

	qr = qrcode.QRCode(version = 1, box_size = 30, border = 3) # QRCode variable #

	data = input(random.choice(list) + "                         Link Destination(ex: www.google.com): ") # Link destination of QRCode #

	print("\n")

	name = input(random.choice(list) + "                         File name(without the extension): ") # File name #

	print("\n")

	qr.add_data(data) # Add data to QRCode #

	qr.make(fit = True) # Make the QRCode fit #

	image = qr.make_image(fill = "black", back_color = "white") # QRCode color(You can experiment with this) #

	path = os.getcwd() # Get path #



	# PROCESS #

	image.save(name + ".png") # Saving image #

	print(random.choice(list) + "                         The image will be saved to " + random.choice(list) + path + random.choice(list) + "/" + name + ".png") 

	print("\n")

	print(random.choice(list) + "                         Thank you for using " + random.choice(list) + "coder" + random.choice(list) + "!" + reset)

	print("\n")



# START #

try:

    if __name__ == "__main__":

        main()

except KeyboardInterrupt:

    print(random.choice(list) + "\n \n                         Exiting..." + reset)

    print("\n")

    exit(1)