import webbrowser
import pygame
import os
import random

# Initialize Pygame mixer for local file playback
pygame.mixer.init()

# Function to play music on Spotify
def play_on_spotify(song=None):
    try:
        if song:
            query = song.replace(" ", "%20")  # URL encoding for spaces
            spotify_url = f"https://open.spotify.com/search/{query}"
            webbrowser.open(spotify_url)
            return f"Spotify opened with search for {song}."
        else:
            webbrowser.open("https://open.spotify.com/")
            return "Spotify opened successfully."
    except Exception as e:
        return f"Error playing on Spotify: {e}"

# Function to play a local music file
def play_local_file(music_directory, song=None):
    try:
        # List all MP3 files in the directory
        songs = [s for s in os.listdir(music_directory) if s.endswith('.mp3')]

        if not songs:
            return "No music files found."

        if song:
            matched_song = next((s for s in songs if song.lower() in s.lower()), None)
            if matched_song:
                song_path = os.path.join(music_directory, matched_song)
                pygame.mixer.music.load(song_path)
                pygame.mixer.music.play()
                return f"Playing {matched_song}."
            else:
                return f"Couldn't find {song} in local files."
        else:
            random_song = random.choice(songs)
            song_path = os.path.join(music_directory, random_song)
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()
            return f"Playing {random_song}."

    except pygame.error as e:
        return f"Error playing local file with Pygame: {e}"
    except Exception as e:
        return f"Error: {e}"

# Stop the currently playing music
def stop_music():
    try:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            return "Music stopped."
        else:
            return "No music is playing."
    except Exception as e:
        return f"Error stopping the music: {e}"
