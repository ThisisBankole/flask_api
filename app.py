from flask import render_template
import connexion

#This tells Connexion which directory to look in for its configuration file.
app = connexion.App(__name__, specification_dir="./")
# This tells the app instance read the swagger.yml file from the specification directory and configure the system to provide the Connexion functionality.
app.add_api("swagger.yml")

#This is the route for the homepage
@app.route("/")
def home():
   return render_template("home.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)