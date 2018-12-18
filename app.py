from flask import Flask,render_template
import datetime
app = Flask(__name__)

# Index Route
@app.route('/')
def index():
    now = datetime.datetime.now()    
    newYear = now.month == 1 and now.day == 1
    # newYear = True
    return render_template('index.html',new_year = newYear)

#if __name__ == '__main__':
#    app.run(debug = True,port = 3030)

