pipeline {
    agent any

    environment {
        // Название вашего Docker-образа
        DOCKER_IMAGE = '<name>:latest'  // Замените на ваше имя образа
    }

    stages {
        stage('Checkout') {
            steps {
                // Получаем код из вашего репозитория
                git url: 'https://github.com/your/repo.git', branch: 'main' // Заменить ссылка на репозиторий
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Собираем Docker-образ из Dockerfile
                    docker.build(DOCKER_IMAGE)
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Запускаем тесты внутри контейнера
                    docker.image(DOCKER_IMAGE).inside {
                        // Выполняем команду тестирования
                        sh 'sudo docker run --rm <image_name> pytest api_tests/ --url=$OPENCART_URL'  // Заменить image_name
                    }
                }
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
        success {
            echo 'Tests completed successfully!'
        }
        failure {
            echo 'Tests failed!'
        }
    }
}