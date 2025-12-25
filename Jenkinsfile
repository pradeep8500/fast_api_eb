pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/pradeep8500/fast_api_eb.git'
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -e .
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest -v
                '''
            }
        }

        stage('Code Quality') {
            steps {
                sh '''
                . venv/bin/activate
                pylint main.py || true
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                docker build -t fastapi-app .
                '''
            }
        }

        stage('Docker Run') {
            steps {
                sh '''
                docker stop fastapi || true
                docker rm fastapi || true
                docker run -d -p 8000:8000 --name fastapi fastapi-app
                '''
            }
        }
    }
}

