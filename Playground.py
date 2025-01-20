from provider.helpers.JobHubUtils import JobHubUtils
from provider.sources_factory.Source import Source
from provider.sources_factory.SourceType import SourceType
from provider.positions_factory.PositionsFactory import PositionsFactory
from provider.sources_factory.SourcesFactory import SourceFactory


def teste():

    fonte = Source()
    fonte.newSource('Grupo Dreamers', SourceType.GUPY, 'https://ambev.gupy.io/', '20-01-2025')
    fonte.newSource('Grupo Dreamers', SourceType.GUPY, 'https://grupo-dreamers.gupy.io/', '20-01-2025')
    fonte.newSource('Grupo Dreamers', SourceType.GUPY, 'https://suzano.gupy.io/', '20-01-2025')
    fonte.newSource('Grupo Dreamers', SourceType.GUPY, 'https://kpmgbrasil.gupy.io/', '20-01-2025')
    fonte.newSource('Grupo Dreamers', SourceType.GUPY, 'https://topazbrasil.gupy.io/', '20-01-2025')


    lista = PositionsFactory.getPositionsFromGupySource(fonte)

    for item in lista:
        print(item.code, " | ",item.page, " | ", item.item_list, " | ", item.title, " | ", item.link, " | ", item.site, " | ", item.scrapping_datetime, " | ")


def sources():

    fonte = Source()
    fonte.newSource('', '', 'https://topazbrasil.gupy.io/', '')
    JobHubUtils.showSource(fonte)
    SourceFactory.updateGupySourceFields(fonte)
    JobHubUtils.showSource(fonte)







sources()