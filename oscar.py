# N1
import sqlite3
conn = sqlite3.connect("oscar_winners.sqlite")
cursor1= conn.cursor()
# N2
output = cursor1.execute('''SELECT * FROM oscar''')
დაბეჭდავს ცხრილის ყველა სვეტს
for i in output :
    print(i)
for ციკლით ვიძახებთ ყველა სტრიქონს ხოლო
output1 = cursor1.execute('''SELECT year, name, movie * FROM oscar''')
ვირჩევთ შემდეგ სვეტებს: წელი, სახელი , ფილმი
print(cursor1.fetchone())
დაბეჭდავს მხოლოდ ერთ სტრიქონს
print(cursor1.fetchall())
დაბეჭდავს ყველა მონაცემს ლისტის სახით
print(cursor1.fetchmany(5))
დაბეჭდავს 5 მონაცემს ლისტის სახით
N3
id = int(input("sheikvanet id: "))
year = int(input("sheikvanet celi: "))
name = input("sheikvanet saxeli: ")
age = int(input("sheikvanet asaki: "))
gender = input("sheikvanet sqesi: ")
movie = input("sheikvanet filmi: ")
# მომხმარებელმა უნდა შეიყვანოს id, წელი , სახელი , ასაკი ,სქესი , ფილმის სახელი
cursor1.execute("INSERT INTO oscar (id, year, name, age, gender, movie) VALUES (?,?,?,?,?,?)", (id, year, name, age, gender, movie))
ამ ფუნქციით ვუთითებთ თუ რა value უნდა დაიწეროს
conn.commit()
# N4
age1 = int(input("msaxiobis asaki,monacemebis shesacvlelad :"))
name1 = input("oskarosani msaxiobis saxeli, monacemebis shesacvlelad :")
მომხმარებელს ვთოხვთ მიუთითოს მსახიობის ასაკი და სახელი მონაცემების შესაცვლელად
update_file= "UPDATE oscar SET age = ? and name = ?"
update-ის მეშვეობით ვასწორებთ შეყვანილ მონაცემებს
cursor1.execute(update_file,(age1,name1))
ამ ფუნქციით კი საბოლოოდ იცვლება ახალი მონაცემებით
conn.commit()