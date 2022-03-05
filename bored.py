import requests


response = requests.get("http://www.boredapi.com/api/activity/").json()

print(f"""\n------------------------------------\nA fun activity for you to do:

Activity name: {response["activity"]}
Accessibility: {response["accessibility"]}
Category: {response["type"]}
Number of participants: {response["participants"]}
Link/resource (if valid): {response["link"]}
      
""")
