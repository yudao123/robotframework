# coding=utf-8

import os, sys
import json
import xmltodict
import pyzmail
import zipfile

# email_sender='yinghua.yu@daocloud.io'
# email_receivers=[email_sender]
# smtp_host='smtp.partner.outlook.cn'
# smtp_port=587
# smtp_mode='tls'
# smtp_login='yinghua.yu@daocloud.io'
# smtp_password='8u7e6Pj6fLuiFaw'

email_sender=os.getenv('EMAIL_SENDER', 'yinghua.yu@daocloud.io')
email_receivers=os.getenv('EMAIL_SENDER', email_sender)
email_receivers=email_receivers.split(';')
smtp_host=os.getenv('SMTP_HOST', 'smtp.partner.outlook.cn')
smtp_port=os.getenv('SMTP_PORT', 587)
smtp_mode=os.getenv('SMTP_MODE', 'tls')
smtp_login=os.getenv('SMTP_LOGIN', email_sender)
smtp_password=os.getenv('SMTP_PASSWORD', '8u7e6Pj6fLuiFaw')

def send_email(title, content, send_filepath):
    filename = os.path.basename(send_filepath)
    attach_file=(open(send_filepath).read(), 'application', 'octet-stream', filename, '')
    payload, mail_from, rcpt_to, msg_id=pyzmail.compose_mail(email_sender, \
                    email_receivers, \
                    title, \
                    'utf-8', None, html=(content, 'utf-8'),
                    attachments=[attach_file])
    ret=pyzmail.send_mail(payload, email_sender, rcpt_to, smtp_host, \
            smtp_port=smtp_port, smtp_mode=smtp_mode, \
            smtp_login=smtp_login, smtp_password=smtp_password)
    print(ret)

def make_report(output_xml_filepath):
    robot_report = xmltodict.parse(open(output_xml_filepath).read())
    stat_info = robot_report['robot']['statistics']
    # print(json.dumps(robot_report['robot']['statistics'], indent=4))
    content = '<h2>Test Complete!</h2>'
    content += '<h2>Total Stat:</h2><h3><ul>'
    for item in stat_info['total']['stat']:
        content += '<li>{}: {} pass(es) , {} fail(s)</li>'.format(item['#text'], item['@pass'], item['@fail'])
    content += '</ul></h3>'
    content += '<h2>Suite Stat:</h2><h3><ul>'
    stat = stat_info['suite']['stat']
    content += '<li>{}: {} pass(es) , {} fail(s)</li>'.format(stat['#text'], stat['@pass'], stat['@fail'])
    content += '</ul></h3>'
    return content

def make_and_send_report(base_dir):
    content = make_report(os.path.join(base_dir, 'output.xml'))
    with zipfile.ZipFile('EMSBTestReport.zip', 'w') as fp:
        fp.write(os.path.join(base_dir, 'output.xml'), 'output.xml')
        fp.write(os.path.join(base_dir, 'log.html'), 'log.html')
        fp.write(os.path.join(base_dir, 'report.html'), 'report.html')
    send_email(u'EMSB Test Report', content, 'EMSBTestReport.zip')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        base_dir = sys.argv[1]
    else:
        base_dir = os.getcwd()
    make_and_send_report(base_dir)
