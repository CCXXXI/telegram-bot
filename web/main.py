import json

from flask import Flask, render_template
from markdown import markdown as md

app = Flask(__name__)


@app.route('/ecnu')
def ecnu_faq():
    faq_list = json.load(open('ecnu_faq.json'))
    for faq in faq_list:
        faq[1] = md(faq[1])
    return render_template('ecnu_faq.html', faqs=faq_list)


if __name__ == '__main__':
    app.run('0.0.0.0', 80, debug=False)
