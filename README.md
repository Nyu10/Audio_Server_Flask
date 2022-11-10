### Simple Flask Server to Handle Audio Projects


## Run the app

    python app.py


### Requests

`GET /info/`  
Returns all files (with their meta dataa) matching (optional) query parameter criteria
        
    curl "http://localhost:5000/info/"

    Min and Max Durations
    curl "http://localhost:5000/info?minduration=120&maxduration=200"
    expected: one republic 

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


`GET /list/`  
Returns all file names matching (optional) query parameter criteria
    
    curl "http://localhost:5000/list/"
    
    Genre
    curl "http://localhost:5000/list?genre=Pop"
    expected: one republic, a.m4a, and flac

`GET /download/`  
Downloads file from audio files folder 

    curl "http://localhost:5000/download?name=b.mp3" --output b.mp3

`POST /post/`  
Uploads file to audio Files Folder
    

    curl -F "file=@TheWeekend.mp3" http://localhost:5000/post

    Not Allowed File Type (Will Error)
    curl -F "file=@p3_starter_code.zip" http://localhost:5000/post

