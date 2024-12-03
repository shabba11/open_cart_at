pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Клонируем репозиторий
                git url: 'https://github.com/shabba11/open_cart_at.git', branch: 'project_open_cart_at'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Обновление pip и установка необходимых зависимостей
                sh '''
                    python3 -m pip install --upgrade pip
                    python3 -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                // Запуск тестов с pytest
                sh 'python3 -m pytest tests/api_tests/'
            }
        }
    }
}