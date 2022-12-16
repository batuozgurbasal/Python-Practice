"""
https://platform.stratascratch.com/coding/9991-top-ranked-songs?code_type=2

Top Ranked Songs

Find songs that have ranked in the top position. Output the track name and the number of times it ranked at the top.
Sort your records by the number of times the song was in the top position in descending order.

<spotify_worldwide_daily_song_ranking>

id: int64
position: int64
trackname: object
artist: object
streams: int64
url: object
date: datetime64[ns]
region: object

"""

# Import your libraries
import pandas as pd

# Start writing code
df = spotify_worldwide_daily_song_ranking
df = df[df['position'] == 1]
df = df.groupby('trackname',as_index = False).sum()
df['times_top1'] = df['position']
result = df[['trackname','times_top1']]
result 
