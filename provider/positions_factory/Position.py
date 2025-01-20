

class Position:

    def __init__(self):
        self.source = ''
        self.item_list = ''
        self.page =     ''
        self.link = ''
        self.title = ''
        self.site = ''
        self.code = ''
        self.publication_date = ''
        self.subscription_deadline = ''
        self.type = ''
        self.status = ''
        self.scrapping_datetime = ''

    def newPosition(self, page, item_list, source, link, title, site, code, publication_date, subscription_deadline, type, status, scrapping_datetime):
        self.page = page
        self.item_list = item_list
        self.source = source
        self.link = link
        self.title = title
        self.site = site
        self.code = code
        self.publication_date = publication_date
        self.subscription_deadline = subscription_deadline
        self.type = type
        self.status = status
        self.scrapping_datetime = scrapping_datetime






