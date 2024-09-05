import os
from pydub import AudioSegment
import shutil

# Define the source and destination folder paths
source_folder = "path/to/source/folder"  # Replace with the folder containing your MP3 files
destination_folder = "path/to/destination/folder"  # Replace with the folder where you want to save WAV files

# Ensure the destination folder exists, create it if it doesn't
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Loop through all files in the source folder
for filename in os.listdir(source_folder):
    if filename.endswith(".mp3"):  # Only process MP3 files
        mp3_file_path = os.path.join(source_folder, filename)
        wav_file_name = os.path.splitext(filename)[0] + ".wav"  # Convert the filename to WAV
        wav_file_path = os.path.join(destination_folder, wav_file_name)
        
        # Read the MP3 file and convert it to WAV
        audio = AudioSegment.from_mp3(mp3_file_path)
        audio.export(wav_file_path, format="wav")
        
        print(f"{filename} successfully converted to {wav_file_name}")

# Optionally delete the original MP3 files after conversion
# for filename in os.listdir(source_folder):
#     if filename.endswith(".mp3"):
#         os.remove(os.path.join(source_folder, filename))

print("All MP3 files have been successfully converted and moved to the destination folder.")
