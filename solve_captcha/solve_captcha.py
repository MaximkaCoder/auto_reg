import os
from twocaptcha import TwoCaptcha


def solveRecaptcha(site_key, url):
    api_key = os.getenv('APIKEY_2CAPTCHA', '04e12e011fb377b81df53b355507b657')

    solver = TwoCaptcha(api_key)

    try:
        result = solver.recaptcha(
            sitekey=site_key,
            url=url)

    except Exception as e:
        print(e)

    else:
        return result
