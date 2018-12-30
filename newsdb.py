import psycopg2

DBNAME = "news"


def connect():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()


def first_query():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(
        "SELECT title, COUNT(path) as views FROM articles "
        "INNER JOIN log ON status LIKE '%200%'"
        " WHERE log.path = concat('/article/', articles.slug) "
        "GROUP BY title ORDER BY views DESC LIMIT 3")
    posts = c.fetchall()
    db.close()
    return posts


def second_query():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("SELECT name, COUNT(path) as views "
              "FROM authors INNER JOIN articles "
              "ON articles.author = authors.id "
              "INNER JOIN log ON status LIKE '%200%' "
              "WHERE log.path = CONCAT('/article/', articles.slug) "
              " GROUP BY name ORDER BY views DESC")
    posts = c.fetchall()
    db.close()
    return posts


def third_query():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = (
        "select day, perc from ("
        "select day, round((sum(requests)/(select count(*) from log where "
        "substring(cast(log.time as text), 0, 11) = day) * 100), 2) as "
        "perc from (select substring(cast(log.time as text), 0, 11) as day, "
        "count(*) as requests from log where status like '%404%' group by day)"
        "as log_percentage group by day order by perc desc) as final_query "
        "where perc >= 1")
    ''''c.execute("WITH refined AS "
              "(SELECT time, "
              "(AVG(CASE WHEN status LIKE '%404%' THEN 1.0 ELSE 0 END"")::DECIMAL *100) "
              " as errors"
              " FROM log GROUP BY time::timestamp::date) "
              "SELECT * FROM refined WHERE (errors*100) > 1")
    '''
    c.execute(query)
    posts = c.fetchall()
    db.close()
    return posts
