# pydrop
File transfer from server to server

Requirement:

2.  On one of the servers, over the course of 10 minutes, generate 100 binary files of random sizes ranging from 1kb to 1Mb at random time intervals ranging from 1ms to 1s, encoded int16.
3.  Transfer those binary files as they are being generated from the first server to the second server over HTTP using Python's async io functionality, thereby effectively implementing data streaming from one server to the other.
<hr>
<p>Python 3.8 was used in development. To install libraries, use:</p>
<h5>pip install -r requirements.txt</h5>

~~Both servers running on development environment, production environment not available~~
LoL now there are three servers for this project. 
<h4>1. File Engine Server</h4>
<p>This server provide functionality and UI to generate the 100 required files.</p>
<p>To start this server, open a terminal and issue:</p>
<h4>FLASK_APP=engine_server flask run -p 5000</h4>
<hr>
<h4>2. Client Server</h4>
<p>This server provide functionality and UI to fetch the files generated from the first server.</p>
<p>To start this server, open a terminal and issue:</p>
<h4>FLASK_APP=client_server flask run -p 5001</h4>
<hr>
<h4>3. File Transfer Server</h4>
<p>This server only serve files</p>
<p>To start this server, open a terminal and issue:</p>
<h4>python3 file_server.py</h4>
<hr>
<h3>How to play</h3>
<h4>File server:   http://localhost:5000</h4>
<h4>Client Server: http://localhost:5001</h4>

<p>To start generate files, click the button on file server home page. The progress is indicated with the list of file generated (named by number)</p>


To start fetch files, click the button on client server home page. The progress in indicated with a list of files on file server and check mark for downloaded file.