# -*- coding:utf-8 -*-
import csv
import json
import sys
import codecs
import pandas as pd

class Channel:
    """
    将json转换成csv
    """

    def __init__(self):
        self.origin_path = 'data/{}'

    def process(self):
        print('Process user data...')
        self._process_user_data()
        print('Process courses data...')
        self._process_movies_date()
        print('Process actions data...')
        self._process_actions_data()
        print('End.')

    def _process_user_data(self, file=''):

    def _process_actions_data(self, file=''):

    def _process_courses_date(self, file=''):


if __name__ == '__main__':
    Channel().process()
