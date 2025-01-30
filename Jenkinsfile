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
                sh 'mkdir -p reports'  // Create the reports directory
                sh 'pytest --junitxml=reports/test-results.xml'
                bat 'dir reports'
                bat 'type reports\\test-results.xml'
            }
        }
    }

    post {
        always {
            junit 'reports/test-results.xml'
        }
    }
}