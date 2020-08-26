import json

from flask import Flask, render_template

app = Flask(__name__)

faq_list = json.load(open('ecnu_faq.json'))


@app.route('/ecnu')
def ecnu_faq():
    return render_template('ecnu_faq.html', faqs=faq_list)


if __name__ == '__main__':
    app.run('0.0.0.0', 80, debug=False)
