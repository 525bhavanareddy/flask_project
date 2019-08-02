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
def showData():
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
		return redirect(url_for('showData'))
	else:
		return render_template('new.html')
@app.route('/<int:register_id>/edit',methods=["POST","GET"])
def editData(register_id):
	editedData=session.query(Register).filter_by(id=register_id).one()
	if request.method=="POST":
		editedData.name=request.form['name']
		editedData.surname=request.form['surname']
		editedData.roll_no=request.form['roll_no']
		editedData.mobile=request.form['mobile']
		editedData.branch=request.form['branch']
		session.add(editedData)
		session.commit()
		return redirect(url_for('showData'))
	else:
		return render_template('edit.html',register=editedData)


@app.route('/<int:register_id>/delete',methods=["POST","GET"])
def deleteData(register_id):
	deletedData=session.query(Register).filter_by(id=register_id).one()
	if request.method=="POST":
		session.delete(deletedData)
		session.commit()
		return redirect(url_for('showData'))
	else:
		return render_template('delete.html',register=deletedData)	

		 		
if __name__=='__main__':
	app.run(debug=True)