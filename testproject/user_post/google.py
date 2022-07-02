import requests

url = "https://google-search3.p.rapidapi.com/api/v1/serp/"

payload = {
	"query": "q=google+search+api&num=100",
	"website": "https://rapidapi.com"
}
headers = {
	"content-type": "application/json",
	"X-User-Agent": "desktop",
	"X-Proxy-Location": "US",
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "google-search3.p.rapidapi.com"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)