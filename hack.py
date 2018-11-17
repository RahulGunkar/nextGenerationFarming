from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
   return "hiii"
   #return render_template('homePage.html')
'''
@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      results = username = request.form['userInput']
      if results == '1':
      	sell = True
      	return render_template("sellCrop.html",sell = sell)


@app.route('/sell',methods = ['POST', 'GET'])  
def sell():
   if request.method == 'POST':
      results = username = request.form['userInput']
      if results == '1':
      	sell = True
      	return render_template("sellCrop.html",sell = sell)  


@app.route('/service',methods = ['POST', 'GET'])  
def service():
   if request.method == 'POST':
      results = username = request.form['userInput']
      if results == '1':
      	sell = True
      	return render_template("sellCrop.html",sell = sell)  

'''
if __name__ == '__main__':
   app.run(debug = True)
