---
title: render免費主機

---

# render主機教學
免費主機-支援flask

## flask
嗨嗨大家，好久不見，最近因為課業比較忙都沒有上線寫文章和寫程式，但想說在我東西忘掉之前先來把東西寫起來放哈哈...，回歸正題，flask是一個可將python和HTML結合的模組，當你不會寫js時是一個非常好用的東西，但當你寫完後想要分享給朋友看主機要一直開著會挺麻煩得，所以這時候就需要主機，但問題是就只是給朋友看還需要付錢也太浪費了吧，所以這時候就是免費主機上場的時刻啦。

## render
這一家公司其實不只主機的功能，還有其他server之類的，但其他東西我們就先不用到，先來開我們主機，首先我們先進入[render](https://render.com/)，註冊完畢後按右上角的new，選擇web service，這時候這家公司會與我們的GitHub連動，我們可以選擇裡面的專案來開主機(此專案內是要有您的網頁需要的東西ex:app.py...)，選定好後，會進到下一個頁面，這裡依序填上名稱等東西，選擇語言python3，接下來要選定國家，因為沒有tw地區，而我們在亞洲地區所以我都習慣選新加坡，接下來比較重要的就是'Build Command'和'Start Command'，假使今天需要的套件都寫在'requirements.txt'中，那麼就如下圖填上'pip install -r requirements.txt'，而要驅動的程式若是'app.py'，則輸入'python3 app.py'，接著往下如果要省錢就選免費吧，哈哈。
![render](https://i.meee.com.tw/0uCXDly.png)

## 部屬成功
部屬時會console一些東西，當出現'==> Your service is live 🎉'就代表可以使用了，接著他會給你帶著他們網域的網址，接下來就可以將他拿來傳給別人使用，但提醒您，因為資源有限，所以如果閒蕩15分鐘就會自動休眠，但只要點回網址它就會自動重啟了。
![open](https://i.meee.com.tw/nD5P9vx.png)