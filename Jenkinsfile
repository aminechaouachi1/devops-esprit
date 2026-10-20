pipeline {
    agent any

    environment {
        SONAR_PROJECT_KEY = 'devops-esprit'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Prepare Python') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    python -m pip install --upgrade pip
                    pip install -r app/requirements.txt
                '''
            }
        }

        stage('Tests') {
            steps {
                sh '''
                    . .venv/bin/activate
                    python -m pytest -v app/test_app.py
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'SonarScanner'

                    withSonarQubeEnv('SonarQube') {
                        sh "\"${scannerHome}/bin/sonar-scanner\""
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished. Check the stage results.'
        }
    }
}