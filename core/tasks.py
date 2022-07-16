from celery import shared_task

from .utilities import youtube_api_caller, go_back_10_seconds, \
        convert_datetime_to_rfc3339_format, save_item_data_to_db, \
        get_datetime_format_for_yt_api

@shared_task
def update_youtube_data():
    '''
    Task for Updating database with new youtube 
        data from youtube api
    '''

    datetime_to_convert = go_back_10_seconds()
    rfc3339_datetime_format = convert_datetime_to_rfc3339_format(datetime_to_convert)
    rfc3339_datetime_format_for_yt_api = get_datetime_format_for_yt_api(rfc3339_datetime_format)

    response = youtube_api_caller(rfc3339_datetime_format_for_yt_api)

    items = response['items']

    for item in items:
        
        save_item_data_to_db(item)

    print("Updated Youtube Data")
