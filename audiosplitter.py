import os
import argparse
from pydub import AudioSegment
from pydub.utils import make_chunks

def split_audio(audio, filename, output_dir):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Split the audio into 5120 ms chunks
    chunk_length_ms = 5120
    chunks = make_chunks(audio, chunk_length_ms)

    # Save the chunks as separate audio files with the same name as the input file
    file_name = os.path.splitext(os.path.basename(filename))[0]
    for i, chunk in enumerate(chunks):
        # Check the duration of the chunk
        if len(chunk) >= 1000:  # Minimum duration of 1 second (1000 milliseconds)
            output_file = os.path.join(output_dir, f"{file_name}_{i}.wav")
            chunk.export(output_file, format="wav")
            print(f"Chunk {i} saved as {output_file}")
        else:
            print(f"Chunk {i} is less than 1 second in duration and will be skipped.")

def process_directory(input_dir, output_dir):
    # Iterate over all files in the input directory
    for filename in os.listdir(input_dir):
        filepath = os.path.join(input_dir, filename)

        # Check if it's an mp3 or wav file
        if filename.lower().endswith(".mp3"):
            # Convert mp3 to wav using pydub
            audio = AudioSegment.from_mp3(filepath)
        elif filename.lower().endswith(".wav"):
            # Load the wav file
            audio = AudioSegment.from_wav(filepath)
        else:
            print(f"Ignoring {filename} as it's not an mp3 or wav file")
            continue

        # Split the audio into chunks
        split_audio(audio, filename, output_dir)

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Split audio files into 5120 ms chunks.")
parser.add_argument("-i", "--input", type=str, help="Input directory containing audio files")
parser.add_argument("-o", "--output", type=str, help="Output directory for split chunks")
args = parser.parse_args()

# Check if both input and output directories are provided
if not args.input or not args.output:
    print("Please provide both input and output directories.")
    parser.print_help()
else:
    # Process the input directory
    process_directory(args.input, args.output)
