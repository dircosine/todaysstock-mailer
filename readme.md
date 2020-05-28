# todaysstock-mailer

## 개요

- 매일 정해진 시간에 채점 완료 알림 메일 발송
- AWS Lambda 에서 구동
- python 3.7

---

### 외부 라이브러리

- `python.zip` 
  - 외부 라이브러리 압축 해 놓은 것
  - `aws-psycopg2`, `sendgrid`
- Lambda 내 새로운 레이어에 압축파일 업로드
- **python.zip 파일명 유지 필수**

### 트리거

- AWS CloudWatch Events
- 매일 19:00 (UTC 10:00)
