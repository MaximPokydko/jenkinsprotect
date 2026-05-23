pipeline {
    agent any

    parameters {
        choice(
            name: 'ENV',
            choices: ['dev', 'prod'],
            description: 'Environment'
        )
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/MaximPokydko/jenkinsprotect.git'
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying to ${params.ENV}"
            }
        }

        stage('Auto Deploy Info') {
            steps {
                echo "Auto deploy triggered by SCM change"
            }
        }

        stage('Clean') {
            steps {
                deleteDir()
            }
        }
    }
}
