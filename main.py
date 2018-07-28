
""" 
Downloading a book from Gutenberg-proj and Internetarchive. 

The two main functions are "get_from_gutenberg" and "get_from_iarchive".
Each function has to be called with 2 arguments: 
   1. The title of the book as you want it (e.g. "moby_dick")
   2. A unqiue identifier of the book which you have to get online from the gutenberg-proj/interneratchive.

Getting unique identifiers:
- Gutenberg-proj - go to page of the book you want - the identifier is a number that you can find in the url.
- Internetarchive - go to page of the book you want - the identifier is on that page in the data section (scroll down), referenced as "identifier".
"""

import gutenberg
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
import internetarchive
from internetarchive import get_item
import shutil, os


""" Downloading from Project Gutenberg """
def get_from_gutenberg(item_title, item_id):
	text = strip_headers(load_etext(item_id)).strip()
	text = text.encode("utf-8")
	title = item_title + ".txt"
	write_to_file(title, text)

def write_to_file(target_file, content):
	with open(target_file, "w") as f:
		f.write(content)

""" Downloading from Internetarchive """
def get_from_iarchive(item_title, item_id):
	id = item_id
	global id
	item = get_item(id)
	# identify the file to download, then download
	for file in item.files:
		for key, val in file.iteritems():
			if key == "name":
				if val.endswith("_djvu.txt"):
					file_name = val
					item.download(file_name)
					new_name = item_title + ".txt"
					adjust_download(id, file_name, new_name)

def adjust_download(id, file_name, new_name):
	download_path = id + "/" + file_name 
	shutil.move(download_path, new_name)
	os.rmdir(id)

get_from_gutenberg("excurions", 9846)
# get_from_iarchive("great expectations","GreatExpectations-CharlesDickens")
