import shelve

from selenium.webdriver.common.by import By

from weixin_po_20200822.page.base_page import BasePage


class Login(BasePage):
    def login(self):
        #数据传入数据库
        # with shelve.open('logincookies') as db:
        #     cookies = [{'domain': 'work.weixin.qq.com', 'expiry': 1598216675, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '432qtk3'}, {'domain': '.qq.com', 'expiry': 1598283605, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.2122934438.1598185141'}, {'domain': '.qq.com', 'expiry': 1661269205, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.2026611589.1598185141'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629616985, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1600789206, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629733205, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1598080990,1598185141,1598197206'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '2660269568'}, {'domain': '.qq.com', 'expiry': 2147483646, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': 'afcfae6fd22537f225eea73310136f64959ea0a79065c03e3ec721593bc3e3f5'}, {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'DOaFZnWS9I'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1598197206'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '10799704162404836'}, {'domain': '.qq.com', 'expiry': 1598197265, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '1796856832'}]
        #     db['cookies'] = cookies
        #     db.close()

        db = shelve.open('logincookies')
        cookies = db['cookies']
        # print(cookies)

        for cookie in cookies:
            # print(cookie)
            if 'expiry' in cookie.keys():
                cookies.pop()
                self._driver.add_cookie(cookie)

    def goto_register(self):

        pass