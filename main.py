import requests
import datetime
from plotly import tools
import plotly.plotly as py
import plotly.graph_objs as go

tools.set_credentials_file(username='starovoitov.anton', api_key='eWEiOWPqQYFUrS0xiNmo')


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
    dates_list = []
    for day in range(week):
        temp_day = date - datetime.timedelta(days=1)
        dates_list.append(temp_day)
        timestamp_list.append(temp_day.timestamp())
        date = temp_day
    return timestamp_list, dates_list


def create_graph(dates, counts):
    coca_cola_posts = go.Bar(
        x=[date for date in dates],
        y=[count for count in counts]
    )
    data = [coca_cola_posts, ]

    py.plot(data, filename='basic-line', auto_open=False)


def main():
    date = datetime.datetime.now()
    dates_timestamps, dates_list = get_timestamp_tuple(date)
    all_posts_counts = []
    for timestamp in dates_timestamps:
        data_json = get_posts(timestamp)
        current_count = count_posts(data_json)
        all_posts_counts.append(current_count)
    create_graph(all_posts_counts, dates_list)


if __name__ == '__main__':
    main()

