from flask import Flask, request
from tinytag import TinyTag
from jsonProcessing import tagToJson, filterTheJson
import json
import os
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


audio_file_path = './Audio_Files'


def filter(args, files_json):
    filtered_files_json = files_json
    name = args.get('name', None)
    minduration = args.get('minduration', None)
    maxduration = args.get('maxduration', None)
    albumartist = args.get('albumartist', None)
    genre = args.get('genre', None)
    #data[0] is file name
    #data[1] is metadata
    if name:
        filtered_files_json = filterTheJson(filtered_files_json, lambda data: data[0] == name)
    if minduration:
        filtered_files_json = filterTheJson(filtered_files_json, lambda data: data[1]['duration'] >= int(minduration))
    if maxduration: 
        filtered_files_json = filterTheJson(filtered_files_json, lambda data: data[1]['duration'] <= int(maxduration))
    if albumartist:
        filtered_files_json = filterTheJson(filtered_files_json, lambda data: data[1]['albumartist'] == albumartist)
    if genre:
        filtered_files_json = filterTheJson(filtered_files_json, lambda data: data[1]['genre'] == genre)
    return filtered_files_json

def handleRequest():
    args = request.args
    files = os.listdir(audio_file_path)
    files_json = {}
    for file_name in files:
        full_file_path = audio_file_path + '/' + file_name
        metadata = TinyTag.get(full_file_path)
        files_json[file_name] = tagToJson(metadata)
    filtered_files_json = filter(args, files_json)
    return filtered_files_json


@app.route('/list', methods =['GET'])
def getList():
    filtered_files_json = handleRequest()
    list_file_names = [key for key in filtered_files_json]
    return {'files': list_file_names}

@app.route('/info', methods =['GET'])
def getInfo():
    return handleRequest()

if __name__ == "__main__":
    app.run()
'''
POST Raw Audio Data and Store it

GET
"Query Parameter to Filter Results"

List of Stored Files
    gets all files with  parameter such as max duration
    min duration
    channel mapping?
    sampling frequency?
    bit depth
Content of STored Files
Metadata of Stored Files

Eg: $ curl http://localhost/download?name=myfile.wav 

Eg: $ curl http://localhost/list?maxduration=300 

Eg: $ curl http://localhost/info?name=myfile.wav 

'''

'''
List Endpoint
Returns FileNames that match the conditions

Genre
curl "http://localhost:5000/list?genre=Pop"
expected: one republic, a.m4a, and flac
'''


'''
Info Endpoint
Allows you to filter and also returns all metadata

Examples

Name
curl "http://localhost:5000/info?name=b.mp3"
expected: b.mp3


MinDuration
curl "http://localhost:5000/info?minduration=120"
expected: one republic and a

Min and Max Durations
curl "http://localhost:5000/info?minduration=120&maxduration=200"
expected: one republic 


Genre
curl "http://localhost:5000/info?genre=Pop"
expected: one republic, a.m4a, and flac

AlbumArtist
curl "http://localhost:5000/info?albumartist=OneRepublic"
expected: one republic

Genre and Artist
curl "http://localhost:5000/info?genre=Pop&albumartist=OneRepublic"
expected: one republic

'''