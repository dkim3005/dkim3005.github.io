
import requests
import json
# //

url = "https://kauth.kakao.com/oauth/token"

data = {
    "grant_type" : "authorization_code",
    "client_id" : "151a95b6bf34800b279117dc9f379d33",
    "redirect_uri" : "https://dkim3005.github.io/",
    "code"         : 'ASeiSBi-LAhlJQb3cHGzXI1BWbJxlTzVyb4RyxZbrsPThyA5BJ5wNQAAAAQKDSAbAAABlp_cYanE017PSiBv1Q'
}
response = requests.post(url, data=data)

tokens = response.json()

print(tokens)