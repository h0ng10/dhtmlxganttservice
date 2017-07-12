# dhtmlxganttservice
A minimal implementation of the REST service that is used by [dhtmlxgantt](https://dhtmlx.com/docs/products/dhtmlxGantt/). Based on Python/Flask.

## Installation
Create a virutal environment (python 2.7):
```
h0ng10@linux-dev:~/development/dhtmlxganttservice$ virtualenv env
New python executable in /home/h0ng10/development/dhtmlxganttservice/env/bin/python
Installing setuptools, pip, wheel...done.
```

Activate the virtual environment:
```
h0ng10@linux-dev:~/development/dhtmlxganttservice$ source env/bin/activate
(env) h0ng10@linux-dev:~/development/dhtmlxganttservice$ pip install -r requirements.txt
``` 
Install the necessary Python packages:
```
Collecting aniso8601==1.2.1 (from -r requirements.txt (line 1))
Collecting click==6.7 (from -r requirements.txt (line 2))
  Using cached click-6.7-py2.py3-none-any.whl
Collecting Flask==0.12.2 (from -r requirements.txt (line 3))
  Using cached Flask-0.12.2-py2.py3-none-any.whl
Collecting Flask-RESTful==0.3.6 (from -r requirements.txt (line 4))
  Using cached Flask_RESTful-0.3.6-py2.py3-none-any.whl
Collecting Flask-SQLAlchemy==2.2 (from -r requirements.txt (line 5))
  Using cached Flask_SQLAlchemy-2.2-py2.py3-none-any.whl
Collecting itsdangerous==0.24 (from -r requirements.txt (line 6))
Collecting Jinja2==2.9.6 (from -r requirements.txt (line 7))
  Using cached Jinja2-2.9.6-py2.py3-none-any.whl
Collecting MarkupSafe==1.0 (from -r requirements.txt (line 8))
Collecting python-dateutil==2.6.1 (from -r requirements.txt (line 9))
  Using cached python_dateutil-2.6.1-py2.py3-none-any.whl
Collecting pytz==2017.2 (from -r requirements.txt (line 10))
  Using cached pytz-2017.2-py2.py3-none-any.whl
Collecting six==1.10.0 (from -r requirements.txt (line 11))
  Using cached six-1.10.0-py2.py3-none-any.whl
Collecting SQLAlchemy==1.1.11 (from -r requirements.txt (line 12))
Collecting Werkzeug==0.12.2 (from -r requirements.txt (line 13))
  Using cached Werkzeug-0.12.2-py2.py3-none-any.whl
Installing collected packages: six, python-dateutil, aniso8601, click, Werkzeug, MarkupSafe, Jinja2, itsdangerous, Flask, pytz, Flask-RESTful, SQLAlchemy, Flask-SQLAlchemy
Successfully installed Flask-0.12.2 Flask-RESTful-0.3.6 Flask-SQLAlchemy-2.2 Jinja2-2.9.6 MarkupSafe-1.0 SQLAlchemy-1.1.11 Werkzeug-0.12.2 aniso8601-1.2.1 click-6.7 itsdangerous-0.24 python-dateutil-2.6.1 pytz-2017.2 six-1.10.0
(env) h0ng10@linux-dev:~/development/dhtmlxganttservice$ 
```
Set the following environment variables:
```
(env) h0ng10@linux-dev:~/development/dhtmlxganttservice$ export FLASK_APP=ganttservice.py 
(env) h0ng10@linux-dev:~/development/dhtmlxganttservice$ export FLASK_DEBUG=1
```
Init the Sqlite3 database:
```
(env) h0ng10@linux-dev:~/development/dhtmlxganttservice$ flask initdb
```

Start the application
```
(env) h0ng10@linux-dev:~/development/dhtmlxganttservice$ flask run
 * Serving Flask app "ganttservice"
 * Forcing debug mode on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 613-510-496
 ```
 ## Links
 [dhtmlxgantt REST service documentation](https://docs.dhtmlx.com/gantt/desktop__server_side.html#savingdatafromrestserver)
