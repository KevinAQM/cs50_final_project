# YouTube Comment Extractor

### Video Demo: <URL HERE>

## Description
This project extracts all comments from a YouTube video and saves them to a CSV file.

## Project Structure
![image](https://github.com/user-attachments/assets/4bc783f8-6b55-4f1a-8300-f66fdbe52a60)

## Requirements

*   Python 3.6+
*   A YouTube Data API v3 key. You can obtain one by following the instructions in the [official documentation](https://developers.google.com/youtube/v3/getting-started).
*   Dependencies are listed in the `requirements.txt` file.

## Installation

1. **Clone the repository:**

    ```bash
    git clone [<repository URL>](https://github.com/KevinAQM/cs50p_final_project.git)
    cd cs50p_final_project
    ```

2. **Create a virtual environment (recommended):**

    ```bash
    python -m venv .venv
    ```

3. **Activate the virtual environment:**

    *   **Windows:**

        ```bash
        .venv\Scripts\activate
        ```

    *   **Linux/macOS:**

        ```bash
        source .venv/bin/activate
        ```

4. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Create a `.env` file in the root of the project and save your YouTube API key:**

    ```
    YOUTUBE_API_KEY=YOUR_API_KEY_HERE
    ```

    **Note:** Replace `YOUR_API_KEY_HERE` with your actual API key.

## Usage

1. **Run the main script `project.py`:**

    ```bash
    python project.py
    ```

2. **The script will prompt you to enter the YouTube video link:**

    ```
    Enter the YouTube link:
    ```

    Enter the full video link, for example: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`

3. **The script will extract the comments and save them to a CSV file inside the `outputs/` folder:**

    The CSV file will be named with the video ID. For example: `outputs/dQw4w9WgXcQ.csv`

    Each row in the CSV will contain the following information for each comment:

    *   `textDisplay`: The comment text.
    *   `likeCount`: The number of likes the comment has.
    *   `authorDisplayName`: The name of the comment's author.
    *   `authorChannelUrl`: The link to the author's channel.
    *   `authorChannelId`: The ID of the author's channel.
    *   `publishedAt`: The date and time the comment was published.
    *   `updatedAt`: The date and time the comment was last updated.

## Notes

*   The YouTube API has a usage quota limit. If the quota is exceeded, the script may fail or not extract all comments.
*   Make sure not to share your API key publicly.

## License

This project is licensed under the [MIT License](LICENSE)
