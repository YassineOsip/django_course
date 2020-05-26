from flask import Flask , render_template , request , redirect
app = Flask(__name__)
app.config["DEBUG"] = True
import instagram_engine 

@app.route("/", methods=['GET', 'POST'])
def home():
    data = {}
    if request.method == 'POST':
        username = request.form["username"]
        data = instagram_engine.getData(username)
    print(data)
    return render_template("home.html" , data = data)
app.run()