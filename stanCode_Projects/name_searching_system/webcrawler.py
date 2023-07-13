"""
File: webcrawler.py
Name: Yutung
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #
        tags = soup.tbody.find_all('td')

        male_total = 0
        female_total = 0
        male_count = 0
        female_count = 0
        # Iterate over a list of tags that are between td and /td
        for i, tag in enumerate(tags):
            if i % 5 == 2:
                male_total += int(tag.text.replace(',', ''))
                male_count += 1
            elif i % 5 == 4:
                female_total += int(tag.text.replace(',', ''))
                female_count += 1
            if male_count == 200 and female_count == 200:
                break

        print('Male Number:', male_total)
        print('Female Number:', female_total)


if __name__ == '__main__':
    main()
