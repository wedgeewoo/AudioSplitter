
# Audio Splitter

This script splits audio files into 5120 ms (5.12 seconds) chunks. It supports both mp3 and wav file formats.

## Usage

```
python audio_splitter.py -i <input_directory> -o <output_directory>
```

- `-i <input_directory>`: Path to the directory containing the audio files to be split.
- `-o <output_directory>`: Path to the directory where the split audio chunks will be saved.

Make sure to provide both the input and output directories when running the script.

## Prerequisites

- Python 3.x
- Required Python packages can be installed using the following command:

```
pip install pydub
```

## How it works

1. The script takes an input directory containing audio files and an output directory for the split chunks as command-line arguments.
2. It checks if both input and output directories are provided. If not, it displays an error message and the script's usage instructions.
3. The script iterates over all files in the input directory.
4. For each file, it checks if it is an mp3 or wav file. If it's neither, it prints a message and ignores the file.
5. If the file is an mp3, it converts it to wav format using the `pydub` library.
6. If the file is already in wav format, it loads the wav file.
7. The audio is then split into 5120 ms (5.12 seconds) chunks.
8. Each chunk with a duration of at least 1 second (1000 milliseconds) is saved as a separate audio file in the output directory.
9. The script prints the filename and path of each saved chunk.
10. If a chunk is less than 1 second in duration, it is skipped and a message is printed.
11. Once all the files in the input directory are processed, the script finishes execution.

Note: The script creates the output directory if it doesn't already exist.

