# Inspired by https://github.com/kfei/slack-cleaner

import datetime
import re
import sys
import time
from slacker import Slacker

counter = 0

def prev_ts(days):
    date = datetime.datetime.today()
    delta = datetime.timedelta(days=days)
    return (date - delta).timestamp()

def remove_files(slack, ts):
  # Deletes everything up to the provided ts
  page = 1
  has_more = True
  while has_more:
    res = slack.files.list(ts_to=ts).body

    if not res['ok']:
      print('SLACK MAD')
      sys.exit(1)

    files = res['files']
    current_page = res['paging']['page']
    total_pages = res['paging']['pages']
    has_more = current_page < total_pages
    page = current_page + 1

    for f in files:
      # Delete user file
      delete_file(slack, f)

def delete_file(slack, f):
    # Actually perform the task
    try:
        # No response is a good response
      slack.files.delete(f['id'])
      counter += 1
    except Exception as error:
        counter -= 1
        print("Can't delete ", f['id'])

def main():
    # Use: python main.py token days
    # Example: python main.py xoxojfiwjfoiwejfejwio 30
    # Get token at https://api.slack.com/custom-integrations/legacy-tokens
    # Everything up to x days ago will be deleted
    [_, token, days] = sys.argv
    api = Slacker(token)
    remove_files (api, prev_ts(int(days)))
    return "Deleted " + str(counter) + " files"

print(main())
