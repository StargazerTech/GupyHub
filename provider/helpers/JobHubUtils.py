from IPython.terminal.shortcuts import suspend_to_bg


class JobHubUtils:

    @staticmethod
    def showSource(source):
        surrounding = '*' * 100
        print(surrounding)
        print("SOURCE: " + source.source_name)
        print("LINK: " + source.link)
        print("TYPE: " + str(source.type))
        print("DATE: " + str(source.add_date))
        print(surrounding)
