step:
1. generate new items. (even its just one item change)
2. call allChange function
update;
move

===========关于在atp网站上爬数据
在atp网站上抓取日期：
<ul class="dropdown" data-value="rankDate">里
^.*<.*$\n 替换为 ''
then:
^\s* 替换为 ''

某一日期的排名前十的网页，url例子是
http://www.atpworldtour.com/en/rankings/singles?rankDate=2000-01-10&rankRange=0-10

排名前十的网页，抓取数据
排名数据选择器#rankingDetailAjaxContainer > table > tbody
遍历所有10个tr
    country: #rankingDetailAjaxContainer > table > tbody > tr:nth-child(1) > td.country-cell > div > div > img, alt属性 //1是变量,排名第几该变量就是几
    player: #rankingDetailAjaxContainer > table > tbody > tr:nth-child(1) > td.player-cell > a, val
    score: #rankingDetailAjaxContainer > table > tbody > tr:nth-child(1) > td.points-cell > a, val

 
