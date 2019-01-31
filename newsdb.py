import psycopg2

DBNAME = "news"


def connect():
    try:
        db = psycopg2.connect("dbname={}".format(DBNAME))
        cursor = db.cursor()
        return db, cursor
    except psycopg2.DatabaseError as e:
        print(e)

'''This method answers the following question :-
What are the most popular three articles of all time?
Which articles have been accessed the most? 
'''
def first_query():
    db, c = connect()
    c.execute("SELECT title, COUNT(path) as views FROM articles "
              "INNER JOIN log ON status LIKE '%200%'"
              " WHERE log.path = concat('/article/', articles.slug) "
              "GROUP BY title ORDER BY views DESC LIMIT 3")
    posts = c.fetchall()
    db.close()
    return posts

'''
This method answers the following question :-
Who are the most popular article authors of all time? 
That is, when you sum up all of the articles each author has written,
which authors get the most page views? 
Present this as a sorted list with the most popular author at the top
'''
def second_query():
    db, c = connect()
    c.execute("SELECT name, COUNT(path) as views "
              "FROM authors INNER JOIN articles "
              "ON articles.author = authors.id "
              "INNER JOIN log ON status LIKE '%200%' "
              "WHERE log.path = CONCAT('/article/', articles.slug) "
              " GROUP BY name ORDER BY views DESC")
    posts = c.fetchall()
    db.close()
    return posts

'''
This method answers the following question :-
On which days did more than 1% of requests lead to errors?
'''
def third_query():
    db, c = connect()
    c.execute("WITH refined AS "
              "(SELECT DATE(log.time) AS date, "
              "(AVG(CASE WHEN log.status LIKE '%404%' THEN 1.0 ELSE 0 END"")) "
              "AS errors"
              " FROM log GROUP BY DATE(log.time)) "
              "SELECT * FROM refined GROUP BY refined.date, refined.errors"
              " HAVING (refined.errors*100) > 1")
    posts = c.fetchall()
    db.close()
    return posts
