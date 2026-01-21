---
title: wsl下載 重灌

---

# wsl下載 重灌
ubuntu

## ubuntu
ubuntu可說為linux當中最為人知的，而若我們的windows想要灌linux除了可以直接雙系統，也可以用子系統，這時候wsl就出現啦。

## 安裝
微軟商城找到ubuntu:
![image alt](https://i.meee.com.tw/3TwpuvL.png)
下載完後就可以進入:
![image alt](https://i.meee.com.tw/PWDyaHP.png)
接著輸入username, psw就完成囉。
![image alt](https://i.meee.com.tw/asn2QGu.png)

## 重灌
在重灌時，如果只是刪除軟體，再次下載，可能會看到'Failed to attach disk'的訊息，這代表我們要在powershell做點加工:
```
wsl --list --verbose
```
確認版本
```
wsl --unregister ubuntu
```
完全的把它註銷掉，接下來就可以回到上面安裝的步驟囉。