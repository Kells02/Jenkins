pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                script {
                    dir('https://github.com/Kells02/Jenkins.git') {
                        git branch: 'main',
                        credentialsId: 'jenkinsgit',
                        url: 'https://github.com/Kells02/Jenkins.git'
                    }
                }
            }
        }

        stage('Create Folder') {
            steps {
                script {
                    dir('https://github.com/Kells02/Jenkins.git') {
                        if (!fileExists('Prueba')) {
                            sh 'mkdir Prueba'
                        } else {
                            echo 'La carpeta ya existe.'
                        }
                    }
                }
            }
        }

        stage('Debug') {
            steps {
                script {
                    dir('https://github.com/Kells02/Jenkins.git') {
                        sh 'ls -R'
                    }
                }
            }
        }
    }
}
