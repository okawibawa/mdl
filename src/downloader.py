import argparse
import os

import yt_dlp


def downloader(video_url, format, resolution):
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    download_dir = os.path.join(base_dir, "downloads")

    os.makedirs(download_dir, exist_ok=True)

    format_lower = format.lower()
    if format_lower not in ["mp3", "mp4"]:
        raise ValueError(f"Unsupported format: {format}. Use 'mp3' or 'mp4'.")

    if format_lower == "mp4" and resolution is None:
        raise ValueError("Resolution is required for MP4 format.")
    if resolution is not None:
        if not isinstance(resolution, int) or resolution <= 0:
            raise ValueError("Resolution must be a positive integer.")

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

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print(f"Downloaded {video_url} as {format.upper()}")
    except yt_dlp.utils.DownloadError as e:
        print(f"Error downloading {video_url}: {e}")


def main():
    parser = argparse.ArgumentParser("Download YouTube video as MP3 or MP4")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument(
        "format",
        choices=["MP3", "MP4", "mp3", "mp4"],
        help="Output format: MP3 or MP4. Case-insensitive",
    )
    parser.add_argument(
        "resolution",
        nargs="?",
        type=int,
        default=None,
        help="Desired resolution for MP4 (e.g. 720, 1080); optional for MP3",
    )

    args = parser.parse_args()

    # video_url = input("Video URL: ").strip()
    #
    # format = ""
    # while format == "":
    #     format = input("Output format: (supported: MP3 & MP4): ").strip()
    #
    #     format_lower = format.lower()
    #
    #     if format_lower not in ["mp3", "mp4"]:
    #         print(f"{format.upper()} is an unsupported format.")
    #         format = ""
    #
    # resolution = ""
    # if format.lower() == "mp4":
    #     resolution = input("Desired resolution (e.g. 720, 1080, etc): ").strip()

    downloader(args.url, args.format, args.resolution)


if __name__ == "__main__":
    main()
