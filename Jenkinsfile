pipeline {
    agent any

    environment {
        IMAGE_NAME = 'fatimasarmadd/21i-1139-assignment1:latest' // Ensure proper tagging
        CONTAINER_NAME = 'assignment1_container'
        ADMIN_EMAIL = 'admin@example.com' // Replace with actual admin email
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'master', url: 'https://github.com/fatimasarmad/21i-1139_Assignment1.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '''
                echo Building Docker Image...
                docker build --no-cache -t %IMAGE_NAME% .
                '''
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    bat '''
                    echo Logging into Docker Hub...
                    echo %DOCKER_PASSWORD% | docker login -u %DOCKER_USERNAME% --password-stdin
                    '''
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                bat '''
                echo Pushing Docker image to Docker Hub...
                docker push %IMAGE_NAME%
                '''
            }
        }

        stage('Deploy Container') {
            steps {
                bat '''
                echo Stopping and removing existing container if running...
                docker stop %CONTAINER_NAME% || exit 0
                docker rm %CONTAINER_NAME% || exit 0

                echo Removing old image...
                docker rmi %IMAGE_NAME% || exit 0

                echo Pulling latest image from Docker Hub...
                docker pull %IMAGE_NAME%

                echo Running new container...
                docker run -d --name %CONTAINER_NAME% -p 5000:5000 %IMAGE_NAME%
                '''
            }
        }
    }

    post {
        success {
            bat '''
            echo Cleaning up unused Docker images...
            docker image prune -f
            '''
            // Sending email notification to admin
            emailext(
                subject: "Deployment Successful: Assignment1",
                body: "The latest version of Assignment1 has been successfully deployed via Jenkins.",
                to: "${ADMIN_EMAIL}"
            )
        }
        failure {
            emailext(
                subject: "Deployment Failed: Assignment1",
                body: "The deployment of Assignment1 has failed. Please check the Jenkins logs for details.",
                to: "${ADMIN_EMAIL}"
            )
        }
    }
}
