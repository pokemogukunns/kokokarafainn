# -*- coding: utf-8 -*-

from pytube import YouTube

# エラーメッセージ
__ERROR_MESSAGE__ = None

# YouTubeの動画をダウンロードする
def get_youtube(y_url, download_location, audio_only_flg):
    global __ERROR_MESSAGE
    # 一旦エラーメッセージをクリア
    __ERROR_MESSAGE = None

    # URLの入力に関する例外処理
    if type(y_url) != str or y_url == "":
        __ERROR_MESSAGE = "URLには文字列を入れてください"
        print(__ERROR_MESSAGE)
        return

    # 「http://」が省略されて入れば付け加える
    if not (y_url.startswith("https://") or y_url.startswith("https://")):
        y_url = "https://" + y_url

    # ダウンロード先フォルダが省略されて入れば、カレントディレクトリに設定
    if download_location == "" or download_location is None:
        download_location = "./"

    # エラーメッセージが出ていなければ動画を取得する
    try:
        youtube = YouTube(y_url)
        # 動画をダウンロードするとき
        if not audio_only_flg:
            youtube.streams.filter(subtype='mp4').first().download(download_location)
        # 音声をダウンロードするとき
        else:
            youtube.streams.filter(only_audio=True, subtype='mp4').first().download(download_location)
        print("ダウンロードが完了しました！")
    except Exception as e:
        __ERROR_MESSAGE = str(e)
        print(f"エラー: {__ERROR_MESSAGE}")

def main():
    print("Youtubeの動画をダウンロードします。")

    # ユーザーからの入力を受け取る
    y_url = input("YoutubeのURLを入力してください: ")
    download_location = input("ダウンロード先のフォルダ（省略可）: ")
    audio_only = input("音声のみをダウンロードしますか？ (y/n): ").lower() == 'y'

    # YouTubeの動画をダウンロードする
    get_youtube(y_url, download_location, audio_only)

if __name__ == "__main__":
    main()
