
import requests
import json
# //

url = "https://kauth.kakao.com/oauth/token"

data = {
    "grant_type" : "authorization_code",
    "client_id" : "151a95b6bf34800b279117dc9f379d33",
    "redirect_uri" : "https://dkim3005.github.io/",
    "code"         : '7kuGFshqE1o9wJvGlxEpUYG4So1dqJ4PeTDiuL9CK9BCWegmL4j01gAAAAQKDRTdAAABlp_n7Xym1x-HnlkNwQ'
}
response = requests.post(url, data=data)

tokens = response.json()

print(tokens)