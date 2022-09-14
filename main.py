from urllib import request
from bs4 import BeautifulSoup;
import requests;
import pandas as pd;

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn';
res = requests.get(url);

soup = BeautifulSoup(res.content, 'html.parser');
title_lst = soup.select('div.tit3');

tit_list = [];
