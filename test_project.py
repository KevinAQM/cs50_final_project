import pytest
import os
from project import extract_video_id, parse_comment, get_csv_filepath

def test_extract_video_id_valid_url_with_v():
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    assert extract_video_id(url) == "dQw4w9WgXcQ"

def test_extract_video_id_valid_url_with_youtu_be():
    url = "https://youtu.be/dQw4w9WgXcQ"
    assert extract_video_id(url) == "dQw4w9WgXcQ"

def test_extract_video_id_invalid_url():
    url = "https://www.youtube.com/playlist?list=PL123456789"
    with pytest.raises(ValueError):
        extract_video_id(url)

def test_parse_comment():
    comment_item = {
        "snippet": {
            "topLevelComment": {
                "snippet": {
                    "textDisplay": "This is a test comment.",
                    "likeCount": 10,
                    "authorDisplayName": "Test User",
                    "authorChannelUrl": "http://www.youtube.com/channel/UC123456789",
                    "authorChannelId": {"value": "UC123456789"},
                    "publishedAt": "2023-10-27T12:00:00Z",
                    "updatedAt": "2023-10-27T12:00:00Z",
                }
            }
        }
    }
    expected_comment_data = {
        "textDisplay": "This is a test comment.",
        "likeCount": 10,
        "authorDisplayName": "Test User",
        "authorChannelUrl": "http://www.youtube.com/channel/UC123456789",
        "authorChannelId": "UC123456789",
        "publishedAt": "2023-10-27T12:00:00Z",
        "updatedAt": "2023-10-27T12:00:00Z",
    }
    assert parse_comment(comment_item) == expected_comment_data


def test_get_csv_filepath():
    video_id = "dQw4w9WgXcQ"
    expected_filepath = os.path.normpath(f"outputs/{video_id}.csv")
    assert get_csv_filepath(video_id) == expected_filepath