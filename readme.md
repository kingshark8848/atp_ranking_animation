
## about
It's a project to grab tennis ATP ranking data from ATP official website, and then do a data visualization demo.

## Step
1. grab data from ATP offical website. 
write python script(use BeautifulSoup) `get_atp_ranking.py` 

2. write a demo html page use Vue.js. import json data from process above and make the animation.
`atp_ranking.html`

## Run
the `atp_ranking.html` can be run in web brower directly. But since this page import local json data, which will violate Cross Origin policy of chrome, so please:
option1: directly open it with Firefox.
option2: build a simple local web server. 

## Misc
### How to display players' national flag properly
To display players' national flag properly, you need to put images into `[project_root]/public/imgs/nation_flags/`. All flags images files are large, so I don't include them on github.