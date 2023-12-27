# youtube-downloader-website

Flask server to download for free YouTube videos and music directly from the browser.

You can try it [here](https://tools.pythoneditor1.repl.co/youtube).



![screenshot](images/screenshot.png)

Just paste the URL of the YouTube video and select the desired format. Make sure to have ffmpeg installed if you want to convert the videos in mp3.

## Dependencies

This project relies on the following dependencies:

- **Flask:** A web framework for Python. Install it using ```pip install flask```
- **pytube:** A lightweight, dependency-free Python library to download YouTube videos. Install it using ```pip install pytube```
  
- **ffmpeg:** (only if you want mp3) Required for converting audio and video formats. Install it based on your operating system. [ffmpg](https://www.ffmpeg.org/download.html)

Ensure all dependencies are installed before running the application.


## API REST

The application also provides a simple REST API for fetching information about YouTube videos. You can access it at:

[https://tools.pythoneditor1.repl.co/api/yt/info](https://tools.pythoneditor1.repl.co/api/yt/info)



#### Response

The response is in JSON format and includes the following information:

- `status`: Indicates the status of the request (`ok` or `error`).
- `title`: Title of the YouTube video.
- `views`: Number of views.
- `author`: Author of the video.
- `length`: Duration of the video.
- `description`: Video description.
- `thumbnail`: URL of the video thumbnail.
- `publish_date`: Date of video publication.
- `url`: URL to watch the video.
- `rating`: Video rating.

#### Example

[https://tools.pythoneditor1.repl.co/api/yt/info?url=https%3A%2F%2Fyoutu.be%2FNrQkdDVupQE](https://tools.pythoneditor1.repl.co/api/yt/info?url=https%3A%2F%2Fyoutu.be%2FNrQkdDVupQE)

```json
{
  "author": "GitHub",
  "description": null,
  "length": 2785,
  "publish_date": "Wed, 08 Nov 2023 00:00:00 GMT",
  "raiting": null,
  "status": "ok",
  "thumbnail": "https://i.ytimg.com/vi/NrQkdDVupQE/hq720.jpg",
  "title": "GitHub Universe 2023 opening keynote- Copilot in the Age of AI",
  "url": "https://youtube.com/watch?v=NrQkdDVupQE",
  "views": 280537
}
```

example of use:

```python

import requests

url = "https://tools.pythoneditor1.repl.co/api/yt/info"
video_url = "https://youtu.be/NrQkdDVupQE"

response = requests.get(url, params={"url": video_url})
data = response.json()
print(data)

```

