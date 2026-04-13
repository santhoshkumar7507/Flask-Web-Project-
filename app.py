from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home_page():
 
    return render_template('home.html',language="Python",project_name="Flask Web Project",number=[1,2,3,4,5,6,7,8,9,10])

@app.route('/about')
def about_page():
    print(request.args)
    return render_template('about.html')

@app.route('/contact')
@app.route('/contact/<int:id>')
def contact_page(id=None):
    if id:
        print(id)
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(port=5000,debug=True)

