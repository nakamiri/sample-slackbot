from slackbot.bot import respond_to


@respond_to('^リンク$')
@respond_to('^link$')
def response_thread_permalink(message):
    channel_id = message.channel._body['id']
    thread_ts = message.thread_ts

    thread_permalink_raw = message._client.webapi.chat.get_permalink(
        channel_id, thread_ts
    )
    thread_permalink = thread_permalink_raw.body['permalink']

    message.reply(thread_permalink)
