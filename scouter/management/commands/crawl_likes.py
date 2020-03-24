import requests
from django.core.management.base import BaseCommand, CommandError
from selenium import webdriver

from scouter.models import Problem


class Command(BaseCommand):
    def handle(self, *args, **options):
        problems = Problem.objects.all()

        for p in problems:
            try:
                driver = webdriver.Chrome(
                    '/Users/jelly/PycharmProjects/leetcode_scouter/scouter/management/commands/chromedriver')
                driver.implicitly_wait(3)
                driver.get("https://leetcode.com/problems/" + p.slug)
                likes_el = driver.find_element_by_css_selector("#app > div > div > div > div > div > div > div > div > div > div > div > div > div > button:nth-child(2) > span")
                likes = int(likes_el.text)

                dislikes_el = driver.find_element_by_css_selector("#app > div > div > div > div > div > div > div > div > div > div > div > div > div > button:nth-child(3) > span")
                dislikes = int(dislikes_el.text)

                p.likes = likes
                p.dislikes = dislikes

                p.save()
            finally:
                driver.close()

