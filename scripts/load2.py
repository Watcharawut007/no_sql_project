import hashlib
import random
import os
import csv

from django.contrib.auth.models import User
from review_production.models import *

from password_generator import PasswordGenerator

file2 = open("C:/Users/peeza/PycharmProjects/djangoProject2/sql_project/scripts/archive/GrammarandProductReviews.csv",encoding="utf8")

csv2 = csv.reader(file2)
def run():
    view_file2()
def create_product_object_file2():
    for test in csv2:
        if not(product.objects.filter(product_name=test[9]).exists()):
            product.objects.create(product_name=test[9],catagories=test[2])
def view_file2():
    count = 0
    for test in csv2:
        for i in test:
            print(count,i)
            count = count + 1
        break
def create_user_object_file2():
    password = PasswordGenerator()
    password.excludeschars = "!$%^{}[]()=/"
    count = 0
    dup = []
    for test in csv2:
        user = User.objects.filter(username=test[23])
        if count == 0:
            pass
            count = count + 1
        elif count == 1000:
            break
        elif len(user) >= 1:
            pass
        else :
            passw = password.generate()
            print(test[23],passw+'\n')
            User.objects.create(username=test[23])
            user = User.objects.get(username=test[23])
            user.set_password(passw)
            user.save()
            dup.append(test[23])
            count = count + 1

def create_random_review_object():
    all_review = review.objects.all()
    all_user = User.objects.all()
    all_product = product.objects.all()
    dup1 = []
    dup2  = []
    dup3  = []
    for i in range(200000):
        number_random1 = random.randrange(1,80000)
        number_random2 = random.randrange(1,80000)
        number_random3 = random.randrange(1,80000)
        if number_random1 in dup1 or number_random2 in dup2 or number_random3 in dup3:
            number_random1 = random.randrange(number_random1, 80000)
            number_random2 = random.randrange(number_random2, 80000)
            number_random3 = random.randrange(number_random3, 80000)
        dup1.append(number_random1)
        dup2.append(number_random2)
        dup3.append(number_random3)
        number_user = random.randrange(1, len(all_user))
        number_product = random.randrange(1, len(all_product))
        review.objects.create(title=all_review[number_random1].title,
                              comment_text=all_review[number_random2].comment_text,
                              rating=all_review[number_random3].rating,
                              product=all_product[number_product],
                              user=all_user[number_user])
        print('title:',all_review[number_random1].title+"\n"+
              'comment_text:',all_review[number_random2].comment_text+"\n"+
              'rating : ',str(all_review[number_random1].rating)+'\n'+
              'product :' ,str(all_product[number_product])+"\n"+
              'user :' ,str(all_user[number_user])
              )
    for i in range(100000):
        number_random1 = random.randrange(1,len(all_review))
        number_random2 = random.randrange(1, len(all_review))
        number_random3 = random.randrange(1, len(all_review))
        if number_random1 in dup1 or number_random2 in dup2 or number_random3 in dup3:
            number_random1 = random.randrange(number_random1, 80000)
            number_random2 = random.randrange(number_random2, 80000)
            number_random3 = random.randrange(number_random3, 80000)
        dup1.append(number_random1)
        dup2.append(number_random2)
        dup3.append(number_random3)
        number_user = random.randrange(1, len(all_user))
        number_product = random.randrange(1, len(all_product))
        review.objects.create(title=all_review[number_random3].title,
                              comment_text=all_review[number_random2].comment_text,
                              rating=all_review[number_random1].rating,
                              product=all_product[number_product],
                              user=all_user[number_user])
        print('title:', all_review[number_random1].title + "\n" +
              'comment_text:', all_review[number_random2].comment_text + "\n" +
              'rating : ', str(all_review[number_random1].rating) + '\n' +
              'product :', str(all_product[number_product])+"\n"+
              'user :' ,str(all_user[number_user])
              )
def create_review_object():
    count = 0
    review_count = 0
    for test in csv2:
        if count == 0:
           pass
        elif (review.objects.filter(comment_text=test[19]).exists()):
            count = count + 1
            print('case1')
            pass
        elif len(User.objects.filter(username=test[23])) == 0:
            product_select = product.objects.filter(product_name=test[9]).first()
            print('case3')
            User_all = User.objects.all()
            user_select = random.choice(User_all)
            print(user_select)
            review.objects.create(title=test[20], comment_text=test[19], rating=int(test[17]),
                                  product=product_select, user=user_select)
            print(count, test[1])
        else:
            product_select = product.objects.filter(product_name=test[9]).first()
            print('case4')
            user_select = User.objects.get(username=test[23])
            review.objects.create(title=test[20], comment_text=test[19], rating=int(test[17]),
                                          product=product_select, user=user_select)
            review_count = review_count + 1
            print(count, test[1])
        count = count + 1

