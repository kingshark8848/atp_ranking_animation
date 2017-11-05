
## about
It's a project to grab tennis ATP ranking data from ATP official website, and then do a data visualization demo.

## Step
1. Write Python3 script `get_atp_ranking.py`. 
    - function: grab data from ATP offical website, export to json data for later usage;
    - tech: Python3 with lib `BeautifulSoup`  

2. Write a demo html page use Vue.js `index.html`
    - function: imported json
    - tech: 
        + main front-end framework is `Vue.js`;
        + to implement animation, I use Vue.js's feature on transition effect, with the help of [`tween.js`](https://github.com/tweenjs/tween.js/);
        + to do data import/transform, I use [`lodash.js`](https://lodash.com/)

## Run
The `index.html` can be run in web brower directly. But since this page import local json data, which will violate Cross Origin policy of chrome, so please:
    - option1: directly open it with Firefox.
    - option2: Build a Web Server. (nginx, apache, or there are many other ways to build a simple local web server. ) 

## Misc
### How to display players' national flag properly
To display players' national flag properly, you need to put images into `[project_root]/public/imgs/nation_flags/`. All flags images files are large, so I don't include them on github.