class Contact:
    def __init__(self, first, last, gender, day, month, year, company) -> None:
        self.id = None
        self.first = first
        self.last = last
        self.gender = gender
        self.born = {
            "day": day,
            "month": month,
            "year": year
        }
        self.company = company
        self.phones = list()
        self.emails = list()
        self.addresses = list()
        self.socials = list()
    
    def add_phone(self, phone):
        self.phones.append(phone)
    
    def add_email(self, email):
        self.emails.append(email)
    
    def add_social(self, social, link):
        self.socials.append({
            "social": social,
            "link": link
        })
    
    def add_address(self, country, city, street, home):
        self.addresses.append({
            "country": country,
            "city": city,
            "street": street,
            "home": home
        })
    
    def __str__(self) -> str:
        return f"""
        {self.first} {self.last}, {self.gender} | {self.born["day"]}.{self.born["month"]}.{self.born["year"]}
        Company: {self.company}
        Addresses: {self.addresses}
        Phones: {self.phones.__str__()}
        Socials: {self.socials.__str__()}
        """
