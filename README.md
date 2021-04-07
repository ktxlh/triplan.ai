# yum-travel-planner


## First Time Setup

1. (Backend) Setup python virtual environment

under ./yum-travel-planner/
```
python -m venv venv
source venv/bin/activate
```

2. (Backend) Install required python packages
```
pip install -r requirements.txt
```
Also add python package to the requirement list after adding new module by
``` 
pip freeze > requirements.txt
```

3. (Backend) Run Flask
```
flask run
```