# -*- coding: utf8


from flask import Flask, make_response
from flask import redirect
from flask import request


import random


app = Flask(__name__)


URLS = [
    'https://docs.google.com/forms/d/e/1FAIpQLSdAfvuQGHb5N9Jj-cbPMNCsqIwOOtLDeqqzkE98WYAnAcx7jA/viewform?usp=sf_link',
    'https://docs.google.com/forms/d/e/1FAIpQLSeHS-2MrkT71dBj95h2wdIWLNsmgEDoMETOucoJP5hZhfmRTg/viewform?usp=sf_link',
    'https://docs.google.com/forms/d/e/1FAIpQLScdfv3wIY_KOOcs-jQHIpg-4R3JzBnA2tePQOuE8cUsZJ_E-Q/viewform?usp=sf_link',
    'https://docs.google.com/forms/d/e/1FAIpQLSf5YuT7iRhLVHRaqTzvFafJaDLkoIA07Qk_MAJhM-N0ASizUQ/viewform?usp=sf_link',
    'https://docs.google.com/forms/d/e/1FAIpQLScfU82UZutDdWkHXTJ9vWd9xKOL0ouT8jqalevH8meX2RjEsQ/viewform?usp=sf_link',
    'https://docs.google.com/forms/d/e/1FAIpQLScHqGp-Ylt84kyFIRrkbGdeIuP6Jj-EhEfkA0olYl7oMJ-hiQ/viewform?usp=sf_link',
    'https://docs.google.com/forms/d/e/1FAIpQLSd0gqQf09YoXQ69qSx4vC8G-xaTNut-qxb9TOeMX03na6ul1Q/viewform?usp=sf_link',
    'https://docs.google.com/forms/d/e/1FAIpQLSe3gGjJYvY8Uw-lkwJT_6bSMZKVntkIBUd5q8B-Q0c4CKJZUw/viewform?usp=sf_link',
    'https://docs.google.com/forms/d/e/1FAIpQLSeQu_YvCYydyH9nlmDhkiUe8Hpn8XZctvflj3zIK1tUNBWhFg/viewform?usp=sf_link',
    'https://docs.google.com/forms/d/e/1FAIpQLSd6FxKN96olxFr1a363ILhAxKU0fBVvGIvQBgKIpEGlYeMp5w/viewform?usp=sf_link',
    'https://docs.google.com/forms/d/e/1FAIpQLSdpCnj6tfXBZ9Wl8LJVyi42XT2EvaOjFDSDa_xi7ksXLY7Nug/viewform?usp=sf_link',
    'https://docs.google.com/forms/d/e/1FAIpQLSfWptB9uAFIPMDmtZp-tPVCh4eZgkc4t8humQrE3fnRDaOS5A/viewform?usp=sf_link',
    'https://docs.google.com/forms/d/e/1FAIpQLSeIE6SLeKXgpyBT_T6x3xAA_Lj-0keflXoMtLbjv8Twjn9WEQ/viewform?usp=sf_link',
    'https://docs.google.com/forms/d/e/1FAIpQLSc_nVoziR1RlMnD31FzAR96JeHqnfSfCkxqQf5Kz-DIHGWpRg/viewform?usp=sf_link',
    'https://docs.google.com/forms/d/e/1FAIpQLSc6JBCPeuLaLoaxvKee3TktI2teD9ONb6WHHKqhgytfcrHIpA/viewform?usp=sf_link',
    'https://docs.google.com/forms/d/e/1FAIpQLScAt-nsvPu85TFK8mPzUyILKXMFJ34aye_PpFeOqkxiiDfzsA/viewform?usp=sf_link'
]


def to_list(cookie: str) -> list:
    return cookie.split()


@app.route('/')
def hello():
    seen = to_list(request.cookies.get('seen', ''))

    to_choose = list(set(URLS).difference(set(seen)))
    random.shuffle(to_choose)

    if len(to_choose) > 0:
        url = to_choose[0]
        seen.append(url)
        resp = redirect(url, code=302)
        resp.set_cookie('seen', ' '.join(seen))
    else:
        resp = make_response('Obrigado!')
    return resp


if __name__ == '__main__':
    app.run()
