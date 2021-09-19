pipeline {
    agent any
    stages {

         stage('Build Dcoker Image') {
            sh 'docker build -t docker-registry.cityapl.com/cityapl_product_service ./'
            sh 'docker image list'
        }
        
        stage('Docker Push') {
            withCredentials([string(credentialsId: 'DOCKER_CRED', variable: 'DOCKER_CRED')]) {
                 sh 'docker login https://docker-registry.cityapl.com -u cityapl_docker_registry -p ${DOCKER_CRED}'
            }
            sh 'docker push docker-registry.cityapl.com/cityapl_product_service'
        }
    }
}
