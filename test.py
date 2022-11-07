from flask import Flask
from tinytag import TinyTag
import json
import os
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


audio_file_path = './Audio_Files'


def tagToJson(tag):
    json = {}
    json['album'] = tag.album      # album as string
    json['albumartist'] = tag.albumartist   # album artist as string
    json['artist'] = tag.artist        # artist name as string
    json['audio_offset'] = tag.audio_offset # number of bytes before audio data begins
    json['bitrate'] = tag.bitrate       # bitrate in kBits/s
    json['comment'] = tag.comment       # file comment as string
    json['composer'] = tag.composer      # composer as string
    json['disc'] = tag.disc          # disc number
    json['disc_total'] = tag.disc_total    # the total number of discs
    json['duration'] = tag.duration      # duration of the song in seconds
    json['filesize'] = tag.filesize      # file size in bytes
    json['genre'] = tag.genre         # genre as string
    json['samplerate'] = tag.samplerate    # samples per second
    json['title'] = tag.title         # title of the song
    json['track'] = tag.track         # track number as string
    json['track_total'] = tag.track_total   # total number of tracks as string
    json['year'] = tag.year          # year or data as string
    return json


def getAudioFiles():
    files = os.listdir(audio_file_path)
    files_json = []
    for file_name in files:
        full_file_path = audio_file_path + '/' + file_name
        metadata = TinyTag.get(full_file_path)
        # print(type(metadata))
        files_json.append(metadata)
        fileJson = tagToJson(metadata)
        print(fileJson)
        break
    return files_json


print(getAudioFiles())
