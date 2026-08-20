import requests


response = requests.get("https://jsonplaceholder.typicode.com/posts", timeout=10)
response.raise_for_status()
posts = response.json()

for post in posts[-5:]:
	print(post["title"])
