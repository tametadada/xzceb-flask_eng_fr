# Importing the required modules
import machinetranslation as mtrs
from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")# Route Decorators
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    french_text = mtrs.translator.englishToFrench(textToTranslate)
    return french_text
    
@app.route("/frenchToEnglish")# Route Decorators
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    english_ext = mtrs.translator.frenchToEnglish(textToTranslate)
    return english_text

@app.route("/") # Default End-point
def renderIndexPage():
    # To render the html template 
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)