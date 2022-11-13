#問user有沒有開車? (有/沒有)
#針對有或沒有的結果問年齡
driving = input('請問您有開過車嗎?(請回答「有」或「沒有」)')
age = input('請問您的年齡多大?')
age = int(age)
if driving == '有':
    if age < 18:
        print('18以下的青年還是不可以開車歐!')
    else:
        print('看來您有通過駕照考試了，很棒!')

elif driving == '沒有':
    if age < 18:
        print('您以後到了18歲可以考駕照去開車歐!')
    else:
        print('您符合考駕照資格，可以試試看考駕照後開車上路!')
else:
    print('您只能輸入「有」或「沒有」')