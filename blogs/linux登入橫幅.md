---
title: linux登入橫幅

---

# linux登入橫幅
ascii

## 登入
大家是否覺得每次啟用wsl都單調了點，那我們就來做點加工吧!以我的theoyu314159為例:
![image alt](https://i.meee.com.tw/V9A2RPX.png)
成品會長這樣喔!

## ascii
ascii是一種美國資訊交換標準代碼，它使用7位元來表示128個不同的字元，而我們就稍微運用它來美化我們wsl一下，我習慣用這一個網頁轉換:
[Text to ASCII Art Generator: Create ASCII Art from Text](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type+Something+&x=none&v=4&h=4&w=80&we=false)
可以自行選擇喜歡的樣式。

## wsl設定
首先，先開啟檔案設定:
```
vim ~/.bashrc
```
去到最底下，換個一兩行，接著:
```
cat << "EOF"

將ascii貼上

EOF
```

接著保存，並從新啟動就能完成了。