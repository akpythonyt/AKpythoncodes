from flask import Flask,request,render_template
import pyshorteners
app=Flask(__name__)

@app.route('/')
def home():
    if request.method == 'GET':
        url=request.args['name']
        s=pyshorteners.Shortener()
        shorter=s.tinyurl.short(url)
        return shorter

    return render_template('home.html')

if __name__=='__main__':
    app.run(debug=True)