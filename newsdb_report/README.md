# newsdb

This Python script uses Python version 2 to pull and correlate log information to report on article and author popularity as well as system error occurrence information.

## Output

Each run of this program will query the database and produce the answers to the following questions:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Use

Using the system that has Python version 2 and the "news" PostGRESQL database running, execute the following command from the directory containing the newsdb.py Python script:

```python newsdb.py```

## View Definitions

### article_hits view

This view provides a table of article titles and hits against each article title in descending order for simple query against in order to provide the top 'X' articles read.

```
CREATE OR REPLACE VIEW article_hits as
SELECT articles.title as article_title,
  count(*) as hits
FROM log,
  articles
WHERE log.path = ('/article/' || articles.slug)
GROUP BY articles.title
ORDER BY hits desc;
```

### errors view

This view provides a table of the date, successful server hits ("200 OK" messages), errors both client and server (400 and 500 errors, respectively) and the success percentage rate in order to avoid division by 0 if there were no errors for the day.

```
CREATE OR REPLACE VIEW errors AS
SELECT ok_count.date AS date,
  ok_count.count AS oks,
  error_count.count AS errors,
  ROUND(100*(ok_count.count/(ok_count.count+error_count.count)::float)::numeric,1) AS percent_good
FROM
  (SELECT date_trunc('day', time) AS date, count(status)
  FROM log
  WHERE status = '200 OK'
  GROUP BY date) AS ok_count
LEFT JOIN
  (SELECT date_trunc('day', time) AS date, count(status)
  FROM log
  WHERE status
  SIMILAR TO '(4|5)%'
  GROUP BY date) AS error_count
ON ok_count.date = error_count.date;
```
