import yagmail

receiver = "reciever email"
message = ("Hello there from Yagmai",'Test1.pdf')

sender = yagmail.SMTP("sender email")
sender.send(
    to=receiver,
    subject="Yagmail test with attachment",
    contents=message
)
