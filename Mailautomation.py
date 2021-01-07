import yagmail

receiver = "queriesakpython@yahoo.com"
message = ("Hello there from Yagmai",'Test1.pdf')

sender = yagmail.SMTP("mailt5582@gmail.com")
sender.send(
    to=receiver,
    subject="Yagmail test with attachment",
    contents=message
)