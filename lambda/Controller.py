import DBUtil

class Controller():

    #
    # データの取得
    # @params httpMethod HTTPメソッド
    # @params url URL
    #
    def __init__(self, httpMethod, url):
        self.httpMethod = httpMethod
        self.url = url
