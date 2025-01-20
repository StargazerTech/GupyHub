import sqlite3
from datetime import datetime

from provider.positions_factory.Position import Position
from playwright.sync_api import sync_playwright

from provider.sources_factory.Source import Source
from provider.sources_factory.SourceType import SourceType


class SourceFactory:

    @staticmethod
    def updateGupySourceFields(source: Source):

        with sync_playwright() as play:

            browser = play.chromium.launch()

            original_page = browser.new_page()

            original_page.goto(source.link)

            original_page.wait_for_selector("#h1")

            item = original_page.query_selector("#h1").text_content().strip()

            if source.type == '' or source.type is None:
                source.type = SourceType.GUPY

            if source.source_name == '' or source.source_name is None:
                source.source_name = item

            if source.add_date == '' or source.add_date is None:
                source.add_date = datetime.now().strftime("%d-%m-%Y")

            SourceFactory.__save_on_database__(source)

            browser.close()

            print('Link: ' + source.link + ' updated.')

    @staticmethod
    def __save_on_database__(source: Source):
        connection = sqlite3.connect("database/identifier.sqlite")
        cursor = connection.cursor()

        sql_update = f"""
        update sources set type='{source.type}', source_name='{source.source_name}', add_date='{source.add_date}' where link='{source.link}'
        """

        cursor.execute(sql_update)
        connection.commit()
        cursor.close()
        connection.close()