# xgboost-web-app




Front end: A user interface, a browser. This is created using flask 



## Backend: ML model

Train model
```
python3 -m venv env
source env/bin/activate

cd files_for_training_model
python train.py
```



## Frontend: Flask Application
A typical Flask app looks like this.
```
my-flask-app
   ├── static/              <-contains assets used by the templates
   │   └── css/
   │       └── main.css
   ├── templates/
   │   ├── index.html
   │   └── student.html
   ├── data.py
   └── students.py
```
Test locally
```
python app.py
Check http://127.0.0.1:5000 on browser. 127.0.0.1 is the local host IP. 5000 is the port the Flask app is running on.
```
Deploy on heroku
The Current python runtime is 3.9.14, which is supported by heroku. This is specified in `runtime.txt`. The two other files needed are `Procfile` amd `requirements.txt`.

Resource
Flask: https://cs.wellesley.edu/~cs304/lectures/flask/flask.html