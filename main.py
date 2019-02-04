import requests

TOKEN = "525005235250052352500523d9520f2aaa55250525005230ba586e141c5ed5a99a33da2"

def get_posts():
    url = "https://api.vk.com/method/newsfeed.search"
    params = {
        "access_token": TOKEN,
        "v": "5.92",
        "q": "coca-cola"
    }
    response = requests.get(url, params=params)
    return response.json()

def main():
    print(get_posts())


if __name__ == '__main__':
    main()