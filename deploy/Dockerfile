FROM --platform=linux/arm64 jenkins/jenkins:lts-jdk17

# Переключаемся на root-пользователя для установки всех зависимостей
USER root

# Устанавливаем необходимые пакеты, Chromium и ChromeDriver
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv wget gnupg2 ca-certificates curl chromium chromium-driver sudo && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Создаем симлинк для chromedriver
RUN ln -s /usr/bin/chromedriver /usr/local/bin/chromedriver

# Устанавливаем права для пользователя Jenkins
COPY . /var/jenkins_home/workspace/luma_shop_tests/
RUN chown -R jenkins:jenkins /var/jenkins_home/workspace/luma_shop_tests

# Переключаемся на пользователя Jenkins
USER jenkins

