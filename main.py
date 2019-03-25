from flask import Flask, render_template, request
from multiprocessing import Process
import math
app = Flask(__name__)

results = []

def to_power(x, y):
    if y == 0:
        return 1
    if y >= 1:
        return x * to_power(x, y - 1)

def primeFactorization(n):
  c = 2
  if n <= c:
    return True
  else:
    while n % c != 0:
      c += 1
      if math.sqrt(n) <= c:
          return True
    return False

def recursivePrime(power):
  global results
  res = primeFactorization(to_power(2, power) - 1)
  if res:
    results.append(power)
  recursivePrime(power + 1)

t1 = False

@app.route('/start')
def start():
  global t1
  power = 1
  power = int(request.args.get('power'))
  t1 = Process(target=recursivePrime, args=[1])
  t1.start()
  return "OK"

@app.route('/stop')
def stop():
    t1.terminate()
    return "OK"

@app.route('/heartbeat')
def heartbeat():
  return str(results)

@app.route('/', methods=['GET', 'POST'])
def index():
  return render_template('index.html')

if __name__ == '__main__':
    app.run()
