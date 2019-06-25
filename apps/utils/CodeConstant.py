class CodeConstant():
    SYSTEM_ERROR = "系统错误，请与管理员联系"
    REQUEST_FAILUE = "请求失败"
    FILE_UPLOAD_FAILUE = "文件上传失败"
    FILE_DELETE_FAILUE = "文件删除失败"
    CODE_000 = "000"  # 接口提交成功
    CODE_001 = "001"  # 接口非法请求错误
    CODE_002 = "002"  # 接口传递参数错误
    CODE_003 = "003"  # 接口异常
    # 接口返回码信息 ** /
    REQUEST_SUCCESS = "000"  # 请求成功 *
    REQUEST_FAIL = "001"  # 请求失败
    COMMON_ILIEGAL_REQUEST = "002"  # 参数信息不合法
    COMMON_NON_MAIN_ACCOUNT_REQUEST = "003"  # 非主帐号
    COMMON_INTERFACE_ERROR = "999"  # 接口异常 *
    # 商户类返回码   以1开头标识 ** /
    REGISTER_ISHAVE = "10001"  # 用户名已存在

    RREGISTER_ISNULL = "10002"  # 用户名为空

    REGISTER_PWD_ISNULL = "10003"  # 密码为空

    RREGISTER_CODE_ISNULL = "10004"  # 验证码为空

    RREGISTER_CODE_ERROR = "10005"  # 验证码错误

    LOGIN_ACCOUNT_ISNULL = "10006"  # 账户或密码为空

    LOGIN_ACCOUNT_ISNOTHAVE = "10007"  # 账户不存在

    LOGIN_ACCOUNT_ERROR = "10008"  # 账户或密码错误

    SENDMESSAGE_MOBILE_ISNULL = "10009"  # 手机号码为空 *

    MOBILE_ISHAVE = "10010"  # 手机号码已注册 *

    COMPANY_BASIC_ISNOTHAVE = "10011"  # 未找到用户信息

    STORE_ID_ISNULL = "10012"  # 店铺ID为空

    FINDPWD_PWD_NOT_AS = "10013"  # 两次密码输入不一致

    COMPANY_MOBILE_BINGING = "10014"  # 手机号码已被绑定

    COMPANY_EMAIL_BINGING = "10015"  # 邮箱已被绑定

    COMPANY_MOBILE_NOTREGISTER = "10016"  # 手机号码在系统中不存在

    COMPANY_CODE_ISNULL = "10017"  # 图形验证码为空

    CODE_PIC_ERR = "10018"  # 图形验证码为空

    COMPANY_EMAIL_ISNULL = "10019"  # 邮箱为空

    COMPANY_MODPWD_ISLOSE = "10020"  # 修改密码地址已失效

    MEMBER_ADDRESS_DEFAULT_ISNOTDEL = "10021"  # 默认地址不能删除

    MEMBER_STATUS_ISNOTDEL = "10022"  # 账号为启用状态，不能删除

    MEMBER_ROLE_ISNULL = "10023"  # 角色不存在

    MEMBER_ROLE_ISLINK_DEL = "10024"  # 角色下存在关联账户

    MEMBER_ROLE_REPEAT = "10025"  # 角色重复

    LOGIN_ACCOUNT_IS_NO_LOGIN = "10026"  # 账号状态为停用

    FINDPWD_TYPE_ISNULL = "10027"  # 找回 / 修改类型为空

    COMPANY_MODMOBILE_ISLOSE = "10028"  # 修改手机地址已失效

    COMPANY_MODEMAIL_ISLOSE = "10029"  # 修改邮箱地址已失效

    COMPANY_EMAIL_NOTREGISTER = "10030"  # 邮箱在系统中不存在

    COMPANY_ACCOUNT_ISHAVE = "10031"  # 该帐号已被占用

    COMPANY_CHECKCODE_ISNULL = "10032"  # 推荐码为空

    COMPANY_CHECKCODE_ISLOSE = "10033"  # 推荐码无效

    COMPANY_CHECKCODE_ISHAVE = "10034"  # 推荐码已使用

    MEMBER_EMPLOYEE_STORE_ISNULL = "10035"  # 账户下未赋予店铺权限
    MEMBER_STORE_AUTH_ERROR = "10036"  # 店铺授权错误

    MEMBER_SUBACCOUNT_NOTREGISTER = "10037"  # 子帐号不存在

    MEMBER_EMPLOYEE_ROLE_ISNULL = "10038"  # 账户下未赋予角色权限
    MEMBER_SUBACCOUNT_ISNULL = "10039"  # 子帐号为空

    UPDATE_SUBACCOUNTSTATUS_TYPE_ISNULL = "10040"  # 修改子帐号状态，类型为空

    UPDATE_SUBACCOUNTSTATUS_SUBACCOUNTID_ISNULL = "10041"  # 修改子帐号状态，子帐号ID为空

    MEMBER_SUBACCOUNTID_ISNULL = "10042"  # 子帐号ID为空

    MEMBER_ACCOUNT_NOAUTHORITY = "10043"  # 此帐号没有操作权限

    MEMBER_ROLEID_ISNULL = "10044"  # 角色ID为空

    # 授权令牌信息返回码  以2开头标识 ** /
    COMPANY_BASIC_TOKEN_ISNULL = "20001"  # 授权令牌为空

    COMPANY_BASIC_TOKEN_ERR = "20002"  # 授权令牌错误

    COMPANY_BASIC_TOKEN_EXPIRE = "20003"  # 授权令牌过期，请重新登录

    COMPANY_STORE_ISHAVE1 = "20004"  # 该站点下已存在店铺

    SENDMESSAGE_TEMPLATE_ERR = "20005"  # 获取短信模板失败

    COMPANY_STORE_ISHAVE = "20006"  # 店铺已存在

    COMPANY_STORE_TOKEN_ISHAVE = "20007"  # 授权信息已授权，请联系管理员

    LOGIN_PASSWORD_ERROR = "20008"  # 原密码错误

    IMAGE_UPLOAD_SIZE_ERROR = "20009"  # 图片大小超出限制

    IMAGE_UPLOAD_TYPE_ERROR = "20012"  # 图片类型错误

    # 供应链管理信息返回码  以3开头标识 ** /

    # 订单任务信息返回码  以4开头标识 ** /

    # 订单  以5开头标识 ** /

    # License授权 ** /
    LICENSE_ERROR = "60001"  # license错误

    # 案场稽核 ** /
    CASE_PROJECT_IS_NULL = "80000"  # 项目未找到

    UPLOAD_FILE_DATA_ERROR = "80001"  # 导入数据错误

    NO_FIND_CASE_FACE_SEARCH = "80002"  # 未匹配到到访信息

    CASE_PROJECT_IS_NOT_NULL = "80003"  # 项目重复

    CASE_PROJECT_SERVER_REPEAT = "80004"  # 项目前端服务器重复

    CASE_PROJECT_INTEGRATED_REPEAT = "80005"  # 项目一体机重复

    CASE_PROJECT_CAMERA_REPEAT = "80006"  # 项目摄像头重复

    CASE_PROJECT_SERVER_FORMAT_ERROR = "80007"  # 项目前端服务器录入格式错误

    CASE_PROJECT_INTEGRATED_FORMAT_ERROR = "80008"  # 项目一体机录入格式错误

    CASE_PROJECT_CAMERA_FORMAT_ERROR = "80009"  # 项目摄像头录入格式错误

    CASE_PROJECT_AUTHORIZE_ERROR = "80010"  # 项目授权码错误

    CASE_PROJECT_AUTHORIZE_IS_USE = "80011"  # 项目授权码已使用
