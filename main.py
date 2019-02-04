import requests
import datetime


TOKEN = "525005235250052352500523d9520f2aaa55250525005230ba586e141c5ed5a99a33da2"


def get_posts(timestamp):
    url = "https://api.vk.com/method/newsfeed.search"
    params = {
        "access_token": TOKEN,
        "v": "5.92",
        "q": "coca-cola",
        "count": "200",
        "start_time": f"{timestamp}",

    }
    response = requests.get(url, params=params)
    return response.json()


def count_posts(json):
    result = len(json['response']['items'])
    return result


def get_timestamp_tuple(date):
    week = 7  # days
    timestamp_list = []
    for day in range(week):
        temp_day = date - datetime.timedelta(days=1)
        timestamp_list.append(temp_day.timestamp())
    return timestamp_list


def main():
    date = datetime.datetime.now()
    dates_timestamps = get_timestamp_tuple(date)
    all_posts = []
    total_posts = []
    for timestamp in dates_timestamps:
        data_json = get_posts(timestamp)
        all_posts.append(data_json)
        current_count = count_posts(data_json)
        total_posts.append(current_count)
    print(sum(total_posts))


if __name__ == '__main__':
    main()
