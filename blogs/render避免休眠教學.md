---
title: render避免休眠教學

---

# render避免休眠
cron-job

## render 
[render](https://render.com/)
render是一個極為好用的免費線上主機，但由於免費資源有限，所以會自動休眠來避免主機消耗，這邊就不詳細介紹了，如果想仔細研究一下請看下文:
[render免費主機教學 作者:theoyu314159](https://hackmd.io/@theoyu314159/render)

## cron-job
[cron-job](https://console.cron-job.org/)
這一次要用到的網站叫做cron-job，免費版本的數量有限制，但這種事情，多創幾個...就可以解決了(噓...)，註冊完帳號之後呢，會先帶你進入儀表板，右上方新增定時工作，輸了標題，還有你的render網址，因為render預設是15分鐘沒動靜就會自動休眠，但避免過度消耗網站流量，所以我們設定10分鐘就夠了。
![job](https://i.meee.com.tw/VQolmVx.png)