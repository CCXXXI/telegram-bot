import json
import sqlite3
from pprint import pformat

from flask import Flask, render_template, request, jsonify
from markdown import markdown as md

db_file = 'ecnu_faq.sqlite'
vote_limit = -3

app = Flask(__name__)


@app.route('/ecnu')
def ecnu_faq_from_json():
    faq_list = json.load(open('ecnu_faq.json', encoding='utf-8'))
    for faq in faq_list:
        faq[1] = md(faq[1])
    return render_template('ecnu_faq.html', faqs=faq_list)


@app.route('/test')
def test():
    r = dict()
    con = sqlite3.connect('ecnu_faq.sqlite')
    cur = con.cursor()
    cur.execute('select * from q')
    r['select * from q'] = cur.fetchall()
    cur.execute('select * from a')
    r['select * from a'] = cur.fetchall()
    return '<pre>' + pformat(r, sort_dicts=False) + '</pre>'


@app.route('/add_q', methods=['POST'])
def _add_q():
    para: dict = request.get_json()
    add_q(para['q'])
    return 'done'


@app.route('/add_a', methods=['POST'])
def _add_a():
    para: dict = request.get_json()
    add_a(para['q'], para['a'])
    return 'done'


@app.route('/get_q', methods=['POST'])
def _get_q():
    para: dict = request.get_json()
    return jsonify(get_q(para['q'] if para and 'q' in para else None))


@app.route('/get_a', methods=['POST'])
def _get_a():
    para: dict = request.get_json()
    return jsonify(get_a(para['q'] if para and 'q' in para else None))


@app.route('/vote_q_up', methods=['POST'])
def _vote_q_up():
    para: dict = request.get_json()
    vote_q(para['q'], 1)
    return 'done'


@app.route('/vote_q_down', methods=['POST'])
def _vote_q_down():
    para: dict = request.get_json()
    vote_q(para['q'], -1)
    return 'done'


@app.route('/vote_a_up', methods=['POST'])
def _vote_a_up():
    para: dict = request.get_json()
    vote_a(para['q'], para['a'], 1)
    return 'done'


@app.route('/vote_a_down', methods=['POST'])
def _vote_a_down():
    para: dict = request.get_json()
    vote_a(para['q'], para['a'], -1)
    return 'done'


@app.route('/del_q', methods=['POST'])
def _del_q():
    para: dict = request.get_json()
    del_q(para['q'])
    return 'done'


@app.route('/del_a', methods=['POST'])
def _del_a():
    para: dict = request.get_json()
    del_a(para['q'], para['a'])
    return 'done'


def add_q(q: str):
    con = sqlite3.connect(db_file)
    cur = con.cursor()

    cur.execute('insert into q values (?,0)', (q,))

    con.commit()


def add_a(q: str, a: str):
    con = sqlite3.connect(db_file)
    cur = con.cursor()

    cur.execute('insert into a values (?,?,0)', (q, a))

    con.commit()


def get_q(q: str = None):
    con = sqlite3.connect(db_file)
    cur = con.cursor()

    if q is None:
        cur.execute('select * from q where vote>=?', (vote_limit,))
    else:
        cur.execute('select * from q where q=? and vote>=?', (q, vote_limit))
    return [{'q': qa[0], 'vote': qa[1]} for qa in cur.fetchall()]


def get_a(q: str = None):
    con = sqlite3.connect(db_file)
    cur = con.cursor()

    if q is None:
        cur.execute('select * from a where vote>=?', (vote_limit,))
    else:
        cur.execute('select * from a where q=? and vote>=?', (q, vote_limit))
        return [{
            'q': qa[0],
            'a': qa[1],
            'vote': qa[2]
        } for qa in cur.fetchall()]


def vote_q(q: str, delta: int):
    con = sqlite3.connect(db_file)
    cur = con.cursor()

    cur.execute('select vote from q where q=?', (q,))
    r = cur.fetchone()
    assert r
    cur.execute('update q set vote=? where q=?', (r[0] + delta, q))

    con.commit()


def vote_a(q: str, a: str, delta: int):
    con = sqlite3.connect(db_file)
    cur = con.cursor()

    cur.execute('select vote from a where q=? and a=?', (q, a))
    r = cur.fetchone()
    assert r
    cur.execute('update a set vote=? where q=? and a=?', (r[0] + delta, q, a))

    con.commit()


def del_q(q: str):
    con = sqlite3.connect(db_file)
    cur = con.cursor()

    cur.execute('delete from q where q=?', (q,))

    con.commit()


def del_a(q: str, a: str):
    con = sqlite3.connect(db_file)
    cur = con.cursor()

    cur.execute('delete from a where q=? and a=?', (q, a))

    con.commit()


if __name__ == '__main__':
    app.run(debug=True)
