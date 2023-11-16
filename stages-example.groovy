pipeline {
    agent any // Define el agente que ejecutará el pipeline (puede ser cualquier agente)

    stages {
        stage('Build') { // Primera etapa de Build
            steps {
                script {
                    echo 'Building the application...' // Mensaje de construcción
                    //sh 'npm install' // Comando para instalar las dependencias
                }
            }
        }

        stage('Test') { // Segunda etapa de Test
            steps {
                script {
                    echo 'Running tests...' // Mensaje de ejecución de pruebas
                    //sh 'npm test' // Comando para ejecutar pruebas
                }
            }
        }

        stage('Deploy') { // Tercera etapa de Deploy
            steps {
                script {
                    echo 'Deploying the application...' // Mensaje de despliegue
                    //sh 'npm deploy' // Comando para desplegar la aplicación
                }
            }
        }
    }
}