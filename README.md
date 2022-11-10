Simple Flask Server to Handle Audio Projects

Endpoints

Post:

Post Raw Audio Data

Get:

List of Stored Files
Metadata of Stored Files (duration of Audio)


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



List Endpoint
Returns FileNames that match the conditions

Genre
curl "http://localhost:5000/list?genre=Pop"
expected: one republic, a.m4a, and flac
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



POST
curl -F "file=@TheWeekend.mp3" http://localhost:5000/post

Not allowed File Type
curl -F "file=@p3_starter_code.zip" http://localhost:5000/post

'''


GET 

Download 

curl "http://localhost:5000/download?name=b.mp3" --output b.mp3

