import webbrowser

def buka_youtube(video_title):
    url = f"https://www.youtube.com/result?search_query={video_title.replace(' ', '+')}"
    # membuka  URL di browser default
    webbrowser.open(url)
    print(f"membuka pencarian youtube untuk: {video_title}")

# meminta pengguna untuk memasukkan judul video
judul_video =  input("masukan judul video youtube yang ingin dibuka: ")
buka_youtube(judul_video) 