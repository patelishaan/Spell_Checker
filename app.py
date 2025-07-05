from flask import Flask, render_template, request, jsonify, session, flash, url_for, redirect
import requests
import pandas as pd
import re
from tqdm import tqdm
from spell_check_backend_logic import spell_check_edit_1

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/", methods = ["GET", "POST"])
def home():
    word = None
    corrected_word = None
    if request.method == 'POST':
        word = request.form.get('Name')
        corrected_word = spell_check_edit_1(word)
    return render_template("index.html", word=word, corrected_word = corrected_word)

if __name__=="__main__":
    app.run(debug=True)
