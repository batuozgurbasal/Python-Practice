"""
https://platform.stratascratch.com/coding/10285-acceptance-rate-by-date?code_type=2

Acceptance Rate By Date

What is the overall friend acceptance rate by date? Your output should have the rate of acceptances by the date the request was sent. 
Order by the earliest date to latest. Assume that each friend request starts by a user sending (i.e., user_id_sender) a friend request to another 
user (i.e., user_id_receiver) that's logged in the table with action = 'sent'. If the request is accepted, the table logs action = 'accepted'. 
If the request is not accepted, no record of action = 'accepted' is logged.

<fb_friend_requests>

user_id_sender: object
user_id_receiver: object
date: datetime64[ns]
action: object

"""

# Import your libraries
import pandas as pd

# Start writing code
df_sent = fb_friend_requests[fb_friend_requests['action']=='sent']
df_accept = fb_friend_requests[fb_friend_requests['action']=='accepted']

# left join df_sent with df_accept
df_action = df_sent.merge(df_accept, how = 'left', on = ['user_id_sender', 'user_id_receiver'], suffixes = ['_sent', '_accept'])

df_rate = df_action.groupby('date_sent').count().reset_index()

df_rate['acceptance_rate'] = df_rate['action_accept']/df_rate['action_sent']
df_rate[['date_sent', 'acceptance_rate']]
