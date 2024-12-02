pipeline {
    agent any  // Использует любой доступный агент

    stages {
        stage('Clone Repository') {
            steps {
                // Клонируем репозиторий содержимое
                git url: 'https://github.com/shabba11/open_cart_at.git', branch: 'project_open_cart_at' // Замените на ваш репозиторий
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Собираем Docker image
                    def app = docker.build("open_cart_at")  // Замените на желаемое имя образа
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    // Запускаем контейнер из только что созданного образа
                    app.run('-d --name open_cart_at sudo docker run --rm opencart_tests pytest tests/api_tests/ --url=$OPENCART_URL')
                }
            }
        }

        stage('Cleanup') {
            steps {
                script {
                    // Останавливаем и удаляем контейнер
                    sh 'docker stop my-running-container || true'
                    sh 'docker rm my-running-container || true'
                    sh "docker rmi my-docker-image:${env.BUILD_ID} || true"  // Удаляем образ, если это необходимо
                }
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