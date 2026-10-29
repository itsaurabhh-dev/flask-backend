pipeline {
    agent any
    triggers { githubPush() }                 // GitHub webhook trigger
    // environment { API_KEY = credentials('api-key') }   // optional: secret from Jenkins credentials
    stages {
        stage('Pull Code') {
            steps { checkout scm }
        }
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps { sh './venv/bin/python -m unittest test_app.py -v' }
        }
        stage('Deploy') {
            steps {
                withEnv(['JENKINS_NODE_COOKIE=dontKillMe']) {
                    sh 'pm2 delete flask-backend || true'
                    sh 'pm2 start app.py --name flask-backend --interpreter ./venv/bin/python'
                    sh 'pm2 save'
                }
            }
        }
    }
}
