import json

from flask import Flask, render_template
from markdown import markdown as md

app = Flask(__name__)


@app.route('/test')
def ecnu_faq_from_json():
    faq_list = json.load(open('ecnu_faq.json', encoding='utf-8'))
    for faq in faq_list:
        faq[1] = md(faq[1])
    return render_template('ecnu_faq.html', faqs=faq_list)


if __name__ == '__main__':
    app.run(debug=True)
