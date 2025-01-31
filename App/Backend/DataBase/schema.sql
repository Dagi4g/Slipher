CREATE TABLE IF NOT EXISTS subjects (
	"subject_id" INTEGER,
	"name" TEXT NOT NULL UNIQUE,
	"last_seen" DATE,
	"rating" NUMERIC,
	PRIMARY KEY("subject_id")
);


CREATE TABLE IF NOT EXISTS "topics"(
	
	"topic_id" INTEGER,
	"name" TEXT NOT NULL,
	"last_seen" DATE,
	"rating" NUMERIC,
	"remember_me" DATE,
	"subject_id" INTEGER,
	PRIMARY KEY ("topic_id"),
	FOREIGN KEY("subject_id") REFERENCES "subject"("subject_id")
);

CREATE TABLE IF NOT EXISTS "subtopics"(
	"subtopic_id" INTEGER,
	"name" TEXT NOT NULL,
	"last_seen" DATE,
	"ratings" NUMERIC,
	"remeber_me" DATE,
	"topic_id" INTEGER,
	PRIMARY KEY("subtopic_id"),
	FOREIGN KEY("topic_id") REFERENCES "topics"("topic_id")
);
