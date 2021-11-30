import csv
import random
import pandas as pd

# 아이템 이름 list
title_list = ['Java',
              'Spring Framework', 'Internet Programming', 'Operating System',
              'Calculus', 'Mathematical Statistics', 'Python', 'Data Analysis', 'Data Engineering',
              'React.js', 'JavaScript', 'HTML/CSS', 'Android', 'Kotlin', 'Swift', 'C#', 'C', 'Linear Algebra'
              'C++', 'Data Structure', 'Algorithm', 'Computer network', 'Statics', 'Thermodynamics', 'Energy power engineering',
              'Self-driving', 'Machine system control', 'fluid mechanics', 'Dynamics', 'Computer Structure', 'Logic Circuit', 'Basic Physics', 'industrial mathematics',
            'Regression Analysis', 'Computational Statistics', 'Elementary Statistics', 'Statistical Software and Lab', 'Probability', 'Statistical Mathematics', 'Big Data Fundamentals', 'Time Series Analysis and Lab', 'Sampling Theory and Lab', 'Experimental Design Lab', 'Categorical Data Analysis', 'Multivariate Statistics and Lab', 'Insurance Statistics', 'Financial Statistics', 'Bayesian Statistics', 'Data Mining',
             'Business English', 'Advertising', 'Business Data Analysis', 'Principles of Business Administration', 'Creative Business Plan Development', 'Corporate Bigdata Analysis', 'Digital Marketing', 'Consumer Behavior', 'Investments', 'Management Information System', 'Principles of Marketing', 'Operations Management','Organizational Behaviour', 'Economics', 'Principle of Accounting', 'Financial Management', 'Database',
              'Electronic Basic Digital Logic Design', 'Properties of Electrical & Electronic Materials', 'circuit theory', 'Computational Electromagnetics', 'Physical Electronics', 'Electronic Circuits', 'Numerical Analysis', 'Communication System', 'Automatic Control', 'Signal and System', 'Semiconductor Devices', 'Analog Circuit Capstone Design', 'Control System Capstone Design', 'Mobile Communications', 'Introductory Digital Signal Processing',
              'Electromagnetics', 'Digital Logic Circuits', 'Electrical Circuit Experiments', 'Electrical & Electronic measurements', 'Probability and Random Variables', 'Autonomous Vehicle Engineering', 'Control System Capstone Design', 'Electrical & Electronic measurements', 'Sensor Engineering', 'Embedded System Capstone Design', 'Robotics', 'Motor Control', 'Automatic Control', 'Electronic Display', 'The Physics of Power Semiconductor Devices', 'Power System Engineering', 'Motor Application', 'Smart Grid', 'High Voltage Engineering', 'Energy Conversion', 'Electric Vehicle Engineering', 
              'TOEIC', 'TOEFL', 'TOEIC Speaking', 'OPIC', 'HSK', 'DELF'
              ]

# 컴퓨터공학과 관련 자료들 이름 list
Computer_Science_list = ['Spring Framework', 'Internet Programming', 'Operating System', 'Calculus',
                         'Mathematical Statistics', 'Python', 'Data Analysis', 'Data Engineering', 'React.js', 'JavaScript', 'HTML/CSS', 'Android', 'Kotlin', 'Swift', 'C#',
                         'C++', 'Data Structure', 'Algorithm', 'Computer network', 'Computer Structure', 'Logic Circuit', 'Database', 'Data Mining', 'Linear Algebra']
# 기계공학과 관련 자료들 이름 list
Mechanical_Engineering_list = ['Dynamics', 'Basic Physics', 'C', 'Statics', 'Thermodynamics', 'industrial mathematics', 'Energy power engineering',
                                'Self-driving', 'Fluid mechanics', 'Machine system control', 'Linear Algebra']
# 경영학과 관련 자료들 이름 list
Business_Administration_list = ['Advertising', 'Business Data Analysis', 'Principles of Business Administration', 'Creative Business Plan Development', 'Corporate Bigdata Analysis', 'Digital Marketing', 'Consumer Behavior', 'Investments', 'Management Information System', 'Principles of Marketing', 'Operations Management','Organizational Behaviour', 'Economics', 'Principle of Accounting', 'Financial Management','Business English']
# 통계학과 관련 자료들 이름 list
Statistics_list = ['Regression Analysis', 'Computational Statistics', 'Linear Algebra', 'Elementary Statistics', 'Statistical Software and Lab', 'Probability', 'Statistical Mathematics', 'Big Data Fundamentals', 'Time Series Analysis and Lab', 'Sampling Theory and Lab', 'Experimental Design Lab', 'Categorical Data Analysis', 'Multivariate Statistics and Lab', 'Insurance Statistics', 'Financial Statistics', 'Bayesian Statistics', 'Data Mining']
# 전자공학과 관련 자료들 이름 list
Electronic_Engineering_list = ['Basic Physics', 'industrial mathematics', 'Electronic Basic Digital Logic Design', 'Properties of Electrical & Electronic Materials', 'circuit theory', 'Computational Electromagnetics', 'Physical Electronics', 'Electronic Circuits', 'Numerical Analysis', 'Communication System', 'Automatic Control', 'Signal and System', 'Semiconductor Devices', 'Analog Circuit Capstone Design', 'Control System Capstone Design', 'Mobile Communications', 'Introductory Digital Signal Processing']
# 전기공학과 관련 자료들 이름 list
Electrical_engineering_list = ['Basic Physics', 'industrial mathematics', 'Electromagnetics', 'Digital Logic Circuits', 'Electrical Circuit Experiments', '(Electrical & Electronic measurements', 'Probability and Random Variables', 'Autonomous Vehicle Engineering', 'Control System Capstone Design', 'Electrical & Electronic measurements', 'Sensor Engineering', 'Embedded System Capstone Design', 'Robotics', 'Motor Control', 'Automatic Control', 'Electronic Display', 'The Physics of Power Semiconductor Devices', 'Power System Engineering', 'Motor Application', 'Smart Grid', 'High Voltage Engineering', 'Energy Conversion', 'Electric Vehicle Engineering' ]

# 평점 DB Attribute
rating_fieldnames = ['userId', 'itemId', 'ratings']
# 유저 수
user_records = 500
# 평점 점수 list
rating_list = [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]

# user DB csv 파일을 불러와 dataframe 형태로 변환
df = pd.read_csv('user_db_test.csv', sep=',')
# item db csv 파일을 불러와 dataframe 형태로 변환
df_item = pd.read_csv('item_db_test.csv', sep=',')
# 필수 column들만 빼와서 정리, 형태는 Dataframe
column_user = df[['userId', 'major', 'double major']]
column_item = df_item[['itemId', 'title']]
# 해당 Dataframe에서 값만 빼와서 list화
user_list = column_user['userId'].values.tolist()
itemId_list = column_item['itemId'].values.tolist()

# rating db 생성 함수
def make_rating_data():
    with open('ratings_db_test.csv', 'w', encoding='UTF8', newline='') as f:
        rating_writer = csv.writer(f)
        rating_writer.writerow(rating_fieldnames)
        
        # 유저 별 아이템을 선택하는 개수가 전부 다름 이를 랜덤 함수를 통해서 구현
        # no_duplicate_list -> 유저가 선택한 아이템의 개수를 가리킴
        no_duplicate_list = []

        for k in range(50):
            d = random.randint(0, 50)
            while d in no_duplicate_list:
                d = random.randint(0, 50)
            no_duplicate_list.append(d)

        for i in range(1, user_records+1):
            rand_int = random.choice(no_duplicate_list)
            # itemId를 임시적으로 받을 변수 temp_itemId_list
            temp_itemId_list = []
            for a in range(len(itemId_list)):
                temp_itemId_list.append(itemId_list[a])
            for j in range(1, rand_int+1):
                temp_item_id = random.choice(temp_itemId_list)
                # Dataframe에서 해당 값에 접근하기 위해서는 index 값을 알아내는 것이 중요 해당 과정은 index 값 추출하는 과정 -> 반환 값이 index의 list 형태기 때문에 주의
                temp_item_index = column_item.index[(
                   column_item['itemId'] == temp_item_id)]
                # 앞서 추출한 index 값을 기반으로 아이템의 이름(title)을 가져오는 작업
                temp_item_title = column_item.at[temp_item_index[0], 'title']
                temp_user_id = random.choice(user_list)
                # index 추출 과정
                temp_index_list = column_user.index[(
                   column_user['userId'] == temp_user_id)]
                temp_index = temp_index_list[0]
                # index 값을 기반으로 major와 double major 값 추출
                temp_major = column_user.at[temp_index, 'major']
                temp_double_major = column_user.at[temp_index, 'double major']

                # 무분별한 아이템 평점 매기는 것을 방지하기 위해 임시적인 수단 도입
                # 해당 학과 주전공(또는 복수전공) 자료에만 평점을 매길 수 있는 장치를 만듬
                # 차후 수정 예정
                if temp_major == 'Computer_Science' or temp_double_major == "Computer_Science":
                   if temp_item_title in Computer_Science_list :
                       rating_writer.writerow(
                   [temp_user_id, temp_item_id, random.choice(rating_list)])
                       temp_itemId_list.remove(temp_item_id)                   
                
                elif temp_major == 'Mechanical_Engineering' or temp_double_major == 'Mechanical_Engineering':
                    if temp_item_title in Mechanical_Engineering_list :
                        rating_writer.writerow(
                   [temp_user_id, temp_item_id, random.choice(rating_list)])
                        temp_itemId_list.remove(temp_item_id) 

                elif temp_major == 'Electronic_Engineering' or temp_double_major == 'Electronic_Engineering' :
                    if temp_item_title in Electronic_Engineering_list :
                        rating_writer.writerow(
                   [temp_user_id, temp_item_id, random.choice(rating_list)])
                        temp_itemId_list.remove(temp_item_id) 

                elif temp_major == 'Electrical_engineering' or temp_double_major == 'Electrical_engineering':
                    if temp_item_title in Electrical_engineering_list :
                        rating_writer.writerow(
                   [temp_user_id, temp_item_id, random.choice(rating_list)])
                        temp_itemId_list.remove(temp_item_id) 

                elif temp_major == 'Business_Administration' or temp_double_major == 'Business_Administration' :
                    if temp_item_title in Business_Administration_list :
                        rating_writer.writerow(
                   [temp_user_id, temp_item_id, random.choice(rating_list)])
                        temp_itemId_list.remove(temp_item_id) 

                elif temp_major == 'Statistics' or temp_double_major == 'Statistics' :
                    if temp_item_title in Statistics_list :
                        rating_writer.writerow(
                   [temp_user_id, temp_item_id, random.choice(rating_list)])
                        temp_itemId_list.remove(temp_item_id) 
                
                # 남은 아이템들(외국어 등)은 전공이 상관없으므로 그냥 대입하는 과정을 거침
                else :
                    rating_writer.writerow(
                   [temp_user_id, temp_item_id, random.choice(rating_list)])
                    temp_itemId_list.remove(temp_item_id) 

    f.close()


make_rating_data()
