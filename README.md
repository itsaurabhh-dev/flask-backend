# Flask Backend

Simple Flask API deployed on AWS EC2 with a Jenkins CI/CD pipeline.


Runs on port **5000**.

## Run locally
```bash
python3 -m venv venv
venv\Scripts\activate        
pip install -r requirements.txt
python app.py
```
Open http://localhost:5000/api/message


## Deploy on EC2 (manual)
```bash
git clone https://github.com/itsaurabhh-dev/flask-backend.git
cd flask-backend
python3 -m venv venv 
./venv/bin/python -m pip install -r requirements.txt
pm2 start app.py 
```

## CI/CD (Jenkins)
`Jenkinsfile` build every time there is a push in the GitHub.

Jenkins is installed on the same EC2 instance, on port 8080.
