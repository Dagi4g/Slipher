CREATE TABLE IF NOT EXISTS subjects (
	"subject_id" INTEGER PRIMARY KEY AUTOINCREMENT,
	"name" TEXT NOT NULL UNIQUE,
	"rating" NUMERIC
);


CREATE TABLE IF NOT EXISTS "topics"(
	
	"topic_id" INTEGER PRIMARY KEY AUTOINCREMENT,
	"name" TEXT NOT NULL,
	"last_seen" DATE,
	"rating" NUMERIC,
	"subject_id" INTEGER,
	FOREIGN KEY("subject_id") REFERENCES "subject"("subject_id")
);

CREATE TABLE IF NOT EXISTS "subtopics"(
	"subtopic_id" INTEGER PRIMARY KEY AUTOINCREMENT,
	"name" TEXT NOT NULL,
	"last_seen" DATE,
	"ratings" NUMERIC,
	"topic_id" INTEGER,
	FOREIGN KEY("topic_id") REFERENCES "topics"("topic_id")
);

CREATE TABLE IF NOT EXISTS "reviews_box"(
	"id" INTEGER PRIMARY KEY AUTOINCREMENT,
	"topic_id" INTEGER ,
	"box_level" INTEGER,
	"next_review" DATE,
	FOREIGN KEY("topic_id") REFERENCES "topics"("topic_id") ON DELETE CASCADE
);

