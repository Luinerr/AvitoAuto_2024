from time import sleep

import pytest
from playwright.sync_api import Page, sync_playwright

paths = ['//*[@id="app"]/div/div[3]/div/div/div/div/div[3]/div/div[2]/div[2]',
         '//*[@id="app"]/div/div[3]/div/div/div/div/div[3]/div/div[2]/div[4]',
         '//*[@id="app"]/div/div[3]/div/div/div/div/div[3]/div/div[2]/div[6]']

ENDPOINT = 'https://www.avito.ru/web/1/charity/ecoImpact/init'
PAGE_LINK = 'https://www.avito.ru/avito-care/eco-impact'


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        yield browser
        browser.close()


@pytest.fixture(scope="module")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


def test_1(page: Page):
    page.goto(PAGE_LINK)
    for i in range(0, 3):
        page.locator(paths[i]).screenshot(path=(f'output/1.{i + 1}.jpg'))
    sleep(1)


def test_2(page: Page):
    page.route(ENDPOINT, lambda route: route.fulfill(path="mock/2_1.json"))
    page.goto(PAGE_LINK)
    for i in range(0, 3):
        page.locator(paths[i]).screenshot(path=(f'output/2_1.{i + 1}.jpg'))

    page.route(ENDPOINT, lambda route: route.fulfill(path="mock/2_2.json"))
    page.goto(PAGE_LINK)
    for i in range(0, 3):
        page.locator(paths[i]).screenshot(path=(f'output/2_2.{i + 1}.jpg'))

    page.route(ENDPOINT, lambda route: route.fulfill(path="mock/2_3.json"))
    page.goto(PAGE_LINK)
    for i in range(0, 3):
        page.locator(paths[i]).screenshot(path=(f'output/2_3.{i + 1}.jpg'))
    sleep(1)


def test_3(page: Page):
    page.route(ENDPOINT, lambda route: route.fulfill(path="mock/3_1.json"))
    page.goto(PAGE_LINK)
    for i in range(0, 3):
        page.locator(paths[i]).screenshot(path=(f'output/3_1.{i + 1}.jpg'))

    page.route(ENDPOINT, lambda route: route.fulfill(path="mock/3_2.json"))
    page.goto(PAGE_LINK)
    for i in range(0, 3):
        page.locator(paths[i]).screenshot(path=(f'output/3_2.{i + 1}.jpg'))

    page.route(ENDPOINT, lambda route: route.fulfill(path="mock/3_3.json"))
    page.goto(PAGE_LINK)
    for i in range(0, 3):
        page.locator(paths[i]).screenshot(path=(f'output/3_3.{i + 1}.jpg'))

    sleep(1)


def test_4(page: Page):
    page.route(ENDPOINT, lambda route: route.fulfill(path="mock/4_1.json"))
    page.goto(PAGE_LINK)
    for i in range(0, 3):
        page.locator(paths[i]).screenshot(path=(f'output/4_1.{i + 1}.jpg'))

    page.route(ENDPOINT, lambda route: route.fulfill(path="mock/4_2.json"))
    page.goto(PAGE_LINK)
    for i in range(0, 3):
        page.locator(paths[i]).screenshot(path=(f'output/4_2.{i + 1}.jpg'))

    page.route(ENDPOINT, lambda route: route.fulfill(path="mock/4_3.json"))
    page.goto(PAGE_LINK)
    for i in range(0, 3):
        page.locator(paths[i]).screenshot(path=(f'output/4_3.{i + 1}.jpg'))

    sleep(1)


def test_5(page: Page):
    page.route(ENDPOINT, lambda route: route.fulfill(path="mock/5_1.json"))
    page.goto(PAGE_LINK)
    for i in range(0, 3):
        page.locator(paths[i]).screenshot(path=(f'output/5_1.{i + 1}.jpg'))

    page.route(ENDPOINT, lambda route: route.fulfill(path="mock/5_2.json"))
    page.goto(PAGE_LINK)
    for i in range(0, 3):
        page.locator(paths[i]).screenshot(path=(f'output/5_2.{i + 1}.jpg'))

    page.route(ENDPOINT, lambda route: route.fulfill(path="mock/5_3.json"))
    page.goto(PAGE_LINK)
    for i in range(0, 3):
        page.locator(paths[i]).screenshot(path=(f'output/5_3.{i + 1}.jpg'))

    sleep(1)


def test_6(page: Page):
    page.route(ENDPOINT, lambda route: route.fulfill(path="mock/6_1.json"))
    page.goto(PAGE_LINK)
    for i in range(0, 3):
        page.locator(paths[i]).screenshot(path=(f'output/6_1.{i + 1}.jpg'))

    page.route(ENDPOINT, lambda route: route.fulfill(path="mock/6_2.json"))
    page.goto(PAGE_LINK)
    for i in range(0, 3):
        page.locator(paths[i]).screenshot(path=(f'output/6_2.{i + 1}.jpg'))

    sleep(1)
