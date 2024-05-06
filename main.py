from pytube import YouTube
import sys

url = input("video_url: ")

def progress_func(stream, chunk, bytes_remaining):
    current = stream.filesize - bytes_remaining
    done = int(50 * current / stream.filesize)

    sys.stdout.write(
        "\r[{}{}] {} MB / {} MB".format('█' * done, ' ' * (50 - done), "{:.2f}".format(bytes_to_megabytes(current)),
                                        "{:.2f}".format(bytes_to_megabytes(stream.filesize))))
    sys.stdout.flush()


def bytes_to_megabytes(bytes_size):
    megabytes_size = bytes_size / (1024 ** 2)
    return megabytes_size

video_yt = YouTube(url, on_progress_callback=progress_func)


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

    print("File Size: ", yt.streams.filter(res=video_dl[0], fps=video_dl[1]).first().filesize_mb, " MB")

    yt.streams.filter(res=video_dl[0], fps=video_dl[1]).first().download()
    yt.streams.filter(res=video_dl[0], fps=video_dl[1]).first().download()

dl_video(video_yt, video_resolution(resos(video_yt)), resos(video_yt))


