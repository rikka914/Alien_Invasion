print("我是utils.py，我的__name__是：", __name__)  # 这行总是会打印

def say_hello():
    print("你好，我是一个好用的函数！")

# 关键的安全检查来了！
if __name__ == "__main__":
    print(">>> 我正在被直接运行，我要开始表演了！ <<<")
    say_hello()
    print(">>> 表演结束！ <<<")