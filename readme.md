Simple way to download books from Project Gutenberg and the Internetarchive.

### Use

#### 1. Download code 

--- git clone git@github.com:JohannesSeikowsky/book_downloader.git

#### 2. Ensure dependencies

--- run pip install internetarchive

--- run pip install gutenberg

#### 3. Use code

- cd book_downloader

- open main.py in text editor of your choice

- at 

- run file | python 
(using python2)

The book will be downloaded directly into the /book_downloader directory that
you're in.


### Getting identifiers of books:

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