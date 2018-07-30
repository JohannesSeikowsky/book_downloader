""" downloading books from Project Gutenberg and Internetarchive """
import gutenberg
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
import internetarchive
from internetarchive import get_item
import shutil, os, time
from utils import write_to_file

start_time = time.time()

def get_from_gutenberg(item_title, identifier):
	""" download from Gutenberg, process content, write to file """
	text = strip_headers(load_etext(identifier)).strip()
	text = text.encode("utf-8")
	target_file = item_title + ".txt"
	write_to_file(target_file, text)

def get_from_iarchive(item_title, identifier):
	""" get item from Archive, identify target file, 
	download, move downloaded file to appropriate place """
	id = identifier
	global id
	item = get_item(id)
	# identify target file, download
	for file in item.files:
		for attr, attr_value in file.iteritems():
			if attr == "name":
				if attr_value.endswith("_djvu.txt"):
					target_file = attr_value
					item.download(target_file)
					item_title = item_title + ".txt"
					adjust_download(id, target_file, item_title)

def adjust_download(id, old_name, new_name):
	""" The internetarchive module saves each download in a dedicated directory of its own.
		We adjust by renaming and moving the downloaded file and deleting that directory. """
	download_path = id + "/" + old_name 
	shutil.move(download_path, new_name)
	os.rmdir(id)


# Project Gutenberg
# get_from_gutenberg("moby_dick", 2701)



# Internetarchive
# get_from_iarchive("great_expectations","GreatExpectations-CharlesDickens")


"""
Getting identifiers of books:
To download from Project Gutenberg and the Internetarchive respectively
you need an identifier for the book you want to download. Here's how you
get the identifier on each platform:

- Project Gutenberg
Go to Project Gutenberg. Go the the page of the book you want to download.
The identifer is a number that can be seen in the url.

- Internetarchive
Go to the Internetarchive. Go the the page of the book you want to download.
Scroll down. There's a section that shows meta-data about the book.
You want the "Identifer".
"""