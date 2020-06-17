from flask import Flask, render_template as render
import matplotlib.pyplot as plt
app = Flask(__name__)


@app.route('/')
def home():
    name = "darani"
    # plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
    return render ("home.html")

@app.route('/developers')
def developers():
    name = "darani"
    return render ("developer.html",name=name)

if __name__=="__main__" :
    app.run(debug=True)
