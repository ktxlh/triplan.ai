# Triplan.ai
![](https://i.imgur.com/Tsu9xSw.png)

The travel industry faces challenges during pandemic years, so it is an important issue to reraise the public's willingness to travel. We will address this problem by revolutionizing the current travel agent business model with a customized recommendation system.  

Since there are existing problems in the current travel business, we expect customized traveling packages can further increase the demand. When consumers need an idea of where to travel, they resort to finding travel packages with discounts. However, travel packages in the market are mostly arranged based on the travel agency’s own cooperative companies‘ interests, and thus they involve some unfavorable shopping itineraries. Besides, consumers might have their own thoughts of detailed preferences or specifications, which is hard to cover in a general traveling package. Also, an automatic recommendation system is easy to scale up in production compared to manual planning, and we can utilize a wide range of online data resources to improve our prediction. Hence, we conclude that we can establish businesses by producing personalized travel plans.

We propose a new traveling agent business by deploying an AI-based application that customized travel packages to users. The application detects users' past usage habits and generates traveling spot candidates. To imitate an experienced travel scheduler and auto-generate a favorable schedule, we consider several spot properties and customized the evaluation criteria for finding the optimal itinerary. Our user interface allows users to indicate numerous preferences of their trip, such as time, price level, and the ratio of outdoor activities. After receiving a recommendation, users can also adjust the recommended schedule or select other places in the recommendation alternatives list.

Our business model targets at three types of customers. The application will be freemium to the public. Each user can make one plan per month for free, and the premium users enjoy unlimited access and other features. The travel agent companies can buy our enterprise plan which can evaluate the publicly trending travel preferences. The system can provide precise advice based on the data acquired by users who consented to provide. After the application gains its popularity, we will cooperate with some restaurants and promote their business via the platform. Users can download discount coupons by making travel plans on our application. This would be a win-win-win situation for the entire travel industry.


**Plan your next trip with [Triplan.ai](http://triplan-ai.herokuapp.com/)!**

**Demo** (click to watch the video on youtube):

[![Triplan.ai Demo Video](http://img.youtube.com/vi/1WqmcVN2O5g/0.jpg)](http://www.youtube.com/watch?v=1WqmcVN2O5g "Triplan.ai Demo Video")

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
