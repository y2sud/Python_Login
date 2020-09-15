# Python_Login

This is a simple UI to register user, and login/logout users using Python. This is not a production app, this is just a simple application for those who want to learn Login using Python.

Start web server:

1. Create conda env using env_py37.yml and activate it
  > conda env create -f env_py37.yml
  
  > conda activate py37

2. Goto the folder containing Python_Login in command prompt and -->
  > set FLASK_APP=Python_Login

  > set FLASK_DEBUG=1

3. Start the web server
  > flask run

4. Goto browser and open 127.0.0.1:5000

That's it!

Note: I'm using MySQL db on AWS cloud. You need to setup your own MySQL - on your local machine, cloud or anywhere and change details in below file -

Model.py:

  -- host (db server ip)
  
  -- db (database name)
  
  -- user (user id that has access to MySQL db)
  
  -- encrypted password --> this needs to be generated using cryp.py --> put your password on line 28 and see the encrypted text from print statement on line 29.

I used MySQL workbench to connect to db server and create tables. Also attached are DDL statements fro MySQL.
