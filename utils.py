""" supporting utilities """

def write_to_file(target_file, text):
	with open(target_file, "w") as f:
		f.write(text)