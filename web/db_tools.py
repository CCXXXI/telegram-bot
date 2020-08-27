import json
import sqlite3


def json2db():
    faqs = json.load(open('ecnu_faq.json', encoding='utf-8'))

    con = sqlite3.connect('ecnu_faq.sqlite')
    cur = con.cursor()
    cur.executemany('insert into q values (?,0)', ((qa[0],) for qa in faqs))
    cur.executemany('insert into a values (?,?,0)', faqs)
    con.commit()
