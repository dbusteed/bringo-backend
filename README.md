# bringo backend
### (to be used with [bringo-frontend](https://github.com/dbusteed/bringo-backend))

## quickstart

clone the repo
```
git clone https://github.com/dbusteed/bringo-backend
cd bringo-backend
```

set up virtual enviroment
```
virtualenv -p python3.6 venv
source venv/bin/activate
pip3 install -r requirements.txt
```

prepare the database and start
```
python3 manage.py migrate
python3 manage.py shell < scripts/load_test_data.py
python3 manage.py runserver
```

the backend will start on `localhost:8000`. you can view the API views by going to `/api/boards` and any other urls found in `urls.py`. run the React frontend (link above) at the same time for the full bringo experience

## other
this was my first time making something with React + Django Rest Framework, so things are kinda messy