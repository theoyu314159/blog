---
title: Huggingface免費主機

---

# Huggingface免費主機
免費主機
## 免費主機
由於本然前陣子蠻喜歡寫網站的緣故，但又沒有錢，在我接觸到Flask之前我是先使用gradio，而這一個gradio主要可以做一些簡單的小網站，但無法像我們使用Flask依樣可以做出一些更精緻的網站，gradio會有固定的模板，一開始做了一開始做了一些網頁，想要給別人分享，但基於資金考量買不起主機，所以就找了一個較huggingface的免費主機。
## gradio
他是一個可以提供把python視覺化的程式，並且將它變成網頁，可以讓他分享給他人。
那這一次就拿個簡單的搜尋ip網站來當作示範，首先先放上程式(這次重點不再這就不做解說了)，這裡程式檔案必須叫做'app.py':
```
import gradio as gr
import socket
def do(url):
  outp=socket.gethostbyname(url)
  return outp
iface=gr.Interface(fn=do,title='網站ip找尋工具',description='輸入一個網址，我們可以幫您找到他的ip.',inputs='text',outputs='text')
iface.launch(share=True)
```
接著還要將我們所使用到的模組放的一個叫做'requirements.txt'的檔案中:
```
gradio
```

## 上架主機
![image](https://hackmd.io/_uploads/BkV9ANx4ee.png)
我們從[hugging face](https://huggingface.co/)按下space之後會跳到一個畫面，你可以輸入一些專案名稱介紹等，在'Select the Space SDK'點下'Gradio'，在下面'Space hardware
'選擇'FREE'，當然需求較大付錢也可以，接著進去之後，把電腦檔案上傳上去讓他開始啟動主機，接著就會開始log出來許多東西了，完成後如果剛剛設定公開就可以將網址傳給他人了，如果你點進去[我做的](https://huggingface.co/spaces/theoyu314159/webip)你將會發現要先啟動主機，沒錯，因為是免費主機，所以平時他會休眠，減少使用量，等到需要啟動時再啟動。

## 總結
我後來去看一下它的功能，感覺主要像是拿給一些AI測試使用的，並且依樣可以將我們的HTML放上去使用，所以本人真心滿推薦hugging face的(我好像在講廢話)。