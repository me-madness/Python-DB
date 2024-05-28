-- Remove Primary key

ALTER TABLE
	products
ADD COLUMN
	"id" SERIAL PRIMARY KEY;