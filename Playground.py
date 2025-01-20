from provider.Source import Source
from provider.SourceType import SourceType
from provider.SourcesFactory import SourceFactory

fonte = Source()
fonte.newSource('Grupo Dreamers', SourceType.GUPY, 'https://ambev.gupy.io/', '20-01-2025')
fonte.newSource('Grupo Dreamers', SourceType.GUPY, 'https://grupo-dreamers.gupy.io/', '20-01-2025')
fonte.newSource('Grupo Dreamers', SourceType.GUPY, 'https://suzano.gupy.io/', '20-01-2025')
fonte.newSource('Grupo Dreamers', SourceType.GUPY, 'https://kpmgbrasil.gupy.io/', '20-01-2025')


lista = SourceFactory.getPositionsFromSource(fonte)

for item in lista:
    print(item.code, " | ",item.page, " | ", item.item_list, " | ", item.title, " | ", item.link, " | ", item.site, " | ", item.scrapping_datetime, " | ")

