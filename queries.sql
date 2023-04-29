-- Database name: n18_contacts_db

-- Database
CREATE DATABASE IF NOT EXISTS n18_contacts_db;

-- Use database
USE n18_contacts_db;

-- contacts
CREATE TABLE IF NOT EXISTS contacts (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(64) NOT NULL,
    last_name VARCHAR(64),
    company VARCHAR(128),
    day INT,
    month INT,
    year INT,
    gender VARCHAR(6),
    notes TEXT
);

-- phones
CREATE TABLE IF NOT EXISTS contact_phones (
    contact_id INT NOT NULL,
    phone VARCHAR(20), -- +998 00 000 00 00
    FOREIGN KEY (contact_id) REFERENCES contacts(id)
);

-- emails
CREATE TABLE IF NOT EXISTS contact_emails (
    contact_id INT NOT NULL,
    email VARCHAR(128), -- a@a.com
    FOREIGN KEY (contact_id) REFERENCES contacts(id)
);

-- socials
CREATE TABLE IF NOT EXISTS contact_socials (
    contact_id INT NOT NULL,
    social VARCHAR(32),
    link VARCHAR(256),
    FOREIGN KEY (contact_id) REFERENCES contacts(id)
);

-- addresses
CREATE TABLE IF NOT EXISTS contact_addresses (
    contact_id INT NOT NULL,
    country VARCHAR(64),
    city VARCHAR(32),
    street VARCHAR(256),
    home INT,
    FOREIGN KEY (contact_id) REFERENCES contacts(id)
);

-- MOCK DATA
-- contacts
insert into contacts (id, first_name, last_name, gender, company, day, month, year, notes) values (1, 'Fields', 'Flippen', 'Male', 'Flashset', 15, 7, 1994, null);
insert into contacts (id, first_name, last_name, gender, company, day, month, year, notes) values (2, 'Egbert', 'Bantham', 'Male', 'Skyndu', 11, 4, 1990, null);
insert into contacts (id, first_name, last_name, gender, company, day, month, year, notes) values (3, 'Miltie', 'Struss', 'Male', 'Zoomdog', 26, 10, 2002, null);
insert into contacts (id, first_name, last_name, gender, company, day, month, year, notes) values (4, 'Corette', 'Philler', 'Female', 'Shuffletag', 25, 3, 1994, null);
insert into contacts (id, first_name, last_name, gender, company, day, month, year, notes) values (5, 'Arv', 'Chellam', 'Male', 'Dabtype', 16, 10, 1999, null);
insert into contacts (id, first_name, last_name, gender, company, day, month, year, notes) values (6, 'Guendolen', 'Purse', 'Female', 'Skibox', 14, 10, 2002, null);
insert into contacts (id, first_name, last_name, gender, company, day, month, year, notes) values (7, 'Udale', 'Christian', 'Male', 'Roodel', 11, 9, 1999, null);
insert into contacts (id, first_name, last_name, gender, company, day, month, year, notes) values (8, 'Alyson', 'Wheelhouse', 'Female', 'Quire', 18, 3, 1997, null);
insert into contacts (id, first_name, last_name, gender, company, day, month, year, notes) values (9, 'Kareem', 'Lescop', 'Male', 'Rhybox', 23, 3, 1996, null);
insert into contacts (id, first_name, last_name, gender, company, day, month, year, notes) values (10, 'Wilhelmina', 'Pischof', 'Female', 'Tanoodle', 7, 4, 1992, null);

-- contact_phones
insert into contact_phones (contact_id, phone) values (5, '+55 (701) 425-4777');
insert into contact_phones (contact_id, phone) values (3, '+60 (222) 468-0699');
insert into contact_phones (contact_id, phone) values (5, '+356 (545) 318-1013');
insert into contact_phones (contact_id, phone) values (6, '+7 (288) 218-7304');
insert into contact_phones (contact_id, phone) values (5, '+63 (992) 885-2027');
insert into contact_phones (contact_id, phone) values (4, '+60 (260) 946-0042');
insert into contact_phones (contact_id, phone) values (5, '+86 (238) 172-3827');
insert into contact_phones (contact_id, phone) values (1, '+960 (185) 621-9033');
insert into contact_phones (contact_id, phone) values (9, '+256 (309) 738-3886');
insert into contact_phones (contact_id, phone) values (5, '+81 (540) 903-8345');
insert into contact_phones (contact_id, phone) values (4, '+380 (984) 348-9277');
insert into contact_phones (contact_id, phone) values (9, '+48 (929) 857-1600');
insert into contact_phones (contact_id, phone) values (4, '+86 (631) 758-6097');
insert into contact_phones (contact_id, phone) values (10, '+62 (698) 642-6832');
insert into contact_phones (contact_id, phone) values (2, '+63 (476) 499-1030');
insert into contact_phones (contact_id, phone) values (5, '+7 (510) 505-3493');
insert into contact_phones (contact_id, phone) values (1, '+223 (122) 354-7909');
insert into contact_phones (contact_id, phone) values (1, '+86 (650) 800-7081');
insert into contact_phones (contact_id, phone) values (7, '+62 (720) 975-7930');
insert into contact_phones (contact_id, phone) values (3, '+86 (843) 784-4055');

-- contact_emails
insert into contact_emails (contact_id, email) values (6, 'wgoodlud0@printfriendly.com');
insert into contact_emails (contact_id, email) values (10, 'thuntar1@bizjournals.com');
insert into contact_emails (contact_id, email) values (3, 'ascholes2@shinystat.com');
insert into contact_emails (contact_id, email) values (10, 'agoodin3@hp.com');
insert into contact_emails (contact_id, email) values (1, 'erowbottom4@goo.gl');
insert into contact_emails (contact_id, email) values (7, 'lgunda5@patch.com');
insert into contact_emails (contact_id, email) values (7, 'ccoundley6@umich.edu');
insert into contact_emails (contact_id, email) values (8, 'skillshaw7@twitpic.com');
insert into contact_emails (contact_id, email) values (9, 'ljohn8@nifty.com');
insert into contact_emails (contact_id, email) values (9, 'shavik9@wp.com');


SELECT * FROM contacts
    LEFT JOIN contact_phones ON contacts.id = contact_phones.contact_id
    LEFT JOIN contact_emails ON contacts.id = contact_emails.contact_id
    LEFT JOIN contact_addresses ON contacts.id = contact_addresses.contact_id
    LEFT JOIN contact_socials ON contacts.id = contact_socials.contact_id;
