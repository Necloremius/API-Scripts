import requests; import webbrowser; webbrowser.open(requests.get("http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true").json()[0], new=2)


