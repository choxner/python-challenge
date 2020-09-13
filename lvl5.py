import pickle
import pickletools
import requests

res = requests.get("http://www.pythonchallenge.com/pc/def/peak.html")
pickled_file = open("peak.p","wb")
pickle.load(res.text, pickled_file)

