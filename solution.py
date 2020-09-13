
# This file sets up the Solution class to be used to solve the problems
# found on www.pythonchallenge.com. Once, a solution has been found, run 
# the class as Solution(extension). Upon initialization, the Solution 
# class will open the resulting url in whatever browser is open or your 
# default browser. 

import webbrowser

class Solution():
	def __init__ (self, extension):
		self.base_url = "http://www.pythonchallenge.com/pc/def/{}.html"
		self.extension = extension
		webbrowser.open(self.base_url.format(extension))

	def __str__ (self):
		print("Input the extension string that you would like to add to the url.")