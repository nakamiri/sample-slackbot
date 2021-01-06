from requests.models import HTTPError
import json
from slackbot.bot import listen_to
from atlassian import Jira
from slackbot_settings import JIRA_ID, JIRA_PW, JIRA_BASE_URL


@listen_to('(TEST-[0-9]*)')
def response_jira_ticket_summary(message, group1):
    jira = Jira(
        url=JIRA_BASE_URL,
        username=JIRA_ID,
        password=JIRA_PW
    )

    issue_id = group1

    try:
        issue = jira.issue(issue_id)
    except HTTPError:
        message.send('{} not found'.format(issue_id))
        return

    summary = issue['fields']['summary']

    attachments = [
        {
            'title': '{0}: {1}'.format(issue_id, summary),
            'title_link': '{0}/browse/{1}'.format(JIRA_BASE_URL, issue_id),
            'color': '#000080'
        }
    ]

    message.send_webapi(text='', attachments=json.dumps(attachments))
