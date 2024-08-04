# YouTube Audio and Lyrics Extractor

## Overview

This Flask application allows users to search for and download the audio of a song from YouTube. Additionally, users can fetch the transcript (lyrics) of a YouTube video.

## Features

- **Home Page**: Displays the base template.
- **Songs**: Fetches and downloads the audio of a specified song from YouTube.
- **Lyrics**: Retrieves the transcript (lyrics) of a specified YouTube video.

## Requirements

- Flask
- youtube_transcript_api
- scrapetube
- pytube
- moviepy
- os

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/your-repo/your-project.git
   cd your-project
   ```

2. Create a virtual environment and activate it:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```sh
   pip install Flask youtube_transcript_api scrapetube pytube moviepy
   ```

## Usage

1. Run the Flask application:

   ```sh
   python app.py
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Endpoints

### Home

- **URL**: `/`
- **Method**: GET
- **Description**: Displays the base template.

### Songs

- **URL**: `/songs`
- **Method**: GET
- **Parameters**:
  - `song` (string) - The name of the song to search for.
- **Description**: Fetches and downloads the audio of a specified song from YouTube. The audio is saved in the `static` folder and can be accessed through a provided link.

### Lyrics

- **URL**: `/lyrics`
- **Method**: POST
- **Request Body**:
  - `lyrics` (string) - The YouTube video ID to fetch the transcript for.
- **Description**: Retrieves the transcript (lyrics) of a specified YouTube video in JSON format.

## Example

To download the audio of a song:

1. Navigate to `http://127.0.0.1:5000/songs?song=Your+Song+Name`
2. The audio will be saved in the `static` folder, and the link to the audio file will be provided.

To get the lyrics of a YouTube video:

1. Make a POST request to `http://127.0.0.1:5000/lyrics` with a JSON body:
   ```json
   {
     "lyrics": "YouTube_video_id"
   }
   ```
2. The transcript will be returned in JSON format.

## Author

Praveen KR  
LinkedIn: [Praveen KR](https://www.linkedin.com/in/mepraveenkr/)
