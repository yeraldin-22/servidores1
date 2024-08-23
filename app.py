from flask import Flask, render_template

servidor1 = Flask(__name__)


@servidor1.route('/inicio')
def index():
    return render_template('index.html')

if __name__=="__main__":
    servidor1.run(debug=True)
