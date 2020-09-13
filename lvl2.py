
# Level 2 of pythonchallenge.com!
# Challenge: within the source code of this level, there is a
# set of jumbled characters. Within these characters, find the 
# letters and join them together to find the correct url.

from solution_framework import Solution

import requests
# to view source code
import re
# to use regular expressions
url_result = ""


res = requests.get("http://www.pythonchallenge.com/pc/def/ocr.html")
# import the HTML code from the site that hosts this challenge.
text_array = res.text.split("<!--")
text_to_search = text_array[2]
# select only the text that needs to be searched

regex_results = re.findall(r'\w', text_to_search)

for item in regex_results:
	if item == '_':
		pass
	else:
		url_result += item

Solution(url_result)