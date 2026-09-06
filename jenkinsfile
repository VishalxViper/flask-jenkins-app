pipeline {

    agent any

    stages {

        stage('Create Environment') {
            steps {
                sh '''
                python3 -m venv flask-env
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                flask-env/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Test Flask App') {
            steps {
                sh '''
                flask-env/bin/python -m py_compile app.py
                '''
            }
        }

        stage('Run Flask App') {
            steps {
                sh '''
                nohup flask-env/bin/python app.py &
                '''
            }
        }
    }
}
