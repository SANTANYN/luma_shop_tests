EN description

🧪 Luma Shop Tests — Pet Project
This is my pet project dedicated to automating tests for the Luma demo online store (previously available at https://magento.softwaretestingboard.com/).

Unfortunately, the website is currently unavailable, meaning some functionality can no longer be executed, and GitHub Actions are failing due to inaccessible endpoints. Nevertheless, the project effectively demonstrates my approach to test architecture and infrastructure management.

💡 About the Project
The main goal is to showcase my automation skills in areas such as:

Building test architecture

Applying the Page Object Model (POM)

Working with Pytest

CI/CD integration

Using Docker

Handling different environments

I planned to add API tests and expand UI test coverage, but the website stopped working before I could complete them. Despite this, the current project reflects my preferred approach to organizing automated tests.

🧱 Architectural Approach: Base Test Class Pattern
The project utilizes the Base Test Class Pattern—a central BaseTest class from which all other test classes inherit.

This approach allows for:

Reusing setup/teardown logic.

Centralized initialization of Page Object Models.

Storing common dependencies in one place.

Avoiding code duplication in individual tests.

Keeping tests clean and readable.

This approach is also known as:

📌 Page Object Injection in Base Test

Since the main focus is on POM, we inject Page Objects through the base class rather than through fixtures in every single test.

🔧 Technologies
Python, Pytest

Selenium / Playwright (if applicable)

Page Object Model (POM)

Docker

GitHub Actions

Jenkins Pipeline

Allure reports (if applicable)

🚀 CI/CD
The project includes configurations for:

✔ GitHub Actions

A complete pipeline that runs tests within a container. Actions are currently failing because the Luma site is unavailable—but the configuration is fully operational.

✔ Jenkins Pipeline

A parallel Jenkins pipeline was created to:

Bring up a Docker container.

Run the tests.

Generate reports.

Save artifacts.

✔ Docker

A dedicated Docker image has been built, allowing tests to be run in an isolated and consistent manner across any environment.

⚠ Status
The Luma website is inaccessible, so the tests fail. However, the project remains a demonstration of:

My level of self-sufficiency.

My architectural approach.

My ability to set up CI/CD.

My proficiency in configuring Docker environments.

📄 Conclusion
This repository serves as a demonstration of my work style, my approach to building test architecture, and my practical automation skills.

If you wish to see how I approach testing in real-world scenarios, this project is a good example.


RU description

🧪 Luma Shop Tests — Pet Project

Это мой пет-проект по автоматизации тестирования демо-интернет-магазина Luma (ранее доступен по адресу https://magento.softwaretestingboard.com/
).

К сожалению, сайт сейчас недоступен, поэтому часть функциональности больше нельзя запустить, а GitHub Actions падают по причине недоступных эндпоинтов. Тем не менее проект хорошо демонстрирует мой подход к архитектуре автотестов и работе с инфраструктурой.

💡 О проекте

Основная цель — показать мои навыки в автоматизации:

построение архитектуры тестов,

применение Page Object модели,

работа с Pytest,

интеграция с CI/CD,

использование Docker,

работа с различными средами.

Я планировал добавить API-тесты и расширить покрытие UI-тестов, но не успел до того, как сайт перестал работать. Тем не менее текущий проект отражает мой любимый подход к организации автотестов.

🧱 Архитектурный подход: Base Test Class Pattern

В проекте используется подход Base Test Class Pattern — базовый тестовый класс BaseTest, от которого наследуются все тесты.

Этот подход позволяет:

переиспользовать setup/teardown,

централизованно инициализировать Page Object модели,

хранить общие зависимости в одном месте,

не дублировать код в тестах,

поддерживать тесты в чистом и читаемом виде.

Также этот подход известен как:

📌 Page Object Injection in Base Test

Так как основной акцент сделан на POM, мы внедряем Page Objects через базовый класс, а не через фикстуры в каждом тесте.

🔧 Технологии

Python, Pytest

Selenium / Playwright (если есть)

Page Object Model

Docker

GitHub Actions

Jenkins pipeline

Allure reports (если есть)

🚀 CI/CD

В проекте настроены:

✔ GitHub Actions

Полный pipeline, который запускает тесты в контейнере. Сейчас Actions падают, так как сайт Luma недоступен — но конфигурация полностью рабочая.

✔ Jenkins Pipeline

Параллельно создан Jenkins pipeline, который:

поднимает Docker-контейнер,

запускает тесты,

генерирует отчёты,

сохраняет артефакты.

✔ Docker

Собран Docker-образ, позволяющий запускать тесты изолированно и одинаково в любых окружениях.

⚠ Статус

Сайт Luma недоступен → тесты не проходят, однако проект сохранился как демонстрация:

степени моей самостоятельности,

архитектурного подхода,

умения поднимать CI/CD,

настройки Docker-окружений.

Заключение

Этот репозиторий — демонстрация моего стиля работы, подхода к построению тестовой архитектуры и практических навыков в автоматизации.

Если вы хотите посмотреть, как я подхожу к тестам в реальных условиях — этот проект хороший пример.
