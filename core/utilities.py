import requests
import datetime
import rfc3339
import environ

from core.models import YTData


# Initialise environment variables
env = environ.Env()
environ.Env.read_env()


def youtube_api_caller(publishedAfter):
    '''
    Function used for calling youtube api with 
        multiple parameters and returns youtube
        data
    '''

    developer_key = env("YT_API_KEY")
    type_of_data = "video"
    order = "date"
    q = "football"
    part = "snippet"

    url = ( f"https://www.googleapis.com/youtube/v3/search/?key={developer_key}"
            f"&type={type_of_data}&order={order}&publishedAfter={publishedAfter}"
            f"&q={q}&part={part}" )

    response = requests.get(url)

    return response.json()

def go_back_10_seconds():
    '''
    Function used for getting current date and time
        then move 10 seconds in the past and return
        datetime 10 seconds in past
    '''

    current_datetime = datetime.datetime.now()
    ten_seconds_before = current_datetime - datetime.timedelta(seconds=10)

    return ten_seconds_before

def convert_datetime_to_rfc3339_format(datetime_to_convert):
    '''
    Function used for converting datetime object
        to rfc3339 formated datetime
    '''

    rfc3339_format_datetime = rfc3339.rfc3339(datetime_to_convert)

    return rfc3339_format_datetime

def get_datetime_format_for_yt_api(raw_datetime):
    '''
    Function used for getting datetime
        as per youtube api requirement
    '''

    return raw_datetime[:-6]+"Z"

def save_item_data_to_db(item):
    '''
    Function used for saving specific data 
        as per requirement in database
    '''

    title = item["snippet"]["title"]
    description = item["snippet"]["description"]
    published_at = item["snippet"]["publishedAt"]
    default_thumbnail_url = item["snippet"]["thumbnails"]["default"]["url"]
    medium_thumbnail_url = item["snippet"]["thumbnails"]["medium"]["url"]
    high_thumbnail_url = item["snippet"]["thumbnails"]["high"]["url"]

    yt_data = YTData(title=title, description=description, published_at=published_at, 
                        thumbnail_url_default=default_thumbnail_url, 
                        thumbnail_url_medium=medium_thumbnail_url, thumbnail_url_high=high_thumbnail_url)
    yt_data.save()