# pydrop
File transfer from server to server

Requirement:

2.  On one of the servers, over the course of 10 minutes, generate 100 binary files of random sizes ranging from 1kb to 1Mb at random time intervals ranging from 1ms to 1s, encoded int16.
3.  Transfer those binary files as they are being generated from the first server to the second server over HTTP using Python's async io functionality, thereby effectively implementing data streaming from one server to the other.


Both servers running on development environment, production environment not available

Python 3.8 was used in development
To install libraries, use:

pip install -r requirements.txt

To start, open two terminal and issue the two cmd

File Server:
FLASK_APP=engine_server flask run -p 5000

Client Server:
FLASK_APP=client_server flask run -p 5001


Then, open browser, open two tabs with

File server:   http://localhost:5000
Client Server: http://localhost:5001


To start generate files, click the button on file server home page. The progress is indicated with the list of file generated (named by number)

To start fetch files, click the button on client server home page. The progress in indicated with a list of files on file server and check mark for downloaded file.