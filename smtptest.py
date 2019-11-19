import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'service@sync.cloudbox.hinet.net'
receivers = ['nicholas@cht.com.tw','oldmon@outlook.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('Python 郵件發送測試...', 'plain', 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')   # 发送者
message['To'] =  Header("測試", 'utf-8')        # 接收者

subject = 'Python SMTP 郵件測試'
message['Subject'] = Header(subject, 'utf-8')


try:
    smtpObj = smtplib.SMTP('hibox.hinet.net')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "郵件發送成功"
except smtplib.SMTPException:
    print "Error: 無法發送郵件"
