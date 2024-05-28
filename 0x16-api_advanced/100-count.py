#!/usr/bin/python3
"""Count it api"""
from collections import Counter
import re
import requests


def count_words(subreddit, word_list, hot_list=[], counts=[], after=None):
    if not counts:
        counts = [0]*len(word_list)
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    if after:
        url += f"?after={after}"
    headers = {'User-Agent': 'Mozilla/5.0 Win11'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json()['data']
    titles = []
    for title in data['children']:
        for word in re.split(r'\W', title['data']['title']):
            titles.append(word.lower())
    for i, word in enumerate(word_list):
        counts[i] += titles.count(word.lower())
    if data['after'] is None:
        word_counts = list(zip(word_list, counts))
        word_counts.sort(key=lambda x: (-x[1], x[0]))
        for word, count in word_counts:
            if count > 0:
                print(f"{word}: {count}")
    else:
        count_words(subreddit, word_list, hot_list, counts, data['after'])
