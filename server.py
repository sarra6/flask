from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def play():
    # Level 1: Render three beautiful looking blue boxes
    return render_template('play.html', times=3, color='blue')

@app.route('/play/<int:x>')
def play_x_times(x):
    # Level 2: Display beautiful looking blue boxes x times
    return render_template('play.html', times=x, color='blue')

@app.route('/play/<int:x>/<color>')
def play_x_times_colored(x, color):
    # Level 3: Display beautiful looking boxes x times in the specified color
    return render_template('play.html', times=x, color=color)

if __name__ == '__main__':
    app.run(debug=True)
