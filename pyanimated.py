from sys import *
from time import *


class IntAnimated:
	"""Intro Animation Class
	"""

	def intro(self):
		"""Return intro text.
		"""

		introText = "<===== PyAnimated, your animated Python Library. =====>"

		for i in introText:
			stdout.write(i), stdout.flush()
			sleep(0.05)
			
	def textAnimated(self, text, speed):
		"""Return customed text with indicated speed(sec)
		"""

		for i in text:
			stdout.write(i), stdout.flush()
			sleep(speed)

#if __name__ == "__main__":
