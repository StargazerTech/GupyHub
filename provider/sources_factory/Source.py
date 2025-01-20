

class Source:
    def __init__(self):
        self.source_name = ''
        self.type = ''
        self.link = ''
        self.add_date = ''

    def newSource(self, source_name, type, link, add_date):
        self.source_name = source_name
        self.type = type
        self.link = link
        self.add_date = add_date
