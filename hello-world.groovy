// Definición del pipeline
pipeline {
    // Especifica que el pipeline puede ejecutarse en cualquier agente disponible
    agent any

    // Definición de las etapas del pipeline
    stages {
        // Etapa llamada "Hello"
        stage('Hello') {
            // Pasos a ejecutar en la etapa
            steps {
                // Imprime 'Hello World!' en la consola de salida de Jenkins
                echo 'Hello World!'
            }
        }
    }
}
