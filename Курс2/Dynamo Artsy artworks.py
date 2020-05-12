import requests
import json

client_id = '764d16e87b32c1ec980a'
client_secret = '44d1d8838e61c277b52810ba8ecd6bdb'

# инициируем запрос на получение токена
ReqSearchArtwork = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                                 data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
ArtworkSearch = json.loads(ReqSearchArtwork.text)

# достаем токен
token = ArtworkSearch["token"]
header = {"X-Xapp-Token": token}

# список url на картины
ArtworksURLs = ['https://www.artsy.net/artwork/leonardo-da-vinci-mona-lisa',
                'https://www.artsy.net/artwork/william-michael-harnett-the-old-violin',
                'https://www.artsy.net/artwork/edouard-manet-luncheon-on-the-grass-le-dejeuner-sur-lherbe',
                'https://www.artsy.net/artwork/rembrandt-van-rijn-the-company-of-frans-banning-cocq-and-willem-van-ruytenburch-the-night-watch',
                'https://www.artsy.net/artwork/pablo-picasso-the-frugal-repast-le-repas-frugal',
                'https://www.artsy.net/artwork/hieronymus-bosch-death-and-the-miser',
                'https://www.artsy.net/artwork/claude-monet-view-of-vetheuil',
                'https://www.artsy.net/artwork/albrecht-durer-the-last-judgment',
                'john-singer-sargent-portrait-of-mrs-edward-l-davis-and-her-son-livingston-davis']
ArtworksData = list()

for AwURL in ArtworksURLs:
    # разбор входящего url, извлечение названия
    ParseURL = AwURL.split('/')
    ArtworkSlug = ParseURL[-1]

    # # запрос на поиск ID картины
    # ReqSearchArtwork = requests.get("https://api.artsy.net/api/search?q=" + ArtworkSlug, headers=header)
    # # разбираем ответ сервера по поиску картины
    # ArtworkSearch = json.loads(ReqSearchArtwork.text)
    # ArtworkHref = ArtworkSearch['_embedded']['results'][0]['_links']['self']['href']
    # ArtworkID = ArtworkHref.split('/')[-1]
    # print(ArtworkID, ArtworkHref)

    # запрос данных картины
    ReqArtworkData = requests.get('https://api.artsy.net/api/artworks/' + ArtworkSlug, headers=header)

    ArtworkData = json.loads(ReqArtworkData.text)

    print(ArtworkData)





    # ArtworksData.append(j)

"""
for row in ArtistsData:
    print(
        'Artist: ' + row[0]['name'],
        'Birthday: ' + row[0]['birthday'],
        'Deathday: ' + row[0]['deathday'],
        'Biography: ' + row[0]['biography'],
        'Artworks: ',
        sep='\n')
"""

