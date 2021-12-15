# 정규 표현식 사용
import re 

# 원본 로그 파일 : read text
f=open('c:\\work\\PV3.txt','rt')
# 복사본 write text
g=open('c:\\work\\PV3_copy.txt','wt',encoding='utf-8')

#많은 라인의 파일이면 
#한번에 한줄씩 읽어서 처리한다.  
#파일의 EOF(End Of File)이 아니면 계속 읽도록 한다. 
line = f.readline()
# EOF를 찾기
while (line != ''):
    # \\\\ 백슬래시가 연속 4개인지아닌지 
    if (re.search("\d{4}", line)):
        g.write(line + "\n")
    line = f.readline()

f.close() 
g.close()








