from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("dictionary.csv")
@app.route("/")
def main():
    return render_template("home.html")

@app.route("/app/v1/<word>")
def definition(word):
    def2 = df.loc[df["word"] == word]['definition'].squeeze()
    return {"definition": def2,
            "word": word}

if __name__ == "__main__":
    app.run(debug=True, port=5001)