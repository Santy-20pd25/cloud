from flask import Flask,render_template,request,redirect
#from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/gym_db'
#SQLALCHEMY_TRACK_MODIFICATIONS = False
#db=SQLAlchemy(app)



    
@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/joinUs', methods=['GET', 'POST'])
def join_form():
    if request.method == "POST":
        name = request.form.get('name')
        if name != "":
            # Instead of database interaction, redirect or display a message
            return redirect(url_for('contactUs'))  # Assuming you have a 'thank_you' route
    return render_template('joining_form.html')

@app.route('/aboutUs')
def aboutUs():
    return render_template('aboutus.html')

@app.route('/gallery')
def gallery():
    imgs=['img/im1.jpg','img/im2.jpg','img/im3.jpg','img/im4.jpg','img/im5.jpg','img/im6.jpg','img/im7.jpg','img/im8.jpg','img/im9.jpg','img/im10.jpg','img/im11.jpg','img/im12.jpg','img/im13.jpg','img/im14.jpg','img/im15.jpg','img/im16.jpg','img/im17.jpg','img/im18.jpg','img/im19.jpg','img/im20.jpg','img/im21.jpg','img/im22.jpg','img/im23.jpg','img/im24.jpg']
    return render_template('gallery.html',imgs=imgs)

@app.route('/contactUs', methods=["GET", "POST"])
def contactUs():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Instead of database interaction, you can:
        # 1. Display a message to the user
        # flash("Thank you for your message!", "success")  # Requires Flask's flash()

        # 2. Redirect to a "thank you" page
        return redirect(url_for('contactUs'))  # Assuming you have a 'thank_you' route

        # 3. (Advanced) Send an email using an email API
        #    (This would require additional configuration and an email sending service)

    return render_template('contact.html')

if __name__=='__main__':
    app.run(debug=True)