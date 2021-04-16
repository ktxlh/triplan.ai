# triplan.ai
![](https://i.imgur.com/Tsu9xSw.png)

You can find the `triplan.ai` demo [here](http://triplan-ai.herokuapp.com/).

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

4. (Frontend) Install Nodejs if not yet installed from https://nodejs.org/en/

5. (Frontend) Go to /frontend and install required frontend modules
```
npm install
```

6. (Frontend) Run React
```
npm start
```
You can also refer to readme under /frontend/
