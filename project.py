import os
import googleapiclient.discovery
from dotenv import load_dotenv
import csv

# Constants
OUTPUT_DIR = "outputs"

# --- Helper Functions ---

def extract_video_id(url):
    """
    Extracts the video ID from a YouTube URL.

    Args:
        url: The YouTube URL.

    Returns:
        The video ID, or raises ValueError if the URL is invalid.
    """
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1]
    else:
        raise ValueError("Invalid YouTube link")

def build_youtube_client(api_key):
    """
    Builds a YouTube API client.

    Args:
        api_key: Your YouTube API key.

    Returns:
        A googleapiclient.discovery.Resource object for interacting with the YouTube API.
    """
    return googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

def fetch_comments_page(youtube, video_id, page_token=None):
    """
    Fetches a single page of comments for a given video.

    Args:
        youtube: The YouTube API client.
        video_id: The ID of the video.
        page_token: The token for the next page of results (optional).

    Returns:
        The API response containing the comments.
    """
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        pageToken=page_token,
        maxResults=100,
    )
    return request.execute()

def parse_comment(item):
    """
    Parses a single comment item from the API response.

    Args:
        item: A single comment item from the API response.

    Returns:
        A dictionary containing the extracted comment data.
    """
    comment_info = item["snippet"]["topLevelComment"]["snippet"]
    return {
        "textDisplay": comment_info["textDisplay"],
        "likeCount": comment_info["likeCount"],
        "authorDisplayName": comment_info["authorDisplayName"],
        "authorChannelUrl": comment_info["authorChannelUrl"],
        "authorChannelId": comment_info["authorChannelId"]["value"],
        "publishedAt": comment_info["publishedAt"],
        "updatedAt": comment_info["updatedAt"],
    }

def get_all_comments(youtube, video_id):
    """
    Retrieves all comments for a given video.

    Args:
        youtube: The YouTube API client.
        video_id: The ID of the video.

    Returns:
        A list of dictionaries, where each dictionary represents a comment.
    """
    comments_data = []
    next_page_token = None

    while True:
        response = fetch_comments_page(youtube, video_id, next_page_token)

        for item in response["items"]:
            comments_data.append(parse_comment(item))

        next_page_token = response.get("nextPageToken")

        if not next_page_token:
            break

    return comments_data

def ensure_output_directory():
    """Ensures that the 'outputs' directory exists."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_csv_filepath(video_id):
    """
    Generates the CSV filepath for a given video ID.

    Args:
        video_id: The ID of the video.

    Returns:
        The full filepath for the CSV file.
    """
    return os.path.join(OUTPUT_DIR, f"{video_id}.csv")

def save_comments_to_csv(comments_data, video_id):
    """
    Saves comments data to a CSV file in the 'outputs/' directory.

    Args:
        comments_data: A list of dictionaries, where each dictionary represents a comment.
        video_id: The ID of the video.
    """
    ensure_output_directory()
    csv_filename = get_csv_filepath(video_id)

    fieldnames = [
        "textDisplay",
        "likeCount",
        "authorDisplayName",
        "authorChannelUrl",
        "authorChannelId",
        "publishedAt",
        "updatedAt",
    ]

    with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for comment_data in comments_data:
            writer.writerow(comment_data)

    print(f"✓ Comments saved to {csv_filename}")

# --- Main Function ---

def main():
    """
    Main function to run the script.
    """
    youtube_url = input("Enter the YouTube link: ")
    load_dotenv()
    api_key = os.getenv("YOUTUBE_API_KEY")

    try:
        video_id = extract_video_id(youtube_url)
        youtube = build_youtube_client(api_key)
        comments_data = get_all_comments(youtube, video_id)

        print(f"✓ Extracted {len(comments_data)} comments from the link: {youtube_url}")
        save_comments_to_csv(comments_data, video_id)

    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()