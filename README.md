# robotframework

## 1、robot testsuite

命令: robot test.robot

## 2、report sender script

命令: python /opt/robot/send_report.py [base_dir]

功能描述: 该命令用于将本地生成的测试报告通过SMTP发送出去

配置方式：环境变量

表格：

| 环境变量名称          | 含义     | 备注                      |      | 是否必填 |
| --------------- | ------ | ----------------------- | ---- | ---- |
| EMAIL_SENDER    | 发件人    |                         |      | 是    |
| EMAIL_RECEIVERS | 收件人    | 多个收件人以(;)分号间隔，不填则与发件人相同 |      |      |
| SMTP_HOST       | SMTP主机 | 需要咨询邮件运营商               |      | 是    |
| SMTP_PORT       | SMTP端口 | 需要咨询邮件运营商，默认587         |      | 是    |
| SMTP_MODE       | SMTP模式 | 默认为tls                  |      |      |
| SMTP_LOGIN      | 邮箱账户名  | 默认与发件人相同                |      |      |
| SMTP_PASSWORD   | 邮箱密码   | 密码必填，填错会导致邮件发送失败        |      | 是    |

