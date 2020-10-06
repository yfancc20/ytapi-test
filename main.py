import requests
import json

base_url = 'https://www.googleapis.com/youtube/v3/'
key = ''

# Dabacabb
#   Overwatch Funny Moments playlist id: PL12qeUdVceZjE0tWbl1GG9f9S7wgJ52T8

def writePlaylist():

    query_playlist = base_url + 'playlistItems?part=snippet,contentDetails,status&playlistId=PL12qeUdVceZjE0tWbl1GG9f9S7wgJ52T8&key=' + key + '&maxResults=1000'
    page_token = ''
    i = 0
    j = 0
    datagroup = []

    with open('playlist.json', 'w', encoding='utf-8') as f:
        while i == 0 or page_token != '':
            i += 1
            re = requests.get(query_playlist + '&page_token=' + page_token)
            data = json.loads(re.text)
            if 'nextPageToken' in data:
                page_token = data['nextPageToken']
            else:
                page_token = ''
            print('page ' + str(i), 'next page token: ' + page_token)
            for item in data['items']:
                j += 1
                datagroup.append(item['snippet'])
                print(j, item['snippet']['title'])
        
        json.dump(datagroup, f)


    

def parsePlaylist():
    with open('playlist.json', encoding='utf-8') as jfile:
        data = json.load(jfile)
        print(len(data))


""" main """
# writePlaylist()
parsePlaylist()