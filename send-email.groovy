pipeline{
    agent any
    stages{ // Definimos las etapas
        stage('Main'){ // Etapa Main
            steps { // Definimos los pasos dentro de la etapa
                emailext body: 'Test Message', // Pluguin para enviar correo y el cuerpo del correo
                    subject: 'Test Subject', // Asunto del correo
                    to: 'cristian.fernandez@tenea.com' // Destinatario del correo
            }
        }
    }
}