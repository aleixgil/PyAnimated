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

if __name__ == "__main__":
    doctest.testmod()