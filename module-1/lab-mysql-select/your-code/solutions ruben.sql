USE pubs;

/* challenge 1*/
Select authors.au_id as AUID,  au_lname as Last_name, au_fname as First_name, titles.title as TITLE, publishers.pub_name as PUBLISHER
FROM authors
LEFT join titleauthor 
on  authors.au_id = titleauthor.au_id
LEFT join titles 
on titleauthor.title_id = titles.title_id 
LEFT join publishers 
on titles.pub_id = publishers.pub_id;

/* Challenge 2*/
Select authors.au_id as 'AUID',  au_lname as 'Last_name', au_fname as 'First_name', publishers.pub_name as 'PUBLISHER', count(titles.title) as 'TITLE_COUNT'
FROM authors
LEFT join titleauthor on  authors.au_id = titleauthor.au_id
LEFT join titles on titleauthor.title_id = titles.title_id 
LEFT join publishers on titles.pub_id = publishers.pub_id
GROUP BY PUBLISHER,authors.au_id
ORDER BY TITLE_COUNT DESC;


/* challenge 3*/
Select a.au_id as auID,  au_lname as Last_name, au_fname as First_name, sum(titles.ytd_sales) as TOTAL
FROM authors as a
LEFT join titleauthor
on titleauthor.au_id = a.au_id
LEFT join titles
on titles.title_id = titleauthor.title_id
LEFT join publishers
on publishers.pub_id = titles.pub_id
GROUP BY auID
ORDER BY TOTAL DESC
LIMIT 3;

/* CHALLENGE 4 */

Select a.au_id as auID,  au_lname as Last_name, au_fname as First_name , coalesce((titles.ytd_sales),0) as PROFIT
FROM authors as a
LEFT join titleauthor
on titleauthor.au_id = a.au_id
LEFT join titles
on titles.title_id = titleauthor.title_id
LEFT join publishers
on publishers.pub_id = titles.pub_id
GROUP BY auID, PROFIT
ORDER BY PROFIT DESC;

/* Bonus*/
Select a.au_id as auID,  au_lname as Last_name, au_fname as First_name, coalesce(((titles.advance + titles.royalty) * (titleauthor.royaltyper / 100)), 0) AS PROFIT
FROM authors as a
LEFT join titleauthor
on titleauthor.au_id = a.au_id
LEFT join titles
on titles.title_id = titleauthor.title_id
GROUP BY auID, PROFIT
ORDER BY PROFIT DESC
LIMIT 3;

*/