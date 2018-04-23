#!/usr/bin/env python
# coding=utf8

import sys
import config
import smtplib
from email.mime.text import MIMEText


def send_email(subject="Alert", contents="Alert"):

    msg = MIMEText(contents)

    me = config.me
    you = config.you

    msg['Subject'] = '[Project] %s' % subject  # 이메일 제목
    msg['From'] = me
    msg['To'] = you

    s = smtplib.SMTP_SSL('smtp.naver.com', 465)
    s.login(config.n_id, config.n_passwd)
    s.sendmail(me, you, msg.as_string())
    s.quit()


if __name__ == '__main__':

    if len(sys.argv) is 1:
        send_email()
    elif len(sys.argv) is 2:
        subject = str(sys.argv[1])
        send_email(subject)
    else:
        subject = str(sys.argv[1])
        contents = str(sys.argv[2])
        send_email(subject, contents)
