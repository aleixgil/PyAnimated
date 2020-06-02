from sys import stdout
from time import sleep

class PyAnimated:
	"""
	Intro Animation Class
	"""
	
	def intro(self):
		"""
		Prints the intro text.
		"""
		self.textAnimated("<===== PyAnimated, your animated Python Library. =====>", 0.05)

	def _outputText(self, text, speed, newLine):
		"""
		Prints the given text with the indicated speed (sec) and appends a new line if needed.
		"""
		for i in text:
			stdout.write(f"{i}{'\n' if newLine else ''}")
	     		stdout.flush()
			sleep(speed)

	def textAnimated(self, text, speed):
		"""
		Prints the given text with the indicated speed(sec)
		"""
		self._outputText(text, speed, false)

	def verticalTextAnimated(self, text, speed):
		"""
		Prints the given text with the indicated speed(sec) in vertical
		"""
		self._outputText(text, speed, true)
