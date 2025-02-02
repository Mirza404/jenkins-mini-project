pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
                bat 'python -m pip install pytest'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'git pull origin main'
                bat 'mkdir reports'  // Create the reports directory
                bat 'pytest tests/ --junitxml=reports/test-results.xml'  // Run all tests inside ./tests/
            }
        }
    }

    post {
        always {
            bat 'copy reports\\test-results.xml %WORKSPACE%\\reports\\'
            junit 'reports/test-results.xml'
        }
    }
}
