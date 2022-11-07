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

def filterTheJson(files_json, callback):
    filtered_files_json = {}
    for (fileName,value) in files_json.items():
        if callback((fileName,value)):
            filtered_files_json[fileName] = files_json[fileName]
    return filtered_files_json
