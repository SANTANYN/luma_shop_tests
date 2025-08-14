pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                dir('/var/jenkins_home/workspace/luma_shop_tests') {
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run tests') {
            steps {
                dir('/var/jenkins_home/workspace/luma_shop_tests') {
                    sh '''
                        . venv/bin/activate
                        export PATH="/usr/bin:$PATH"
                        pytest tests/ -v --tb=short
                    '''
                }
            }
        }
    }

    post {
        always {
            dir('/var/jenkins_home/workspace/luma_shop_tests') {
                archiveArtifacts artifacts: 'allure-results/**/*', allowEmptyArchive: true
            }
        }
    }
}
