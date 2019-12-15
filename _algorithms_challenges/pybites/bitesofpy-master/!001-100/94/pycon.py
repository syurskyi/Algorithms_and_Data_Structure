import os
import pickle
import re
import urllib.request
from collections import namedtuple
from datetime import timedelta

# prework
# download pickle file and store it in a tmp file
pkl_file = 'pycon_videos.pkl'
data = 'http://projects.bobbelderbos.com/pcc/{}'.format(pkl_file)
pycon_videos = os.path.join('/tmp', pkl_file)
urllib.request.urlretrieve(data, pycon_videos)

# the pkl contains a list of Video namedtuples
Video = namedtuple('Video', 'id title duration metrics')


def load_pycon_data(pycon_videos=pycon_videos):
    """Load the pickle file (pycon_videos) and return the data structure
       it holds"""
    with open(pycon_videos, 'rb') as pkl:
        return pickle.load(pkl)


def get_most_popular_talks_by_views(videos):
    """Return the pycon video list sorted by viewCount"""
    return sorted(videos, key=lambda vid: -int(vid.metrics['viewCount']))


def _like_ratio(vid):
    metrics = vid.metrics
    return -(float(metrics['likeCount']) - float(metrics['dislikeCount'])) / float(metrics['viewCount'])


def get_most_popular_talks_by_like_ratio(videos):
    """Return the pycon video list sorted by most likes relative to
       number of views, so 10 likes on 175 views ranks higher than
       12 likes on 300 views. Discount the dislikeCount from the likeCount.
       Return the filtered list"""
    return sorted(videos, key=_like_ratio)


duration_regex = re.compile(r'PT(?:(?P<hrs>\d+)H)?(?:(?P<mins>\d+)M)?(?:(?P<secs>\d+)S)?')


def _vid_time(vid):
    time_parts = duration_regex.match(vid.duration).groupdict(default=0)
    return timedelta(hours=int(time_parts['hrs']), minutes=int(time_parts['mins']), seconds=int(time_parts['secs']))


def get_talks_gt_one_hour(videos):
    """Filter the videos list down to videos of > 1 hour"""
    return [vid for vid in videos if _vid_time(vid) > timedelta(hours=1)]


def get_talks_lt_twentyfour_min(videos):
    """Filter videos list down to videos that have a duration of less than
       24 minutes"""
    return [vid for vid in videos if _vid_time(vid) < timedelta(minutes=24)]
