
# This file sets up the Solution class to be used to solve the problems
# found on www.pythonchallenge.com. Once, a solution has been found, run 
# the class as Solution(extension). Upon initialization, the Solution 
# class will open the resulting url in whatever browser is open or your 
# default browser. 

import webbrowser
# allows this .py file to interact with your browser

class Solution():
	def __init__ (self, ext, lang = "html"):
		# original values are assigned

		self.base_url = "http://www.pythonchallenge.com/pc/def/{}.{}"
		# sets base url to be modified
		
		self.extension = ext
		self.language = lang
		
		webbrowser.open(self.base_url.format(self.extension, self.language),new=0)
		# adds the extensions to the base url

	def __str__ (self):
		print("Input the extension string that you would like to add to the url.")
		# prints a message in case Solution is printed instead of called