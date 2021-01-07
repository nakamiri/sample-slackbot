import json
import re
from slackbot_settings import CONFLUENCE_BASE_URL, CONFLUENCE_ID, CONFLUENCE_PW
from atlassian import Confluence, errors
from slackbot.bot import listen_to, respond_to


cfl = Confluence(
    url=CONFLUENCE_BASE_URL,
    username=CONFLUENCE_ID,
    password=CONFLUENCE_PW
)


@listen_to(
    '{0}/display/.*/.*'.format(CONFLUENCE_BASE_URL)
)
def response_confluence_page_by_title(message):
    url = re.search('https?://[\w/:%#\$&\?\(\)~\.=\+\-]+',  # noqa: W605
                    message.body['text']).group()

    page_param = re.search(
        '{0}/display/(.*)/(.*)'.format(CONFLUENCE_BASE_URL), url).groups()

    space = page_param[0]
    title = page_param[1]

    if not cfl.page_exists(space=space, title=title):
        return

    attachments = [
        {
            'title': '{0}: {1}'.format(space, title),
            'title_link': url,
            'color': '#000080'
        }
    ]

    message.send_webapi(text='', attachments=json.dumps(attachments))


@respond_to(
    '{0}/pages/viewpage.action\?pageId=([0-9]*)'.format(  # noqa: W605
        CONFLUENCE_BASE_URL
        )
)
@listen_to(
    '{0}/pages/viewpage.action\?pageId=([0-9]*)'.format(  # noqa: W605
        CONFLUENCE_BASE_URL
        )
)
def response_confluence_page_by_id_summary(message, group1):
    page_id = group1

    try:
        page = cfl.get_page_by_id(page_id=page_id)
    except errors.ApiError:
        # message.send('{} not found'.format(page_id))
        return

    title = page['title']
    space = page['space']['name']

    attachments = [
        {
            'title': '{0}: {1}'.format(space, title),
            'title_link': '{0}/pages/viewpageaction?pageId={1}'.format(
                CONFLUENCE_BASE_URL, page_id
            ),
            'color': '#000080'
        }
    ]

    message.send_webapi(text='', attachments=json.dumps(attachments))
