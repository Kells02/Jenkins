pipeline {
    agent any

    stages {
        stage('Main') {
            steps {
                script {
                    def client_folder = 'Prueba/'

                    dir(client_folder) {
                        echo "Verificando la existencia de la carpeta..."
                        if (sh(script: "test -d $client_folder", returnStatus: true) == 0) {
                            echo "La carpeta ya existe. Realizar acciones de rollback si es necesario."
                        } else {
                            echo "La carpeta no existe. Creando la carpeta..."
                            sh "mkdir $client_folder"
                            echo "Carpeta creada exitosamente."
                        }
                    }
                }
            }
        }
    }
}
