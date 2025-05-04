from flask import Flask

# Flask uygulamasını başlatıyoruz
app = Flask(__name__)

# Ana sayfa için bir route tanımlıyoruz
@app.route('/')
def hello_world():
    return "Merhaba, dünya!"
# Sunucuyu başlatıyoruz
if __name__ == '__main__':
    app.run(debug=True)
