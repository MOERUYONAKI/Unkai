import asyncio
import spotify
import json

async def playlist(name : str):
    client = spotify.Client('04a5a6ece2b24f9aa051ec3ff0fc7b6d', 'b62aaa0e2b7e431d8f05544695e7bd05')
    
    user = await client.get_user('31cpavcvtxdr6yc7eqdodslkllzq')
    playlists = (await user.get_playlists())

    playlist = spotify.Playlist

    for pl in playlists:
        if pl.name == name:
            playlist = pl
    
    tracks = await playlist.get_all_tracks()

    await client.close()
    return tracks

async def main(write : bool = True):
    tracks = await playlist('UNKAI')
    
    with open('Blind_test\\scripts\\ressources\\songs.json', mode = 'r', encoding = 'utf-8') as songs_list:
        songs = json.load(songs_list)

    songs['unknow'] = [{} for elt in tracks]

    for i in range(len(songs['unknow'])):
        artists = ''
        arts = []

        for elt in tracks[i].artists:
            artists += f'{elt.name}, '
            arts.append(elt.name)

        songs['unknow'][i]['path'] = f'Blind_test\\songs\\{artists[0 : -2]} - {tracks[i].name}.mp3'
        songs['unknow'][i]['title'] = tracks[i].name
        songs['unknow'][i]['artists'] = arts

    if write:
        with open('Blind_test\\scripts\\ressources\\songs.json', mode = 'w', encoding = 'utf-8') as songs_list:
            json.dump(obj = songs['unknow'], fp = songs_list, indent = 4)
    
    else:
        print(songs)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())