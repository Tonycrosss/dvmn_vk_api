import requests

TOKEN = "525005235250052352500523d9520f2aaa55250525005230ba586e141c5ed5a99a33da2"

def get_posts():
    url = "https://api.vk.com/method/newsfeed.search"
    params = {
        "access_token": TOKEN,
        "v": "5.92",
        "q": "coca-cola",
        "count": "200",
        "start_time": "1549152000"
    }
    response = requests.get(url, params=params)
    return response.json()


def count_posts(json):
    result = len(json['response']['items'])
    return result


def main():
    data_json = get_posts()
    total_posts = count_posts(data_json)


if __name__ == '__main__':
    main()