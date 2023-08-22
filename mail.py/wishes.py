import smtplib
my_email = "junedsaifi586@gmail.com"
password = "ntyhjedejqejvumw"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs="jnx001@yahoo.com",
    msg="subject:hello\n\nthis is the body of my email"
    )
connection.close()

