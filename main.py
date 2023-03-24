import counter_app
from counter_app import home_page, app, show, db
from flask import Flask, render_template_string

# database = {'number': 0}
html = '''
<link rel='stylesheet' href='./static/counter_styles.css'>
<span>
<h2 id="Number">{{ count }}</h2>
</span>
<form action="/decrement">
  <button>-</button>
</form>
<form action="/increment">
  <button>+</button>
</form>

'''
db = {'c': 0} ;

@app.route('/')
def home():
  #return show(home_page, number=db['number'])
  return render_template_string(html, count = db['c'])


@app.route('/decrement')
def func()->str:
  db['c']-=1
  return render_template_string(html, count = db['c'])

@app.route('/increment')
def staberry()->str:
  db['c']+=1
  return render_template_string(html, count = db['c'])


  
# @app.route('/increment')
# def increment()->str:
#   db['number']+=1
#   return show(home_page, number=db['number'])

# @app.route('/decrement')
# def decrement()->str:
#   if db['number']>0:
#     db['number']-=1
  
#   return show(home_page, number = db['number'])
  
app.run(host='0.0.0.0', port=81)