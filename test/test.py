import requests
import json
import io

video_id = '7wnove7K-ZQ'
api_key= "AIzaSyDjSwM29FKKygXoZky8Xa4p6H9GMsMx154"
response = requests.get(f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}')

video_info = json.loads(response.text)
try:
    thumbnail_url = video_info['items'][0]['snippet']['thumbnails']['high']['url']
    thumbnail = requests.get(thumbnail_url)
    image = io.BytesIO(thumbnail.content)
    likes = int(video_info['items'][0]['statistics'].get('likeCount', 0))
    print(likes)
    title = video_info['items'][0]['snippet']['title']
    description = video_info['items'][0]['snippet']['description']
    url = f"https://www.youtube.com/watch?v={video_id}"

except Exception as e:
    print(e)