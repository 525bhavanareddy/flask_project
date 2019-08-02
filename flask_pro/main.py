from flask import Flask,redirect,url_for,request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from project_database import Register_Base
engine = create_engine('sqlite:///bvc.db',connect_args={'check_same_thread':False},echo=True)
Base.metadata.bind=engine
DBSession=sessionmaker(bind=engine)
session = DBSession()
app=Flask('__name__')
@app.route("/home")
def hello():
	return"my name is bhavana"
@app.route("/admin")
def admin():
	return"<h2>welcome to admin page</h2>" 
@app.route("/student")
def student():
	return "<font colour='red'>hello welocme to student page"
@app.route("/faculty")
def faculty():
	return "welcome to faculty data"
@app.route("/user/<name>")
def user(name):
	if name=='faculty':
		return redirect(url_for('faculty'))
	elif name=='student':
		return redirect(url_for('student'))
	elif name=='admin':
		return redirect(url_for('admin'))
	else:
		return"no url found"
@app.route("/show_data")
def showData():
	register=session.query(Register).all()
	return render_template('show.html',register=register)		
		 		
if __name__=='__main__':
	app.run(debug=True)