PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

DROP TABLE problems;
DROP TABLE settings;
DROP TABLE default_sync;

CREATE TABLE problems (

pid text,

site text,

code text);
CREATE TABLE settings (

option TEXT,

value TEXT,

number_i INT,

number_f FLOAT);
INSERT INTO settings VALUES('loginWhenStartup',NULL,1,NULL);
INSERT INTO settings VALUES('oiclassUsername','',NULL,NULL);
INSERT INTO settings VALUES('oiclassPassword','',NULL,NULL);
INSERT INTO settings VALUES('hydroojUsername','',NULL,NULL);
INSERT INTO settings VALUES('hydroojPassword','',NULL,NULL);
INSERT INTO settings VALUES('uojUsername','',NULL,NULL);
INSERT INTO settings VALUES('uojPassword','',NULL,NULL);
INSERT INTO settings VALUES('codeforcesUsername','',NULL,NULL);
INSERT INTO settings VALUES('codeforcesPassword','',NULL,NULL);
INSERT INTO settings VALUES('language','Simplified Chinese',NULL,NULL);
CREATE TABLE default_sync (
site TEXT,
onOroff BOOLEAN);
INSERT INTO default_sync VALUES('Oiclass',0);
INSERT INTO default_sync VALUES('HydroOJ',0);
INSERT INTO default_sync VALUES('UOJ',0);
INSERT INTO default_sync VALUES('Codeforces',0);
COMMIT;
