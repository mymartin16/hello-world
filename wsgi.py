from flask import Flask, render_template
application = Flask(__name__)

@application.route("/")
def main():
    return ("Vikas")

if __name__ == "__main__":
    application.run()
