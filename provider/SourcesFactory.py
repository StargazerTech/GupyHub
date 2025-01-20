from datetime import datetime

from provider.Position import Position
from playwright.sync_api import sync_playwright

from provider.Source import Source


class SourceFactory:

    @staticmethod
    def getPositionsFromSource(source: Source):

        with sync_playwright() as play:
            # browser = play.chromium.launch(headless=True)
            browser = play.chromium.launch()
            context = browser.new_context()

            original_page = browser.new_page()

            original_page.goto(source.link)

            position_list = []

            title_selector = "#h1"
            pagination = "#job-listing > div.sc-ce195266-0.sZklj > nav > ul > li:nth-child(5) > button"
            table_selector = '#job-listing > ul'
            page = 1

            while True:
                original_page.wait_for_selector(title_selector)

                original_page.evaluate('window.scrollTo(0, document.body.scrollHeight)')  # Rola até o final
                original_page.wait_for_timeout(500)

                items = original_page.query_selector_all(f"{table_selector} li")

                item_list = 0
                for item in items:
                    item_list += 1
                    position = Position()

                    title = item.query_selector("div.sc-d1f2599d-2.jUrPXI").text_content().strip()
                    link = item.query_selector("a").get_attribute("href")
                    site = item.query_selector("div.sc-d1f2599d-3.dsYcYo").text_content().strip()

                    position.newPosition(page,item_list, source.source_name, link, title, site, "", "", "", "", "", str(datetime.now()))
                    position_list.append(position)

                next_page = original_page.query_selector(pagination)
                if next_page and next_page.is_enabled():
                    next_page.click()
                    original_page.wait_for_load_state("networkidle")
                    page += 1
                else:
                    break

            browser.close()
            return position_list