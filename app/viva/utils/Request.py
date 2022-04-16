#!/usr/bin/env python3

import requests
from django.core.cache import cache


class Request():
    """request hackerank API"""

    def store_result(self):
        """store result of request in cache"""
        lst = []
        res = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty').json()
        for i in res:
            r = requests.get('https://hacker-news.firebaseio.com/v0/item/' + str(i) +'.json?print=pretty').json()
            lst.append({'ID': r.get('id'), 'titulo': r.get('title')})
        cache.set('full_lst', lst)


    def req(self, idx, n_max):
        """request hackerank API"""
        #lst = []
        res = cache.get('full_lst')
        return res[idx:n_max]

        """ res = res[idx:]
        for i in res[:n_max]:
            r = requests.get('https://hacker-news.firebaseio.com/v0/item/' + str(i) +'.json?print=pretty').json()
            lst.append({'ID': r.get('id'), 'titulo': r.get('title')})
        return lst """

    def req_one(self, idx, n_max):
        """request hackerank API"""
        lst = []
        res = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty').json()
        res = res[idx:]
        for i in res[:n_max]:
            r = requests.get('https://hacker-news.firebaseio.com/v0/item/' + str(i) +'.json?print=pretty').json()
            lst.append({'ID': r.get('id'), 'titulo': r.get('title')})
        return lst
