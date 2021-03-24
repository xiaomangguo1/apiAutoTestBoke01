import api
import requests

from tool.get_log import GetLog

log=GetLog().get_log()
class ApiMp:
    # 初始化
    def __init__(self):
        # 登录接口url
        self.url_login = api.host + "/api/sign-in"
        log.info("正在初始化自媒体登录url:{}".format(self.url_login))
        # 发布文章接口url
        self.url_article = "https://i.cnblogs.com/api/posts"
        log.info("正在初始化自媒体发布文章url:{}".format(self.url_article))

    # 登录接口
    def api_mp_login(self, mobile, code):
        """

        :param mobile: 手机号
        :param code: 验证码
        :return: 响应对象
        """
        # 定义请求数据
        data = {"mobile": mobile, "code": code}
        log.info("正在调用自媒体登录接口，请求数据{}".format(data))
        # 调用post
        return requests.post(url=self.url_login, json=data, headers=api.headers)

    # 发布文章接口
    def api_mp_article(self, title, content):
        """

        :param title: 文章标题
        :param content: 文章内容
        :return: 响应对象
        """
        # 定义请求数据
        data = {"postType": 1, "accessPermission": 268435456, "title": title, "postBody": content}
        log.info("正在调用自媒体发布文章接口，请求数据{}".format(data))
        # 调用post
        return requests.post(url=self.url_article, json=data, headers=api.headers)
