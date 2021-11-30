import csv
import random
import numpy as np
from faker import Faker # 이름 무작위로 받기 위한 라이브러리


user_records = 500 # 유저 수

user_fieldnames = ['userId', 'name', 'major', 'double major'] # 유저 디비에 들어갈 attribute

# 학과 정보
department_list = ['Computer_Science', 'Mechanical_Engineering', 'Business_Administration', 'Statistics', 'Electronic_Engineering', 'Electrical_engineering']
# item 정보
category_list = ['Document', 'Test Material', 'Video Lecture', 'Abridgment', 'Lecture Note', 'Book', 'Private lessons', 'Mentoring']
# 선호도 점수 list
preference_list = [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
# 평점 list
rating_list = [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
# userId 정보를 담을 list
user_list = []

# userId를 random 라이브러리를 통해 생성 후 user list에 해당 값 대입
def make_user_list():
    for i in range(user_records):
        d = random.randint(12150000, 12180000)
        while d in user_list:
            d = random.randint(12150000, 12180000)
        user_list.append(d)


# user 생성 함수
def make_user_data():
    
    with open('user_db_test.csv', 'w', encoding='UTF8', newline='') as f:
        # 랜덤 이름을 생성하기 위한 Faker 라이브러리 이용
        fake = Faker()
        # csv 파일을 작성하기 위한 파일 처리 변수
        user_writer = csv.writer(f)
        # 상단에 attribute 추가 -> user_fieldnames list에 담겨진  
        user_writer.writerow(user_fieldnames)
        # 임시적으로 user_list를 담을 user_temp_list
        user_temp_list = user_list

        # user db 생성 과정 
        for i in range(1, user_records+1):
            # 임시 변수 생성, double_major -> 복수 전공
            tmp_Id = random.choice(user_temp_list)
            tmp_major = random.choice(department_list)
            tmp_probability = random.randint(1, 10)
            if tmp_probability == 7 or tmp_probability == 8 or tmp_probability == 9 : 
                tmp_double_major = random.choice(department_list)
                # 복수전공과 주전공이 겹치면 안되기 때문에 
                while tmp_major == tmp_double_major :
                    tmp_double_major = random.choice(department_list)
                # 유저 정보 작성 과정
                user_writer.writerow([tmp_Id, fake.name(), tmp_major, tmp_double_major])        
                user_temp_list.remove(tmp_Id)
            
            else :
                tmp_double_major = ''
                # 유저 정보 작성 과정
                user_writer.writerow([tmp_Id, fake.name(), tmp_major, tmp_double_major])        
                user_temp_list.remove(tmp_Id)
    
    f.close()



make_user_list()
print(user_list)
make_user_data()

