pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo "Build Docker Image"
                sh "docker build -t mypythonflaskapp ."
            }
        }

        stage('Run') {
            steps {
                echo "Run application in Docker Container"
                sh "docker rm -f mycontainer || true"
                sh "docker run -d -p 5000:5000 --name mycontainer mypythonflaskapp"
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}
