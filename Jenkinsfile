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
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                // Запуск тестов с pytest
                sh 'pytest tests/api_tests/'
            }
        }
    }
}