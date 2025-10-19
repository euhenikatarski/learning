from playwright.sync_api import sync_playwright, expect


def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # 1. Переходим на страницу логина
        page.goto("https://cp.wowcircle.net/login")

        # 2. Заполняем поля логина и пароля
        page.locator("//input[@name='accountName']").fill("zaxi")
        page.locator("//input[@name='password']").fill("RpiXvel678")

        # 3. Нажимаем кнопку входа
        page.locator("//button[@class='cp-login-button' and normalize-space(text())='Вход']").click()

        # 4. Проверяем успешный вход (ожидаем кнопку "Выход")
        expect(page.locator("//div[text()=' Выход ']")).to_be_visible()

        # Закрываем
        context.close()
        browser.close()
