import csv
import random
import numpy as np
from faker import Faker

# 아이템 개수
item_records = 10000
# 아이템 Attribute
item_fieldnames = ['itemId', 'title', 'category']
# 아이템 형태
category_list = ['Document', 'Test Material', 'Video Lecture',
                 'Abridgment', 'Lecture Note', 'Book', 'Private lessons', 'Mentoring']
# 아이템 이름 list
title_list = ['Java',
              'Spring Framework', 'Internet Programming', 'Operating System',
              'Calculus', 'Mathematical Statistics', 'Python', 'Data Analysis', 'Data Engineering',
              'React.js', 'JavaScript', 'HTML/CSS', 'Android', 'Kotlin', 'Swift', 'C#', 'C', 'Linear Algebra'
              'C++', 'Data Structure', 'Algorithm', 'Computer network', 'Statics', 'Thermodynamics', 'Energy power engineering',
              'Self-driving', 'Machine system control', 'fluid mechanics', 'Dynamics', 'Computer Structure', 'Logic Circuit', 'Basic Physics', 'industrial mathematics',
              'Regression Analysis', 'Computational Statistics', 'Elementary Statistics', 'Statistical Software and Lab', 'Probability', 'Statistical Mathematics', 'Big Data Fundamentals', 'Time Series Analysis and Lab', 'Sampling Theory and Lab', 'Experimental Design Lab', 'Categorical Data Analysis', 'Multivariate Statistics and Lab', 'Insurance Statistics', 'Financial Statistics', 'Bayesian Statistics', 'Data Mining',
              'Business English', 'Advertising', 'Business Data Analysis', 'Principles of Business Administration', 'Creative Business Plan Development', 'Corporate Bigdata Analysis', 'Digital Marketing', 'Consumer Behavior', 'Investments', 'Management Information System', 'Principles of Marketing', 'Operations Management', 'Organizational Behaviour', 'Economics', 'Principle of Accounting', 'Financial Management', 'Database',
              'Electronic Basic Digital Logic Design', 'Properties of Electrical & Electronic Materials', 'circuit theory', 'Computational Electromagnetics', 'Physical Electronics', 'Electronic Circuits', 'Numerical Analysis', 'Communication System', 'Automatic Control', 'Signal and System', 'Semiconductor Devices', 'Analog Circuit Capstone Design', 'Control System Capstone Design', 'Mobile Communications', 'Introductory Digital Signal Processing',
              'Electromagnetics', 'Digital Logic Circuits', 'Electrical Circuit Experiments', 'Electrical & Electronic measurements', 'Probability and Random Variables', 'Autonomous Vehicle Engineering', 'Control System Capstone Design', 'Electrical & Electronic measurements', 'Sensor Engineering', 'Embedded System Capstone Design', 'Robotics', 'Motor Control', 'Automatic Control', 'Electronic Display', 'The Physics of Power Semiconductor Devices', 'Power System Engineering', 'Motor Application', 'Smart Grid', 'High Voltage Engineering', 'Energy Conversion', 'Electric Vehicle Engineering',
              'TOEIC', 'TOEFL', 'TOEIC Speaking', 'OPIC', 'HSK', 'DELF'
              ]


# 아이템 DB 생성 과정
def make_item_data():

    # random.sample() -> no duplicate
    with open('item_db_test.csv', 'w', encoding='UTF8', newline='') as f:
        item_writer = csv.writer(f)
        item_writer.writerow(item_fieldnames)

        for i in range(1, item_records+1):
            item_writer.writerow(
                [str(i), random.choice(title_list), random.choice(category_list)])

    f.close()


make_item_data()
