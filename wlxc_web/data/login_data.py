
#登录失败
login_error = [
    {
        "username":"",
        "password":"",
        "expected":{"first":"请输入用户名","second":"请输入6位以上数字字母组合密码!"}
     }
]

login_success = [
    {"username":"admin","password":"szxc123","expected":"管理员"}
]

#登录未授权
login_invalid = [
    {"username":"admin","password":"hh123456","expected":"密码不正确"}
]