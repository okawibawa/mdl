import os

import yt_dlp


def downloader(video_url, format, resolution):
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    download_dir = os.path.join(base_dir, "downloads")

    os.makedirs(download_dir, exist_ok=True)

    ydl_opts = {"outtmpl": os.path.join(download_dir, "%(title)s.%(ext)s")}

    if format.lower() == "mp4":
        ydl_opts.update({"format": f"bestvideo[height<={resolution}]+bestaudio/best"})
        ydl_opts.update({"merge_output_format": "mp4"})
    elif format.lower() == "mp3":
        ydl_opts.update({"format": "bestaudio/best"})
        ydl_opts.update(
            {
                "postprocessors": [
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192",
                    }
                ]
            }
        )
    else:
        raise ValueError(f"Unsupported format: {format}. Use 'mp3' or 'mp4'.")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print(f"Downloaded {video_url} as {format.upper()}")
    except yt_dlp.utils.DownloadError as e:
        print(f"Error downloading {video_url}: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    video_url = input("Video URL: ").strip()

    format = ""
    while format == "":
        format = input("Output format: (supported: MP3 & MP4): ").strip()

        format_lower = format.lower()

        if format_lower not in ["mp3", "mp4"]:
            print(f"{format.upper()} is an unsupported format.")
            format = ""

    resolution = ""
    if format.lower() == "mp4":
        resolution = input("Desired resolution (e.g. 720, 1080, etc): ").strip()

    downloader(video_url, format, resolution)
