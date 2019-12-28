#encoding = utf-8
from bottle import route, run, request

@route('/hello')
def hello():
    name = request.GET["name"]
    print(name)
    return "Hello ,everybody.My name is " + name

@route('/old')
def old():
    return "I'm 11 years old."

@route('/about')
def about():
    return "Let' s have a look."

@route("/showimg")
def show_dabao():
    # HTML code
    return '''
    <img src = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1577550048099&di=274cf4fc82244e13d4e0a648cbb8b016&imgtype=0&src=http%3A%2F%2Fc.hiphotos.baidu.com%2Fzhidao%2Fpic%2Fitem%2F96dda144ad345982308639ce0ff431adcbef845a.jpg">
    ladys and gentlemen,my name is kdKID. And now, it's a show time.
    <img src = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1577550048097&di=48914a83952a33528bc92c7ff01de0cb&imgtype=0&src=http%3A%2F%2Fhbimg.b0.upaiyun.com%2Fc96b62a83c9539ec102958e083c9bd77f600d865899cc-2AxMtY_fw658">
    <img src = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1577550048096&di=1df8a8ae9fe03a897d9ae478f87d4c99&imgtype=0&src=http%3A%2F%2Fe.hiphotos.baidu.com%2Fzhidao%2Fpic%2Fitem%2Fd009b3de9c82d158809a3a6c860a19d8bd3e42d6.jpg">
    <img src = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1577550814681&di=3ed76bbbc4b76c704966b4e9b72e8026&imgtype=0&src=http%3A%2F%2Fp.ssl.qhimg.com%2Ft017667b2048be89acb.jpg">
    <img src = "
    '''

@route('/')
def index():
    return "Welcome!"

@route('/add')
def add():
    a = request.GET["a"]
    b = request.GET["b"]
    ab = int(a) * int(b)
    return str(ab)

run(host='localhost', port=1212, debug=True)
