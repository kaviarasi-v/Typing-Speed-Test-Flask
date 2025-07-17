from flask import Flask, render_template, request
import time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        user_input = request.form['typed_text']
        start_time = float(request.form['start_time'])
        end_time = time.time()
        total_time = round(end_time - start_time, 2)
        result = f"⏱️ Time taken: {total_time} seconds"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)