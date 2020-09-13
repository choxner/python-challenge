
# Level 0 of pythonchallenge.com!
# Challenge: within the block of letters, find a pattern that
# matches xXXXxXXXx, where there are 3 uppercase letters around
# one lowercase letter. Join the lowercase letter in the middle
# into one string.

from solution_framework import Solution

import requests
# to view source code
url_result = ""


res = requests.get("http://www.pythonchallenge.com/pc/def/equality.html")
# import the HTML code from the site that hosts this challenge.

text_array = res.text.split("<!--")
text_array = text_array[1]
# select only the text that needs to be searched

text_array = text_array.split("\n")
text_to_search = "".join(text_array)
# combine into one string

def seven_char_segment_gen(full_text):
	# use a generator to segment the text
	# this limits memory use
	for char in range(1,len(full_text)):
		# creates substrings that are a length of 9 characters
		substring = full_text[char:(char + 9)]
		if len(substring) == 9:
			yield(substring)


for segment in seven_char_segment_gen(text_to_search):
	# check for the pattern xXXXxXXXx, where there are exactly 3
	# uppercase letters around a middle letter
	if segment[1].isupper() and segment[2].isupper() and segment[3].isupper():
			if segment[-2].isupper() and segment[-3].isupper() and segment[-4].isupper():
				if segment[0].islower() and segment[4].islower() and segment[-1].islower():
					url_result += segment[4]
					# join all the middle letters to one string

Solution(url_result, lang = "php")
# the next level requires navigation to php instead of html