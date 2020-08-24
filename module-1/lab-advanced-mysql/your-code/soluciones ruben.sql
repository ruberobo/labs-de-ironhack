USE pubs;
/* Bonus del lab pasado*/
/*Select a.au_id as auID,  au_lname as Last_name, au_fname as First_name, coalesce(((titles.advance + titles.royalty) * (titleauthor.royaltyper / 100)), 0) AS PROFIT
FROM authors as a
LEFT join titleauthor
on titleauthor.au_id = a.au_id
LEFT join titles
on titles.title_id = titleauthor.title_id
GROUP BY auID, PROFIT
ORDER BY PROFIT DESC;*/

/*Challenge 1
step 1*/
Select titleauthor.title_id as Title_ID, titleauthor.au_id as Author_ID,
(titles.price * sales.qty * titles.royalty / 100 * titleauthor.royaltyper / 100) AS Royalty
FROM titleauthor
left join titles
on titleauthor.title_id = titles.title_id
left join sales
on titles.title_id = sales.title_id;

/* step 2*/
Select titleauthor.title_id as Title_ID, titleauthor.au_id as Author_ID,
sum(titles.price * sales.qty * titles.royalty / 100 * titleauthor.royaltyper / 100) AS total_Royalty
FROM titleauthor
left join titles
on titleauthor.title_id = titles.title_id
left join sales
on titles.title_id = sales.title_id
group BY Title_ID, Author_ID;

/*step 3*/
Select titleauthor.title_id as Title_ID, titleauthor.au_id as Author_ID,
Royalty + titles.advance AS profit
FROM titleauthor
left join titles
on titleauthor.title_id = titles.title_id
left join sales
on titles.title_id = sales.title_id
group BY Title_ID, Author_ID;