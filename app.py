from flask import Flask,render_template,redirect,url_for
import time

IMAGE_PATH = './templates/src'
CAT_TOTAL = 9
app = Flask(__name__, static_folder=IMAGE_PATH)

@app.route('/')
def main():
    print(url_for('filtering',num=1))
    return render_template('main.html')

@app.route('/redirect', methods=['POST'])
def redirection():
    # POSTの内容は捨てる
    # 各種ネコチャンのページへリダイレクト
    num = int(time.time()) % CAT_TOTAL

    return redirect(url_for('filtering',num=num))

@app.route('/filtering/<num>')
def filtering(num):
    # POSTの内容は捨てる

    # ネコチャンの画像はUNIX TIME基準で適当に
    cat_num = str(num)
    path = "src/img/cat/" + cat_num +".jpg"

    return render_template('filtering.html', cat_image=path, img_num=cat_num)


## おまじない
if __name__ == "__main__":
    app.run()
