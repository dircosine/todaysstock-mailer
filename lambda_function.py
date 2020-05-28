import json
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import psycopg2
from datetime import datetime

HOST = os.environ['HOST']
DB_NAME = os.environ['DB_NAME']
USER = os.environ['USER']
PW = os.environ['PW']
SENDGRID_API_KEY = os.environ['SENDGRID_API_KEY']

TODAY = datetime.now().strftime('%Y%m%d')

def send_mail(to_addrs):
    message = Mail(
        from_email='contact.chartys@gmail.com',
        to_emails=to_addrs,
        subject='[차트연습장] 첫번째 채점 결과가 나왔어요!',
        html_content='<p>아래 주소로 이동해서 채점 결과를 확인해보세요😀<br/> <strong>https://chartys.netlify.app/scorebook</strong></p>')
    try:
        sg = SendGridAPIClient(
            SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)


def get_addrs():
    conn = psycopg2.connect(
        host=HOST,
        dbname=DB_NAME,
        user=USER,
        password=PW,
        port="5432",
    )
    cur = conn.cursor()

    cur.execute(f"""SELECT email FROM "public"."User" WHERE "noticeDate" = '{TODAY}'""")
    addrs = [r[0] for r in cur.fetchall()]
    
    cur.close()
    conn.close()

    print(addrs)
    print(len(addrs))
    return addrs

def lambda_handler(event, context):
    addrs = get_addrs()
    send_mail(addrs)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
