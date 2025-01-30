pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pip install pytest'  // Ensure pytest is installed

            }
        }
        stage('Run Tests') {
            steps {
                sh 'git pull origin main'
                sh 'pytest --junitxml=test-results.xml'
                bat 'dir'
                bat 'type test-results.xml'
            }
        }
    }

    post {
        always {
            junit 'test-results.xml'
        }
    }
}