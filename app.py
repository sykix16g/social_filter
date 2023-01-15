from flask import Flask,render_template
import time

IMAGE_PATH = './templates/src'
CAT_TOTAL = 9
app = Flask(__name__, static_folder=IMAGE_PATH)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/filtering', methods=['POST'])
def filtering():
    # POSTの内容は捨てる

    # ネコチャンの画像はUNIX TIME基準で適当に
    num = int(time.time()) % CAT_TOTAL
    path = "src/img/cat/" + str(num) +".jpg"

    return render_template('filtering.html', cat_image=path, img_num=str(num))

## おまじない
if __name__ == "__main__":
    app.run()
