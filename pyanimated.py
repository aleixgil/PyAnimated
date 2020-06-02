from sys import *
from time import *



class PyAnimated:
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


	def verticalTextAnimated(self, text, speed):
		"""Return customed text with indicated speed(sec) in vertical
		"""

		for i in text:
			print(i)
			sleep(speed)



#if __name__ == "__main__":
