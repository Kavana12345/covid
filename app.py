# -*- coding: utf-8 -*-
from flask import Flask,render_template
app=Flask(__name__,static_folder='static')

@app.route('/')
def fun():
    return render_template("firstpage.html")

@app.route('/second')
def fun1():
    return render_template("second.html")

if __name__=="__main__":
    app.run(debug=True)
