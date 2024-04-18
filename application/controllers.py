from flask import Flask, request, redirect, jsonify
from flask import render_template
from flask import current_app as app



@app.route("/", methods=["GET","POST"])
def home():
    if(request.method=="GET"):
        return  render_template('home.html', answer="none")
    if(request.method=="POST"):
        num1=request.form.get('1num')
        num2=request.form.get('2num')
        num3=request.form.get('3num')
        #do  the largest finding
        l=[int(num1),int(num2),int(num3)]
        l.sort()
        largest=l[2]
        return render_template('home.html', answer=largest, num1=num1, num2=num2, num3=num3)