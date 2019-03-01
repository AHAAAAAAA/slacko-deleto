Everything up to x days ago of filetypes a,b,c will be deleted.

## Setup
1. `pipenv install`

or just `pip install slacker` like a normal person

## Use
`(pipenv run) python main.py token days filetypes`

Example: `python main.py xoxojfiwjfoiwejfejwio 30 images,zips`

filetypes: ` all, spaces (Posts), snippets, images, gdocs, zips, pdfs`

Get token [here](https://api.slack.com/custom-integrations/legacy-tokens)

Inspired by [slack-cleaner](https://github.com/kfei/slack-cleaner)
