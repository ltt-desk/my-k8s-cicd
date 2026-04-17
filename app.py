from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    # 核心测试点：注意这里的版本号，等下我们要通过修改它来触发流水线
    return "<h1>Hello, GitOps! This is Version 1.0</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
