from contact import Contact
import mysql.connector


class DBHandler:
    def __init__(self) -> None:
        self.c = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Qwerty!2345"
        )
        self.c.cursor().execute("USE n18_contacts_db;")

    def create_contact(self, contact: Contact):
        query = f"""insert into contacts (first_name, last_name, gender, company, day, month, year, notes) 
            values ('{contact.first}', '{contact.last}', '{contact.gender}', 
            '{contact.company}', {contact.born["day"]}, {contact.born["month"]}, {contact.born["year"]}, NULL);"""
        cursor = self.c.cursor()
        cursor.execute(query)
        contact.id = cursor.lastrowid

        for i in contact.phones:
            query = f"""insert into contact_phones (contact_id, phone) values ({contact.id}, '{i}')"""
            cursor.execute(query)
        
        for i in contact.emails:
            query = f"""insert into contact_emails (contact_id, email) values ({contact.id}, '{i}')"""
            cursor.execute(query)
        
        for i in contact.addresses:
            query = f"""insert into contact_addresses (contact_id, country, city, street, home) 
                        values ({contact.id}, '{i["country"]}', '{i["city"]}', '{i["street"]}', {i["home"]});"""
            cursor.execute(query)

        for i in contact.socials:
            query = f"""insert into contact_socials (contact_id, social, link) 
                        values ({contact.id}, '{i["social"]}', '{i["link"]}')"""
            cursor.execute(query)
        
        self.c.commit()
    
    def get_all(self) -> dict:
        query = """SELECT * FROM contacts
            LEFT JOIN contact_phones ON contacts.id = contact_phones.contact_id
            LEFT JOIN contact_emails ON contacts.id = contact_emails.contact_id
            LEFT JOIN contact_addresses ON contacts.id = contact_addresses.contact_id
            LEFT JOIN contact_socials ON contacts.id = contact_socials.contact_id;"""
        cursor = self.c.cursor()
        cursor.execute(query)
        data = cursor.fetchall()

        contacts = dict()
        for item in data:
            if item[0] in contacts:
                if item[9] is not None: contacts[item[0]].add_phone(item[10])
                if item[11] is not None: contacts[item[0]].add_email(item[12])
                if item[13] is not None: contacts[item[0]].add_address(item[14],item[15],item[16],item[17])
                if item[18] is not None: contacts[item[0]].add_social(item[19],item[20])

            else:
                contacts[item[0]] = Contact(
                    first=item[1],
                    last=item[2],
                    company=item[3],
                    day=item[4],
                    month=item[5],
                    year=item[6],
                    gender=item[7],
                )
                contacts[item[0]].id = item[0]
                if item[9] is not None: contacts[item[0]].add_phone(item[10])
                if item[11] is not None: contacts[item[0]].add_email(item[12])
                if item[13] is not None: contacts[item[0]].add_address(item[14],item[15],item[16],item[17])
                if item[18] is not None: contacts[item[0]].add_social(item[19],item[20])

        return contacts

    def get_contact_names(self):
        query = f"SELECT CONCAT(first_name, ' ', last_name) FROM contacts ORDER BY first_name;"
        cursor = self.c.cursor()
        cursor.execute(query)
        return cursor.fetchall()


if __name__ == "__main__":
    d = DBHandler()

    for k, v in d.get_all().items():
        print(k)
        print(v)


    # c = Contact("John", "McAdams", "Male", 12, 9, 1997, "Alpahbet Inc.")
    # c.add_phone("+998 96 127 18 82")
    # c.add_phone("+998 97 100 29 92")
    # c.add_email("johnmcadams@google.com")
    # c.add_email("john1997129@gmail.com")
    # c.add_address("Uzbekistan", "Tashkent", "Amir Temur", 45)

    # d.create_contact(c)
