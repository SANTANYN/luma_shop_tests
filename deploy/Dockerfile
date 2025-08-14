FROM --platform=linux/arm64 jenkins/jenkins:lts-jdk17

# Switch to root user to install all dependencies
USER root

# Install packages, Chromium and ChromeDriver
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv wget gnupg2 ca-certificates curl chromium chromium-driver sudo \
    postgresql-client libpq-dev python3-dev gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create a symlink for chromedriver
RUN ln -s /usr/bin/chromedriver /usr/local/bin/chromedriver

# Set permissions for the Jenkins user
COPY . /var/jenkins_home/workspace/luma_shop_tests/
RUN chown -R jenkins:jenkins /var/jenkins_home/workspace/luma_shop_tests

# Change to the Jenkins user
USER jenkins

