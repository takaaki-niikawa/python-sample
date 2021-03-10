import tkinter.messagebox as mb

ans = mb.askyesno('質問','動物は好き？')

if ans == True:
    ans = mb.askyesno('質問','犬と猫、犬のほうが好き？')
    if ans == True:
        ans = mb.askyesno('質問','犬は飼ってる？')
        if ans == True:
            mb.showinfo('ほんと！？','いいなー')
        else:
            mb.showinfo('ほんと！？','飼ってないんだ')
    else:
        ans = mb.askyesno('質問','猫は飼ってる？')
        if ans == True:
            mb.showinfo('僕も','僕も同じ')
        else:
            mb.showinfo('ほんと！？','飼ってないんだ')
else:
    mb.showinfo ('僕は','僕は猫を飼っている')
