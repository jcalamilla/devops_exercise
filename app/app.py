from flask import Flask
from pathlib import Path

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "Hello World!!!"

@app.route("/counter", methods=['POST'])
def post_counter():
    file = Path('/opt/counter.txt')
    file.touch(exist_ok=True)
    f = open(file,"r+")
    content = f.readline()
    if len(content.strip()) == 0 :
        content = 1
        f.seek(0)
        f.write(str(content))
        return str(content)
    else:
        content = int(content)
        content += 1
        f.seek(0)
        f.write(str(content))
        return str(content)

@app.route("/counter", methods=['GET'])
def get_counter():
    file = Path('/opt/counter.txt')
    file.touch(exist_ok=True)
    f = open(file,"r")
    content = f.readline()
    if len(content.strip()) == 0 :
        return "No hay peticiones..."
    else:
        return "Hay %s peticiones..."%content
    


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)