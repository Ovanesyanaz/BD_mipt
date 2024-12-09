DELETE FROM USERS;
DELETE FROM LOG;


-- чистка бд
INSERT INTO USERS (user_id, email, geo)
SELECT substr(user_id, 6, 4), email, geo
FROM USERS_DIRTY WHERE geo is not null AND email is not null;

INSERT INTO LOG (user_id, time, bet, win)
SELECT substr(user_id, 30, 4) as userid, substr(time, 2), bet, win
FROM LOG_DIRTY WHERE user_id != "#error" AND time is not null AND userid in (SELECT user_id FROM USERS);

-- task a
SELECT avg(CAST(visits as REAL) / CAST(bets as REAL))
FROM 
     (SELECT user_id, count(*)  as visits FROM LOG GROUP BY user_id) as visits,
     (SELECT user_id, count(*) as bets FROM LOG WHERE bet != 0 GROUP BY user_id) as bets
WHERE visits.user_id = bets.user_id;

-- task b
SELECT avg(procent_win)
FROM (
    SELECT
        case when sum(win) != 0
        then (CAST(sum(win) as REAL) * 100.0) /  CAST(sum(bet) as REAL)
        else 0
        end as procent_win
    FROM LOG group by user_id
);

-- task c
SELECT user_id, MAX(0, sum(win) - sum(bet))
FROM LOG group by user_id;

-- task d
SELECT geo, sum(bet - win) as dohod
FROM LOG JOIN USERS ON USERS.user_id = LOG.user_id 
GROUP BY geo ORDER BY dohod DESC;

-- task e
SELECT geo, max(bet) as max_bet 
FROM LOG JOIN USERS ON USERS.user_id = LOG.user_id 
GROUP BY geo ORDER BY max_bet DESC;