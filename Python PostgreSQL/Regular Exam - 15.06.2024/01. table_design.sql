CREATE TABLE IF NOT EXISTS accounts(
	id SERIAL PRIMARY KEY,
	username VARCHAR(30) UNIQUE NOT NULL,
	password VARCHAR(30) NOT NULL,
	email VARCHAR(50) NOT NULL,
	gender CHAR(1) check(gender in ('F','M')) NOT NULL, 
	age INTEGER NOT NULL,
	job_title VARCHAR(40) NOT NULL,
	ip VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS addresses(
	id SERIAL PRIMARY KEY,
	street VARCHAR(30) NOT NULL,
	town VARCHAR(30) NOT NULL,
	country VARCHAR(30) NOT NULL,
	account_id INTEGER NOT NULL, 

	CONSTRAINT fc_addresses_accounts
		FOREIGN KEY (account_id)
		REFERENCES accounts(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS photos(
	id SERIAL PRIMARY KEY,
	description TEXT,
	capture_date TIMESTAMP NOT NULL,
	views INTEGER DEFAULT 0,

	CONSTRAINT ck_photos_views_is_positive
		CHECK (views >= 0)
);

CREATE TABLE IF NOT EXISTS comments(
	id SERIAL PRIMARY KEY,
	content VARCHAR(255) NOT NULL,
	published_on TIMESTAMP NOT NULL,
	photo_id INTEGER NOT NULL, 

	CONSTRAINT fc_comments_photos
		FOREIGN KEY (photo_id)
		REFERENCES photos(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS accounts_photos(
	account_id INTEGER NOT NULL, 
	photo_id INTEGER NOT NULL, 

	CONSTRAINT my_primary_key PRIMARY KEY (account_id, photo_id),

	CONSTRAINT fc_accounts_photos_accounts
		FOREIGN KEY (account_id)
		REFERENCES accounts(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE,

	CONSTRAINT fc_accounts_photos_photos
		FOREIGN KEY (photo_id)
		REFERENCES photos(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS likes(
	id SERIAL PRIMARY KEY,
	photo_id INTEGER NOT NULL,
	account_id INTEGER NOT NULL, 

	CONSTRAINT fc_likes_photos
		FOREIGN KEY (photo_id)
		REFERENCES photos(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	
	CONSTRAINT fc_likes_accounts
		FOREIGN KEY (account_id)
		REFERENCES accounts(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);