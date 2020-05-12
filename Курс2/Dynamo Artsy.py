import requests
import json

client_id = '764d16e87b32c1ec980a'
client_secret = '44d1d8838e61c277b52810ba8ecd6bdb'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]
header = {"X-Xapp-Token": token}

# инициируем запрос с заголовком
ArtistsList = ['pablo-picasso',
               'claude-monet',
               'edouard-manet',
               'leonardo-da-vinci',
               'hieronymus-bosch',
               'rembrandt-van-rijn',
               'albrecht-durer',
               'john-singer-sargent']
ArtistsData = list()
for Artist in ArtistsList:
    r = requests.get("https://api.artsy.net/api/artists/"+Artist, headers=header)
    # разбираем ответ сервера по художнику
    j = json.loads(r.text)
    print(j)
    r2 = requests.get(j['_links']['artworks']['href'], headers=header)
    # разбираем ответ сервера по работам
    j2 = json.loads(r2.text)
    print(j2['_embedded'])
    ArtistsData.append([j, j2])

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

"""
with open('/home/igor/Загрузки/ArtistsList.txt', 'w') as ArtistsListF:
    for Artist in ArtistsListS:
        print(Artist[4:])
        ArtistsListF.write(Artist[4:]+'\n')
"""