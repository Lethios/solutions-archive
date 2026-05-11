-- https://leetcode.com/problems/duplicate-emails/

SELECT p.email
FROM Person p
GROUP BY p.email
HAVING COUNT(p.email) > 1
