# Alter the Table

ALTER TABLE minions_nfo
ADD COLUMN code CHAR(4),
ADD COLUMN task TEXT,
ADD COLUMN salary NUMERIC(8, 3);