import win32com.client as win32
def send_mail():
    outlook=win32.Dispatch('Outlook.Application')
    mail_item=outlook.CreateItem(0)
    mail_item.Recipient.Add('XXX@mail.com')
    mail_item.Attachments.Add('D:\data.txt')
    mail_item.Subject="mail Test"
    mail_item.BodyFormat=2
    body='Test revision'
    mail_item.Body=body.decode('utf-8')
    mail_item.Send()