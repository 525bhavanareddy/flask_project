from flask import Flask,redirect,url_for,request,render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from project_database import Register,Base
engine=create_engine


@app.route("/file")
def file_upload():
	return render-template("file-upload.html")
@app.route("/success",method = ['POST'])
def success():
	if request.method=='POST':
	f=request.files["file"]
	f.save(f.filename)
	return render-template("display-html",name=f.file)

from flask import Flask,redirect,url_for,request,render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from project_database import Register,Base
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
def show_data():
	register=session.query(Register).all()
	return render_template('show.html',register=register)	
@app.route('/add',methods=["POST","GET"])
def addData():
	if request.method=='POST':
		newData=Register(name=request.form['name'],
			surname=request.form['surname'],
			roll_no=request.form['roll_no'],
			mobile=request.form['mobile'],
			branch=request.form['branch']
			)
		session.add(newData)
		session.commit()
		return redirect(url_for('show_data'))
	else:
		return render_template('new.html')


		 		
if __name__=='__main__':
	app.run(debug=True)















































	if(__name__ =="__main__"):
		app.run(debug=True)