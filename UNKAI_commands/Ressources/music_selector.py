import difflib
import unidecode
import json

def normalize(text): # Supprime les accents et passe le texte en minuscule
    return unidecode.unidecode(text).lower()

def calculate_similarity(input_title, db_title, input_artists, db_artists):
    norm_input_title = normalize(input_title)
    norm_db_title = normalize(db_title)
    
    norm_input_artists = normalize(input_artists)
    norm_db_artists = normalize(", ".join(db_artists))
    
    title_similarity = difflib.SequenceMatcher(None, norm_input_title, norm_db_title).ratio()
    
    input_artists_list = norm_input_artists.split(", ")
    db_artists_list = norm_db_artists.split(", ")
    
    artist_similarity = 0
    for i, input_artist in enumerate(input_artists_list):
        if i < len(db_artists_list):
            artist_similarity += difflib.SequenceMatcher(None, input_artist, db_artists_list[i]).ratio() * (0.6 if i == 0 else 0.4)
        else:
            break
    
    artist_similarity /= len(input_artists_list) if input_artists_list else 1

    overall_similarity = (title_similarity * 0.6) + (artist_similarity * 0.4)
    
    return overall_similarity

def find_best_match_in_genre(user_input_title, user_input_artists, genre_database):
    best_match = None
    highest_similarity = 0
    
    for record in genre_database:
        db_title = record['title']
        db_artists = record['artists']
        similarity = calculate_similarity(user_input_title, db_title, user_input_artists, db_artists)
        
        if similarity > highest_similarity:
            highest_similarity = similarity
            best_match = record
            
    return best_match, highest_similarity

def find_best_match(user_input_title, user_input_artists, database):
    best_match = None
    highest_similarity = 0
    best_genre = None
    
    for genre, genre_database in database.items():
        match, similarity = find_best_match_in_genre(user_input_title, user_input_artists, genre_database)
        if similarity > highest_similarity:
            highest_similarity = similarity
            best_match = match
            best_genre = genre
    
    return best_match, highest_similarity, best_genre

def song_select(song_name : str, artist : str = None):
    with open('Blind_test\\scripts\\ressources\\songs.json', 'r') as songs_list:
        songs = json.load(songs_list)

    match, similarity, genre = find_best_match(song_name, artist if artist != None else ' ', songs)
    
    return (match, similarity, genre)