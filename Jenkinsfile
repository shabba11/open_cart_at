pipeline {
    agent any  // Использует любой доступный агент

    stages {
        stage('Clone Repository') {
            steps {
                // Клонируем репозиторий содержимое
                git url: 'https://github.com/shabba11/open_cart_at.git', branch: 'project_open_cart_at' // Замените на ваш репозиторий
            }
        }

        stage('Run Container') {
            steps {
                script {
                    sh 'pytest tests/api_tests/ --url=$OPENCART_URL')
                }
            }
        }

    post {
        always {
            echo 'Pipeline завершён.'
        }
        success {
            echo 'Тесты пройдены успешно!'
        }
        failure {
            echo 'Сборка завершилась ошибкой.'
        }
    }
}