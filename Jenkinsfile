pipeline {
    agent any
    stages {
        //stage('Prueba') {
        //    steps {
        //        script{
        //            sh 'echo =============================================='
        //                // deploy and rollback folders
        //                dir('Prueba') {
        //                    git branch: 'main',
        //                    credentialsId: 'jenkinsgit',
        //                    url: '$FOLDER' 
        //                }
                    
                    // scripts
        //               git branch: 'main',
        //                credentialsId: 'jenkinsgit',
        //                url: 'ssh://git@github.com:Kells02/Jenkins.git' 
        //                sh 'echo =============================================='
        //                sh 'echo ============= FIN CLON ======================='
        //                sh 'echo =============================================='
        //            
        //        }
        //    }
        //}
        stage('folder') {
                steps {
                    script {
                        sh 'echo =============================================='
                        sh 'echo ================= ST 1 ======================='
                        sh 'echo =============================================='
                        sh "python3 stage-folders.py"
                    }
                }
            }
    }
}