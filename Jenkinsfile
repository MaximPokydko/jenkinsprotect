pipeline {
    agent any

    parameters {
        choice(
            name: 'ENV',
            choices: ['dev', 'prod'],
            description: 'Choose environment'
        )
    }

    stages {

        stage('Clone') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/MaximPokydko/jenkinsprotect.git'
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying to ${params.ENV}"

                sshPublisher(
                    publishers: [
                        sshPublisherDesc(
                            configName: 'myserver',
                            transfers: [
                                sshTransfer(
                                    sourceFiles: '**/*',
                                    removePrefix: '',
                                    remoteDirectory: "deploy/${params.ENV}"
                                )
                            ],
                            verbose: true
                        )
                    ]
                )
            }
        }

        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }
    }
}
