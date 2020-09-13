
# Level 4 of pythonchallenge.com!
# Challenge: from the source code, find the pattern that the 
# url should end in /linkedlist.php?nothing=_____. Starting at 
# nothing = 12345, loop through by scraping each site until
# you find a site that breaks the pattern. The text on this
# page is the solution.
# Warning: This one takes a littl over a minute to run because 
# it is scraping hundreds of websites!

from solution_framework import Solution
import requests

res = requests.get("http://www.pythonchallenge.com/pc/def/linkedlist.php")
# print(res)
# find the base url
lvl4_base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}"

nothing = "12345"
nothing_string = "and the next nothing is "
# string values

for iterator in range(1,400):
	# comments within the page source file say to not go 
	# past 400, to prevent any indefinite looping
	new_res = requests.get(lvl4_base_url.format(nothing))
	if new_res.text.find(nothing_string) == -1:
		# if the text differs from the pattern, break from 
		# the loop
		break
	else:
		nothing = new_res.text.replace(nothing_string, "")
		# remove the noise

extension = new_res.text.split(".html")[0]
# remove ".html" at the end

Solution(extension)
