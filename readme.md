Simple way to download books from Project Gutenberg and the Internetarchive.

Use:

1. Download code 
--- In command-line: git@github.com:JohannesSeikowsky/book_downloader.git

2. Ensure dependencies
--- pip install internetarchive
--- pip install gutenberg
--- Install Python 2.7 (If you don't have it)

3. Navigate to /book_downloader directory on cmd-line.
4. Open main.py, comment out the relevant example code,
fill in the book title you want to donwload and that books identifier.
5. run programme as you normally woud. (python main.py in cmd-line)

The book will be downloaded directly into the /book_downloader directory
you're in.


Getting identifiers:
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