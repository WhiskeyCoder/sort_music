# Music Organizer Script
This Python script organizes your music files into folders based on their metadata tags (artist and album). It scans a specified directory for MP3 files and moves them into appropriate folders.

## Features
- Reads ID3 metadata from MP3 files to determine artist and album.
- Sanitizes filenames to avoid issues with special characters.
- Creates artist and album folders if they don't already exist.
- Moves files to their respective artist/album folders.

## Requirements
- Python 3.x
- `mutagen` library

## Installation
1. Make sure you have Python 3 installed on your system.
2. Install the `mutagen` library using pip:

    ```sh
    pip install mutagen
    ```

## Usage
1. Save the script to a file, for example, `organize_music.py`.
2. Modify the `folder_path` variable to point to the directory containing your MP3 files.
3. Run the script:


## Notes
- Ensure you have the necessary permissions to read and write files in the target directory.
- Backup your music files before running the script, as it moves files to new locations.


## Contributions
Feel free to fork this repository and submit pull requests. Your contributions are welcome!


## License
This project is licensed under the MIT License.
