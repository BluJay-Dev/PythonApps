import os

from instabot import Bot
from dotenv import load_dotenv


def env_variables():
    load_dotenv()
    global us, pw
    us = os.getenv('user')
    pw = os.getenv('pass')
    print(f'User: {us} pass: {pw}')


def main(user):
    bot = Bot()
    bot.login(username=us, password=pw)
    my_followers = bot.get_user_followers(user)
    os.chdir('/Users/jayelms/PycharmProjects/course/PythonApps/10_apps/instagram')
    with open(user + '.txt', 'w') as file:
        file.write(f'List of followers for: {user}\n')
        for follower in my_followers:
            f = bot.get_user_info(follower)
            value = f['username']
            file.write(value + '\n')
            print(value)


env_variables()
main(input("Username: "))
