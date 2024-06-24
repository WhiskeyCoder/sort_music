import os
import re
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from shutil import move


def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*\']', '_', filename)


def organize_music_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.mp3'):
            file_path = os.path.join(folder_path, filename)
            if not os.path.isfile(file_path):
                print(f'Skipping {filename}: not a valid file')
                continue
            try:
                audio = MP3(file_path, ID3=EasyID3)
                artist = audio.get('artist', ['Unknown Artist'])[0]
                album = audio.get('album', ['Unknown Album'])[0]
                artist = sanitize_filename(artist)
                album = sanitize_filename(album)
                artist_folder = os.path.join(folder_path, artist)
                album_folder = os.path.join(artist_folder, album)
                if not os.path.exists(artist_folder):
                    os.makedirs(artist_folder)
                if not os.path.exists(album_folder):
                    os.makedirs(album_folder)

                move(file_path, os.path.join(album_folder, filename))
                print(f'Moved: {filename} to {album_folder}')

            except Exception as e:
                print(f'Error processing {filename}: {e}')


if __name__ == "__main__":
    folder_path = r'ADD PATH TO MUSIC FOLDER'
    organize_music_files(folder_path)
