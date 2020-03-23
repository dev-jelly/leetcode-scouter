import json

import requests
from django.core.management.base import BaseCommand, CommandError
from selenium import webdriver

from scouter.models import Problem


class Command(BaseCommand):
    def handle(self, *args, **options):
        response = requests.get('https://leetcode.com/api/problems/all/')
        problems = json.loads(response.json())['stat_status_pairs']

        for p in problems:
            stat = p.stat
            problem = Problem()
            problem.problem_number = stat.question_id
            problem.title = stat.question__title
            problem.slug = stat.question__title_slug
            problem.likes = 0
            problem.difficulty = stat.difficulty.level
            problem.accepted = stat.total_acs
            problem.submitted = stat.total_submitted
            problem.save()

        driver = webdriver.Chrome('/Users/jelly/PycharmProjects/leetcode_scouter/scouter/management/commands/chromedriver')
        driver.implicitly_wait(3)

        driver.close()
