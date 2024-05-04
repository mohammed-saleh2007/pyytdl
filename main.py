from pytube import YouTube

# Get the video link from the user
video_url = input("Please enter the video link: ")

# Create a YouTube object
yt = YouTube(video_url)

# Get the available streams for the video
streams = yt.streams

# Extract the unique video resolutions
resolutions = set(stream.resolution for stream in streams if stream.resolution)

# Print the available video qualities
print("Available video qualities:")
for resolution in sorted(resolutions):
    print(resolution)

# Get the desired content type (video or audio) from the user
content_type = input("Do you want to download video or audio? (Enter 'video' or 'audio'): ")

# If the user wants to download video, ask for the desired video quality
if content_type.lower() == 'video':
    video_quality = input("Please enter the video quality (e.g., 720p): ")

    # Find the video stream with the specified quality
    video_stream = streams.filter(only_video=True, resolution=video_quality).first()

    # Check if the video stream exists
    if video_stream:
        output_filename = input("Enter the output filename (including extension): ")
        video_stream.download(filename=output_filename)
        print("Video downloaded successfully.")
    else:
        print(f"No video available in {video_quality} resolution.")
elif content_type.lower() == 'audio':
    # Find the audio stream
    audio_stream = streams.filter(only_audio=True).first()

    if audio_stream:
        output_filename = input("Enter the output filename (including extension): ")
        audio_stream.download(filename=output_filename)
        print("Audio downloaded successfully.")
    else:
        print("No audio available.")
else:
    print("Invalid content type.")
