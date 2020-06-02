import doctest
from sys import *
from time import *


class IntAnimated:
	"""Intro Animation Class
	"""

	def intro(self):
		"""Return intro text.
		>>> IntAnimated().intro()
		"""

		introText = "<===== PyAnimated, your animated Python Library. =====>"

		for i in introText:
			stdout.write(i), stdout.flush()
			sleep(0.01)

	def textAnimated(self, text, speed):
			"""Return customed text with indicated speed(sec)
			>>> IntAnimated().textAnimated("Hello world! Hello world! Hello world!", 0.01)
			"""

			for i in text:
				stdout.write(i), stdout.flush()
				sleep(speed)

if __name__ == "__main__":
    doctest.testmod()