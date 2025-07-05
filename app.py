from flask import Flask, render_template, Response
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/plot.png")
def plot_png():
    # 그래프 생성
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [10, 5, 8, 12])
    ax.set_title("Sample Plot")

    # 이미지 버퍼로 저장
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)

    # 이미지 응답
    return Response(buf.getvalue(), mimetype='image/png')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)