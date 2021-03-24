import pytest

from api.api_mp import ApiMp
import api
from tool.Tool import Tool
from tool.get_log import GetLog
from tool.read_yaml import read_yaml

log = GetLog().get_log()


class TestMp:
    # 初始化
    def setup_class(self):
        # 获取ApiMp对象
        self.api_mp = ApiMp()

    # 接口登录测试方法
    @pytest.mark.parametrize("mobile, code", read_yaml("mp_login.yaml"))
    def test01_mp_login(self, mobile, code):
        # 调用登录接口
        r = self.api_mp.api_mp_login(mobile=mobile, code=code)
        # 打印输出结果
        print("登录的结果为：", r.json())
        try:
            # 提取token
            Tool().common_token(response=r)
            # 断言状态码
            Tool().common_assert(response=r, status_code=201)
        except Exception as e:
            # 写日志
            log.error(e)
            # 抛异常
            raise

    # 接口发布文章测试方法
    def test02_mp_article(self, title="88", content="<p>77</p>"):
        # 调用发布文章测试方法
        self.api_mp.api_mp_article(title=title, content=content)
