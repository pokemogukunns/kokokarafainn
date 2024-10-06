# -*- coding: utf-8 -*-
from flask import Flask, request, render_template_string
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
        <form action="/download" method="post">
            <label for="url">YoutubeのURL:</label><br>
            <input type="text" id="url" name="url"><br>
            <label for="location">ダウンロード先のフォルダ（省略可）:</label><br>
            <input type="text" id="location" name="location"><br>
            <label for="audio">音声のみ:</label>
            <input type="checkbox" id="audio" name="audio"><br>
            <input type="submit" value="ダウンロード">
        </form>
    ''')

@app.route('/download', methods=['POST'])
def download():
    y_url = request.form['url']
    download_location = request.form['location'] or './'
    audio_only_flg = 'audio' in request.form

    # YouTube動画をダウンロードする関数
    try:
        youtube = YouTube(y_url)
        if audio_only_flg:
            youtube.streams.filter(only_audio=True, subtype='mp4').first().download(download_location)
            return "音声のダウンロードが完了しました。"
        else:
            youtube.streams.filter(subtype='mp4').first().download(download_location)
            return "動画のダウンロードが完了しました。"
    except Exception as e:
        return f"エラーが発生しました: {e}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
