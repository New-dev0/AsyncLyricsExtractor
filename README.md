# AsyncLyricsExtractor


## Installation

```bash
pip3 install git+https://github.com/New-dev0/AsyncLyricsExtractor.git
```

## Requirements

* You will need an API Key and Engine ID of Google Custom Search JSON API.
  * Create your new Custom Search Engine here: https://cse.google.com/cse/create/new
  * Add any of the following or all websites as per your choice in your Custom Search Engine:
    * https://genius.com/
    * http://www.lyricsted.com/
    * http://www.lyricsbell.com/
    * https://www.glamsham.com/
    * http://www.lyricsoff.com/
    * http://www.lyricsmint.com/

## Usage
```python
from lyrics_extractor import SongLyrics
extract_lyrics = SongLyrics(GCS_API_KEY, GCS_ENGINE_ID)
# Replace 'GCS_API_KEY' and 'GCS_ENGINE_ID' with the API key and Engine ID received.
data = await extract_lyrics.get_lyrics("Shape of You")
print(data["title"])
print(data["lyrics"])
```

# Disclaimer
- All Details and Credits are as mentioned in parent repository. 
