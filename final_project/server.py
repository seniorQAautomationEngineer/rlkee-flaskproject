from flask import Flask, render_template, request
from final_project.machinetranslation.translator import translate_en_to_fr, translate_fr_to_en

app = Flask("Web Translator")


@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    return translate_en_to_fr(textToTranslate)


@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    return translate_fr_to_en(textToTranslate)


@app.route("/")
def homepage():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
