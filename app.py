from flask import Flask, render_template

app = Flask(__name__)

@app.route('/market')
def market():
    return render_template('virtual_market.html')

if __name__ == "__main__":
    app.run(debug=True)
