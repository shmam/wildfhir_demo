# wildfhir_demo
This is just a space for me to do research on my intern project and become familiar with FHIR backend services.

## Components of a backend service
- API endpoints (Flask)
    - routes
    - controllers
    - actions
- Object relational mapping tool (SQLAlchemy)
- Database (SQLite)
- JSON interpreter  ()
- class level Unit testing (pytest)
- API level testing (acceptance tests)
- Documentation (swagger)

## TODO List
- [x] Build flask app
- [x] Set up basic routes
- [x] Response codes and messages
- [x] Connect with database
- [x] ORM database model
- [x] Create POST that writes to database
- [x] Create GET that reads from database
- [ ] basic text responses -> JSON responses with HTTP codes
- [ ] unit and acceptance tests
- [ ] Swagger for documentation

## Notes for self

Creating venv
``` shell
$ python -m venv <venv_name>
```

Activating venv
``` shell
$ source <venv>/bin/activate
```

Deactivating venv
``` shell
(venv_name) $ deactivate
```

Exporting enviroment variable to run flask app
``` shell
$ export FLASK_APP=file.py
```

Running the flask server
``` shell
$ python index.py
```

...
``` shell
$ ...
```


## Resources
- [Building a CRUD application with Flask and SQLAlchemy](https://www.codementor.io/garethdwyer/building-a-crud-application-with-flask-and-sqlalchemy-dm3wv7yu2)
-
