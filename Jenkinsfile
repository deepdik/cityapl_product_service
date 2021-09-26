pipeline {
    agent any
    stages {
         stage('Build Dcoker Image') {
            steps {
            sh 'docker-compose build'
            }
        }
        
        stage('Docker Push') {
            steps {
                withCredentials([string(credentialsId: 'DOCKER_CRED', variable: 'DOCKER_CRED')]) {
                     sh 'docker login https://docker-registry.cityapl.com -u cityapl_docker_registry -p ${DOCKER_CRED}'
                }
                sh 'docker-compose push'
            }
        }
        stage('Deploy') {
            steps {
                withCredentials([string(credentialsId: 'REMOTE_USER', variable: 'REMOTE_USER'),
                    string(credentialsId: 'REMOTE_HOST_3', variable: 'REMOTE_HOST_3')]) {
                    sh 'scp -v -o StrictHostKeyChecking=no  -r $(pwd) ${REMOTE_USER}@${REMOTE_HOST_3}:~/'

                }   
            }
        }
    }
}

