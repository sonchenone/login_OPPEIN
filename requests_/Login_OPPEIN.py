import requests, re


# 抓取formhash值（登录表单需要）
def get_formhash(login_url, headers):
    html = requests.get(login_url, headers=headers).text
    p_formhash = r'name="execution" value="(....)"'
    print(re.findall(p_formhash, html))
    formhash = re.findall(p_formhash, html)[0]
    print(formhash)
    return formhash


# 登录与改密
def change_password(login_url, test_url, headers, formhash):
    # 创建会话以保持登录状态
    session = requests.session()
    name = input("请输入登录账号：")
    password_prompt = "请输入登录密码："  # 密码提示语
    while True:
        password = input(password_prompt)
        # 登录账号所需要传输的数据
        form_data = {}
        form_data1={}
        form_data["systemld"]="OPPEIN.COM"
        form_data["username"] = name
        form_data["password"] = password
        form_data["captcha"]=""
        form_data["execution"] = formhash
        form_data["_eventld"]="submit"
        form_data["geolocation"] = ""
        form_data1["CheckCardCode"]="KHK2020010200051"
        login_response = session.post(login_url, headers=headers, data=form_data)
        test_response = session.get(test_url, headers=headers,data=form_data1)  # test_response 用于验证是否登录成功。

        # 验证是否登录成功
        if "绩效考核" in test_response.text:
            print("登录成功")
        #     while True:
        #         new_password = input("请输入新的登录密码：")
        #         re_password = input("请再次输入新的登录密码：")
        #         if new_password != re_password:
        #             print("两次密码输入结果不一致，请重新输入！")
        #             continue
        #         else:
        #             break
        #     # 修改密码所所需要提交的数据。
        #     change_password_data = {}
        #     change_password_data["nowpassword"] = password
        #     change_password_data["password"] = new_password
        #     change_password_data["repassword"] = re_password
        #     change_password_data["issub"] = 1
        #     change_response = session.post(change_url, headers=headers, data=change_password_data)
        #     print("改密成功")
        #     break
        # else:
        #     password_prompt = ("登录失败，请重新输入登录密码：")
        #     continue


def main():
    login_url = "http://opsso.oppein.com/sso/login?service=http://oa.oppein.com/Login2016.aspx"
    test_url = "http://oa.oppein.com/2016App/HR/JX/FrmCheckedCardScoreViewV1.aspx?CheckCardCode=KHK2020010200051"

    headers = {}
    headers[
        "User-Agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"

    formhash = get_formhash(login_url, headers)
    change_password(login_url, test_url, headers, formhash)


if __name__ == "__main__":
    main()