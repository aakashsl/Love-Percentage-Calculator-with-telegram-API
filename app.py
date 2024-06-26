from flask import Flask, render_template,request, url_for,redirect,session
import random,requests



app = Flask(__name__)

app.secret_key = '3280151'

bot_token = 'YOUR_BOT_TOKEN'
chat_id =['YOUR_CHAT_ID']

@app.route('/')
def home():
   n= random.randint(1, 5)
   session['n'] = n
   capt=captcha(n)
   return render_template("index.html",captcha=capt)

def captcha(n):
   if (n==1):
      return "A,B,C,?,E"
   elif(n==2):
      return "I,J,?,L,M"
   elif(n==3):
      return "L,M,N,?,P"
   elif(n==4):
      return "10,11,12,?,14"
   elif(n==5):
      return "100,99,?,97,96"

def capans(n):
   if(n==1):
      return "D"
   elif(n==2):
      return "K"
   elif(n==3):
      return "O"
   elif(n==4):
      return "13"
   elif(n==5):
      return "98"

def get_data():
    name1 = request.form['name1']
    name2 = request.form['name2']
    a = random.randint(1, 100)
    p=para(a)
    return name1, name2, a, p

@app.route('/check' ,methods=['POST'] )
def check():
   name1, name2, a, p = get_data()
   cap = request.form['cap']
   n = session.get('n', None)
   checkans=capans(n)
   if (checkans==cap):
      Tele_send(name1,name2,a) 
      return final(name1,name2,a,p)
   else:
      return render_template("bad.html")


def final(name1,name2,a,p):
   return redirect(url_for('result', name1=name1, name2=name2, a=a, p=p))
   
@app.route('/result')
def result():
   name1 = request.args.get('name1')
   name2 = request.args.get('name2')
   a = request.args.get('a')
   p = request.args.get('p')
   return render_template("result.html", names1=name1, names2=name2, per=a, qut=p)

def para(a):
   if(a<50):
      return "Don't Worry, try one more time"
   elif(a<70):
      return "To love is to burn, to be on fire"
   elif(a<99):
      return "He best thing to hold onto in life is each other"
   elif(a==100):
      return "WoW 100% your Love was very Strong"
   else:
      return " "

def Tele_send(name1,name2,a):
   telegram_message = f'From Love Percentage \n Name 1: {name1} \n Name 2: {name2} \n Percentage : {a}'
   requests.post(f'https://api.telegram.org/bot{bot_token}/sendMessage',
                        data={'chat_id': chat_id, 'text': telegram_message})

if __name__ == '__main__':
    app.run(debug=True)
