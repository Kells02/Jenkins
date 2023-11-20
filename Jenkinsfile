pipeline {
    agent any

    environment {
        client_folder = 'Prueba/'
    }

    stages {
        stage('Main') {
            steps {
                script {
                    echo "Verificando la existencia de la carpeta..."
                    if (fileExists(client_folder)) {
                        echo "La carpeta ya existe. Realizar acciones de rollback si es necesario."
                    } else {
                        echo "La carpeta no existe. Creando la carpeta..."
                        dir(client_folder) {
                            echo "Carpeta creada exitosamente."
                        }
                    }

                    stage('Debug') {
                        steps {
                            sh 'ls -R'
                        }
                    }

                }
            }
        }
    }
}