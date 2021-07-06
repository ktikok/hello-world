# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
2021.07.06
this file is tested on Ubuntu
1. 원래는 영어 자막을 클릭했지만, select에서 옵션을 선택하는 것으로 바꿨다.
2. pause가 안되서, 
"""

from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

special_symbal=[]

for i in range(65,91):
    special_symbal.append(chr(i))
print('')
for i in range(97,123):
    special_symbal.append(chr(i))
    
special_symbal_1=['.','\'','\"','?','!']

lecture=1

browser=webdriver.Chrome('chromedriver_linux64/chromedriver')
# /home/yhep_ex_04/hello-world/LearningEnglish/chromedriver_linux64/chromedriver
browser.maximize_window()
#브라우저 창을 최대로
#name_title='yasin kakande what's missing in the global debate over refugees
browser.get('https://www.ted.com/talks?sort=popular&duration=0-6&language=ko')#  &language=ko&duration=0-6, popular
# https://www.ted.com/talks?sort=popular&duration=0-6&language=ko
# 'https://www.ted.com/talks?sort=newest&language=ko&duration=0-6'

browser.find_element_by_xpath('//*[@id="browse-results"]/div[1]/div['+str(lecture)+']/div/div/div/div[2]/h4[2]/a').click()
#time.sleep(3) # 페이지 뜨는 시간이 느려서... 뜨기까지 기다려야함..


"""
try:
    browser.find_element_by_xpath('//*[@id="content"]/div/div[4]/div[3]/section/div[1]/div[1]/select/option[1]').click()#english 누르기
except:
    browser.find_element_by_xpath('//*[@id="content"]/div/div[4]/div[2]/section/div[1]/div[1]/select/option[1]').click()#english 누르기
#English
#화면크기에 따라 버튼들의 위치가 바뀌어 오류가 날 수 있다.

"""

#'''
time.sleep(5)
# changing webpage taking time
try:
    browser.find_element_by_xpath('//*[@id="content"]/div/div[4]/div[1]/div/a[3]').click()#transcript 누르기
    # If there are theree options
    
except:
    browser.find_element_by_xpath('//*[@id="content"]/div/div[4]/div[1]/div/a[2]/span[1]').click()
    # if there are two options : details, transicript

select_element = browser.find_element_by_xpath('//*[@id="content"]/div/div[4]/div[2]/section/div[1]/div[1]/select')
#//*[@id="content"]/div/div[4]/div[2]/section/div[1]/div[1]/select
# 목차 가져오기

select_object = Select(select_element)
select_object.select_by_visible_text('English')
# 영어 선택하기
time.sleep(5)
english_sentences=browser.find_elements_by_xpath('//*[@id="content"]/div/div[4]/div[2]/section/div/div[2]/p/span/a') # this for big window
#english_sentences=browser.find_elements_by_xpath('//*[@id="content"]/div/div[4]/div[3]/section/div/div[2]/p/span/a') # this for smaill window
# 시간 별로 파트가 나눠진 경우까지 포함하기 위해서 div[2]>div로 바꿈.
# first sentence : //*[@id="content"]/div/div[4]/div[2]/section/div[2]/div[2]/p/span[1]/a
# //*[@id="content"]/div/div[4]/div[2]/section/div[2]/div[2]/p/span[1]/a

url=browser.current_url
f=open('score_list7.txt')
f_list=f.readlines()
writer_title1=f_list[-1].split(' ')[3].split('/')[4]
writer_title2=url.split('/')[4]
if writer_title2==writer_title1:
    if int(f_list[-1].split(' ')[1])+int(f_list[-1].split(' ')[0])<len(english_sentences):
        answer_count=[int(f_list[-1].split(' ')[0]), int(f_list[-1].split(' ')[1]), 0, url]
        for i in f_list[-1].split(' ')[4:-1]:
            answer_count.append(int(i))
    elif len(f_list[-1].split(' ')[4:-1])<len(english_sentences):
        answer_count=[0,0,0,url]
        for i in f_list[-1].split(' ')[4:-1]:
            answer_count.append(int(i))
    else:
        answer_count=[0,0,0,url]
else:        
    answer_count=[0,0,0,url]

f.close()
english_count=[answer_count[1]+answer_count[0]]
#'''

def pause(pause_count):
    if pause_count==10:
        pass
    else:
        try:
            # //*[@id="ted-player"]/div[4]/button
            # //*[@id="ted-player"]/div[4]/div/div/div[2]/div/div[1]/button
            # //*[@id="ted-player"]/div[3]/button
            browser.find_element_by_xpath('//*[@id="ted-player"]/div[3]/button').click()# 버튼이 보여야함, 자막이 없으면 'div3', 있으면 'div4'
            #print("script off")
        except:
            try:
                browser.find_element_by_xpath('//*[@id="ted-player"]/div[4]/button').click()# 2021.07.01추가
                #print("script on")
            except:
                try:
                    # //*[@id="ted-player"]/div[4]/button
                    # //*[@id="ted-player"]/div[4]/button
                    browser.find_element_by_xpath('//*[@id="ted-player"]/div[4]/div/div/div[2]/div/div[1]/button').click()# 2021.07.01추가
                    #print("clicked play button")
                except:
                    print("try to pause again")
                    time.sleep(0.1)
                    pause(pause_count+1)
                

def english(english_count):
    print('')
    if english_count!=1:
        print(english_sentences[english_count-2].text)
    words = english_sentences[english_count-1]
    words=words.text
    letter=''
    for words_1 in words:
        if (letter not in special_symbal):
            print(words_1,end='')
            letter=words_1
        elif(words_1 not in special_symbal):
            print(words_1,end='')
            letter=words_1
        else:
            print('*',end='')
            letter=words_1
    print('')#이게 없으면 어디까지가 정답인지 모르뮤ㅠ

def play(sentences,english_count):
    if english_count==1:
        sentences[english_count-1].click()
    else:
        sentences[english_count-2].click()
        
def main():
    #english_count=8
    #sentence_count=0
    
    print(len(english_sentences))
    while(english_count[0]<len(english_sentences)):
        #sentence_count=sentence_count+1
        english_count[0]=english_count[0]+1
        if english_count[0] in answer_count[4:]:
            
            #print(english_count[0])
            
            answer_count[0]=answer_count[0]+1
            continue
        english(english_count[0])
            
        play(english_sentences,english_count[0])
        answer=(english_sentences[english_count[0]-1]).text
        while(1):
            #print((english_sentences[english_count+sentence_count-1]).text)
            guess=input()
            check=1
            for i, j in zip(guess,answer):
                if i != j and i in special_symbal:
                    check=0
                    break
                else:
                    pass
                
            if(guess==''):
                pause(0)
            
            elif(guess=='raise'):
                raise
            
            elif(guess=='save'):
                f=open('score_list7.txt','a')
                answer_count[2]=answer_count[0]/(answer_count[1]+answer_count[0])*100
                for i in answer_count: 
                    f.write('%s ' % str(i))
                f.write('\n')
                f.close()
                print(english_count[0])
                print(answer_count)
                print('score:',answer_count[0]/answer_count[1]*100)
                raise
            elif check==1 and len(guess)==len(answer):                    
                #print('Correct answer!')
                answer_count[0]=answer_count[0]+1
                answer_count.append(english_count[0])
                break
            else:
                #print(english_sentences[english_count[0]-1].text)
                #print('Wrong answer!')
                answer_count[1]=answer_count[1]+1
                break

if __name__=='__main__':
    main()
    answer_count[2]=answer_count[0]/(answer_count[1]+answer_count[0])*100
    f=open('score_list7.txt','a')
    for i in answer_count: 
        f.write('%s ' % str(i))
        
    f.write('\n')
    f.close()
    print(english_count[0])
    print('correct : ', answer_count[0], 'wrong : ', answer_count[1], answer_count[0],)
    print('score:',answer_count[2])
    print('done')