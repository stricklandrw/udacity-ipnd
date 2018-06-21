#!/usr/bin/env python
"""Database article and errors report generator."""
import datetime
import psycopg2
import bleach

DBNAME = "news"
TOP_ARTICLES = "3"


def get_article_counts(parameters):
    """Return all posts from the 'database', most recent first."""
    """Open PostGRES database session and returns a new connection instance"""
    db = psycopg2.connect(database=DBNAME)
    """Sets up interaction with the database to perform operations"""
    c = db.cursor()
    """Pull article titles and hit counts from article_hits database view"""
    """Example - ('Candidate is jerk, alleges rival', 338647L)"""
    sql = '''SELECT * FROM article_hits limit (%s);'''
    data = (bleach.clean(parameters),)
    """Execute sends command to the database"""
    c.execute(sql, data)
    """Returns all information from executed command"""
    print """\r\nWhat are the most popular three articles of all time?\r\n"""
    for row in c.fetchall():
        title = row[0]
        count = row[1]
        print '''"''' + str(title) + '''" - ''' + str(count) + """ views"""
    """Closes database connection"""
    db.close()


def popular_authors():
    """Return all posts from the 'database', most recent first."""
    """Open PostGRES database session and returns a new connection instance"""
    db = psycopg2.connect(database=DBNAME)
    """Sets up interaction with the database to perform operations"""
    c = db.cursor()
    """Pull correlated data of authors and the sums of hits against all their
    articles from article_hits database view"""
    """Example - ('Ursula La Multa', Decimal('507594'))"""
    sql = """SELECT authors.name, SUM( article_hits.hits )
    FROM authors, articles, article_hits
    WHERE article_hits.article_title = articles.title
    AND authors.id = articles.author
    GROUP BY authors.name
    ORDER BY sum desc;"""
    """Execute sends command to the database"""
    c.execute(sql)
    """Return all info from executed command & formats for report view"""
    print """\r\nWho are the most popular article authors of all time?\r\n"""
    for row in c.fetchall():
        author = row[0]
        count = row[1]
        print str(author) + """ - """ + str(count) + """ views"""
    """Closes database connection"""
    db.close()


def error_report():
    """Return all posts from the 'database', most recent first."""
    """Open PostGRES database session and returns a new connection instance"""
    db = psycopg2.connect(database=DBNAME)
    """Sets up interaction with the database to perform operations"""
    c = db.cursor()
    """Pull days from errors view of database with more than 1% error"""
    """Ex. - ('July 17, 2016', Decimal('97.7'))"""
    sql = """SELECT to_char(date, 'FMMonth FMDD, FMYYYY') as day, percent_good
    FROM errors
    WHERE percent_good < '99'
    ORDER BY date;"""
    """Execute sends command to the database"""
    c.execute(sql)
    """Returns all info from executed command and formats for report viewing"""
    print "\r\nOn which days did more than 1% of requests lead to errors?\r\n"
    for row in c.fetchall():
        date = row[0]
        error_percent = 100 - row[1]
        print str(date) + """ - """ + str(error_percent) + """% errors"""
    """Closes database connection"""
    db.close()


def report():
    """Generate a report of the most popular 3 articles of all time."""
    get_article_counts(TOP_ARTICLES)
    """Generate a report of the most popular authors of all time."""
    popular_authors()
    """Generate a report of the day(s) with more than 1% errors requests."""
    error_report()


report()
