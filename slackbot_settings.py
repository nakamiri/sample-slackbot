from os import environ


# botアカウントのトークンを指定
API_TOKEN = environ['API_TOKEN']

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "何言ってんだこいつ"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins']

JIRA_BASE_URL = environ['JIRA_BASE_URL']
JIRA_ID = environ['JIRA_ID']
JIRA_PW = environ['JIRA_PW']

CONFLUENCE_BASE_URL = environ['CONFLUENCE_BASE_URL']
CONFLUENCE_ID = environ['CONFLUENCE_ID']
CONFLUENCE_PW = environ['CONFLUENCE_PW']
