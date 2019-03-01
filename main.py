# Inspired by https://github.com/kfei/slack-cleaner

import datetime
import re
import sys
import time
from slacker import Slacker

def prev_ts(days):
    date = datetime.datetime.today()
    delta = datetime.timedelta(days=days)
    return (date - delta).timestamp()

def remove_files(slack, ts, types):
  # Deletes everything up to the provided ts
  page = 1
  has_more = True
  counter = 0
  while has_more:
    res = slack.files.list(ts_to=ts, types=types).body

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
        counter += delete_file(slack, f)
    return counter

def delete_file(slack, f):
    # Actually perform the task
    try:
        # No response is a good response
      slack.files.delete(f['id'])
      return 1
    except Exception as error:
        print("Can't delete ", f['id'])
        return 0

def main():
    # Use: python main.py token days
    # Example: python main.py xoxojfiwjfoiwejfejwio 30
    # Get token at https://api.slack.com/custom-integrations/legacy-tokens
    # Everything up to x days ago will be deleted
    [_, token, days, types] = sys.argv
    api = Slacker(token)
    deleted = remove_files (api, prev_ts(int(days)), types)
    return "Deleted " + str(deleted) + " files"

print(main())
