from flask import Flask,render_template,request
app= Flask(__name__)

@app.route('/',methods=['GET','POST'])
def my_route():
    if request.method=='GET':
        return render_template('main.html')

@app.route('/info')
def info():
    if request.method=='GET':
        return render_template('info.html')

if __name__=='__main__':
    app.run(host='localhost',port=5000,debug=True)


