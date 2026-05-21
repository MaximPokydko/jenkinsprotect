pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                echo 'Repo cloned'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t mini-ci-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker rm -f mini-ci-app || true'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker run -d \
                  --name mini-ci-app \
                  -p 8080:8000 \
                  mini-ci-app
                '''
            }
        }

        stage('Check') {
            steps {
                sh '''
                sleep 3
                docker ps
                curl http://localhost:8080/health || true
                '''
            }
        }
    }

    post {
        always {
            deleteDir()
        }
    }
}
