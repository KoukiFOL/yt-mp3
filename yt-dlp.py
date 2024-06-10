#usr/bin/python

"""
youtubeの動画をmp3もしくはmp4方式でダウンロードするスクリプト
"""
date = "2024/05/29"
author = "UEYAMA Koki"

global ydl_opts
from yt_dlp import YoutubeDL
urlfile = open('urls.txt', 'r')
logfile =open('log.txt', 'a')
format = "mp3"
urls = urlfile.readlines()
failedUrls = []
successUrls = []

ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': './out/%(title)s.%(ext)s',
        'postprocessors': [
            {'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'},
            {'key': 'FFmpegMetadata'},
        ],
    }
"""
ydl_opts = {
        'format': 'best',
        'outtmpl': './out/%(title)s.%(ext)s'
    }
"""
for url in urls:
    if url.startswith('https://www.youtube.com/watch?v=') == False:
        
        print("youtubeのurlではありません。")
        failedUrls.append(url)
        continue

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
print(f"{len(urls)}件の動画のダウンロードが完了しました。")
if 0 < len(failedUrls):
    print(f"{len(failedUrls)}件の動画のダウンロードに失敗しました。")
    print("以下に失敗したurlを記載します。")
    for i in range(len(failedUrls)):
        failedUrl = failedUrls[i]
        print(f"{i}番目 {failedUrl}")

