SELECT * FROM public.votes
ORDER BY user_id ASC, post_id ASC 
	
select post. *,count(votes.post_id)  as Total_votes from post left join votes on post.id = votes.post_id 
group by post.id 

