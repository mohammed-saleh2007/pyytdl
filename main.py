from pytube import YouTube


url = "https://www.youtube.com/watch?v=Cl5Vkd4N03Q"

video_yt = YouTube(url)

print(video_yt.title)
print("Thumbnail", video_yt.thumbnail_url)

def resos(yt):
    streams = yt.streams.filter(file_extension='mp4', progressive=True).order_by("resolution")
    reso_list = {}
    
    for stream in streams:
        reso_list[f"{stream.resolution}@{stream.fps}"] = [stream.resolution, stream.fps]

    return reso_list


def video_resolution(reso_list):
    print("available Qulaities")
    for i in reso_list.keys():
        print(i)
        
    return input("what do you want? (ex: 720p@30): ")

def dl_video(yt, reso, reso_list):
    for i in reso_list.keys():
        if i == reso:
            video_dl = reso_list[i]
    print(video_dl)
    yt.streams.filter(res=video_dl[0], fps=video_dl[1]).first().download()

dl_video(video_yt, video_resolution(resos(video_yt)), resos(video_yt))


