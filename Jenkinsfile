pipeline {
    agent any
    stages {
         stage('Build Dcoker Image') {
            steps {
            sh 'docker build -t docker-registry.cityapl.com/cityapl_product_service ./'
            sh 'docker image list'
            }
        }
        
        stage('Docker Push') {
            steps {
                withCredentials([string(credentialsId: 'DOCKER_CRED', variable: 'DOCKER_CRED')]) {
                     sh 'docker login https://docker-registry.cityapl.com -u cityapl_docker_registry -p ${DOCKER_CRED}'
                }
                sh 'docker push docker-registry.cityapl.com/cityapl_product_service'
            }
        }
        stage('Deploy') {
            steps {
                withCredentials([string(credentialsId: 'REMOTE_USER', variable: 'REMOTE_USER'),
                    string(credentialsId: 'REMOTE_HOST_3', variable: 'REMOTE_HOST_3')]) {
                    sh 'scp build.sh ubuntu@168.138.113.89:~/'
                    sh 'ssh ubuntu@168.138.113.89 "chmod +x build.sh"'
                    sh 'ssh ubuntu@168.138.113.89 ./build.sh'
                }   
            }
        }
    }
}

