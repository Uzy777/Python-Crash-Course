# 17-2. Active Discussions:     Using the data from 'hn_submissions.py', make a bar chart showing the most active discussions
#                               currently happening on Hacker News. The height of each bar should correspond to the number of
#                               comments each submission has. The label for each bar should include the submission's title and
#                               act as a link to the discussion page for that submission. If you get a 'KeyError' when creating a chart,
#                               use a 'try-except' block to skip over the promotional posts.

from operator import itemgetter

import requests
import plotly.express as px

# Make an API call and check the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:6]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

titles = [f"<a href='{item['hn_link']}'>{item['title']}</a>" for item in submission_dicts]
comments = [item['comments'] for item in submission_dicts]


# Make visualisation.
title = "Most Active Discussions currently on Hacker News"
labels = {'x': 'Submission Title', 'y': 'Number of Comments'}
fig = px.bar(x=titles, y=comments, title=title, labels=labels)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20, xaxis_tickangle=-45)  # Rotate x labels if they're long)

fig.show()