CREATE TABLE IF NOT EXISTS subjects (
	"subject_id" INTEGER,
	"name" TEXT NOT NULL UNIQUE,
	"rating" NUMERIC,
	PRIMARY KEY("subject_id")
);


CREATE TABLE IF NOT EXISTS "topics"(
	
	"topic_id" INTEGER,
	"name" TEXT NOT NULL,
	"last_seen" DATE,
	"rating" NUMERIC,
	"subject_id" INTEGER,
	PRIMARY KEY ("topic_id"),
	FOREIGN KEY("subject_id") REFERENCES "subject"("subject_id")
);

CREATE TABLE IF NOT EXISTS "subtopics"(
	"subtopic_id" INTEGER,
	"name" TEXT NOT NULL,
	"last_seen" DATE,
	"ratings" NUMERIC,
	"topic_id" INTEGER,
	PRIMARY KEY("subtopic_id"),
	FOREIGN KEY("topic_id") REFERENCES "topics"("topic_id")
);

CREATE TABLE IF NOT EXISTS "reviews_box"(
	"id" INTEGER ,
	"topic_id" INTEGER ,
	"box_level" INTEGER,
	"next_rievew" DATE,
	PRIMARY KEY("id")
	FOREIGN KEY("topic_id") REFERENCES "topics"("topic_id")
);

