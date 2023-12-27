from flask import Flask, request, render_template, jsonify, send_file
import pytube
import subprocess, os


app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 200



def mp4_to_mp3(input_path, output_path="output.mp3"):
    """Convert mp4 to mp3 with FFmpeg"""
    subprocess.run(
        f"""ffmpeg -i "{input_path}" -y -codec:a libmp3lame -ac 2 -ar 44100 "{output_path}" """,
        shell=True)
    print('done')


@app.route('/api/yt/info')
def yt_info():
    """Rest api for youtube"""
    url = request.args.get('url')
    print(url)
    try:
        yt = pytube.YouTube(url)
        return jsonify({
            'status': "ok",
            "title": yt.title,
            "views": yt.views,
            "author": yt.author,
            "length": yt.length,
            "description": yt.description,
            "thumbnail": yt.thumbnail_url,
            "publish_date": yt.publish_date,
            "url": yt.watch_url,
            "raiting": yt.rating
        })
    except Exception as e:
        return jsonify({'status': "error", "error": str(e)})


@app.route('/api/yt/download')
def youtube_download():
    """Download the file"""
    name = request.args.get('name')
    response = send_file(f"{name}", as_attachment=True)
    os.remove(f"{name}")

    return response


@app.route('/api/yt/process')
def youtube_process():
    """process the video"""
    url = request.args.get("url")
    filetype = request.args.get("format") or "mp4"
    print(url)
    print(filetype)
    try:
        youtube = pytube.YouTube(url)
        video = youtube.streams.get_highest_resolution()
        name = video.title
        video.download(filename=f"{name}.mp4")

    except pytube.exceptions.RegexMatchError:

        print("Invalid URL")
        response = jsonify({"status": "error", "error": "invalid_url"})
        return response
    
    except Exception as e:

        print(str(e))
        response = jsonify({"status": "error", "error": str(e)})
        return response

    if filetype == "mp3":
        print(f"Converting {name}.mp4 to {name}.mp3")

        mp4_to_mp3(f"{name}.mp4", output_path=f"{name}.mp3")
        os.remove(f"{name}.mp4")

    response = jsonify({"status": "ok", "name": name + '.' + filetype})

    return response



@app.route('/')
def index():
    return render_template("youtube.html")



if __name__ == '__main__':
    #run the app
    app.run(host='0.0.0.0', port=81, debug=True)
