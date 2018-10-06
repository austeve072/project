from flask import Flask, render_template, request, redirect, url_for, flash, session
from project import Project
import pygal
from user import User

app = Flask(__name__)
app.secret_key = 'llsaugiSIUDauhhfs;oi'
projects = Project.select()

def authenticator():
    if session:
        return True
    else:
        return False

#def login():
    ##check if user exists
    #If session is set
    #if flase, send message

@app.route('/register', methods=['POST'])
def register():
    try:
        User.get(User.email == request.form['email']).email
        flash('User Already Exists')
        return render_template('authentication.html')
    except:

        if request.form['password'] == request.form['confirm-password']:
            User(name = request.form['username'], email = request.form['email'], password=request.form['password'] )
            User.save()
            session['msee'] = True
            session['id'] = 1
            return redirect(url_for('home'))

        flash('Passwords dont match!')
        return render_template('authentication.html')


    #check if email exists
    #if does not exist, create
    #set session
@app.route('/logout')
def logout():
    session.clear()
    return redirect('')

def pieChart():
    pie_chart = pygal.Pie()
    pie_chart.title = 'Projects Type'
    internal = 0
    external = 0

    for row in projects:
        if row.type == 'Internal':
            internal = internal + 1
        else:
            external = external + 1
    pie_chart.add('Internal', internal)
    pie_chart.add('External', external)
    return pie_chart.render_data_uri()

def barChart():
    bar_chart = pygal.Bar()       # Then create a bar graph object
    data = []
    rows = Project.select()       #this is redundancy, was already defined up there

    for i in rows:                #loop through each row and add the amount for each
        data.append(i.amount)     #in the loop add the amount to an existing list

    label = 'Amount'
    bar_chart.add(label, data)
    bar_chart.render_to_file('bar_chart.svg')  # Save the svg to a file
    bar_graph = bar_chart.render_data_uri()
    return bar_graph


@app.route('/')

def home():
        if authenticator():
            projects = Project.select().order_by(Project.id)
            return render_template('index.html', pie_chart = pieChart(), bar_graph = barChart(), projectsHtml = projects)
        else:
            return render_template('authentication.html')

@app.route('/save', methods=['POST'])
def save():
    projectOne = Project(title =request.form['titleForm'],
                          type = request.form['typeForm'],
                          start_from = request.form['startDateForm'],
                          end_at = request.form['endDateForm'],
                          description = request.form['descriptionForm'],
                          amount = request.form['amountForm'],
                          status = 1)
    projectOne.save()
    flash('SUCCESSFUL!')
    return redirect(url_for('home'))

#function for updating
@app.route("/update/<int:id>", methods=['POST','GET'])
def update(id):
    projects  = Project.get(Project.id == id)
    projects.title = request.form['titleForm']
    projects.save()
    return redirect(url_for("home"))  #redirect to home url

#function to delete from DB
@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    try:
        project = Project.get(Project.id==id)
        project.delete_instance()
        flash('RECORD DELETED!')
        return redirect(url_for('home'))
    except:
        return 'Server Error'

if __name__ == '__main__':
    app.run(debug=True)