from flask import Flask, request, render_template, send_file
from module import SpellCheckerModule
import io

app = Flask(__name__)

spell_checker_module = SpellCheckerModule()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/spell', methods=['POST'])
def spell():

    text = request.form.get('text')
    file = request.files.get('file')

    # File upload handling
    if file and file.filename != "":
        text = file.read().decode('utf-8')

    if not text:
        return render_template('index.html', corrected_text="No input provided")

    # Spell + Grammar
    corrected_text = spell_checker_module.correct_spell(text)
    final_text, mistakes = spell_checker_module.correct_grammar(corrected_text)

    return render_template(
        'index.html',
        input_text=text,
        corrected_text=final_text,
        mistakes=mistakes
    )


# Download corrected text
@app.route('/download', methods=['POST'])
def download():
    text = request.form.get('corrected_text')

    buffer = io.BytesIO()
    buffer.write(text.encode('utf-8'))
    buffer.seek(0)

    return send_file(buffer, as_attachment=True, download_name="corrected_text.txt", mimetype='text/plain')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

