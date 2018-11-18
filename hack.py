from flask import Flask, render_template, request
import random

app = Flask(__name__)


farmer = {'12345678':"Rahul Gunkar",
		'11111111':" NIkhil Ghirepunje",
		'22222222':" Panda Patil",
		'33333333':" Sayalo Patil",
		'44444444':" Shubham Sawarkar"


}


otpSell = ""
otpSellSeed = ""
otpCropMon = ""	#crop monitoring
otpServReq =""	#service request
otpServProvide=""	#service raise

aadharServReq=""
aadharServProvide=""
aadharCropMon= "" #corp monitoring
sellSeedAadhar=""	#seed
sellAadhar = ""	#crop


@app.route('/')
def home():
   return render_template('index.html')


@app.route('/mainPage',methods = ['POST', 'GET'])
def mainPage():
   if request.method == 'POST':
      result = request.form
      return render_template("homePage.html",result = result,farmer=farmer)


@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form['userInput']
     
      if result == '1':
      	return render_template("sell.html")
      elif result == '2':
      	return render_template("service.html")
      elif result == '3':
      	return render_template("checkUp.html")
      else:
      	return render_template("homePage.html",result = result)
      

@app.route('/sell',methods = ['POST', 'GET'])
def sell():
   if request.method == 'POST':
      result = request.form['userInput']
     
      if result == '1':
      	return render_template("sellCrop.html")
      elif result == '2':
      	return render_template("sellSeed.html")
     
      else:
      	return render_template("sell.html",result = result)









@app.route('/serviceMapper',methods = ['POST', 'GET'])
def serviceMapper():
   if request.method == 'POST':
      result = request.form['userInput']
     
      if result == '1':
      	return render_template("requestService.html")
      elif result == '2':
      	return render_template("provideService.html")
     
      else:
      	return render_template("service.html",result = result)



@app.route('/reqServMap',methods = ['POST', 'GET'])
def reqServMap():
   if request.method == 'POST':
      result = request.form['userInput']
     
      return render_template("reqServMap.html",aadhar=result,otp=random.randint(1,1000))


@app.route('/reqServMap2',methods = ['POST', 'GET'])
def reqServMap2():
   if request.method == 'POST':
      result = request.form['userInput']
     
      return render_template("reqServMap2.html",aadhar=result,otp=random.randint(1,1000))

@app.route('/serviceRaised',methods = ['POST', 'GET'])
def serviceRaised():
   if request.method == 'POST':
      
     
      return render_template("served.html",otp=random.randint(1,1000))



@app.route('/serviceRaised2',methods = ['POST', 'GET'])
def serviceRaised2():
   if request.method == 'POST':     
     
      return render_template("served2.html",otp=random.randint(1,1000))











@app.route('/mapper',methods = ['POST', 'GET'])
def mapper():
   if request.method == 'POST':
      result = request.form['userInput']
      global sellAadhar
      sellAadhar = sellAadhar + result
      print(sellAadhar)
      global otp
      global otpSell
      otp=random.randint(1,1000)
      otpSell = "*307*" +str(otp)+"#"
      print (otpSell)
      return render_template("mapper.html",farmer=farmer,aadhar=result,otp=otp)

 

@app.route('/seedMapper',methods = ['POST', 'GET'])
def seedMapper():
   if request.method == 'POST':
      result = request.form['userInput']
      global sellSeedAadhar
      global otpSellSeed
      otpSellSeed = str(random.randint(1,1000))
      sellSeedAadhar = sellSeedAadhar + result
      return render_template("seedMapper.html",aadhar=result,otp=otpSellSeed)


@app.route('/seedSold',methods = ['POST', 'GET'])
def seedSold():
   if request.method == 'POST':
      result = request.form['userInput']
      if result == "*307*"+otpSellSeed+"#":
      	
      	return render_template("seedSold.html",aadhar =sellSeedAadhar, farmer=farmer)
      else:
      	return render_template("seedMapper.html",farmer=farmer,otp=otp)



@app.route('/cropSold',methods = ['POST', 'GET'])
def cropSold():
   if request.method == 'POST':
      result = request.form['userInput']
      print(result)
      if result == otpSell:
      	
      	return render_template("cropSold.html",aadhar =sellAadhar, farmer=farmer)
      else:
      	return render_template("mapper.html",farmer=farmer,otp=otp)

      



@app.route('/checkUpRaised',methods = ['POST', 'GET'])
def checkUpRaised():
	return render_template("checkUpRaised.html")



if __name__ == '__main__':
   app.run(debug = True)