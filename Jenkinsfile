pipeline {
    agent any

    stages {
        steps {
                sh 'python -m pip install --upgrade pip'
                sh 'python -m pip install -r requirements.txt'
                sh 'python -m pip install pytest'
            }  
        stage('Run Tests') {
            steps {
                sh 'git pull origin main'
                sh 'mkdir -p reports'  // Create the reports directory
                sh 'pytest --junitxml=reports/test-results.xml'
            }
        }
    }

    post {
        always {
            junit 'reports/test-results.xml'
        }
    }
}