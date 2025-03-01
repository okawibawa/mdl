# MDL

This simple script was created to streamline downloading YouTube videos and audio for use in my other projects, where I frequently need both MP4 videos and MP3 audio files. My personal use case involves adding an alias to my .zshrc for quick access and customizing the download folder to fit my workflow. Built with yt-dlp, this command-line tool makes it easy to grab media with a single command.

## Features

- Download YouTube videos as MP4 with a specified maximum resolution (e.g., 1080p).

- Extract audio from YouTube videos and save as MP3 (192 kbps by default).

- Saves files to a `downloads/` folder in the project root.

- Error handling for invalid URLs or unavailable formats.

- Cross-platform support (tested on Arch Linux and macOS).

## Prerequisites

- **Python 3.7+:** Ensure Python is installed (`python --version`).

- **ffmpeg:** Required for MP4 merging and MP3 conversion.

    - **Arch Linux:** `sudo pacman -S ffmpeg`

- **Verify:** `ffmpeg -version`

## Installation

1. Clone the Repository (if using Git):

```bash
git clone https://github.com/okawibawa/mdl.git
cd youtube_downloader
```

Or manually create the folder structure and copy `downloader.py` into `src/`.

2. Set Up a Virtual Environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
```

3. Install Dependencies:

```bash
pip install -r requirements.txt
```

4. Ensure ffmpeg is Installed:

- See "Prerequisites" above.

## Usage

Run the script from the project root:

```bash
python src/downloader.py <url> <format> [resolution]
```

### Arguments

- `<url>`: YouTube video URL (required).

- `<format>`: Output format, either "MP3" or "MP4" (case-insensitive, required).

- `[resolution]`: Maximum resolution in pixels for MP4 (e.g., 720, 1080); optional for MP3, required for MP4.

## Example runs

- Download as MP3:

```bash
python src/downloader.py "https://youtu.be/cbHkzwa0QmM" mp3
```

Saves to `downloads/{video_title}.mp3`

- Download as MP4:

```bash
python src/downloader.py "https://youtu.be/cbHkzwa0QmM" mp4 1080
```

Saves to `downloads/{video_title}.mp4`

- Get help:

```bash
python src/downloader.py --help
```
