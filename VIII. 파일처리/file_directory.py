import os

# data = os.listdir(".")      # 상대경로, 현재 디렉터리
# data = os.listdir("..")      # 상대경로, 상위 디렉터리
data = os.listdir("C:/Users")      # 절대경로, Users 디렉토리
# data = os.listdir("C:\Users")      # 따옴표 안에서 사용되는 \는 이스케이프 문자임.
# data = os.listdir("C:\\Users")      # 역슬래시 표현 시에는 \\ 를 사용.
print(data)

for d in data:
    print(d)
    print("is directory? : " + str(os.path.isdir(d)))
    print("is file? : " + str(os.path.isfile(d)))