from django.shortcuts import render, redirect
from pytube import YouTube

# Create your views here.


def index(request):
    # checking whether request.method is post or not
    if request.method == "POST":
        # getting link from frontend
        link = request.POST["link"]
        video = YouTube(link)

        # setting video resolution
        stream = video.streams.get_lowest_resolution()

        # downloads video
        stream.download()

        # returning HTML page
        return render(request, "ytdown/index.html")
    return render(request, "ytdown/index.html")


"""
    if request.POST.get("fetch-vid"):
        url = request.POST.get("given_url")

        video = YouTube(self.url)
        vidTitle, vidThumbnail = video.title, video.thumbnail_url
        qual, stream = [], []
        for vid in video.streams.filter(progressive=True):
            qual.append(vid.resolution)
            stream.append(vid)
        context = {
            "vidTitle": vidTitle,
            "vidThumbnail": vidThumbnail,
            "qual": qual,
            "stream": stream,
            "url": self.url,
        }

        return render(request, "ytdown/index.html", context)

    # for downloading the video
    elif request.POST.get("download-vid"):
        self.url = request.POST.get("given_url")
        video = YouTube(self.url)
        stream = [x for x in video.streams.filter(progressive=True)]
        video_qual = video.streams[int(request.POST.get("download-vid")) - 1]
        video_qual.download(output_path="../../Downloads")
        return redirect("ytdown/index.html")

    return render(request, "ytdown/index.html")

"""

"""
from pytube import YouTube


def download_video(url):
    try:
        # Get the video from the URL
        yt = YouTube(url)

        # Get the highest quality video stream available
        video = (
            yt.streams.filter(only_audio=True)
            # yt.streams.filter(progressive=True, file_extension="mp4")
            # .order_by("resolution")
            # .desc()
            .first()
        )
        print(yt.title)

        # Download the video to the current directory
        video.download()

        print("Video downloaded successfully")
    except Exception as e:
        print("An error occurred while downloading the video")
        print(e)


# Ask the user for the YouTube URL
url = input("Enter the YouTube URL: ")

# Download the video
download_video(url)
"""
