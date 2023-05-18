from flask import Flask, request
from pydub import AudioSegment

app = Flask(__name__)


@app.route('/split_audio', methods=['POST'])
def split_audio():
    # file = request.files["file"]

    audio = AudioSegment.from_mp3("1.mp3")
    chunk_length = 10 * 60 * 1000

    # Get the length of the audio file in milliseconds.
    audio_length = len(audio)

    # Create a list to store the audio chunks.
    chunks = []

    # Iterate over the audio file, splitting it into `chunk_length` chunks.
    for i in range(0, audio_length, chunk_length):
        # Get the start and end times of the current chunk.
        start = i
        end = start + chunk_length

        # Create a new AudioSegment object for the current chunk.
        chunk = audio[start:end]

        # Add the current chunk to the list of chunks.
        chunks.append(chunk)

    # Iterate over the list of chunks, exporting each chunk to a wav file.
    i = 1
    for chunk in chunks:
        chunk.export(f"chunk-{i}.wav", format="wav")
        i += 1

    return "Success"


if __name__ == '__main__':
    app.run()
