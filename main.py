from flask import Flask
from flask import Flask, render_template, Response, redirect, request, session, abort, url_for
import os
import base64
from PIL import Image
from datetime import datetime
from datetime import date
import datetime
import random
from random import seed
from random import randint
from werkzeug.utils import secure_filename
from flask import send_file
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import threading
import time
import shutil
import hashlib
import urllib.request
import urllib.parse
from urllib.request import urlopen
import webbrowser

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  charset="utf8",
  database="interview_app"
)


app = Flask(__name__)
##session key
app.secret_key = 'abcdef'
UPLOAD_FOLDER = 'static/upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#####

@app.route('/',methods=['POST','GET'])
def index():
    cnt=0
    act=""
    msg=""

    
    if request.method == 'POST':
        username1 = request.form['uname']
        password1 = request.form['pass']
        mycursor = mydb.cursor()
        mycursor.execute("SELECT count(*) FROM ap_user where uname=%s && pass=%s",(username1,password1))
        myresult = mycursor.fetchone()[0]
        print(myresult)
        if myresult>0:
            session['username'] = username1
            
            result=" Your Logged in sucessfully**"
            return redirect(url_for('userhome')) 
        else:
            msg="Invalid Username or Password!"
            result="Your logged in fail!!!"
        

    return render_template('index.html',msg=msg,act=act)

@app.route('/login',methods=['POST','GET'])
def login():
    cnt=0
    act=""
    msg=""
    if request.method == 'POST':
        
        username1 = request.form['uname']
        password1 = request.form['pass']
        mycursor = mydb.cursor()
        mycursor.execute("SELECT count(*) FROM ap_login where username=%s && password=%s",(username1,password1))
        myresult = mycursor.fetchone()[0]
        if myresult>0:
            session['username'] = username1
            #result=" Your Logged in sucessfully**"
            return redirect(url_for('admin')) 
        else:
            msg="Your logged in fail!!!"
        

    return render_template('login.html',msg=msg,act=act)

@app.route('/login_hr',methods=['POST','GET'])
def login_hr():
    cnt=0
    act=""
    msg=""

    
    
    if request.method == 'POST':
        username1 = request.form['uname']
        password1 = request.form['pass']
        mycursor = mydb.cursor()
        mycursor.execute("SELECT count(*) FROM ap_hr where uname=%s && pass=%s",(username1,password1))
        myresult = mycursor.fetchone()[0]
        if myresult>0:
            session['username'] = username1
            result=" Your Logged in sucessfully**"
            return redirect(url_for('hr_home')) 
        else:
            msg="Invalid Username or Password!"
            result="Your logged in fail!!!"
        

    return render_template('login_hr.html',msg=msg,act=act)

@app.route('/register', methods=['GET', 'POST'])
def register():
    msg=""
    act=request.args.get("act")
    mycursor = mydb.cursor()
    

    if request.method=='POST':
        name=request.form['name']
        gender=request.form['gender']
        dob=request.form['dob']
        address=request.form['address']
        city=request.form['city']
        mobile=request.form['mobile']
        email=request.form['email']
        uname=request.form['uname']
        pass1=request.form['pass']

        

        mycursor.execute("SELECT count(*) FROM ap_user where uname=%s",(uname,))
        myresult = mycursor.fetchone()[0]

        if myresult==0:
        
            mycursor.execute("SELECT max(id)+1 FROM ap_user")
            maxid = mycursor.fetchone()[0]
            if maxid is None:
                maxid=1
            
            now = date.today() #datetime.datetime.now()
            rdate=now.strftime("%d-%m-%Y")
            
            sql = "INSERT INTO ap_user(id,name,gender,dob,address,city,mobile,email,uname,pass,create_date) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (maxid,name,gender,dob,address,city,mobile,email,uname,pass1,rdate)
            mycursor.execute(sql, val)
            mydb.commit()

            
            print(mycursor.rowcount, "Registered Success")
            msg="success"
            
            #if cursor.rowcount==1:
            #    return redirect(url_for('index',act='1'))
        else:
            
            msg='Already Exist'
            
    
    return render_template('register.html', msg=msg)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    msg=""
    act=request.args.get("act")
    mycursor = mydb.cursor()
    
    if request.method=='POST':
        category=request.form['category']
        
        mycursor.execute("SELECT max(id)+1 FROM ap_category")
        maxid = mycursor.fetchone()[0]
        if maxid is None:
            maxid=1
        
        sql = "INSERT INTO ap_category(id,category) VALUES (%s,%s)"
        val = (maxid,category)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect(url_for('admin')) 
        

    mycursor.execute("SELECT * FROM ap_category")
    data = mycursor.fetchall()

    if act=="del":
        did=request.args.get("did")
        mycursor.execute("delete from ap_category where id=%s",(did,))
        mydb.commit()
        return redirect(url_for('admin')) 
    
    return render_template('admin.html', msg=msg,data=data)

@app.route('/view_hr', methods=['GET', 'POST'])
def view_hr():
    msg=""
    email=""
    mess=""
    act=request.args.get("act")
    mycursor = mydb.cursor()
    
    if request.method=='POST':
        name=request.form['name']
        company=request.form['company']
        address=request.form['address']
        mobile=request.form['mobile']
        email=request.form['email']
        uname=request.form['uname']
        pass1=request.form['pass']
        
        mycursor.execute("SELECT max(id)+1 FROM ap_hr")
        maxid = mycursor.fetchone()[0]
        if maxid is None:
            maxid=1
        
        sql = "INSERT INTO ap_hr(id,name,company,address,mobile,email,uname,pass) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (maxid,name,company,address,mobile,email,uname,pass1)
        mycursor.execute(sql, val)
        mydb.commit()
        mess="Dear "+name+", HR Login - Username:"+uname+", Password:"+pass1
        msg="success"
        

    mycursor.execute("SELECT * FROM ap_hr")
    data = mycursor.fetchall()

    if act=="del":
        did=request.args.get("did")
        mycursor.execute("delete from ap_hr where id=%s",(did,))
        mydb.commit()
        return redirect(url_for('view_hr')) 
    
    return render_template('view_hr.html', msg=msg,data=data,email=email,mess=mess)

@app.route('/view_user', methods=['GET', 'POST'])
def view_user():
    msg=""
    email=""
    mess=""
    act=request.args.get("act")
    mycursor = mydb.cursor()
    
    
        

    mycursor.execute("SELECT * FROM ap_user")
    data = mycursor.fetchall()

    if act=="del":
        did=request.args.get("did")
        mycursor.execute("delete from ap_user where id=%s",(did,))
        mydb.commit()
        return redirect(url_for('view_user')) 
    
    return render_template('view_user.html', msg=msg,data=data,email=email,mess=mess)

@app.route('/add_cat', methods=['GET', 'POST'])
def add_cat():
    msg=""
    act=request.args.get("act")
    mycursor = mydb.cursor()
    
    if request.method=='POST':
        category=request.form['category']
        
        mycursor.execute("SELECT max(id)+1 FROM ap_category")
        maxid = mycursor.fetchone()[0]
        if maxid is None:
            maxid=1
        
        sql = "INSERT INTO ap_category(id,category) VALUES (%s,%s)"
        val = (maxid,category)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect(url_for('add_cat')) 
        

    mycursor.execute("SELECT * FROM ap_category")
    data = mycursor.fetchall()

    if act=="del":
        did=request.args.get("did")
        mycursor.execute("delete from ap_category where id=%s",(did,))
        mydb.commit()
        return redirect(url_for('add_cat')) 
    
    return render_template('add_cat.html', msg=msg,data=data)

@app.route('/add_subcat', methods=['GET', 'POST'])
def add_subcat():
    msg=""
    act=request.args.get("act")
    cid=request.args.get("cid")
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM ap_category where id=%s",(cid,))
    data1 = mycursor.fetchone()
    category=data1[1]
    
    if request.method=='POST':
        subcat=request.form['category']
        
        mycursor.execute("SELECT max(id)+1 FROM ap_subcat")
        maxid = mycursor.fetchone()[0]
        if maxid is None:
            maxid=1
        
        sql = "INSERT INTO ap_subcat(id,cat_id,subcat) VALUES (%s,%s,%s)"
        val = (maxid,cid,subcat)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect(url_for('add_subcat',cid=cid)) 
        

    mycursor.execute("SELECT * FROM ap_subcat where cat_id=%s",(cid,))
    data = mycursor.fetchall()

    if act=="del":
        did=request.args.get("did")
        mycursor.execute("delete from ap_subcat where id=%s",(did,))
        mydb.commit()
        return redirect(url_for('add_subcat')) 
    
    return render_template('add_subcat.html', msg=msg,data=data,category=category)

@app.route('/hr_home', methods=['GET', 'POST'])
def hr_home():
    msg=""
    act=request.args.get("act")

    uname=""
    if 'username' in session:
        uname = session['username']

    print(uname)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ap_hr where uname=%s",(uname, ))
    data = mycursor.fetchone()

 
    return render_template('hr_home.html',data=data)


@app.route('/add_meet', methods=['GET', 'POST'])
def add_meet():
    msg=""
    mess=""
    email=""
    act=request.args.get("act")

    uname=""
    if 'username' in session:
        uname = session['username']

    print(uname)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ap_hr where uname=%s",(uname, ))
    data = mycursor.fetchone()

    if request.method=='POST':
        
        user=request.form['user']
        t1=request.form['t1']
        t2=request.form['t2']
        t3=request.form['t3']
        t4=request.form['t4']
        td1=request.form['tdate']
        tt=td1.split("-")
        tdate=tt[2]+"-"+tt[1]+"-"+tt[0]

        mycursor.execute("SELECT * FROM ap_user where uname=%s",(user, ))
        udata = mycursor.fetchone()
        email=udata[7]

        mess="Dear "+user+", Zoom Meet on "+tdate+", "+t1+":"+t2+" to "+t3+":"+t4
        
        mycursor.execute("SELECT max(id)+1 FROM ap_time")
        maxid = mycursor.fetchone()[0]
        if maxid is None:
            maxid=1
        
        now = date.today() #datetime.datetime.now()
        rdate=now.strftime("%d-%m-%Y")
        
        sql = "INSERT INTO ap_time(id,user,t1,t2,t3,t4,tdate,rdate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (maxid,user,t1,t2,t3,t4,tdate,rdate)
        mycursor.execute(sql, val)
        mydb.commit()

        
        print(mycursor.rowcount, "Registered Success")
        msg="success"
        
        #if cursor.rowcount==1:
        #    return redirect(url_for('index',act='1'))

    mycursor.execute("SELECT * FROM ap_time order by id desc")
    data = mycursor.fetchall()

    if act=="del":
        did=request.args.get("did")
        mycursor.execute("delete from ap_time where id=%s",(did,))
        mydb.commit()
        return redirect(url_for('add_meet')) 

 
    return render_template('add_meet.html',msg=msg,data=data,mess=mess,email=email)

@app.route('/meetapi',methods=['POST','GET'])
def meetapi():
    msg=""

    return render_template('meetapi.html',msg=msg)

@app.route('/userhome', methods=['GET', 'POST'])
def userhome():
    msg=""
    st=""
    act=request.args.get("act")
    cid=request.args.get("cid")
    category=""
    data1=[]
    data2=[]
    data3=[]
    uname=""
    if 'username' in session:
        uname = session['username']

    print(uname)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ap_user where uname=%s",(uname, ))
    data = mycursor.fetchone()

    mycursor.execute("SELECT * FROM ap_category")
    data1 = mycursor.fetchall()

    if act=="ok":
        mycursor.execute("SELECT * FROM ap_category where id=%s",(cid,))
        dd1 = mycursor.fetchone()
        category=dd1[1]
        mycursor.execute("SELECT * FROM ap_subcat where cat_id=%s",(cid,))
        data2 = mycursor.fetchall()

    t = time.localtime()
    rtime = time.strftime("%H", t)
    rmin = time.strftime("%M", t)
    rm=int(rmin)    
    rh=int(rtime)

    mycursor.execute("SELECT count(*) FROM ap_time where user=%s",(uname,))
    cnt = mycursor.fetchone()[0]
    if cnt>0:
        st="1"
        mycursor.execute("SELECT * FROM ap_time where user=%s",(uname,))
        dd2 = mycursor.fetchall()
        for ds in dd2:
            dt=[]
            dt.append(ds[0])
            dt.append(ds[1])
            dt.append(ds[2])
            dt.append(ds[3])
            dt.append(ds[4])
            dt.append(ds[5])
            dt.append(ds[6])
            dt.append(ds[7])

            
            x=0
            sh1=int(ds[2])
            sh2=int(ds[4])
            sm1=int(ds[3])
            sm2=int(ds[5])
            if sh1<=rh and rh<=sh2:
                if sm1<=rm or rm<=sm2:
                    x+=1
            if x>0:
                dt.append("1")
            else:
                dt.append("2")
            
            data3.append(dt)

        
    return render_template('userhome.html',data=data,data1=data1,data2=data2,act=act,cid=cid,category=category,data3=data3,st=st)


@app.route('/user_file', methods=['GET', 'POST'])
def user_file():
    msg=""
    act=request.args.get("act")
    cid=request.args.get("cid")
    sid=request.args.get("sid")
    category=""
    data1=[]
    data2=[]
    uname=""
    if 'username' in session:
        uname = session['username']

    print(uname)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ap_user where uname=%s",(uname, ))
    data = mycursor.fetchone()

    mycursor.execute("SELECT * FROM ap_category")
    data1 = mycursor.fetchall()

    
    mycursor.execute("SELECT * FROM ap_category where id=%s",(cid,))
    dd1 = mycursor.fetchone()
    category=dd1[1]
    mycursor.execute("SELECT * FROM ap_subcat where cat_id=%s",(cid,))
    data2 = mycursor.fetchall()
    mycursor.execute("SELECT * FROM ap_files where sid=%s",(sid,))
    data3 = mycursor.fetchall()
        
    return render_template('user_file.html',data=data,data1=data1,data2=data2,act=act,cid=cid,category=category,data3=data3)



@app.route('/user_meet', methods=['GET', 'POST'])
def user_meet():
    msg=""
    act=request.args.get("act")

    uname=""
    if 'username' in session:
        uname = session['username']

    print(uname)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ap_user where uname=%s",(uname, ))
    data = mycursor.fetchone()

 
    return render_template('user_meet.html',data=data)

@app.route('/user_train', methods=['GET', 'POST'])
def user_train():
    msg=""
    act=request.args.get("act")
    cid=request.args.get("cid")
    sid=request.args.get("sid")
    category=""
    data1=[]
    data2=[]
    uname=""
    if 'username' in session:
        uname = session['username']

    print(uname)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ap_user where uname=%s",(uname, ))
    data = mycursor.fetchone()

    mycursor.execute("SELECT * FROM ap_category")
    data1 = mycursor.fetchall()

    
    mycursor.execute("SELECT * FROM ap_category where id=%s",(cid,))
    dd1 = mycursor.fetchone()
    category=dd1[1]
    mycursor.execute("SELECT * FROM ap_subcat where cat_id=%s",(cid,))
    data2 = mycursor.fetchall()

    mycursor.execute("SELECT * FROM ap_train_question where sid=%s",(sid,))
    data3 = mycursor.fetchall()
        
    return render_template('user_train.html',data=data,data1=data1,data2=data2,data3=data3,act=act,cid=cid,category=category)


@app.route('/add_train', methods=['GET', 'POST'])
def add_train():
    msg=""
    act=request.args.get("act")
    cid=request.args.get("cid")
    sid=request.args.get("sid")
    mycursor = mydb.cursor()
    

    if request.method=='POST':
        
        question=request.form['question']
        option1=request.form['option1']
        option2=request.form['option2']
        option3=request.form['option3']
        option4=request.form['option4']
        answer=request.form['answer']
        details=request.form['details']
        
        mycursor.execute("SELECT max(id)+1 FROM ap_train_question")
        maxid = mycursor.fetchone()[0]
        if maxid is None:
            maxid=1
        
        now = date.today() #datetime.datetime.now()
        rdate=now.strftime("%d-%m-%Y")
        
        sql = "INSERT INTO ap_train_question(id,cid,sid,question,option1,option2,option3,option4,answer,details,filename) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (maxid,cid,sid,question,option1,option2,option3,option4,answer,details,'')
        mycursor.execute(sql, val)
        mydb.commit()

        
        print(mycursor.rowcount, "Registered Success")
        msg="success"
        
        #if cursor.rowcount==1:
        #    return redirect(url_for('index',act='1'))

    mycursor.execute("SELECT * FROM ap_train_question where sid=%s",(sid,))
    data = mycursor.fetchall()

    if act=="del":
        did=request.args.get("did")
        mycursor.execute("delete from ap_train_question where id=%s",(did,))
        mydb.commit()
        return redirect(url_for('add_train',cid=cid,sid=sid)) 
    
    return render_template('add_train.html', msg=msg,sid=sid,cid=cid,data=data)

@app.route('/addfile', methods=['GET', 'POST'])
def addfile():
    msg=""
    act=request.args.get("act")
    cid=request.args.get("cid")
    sid=request.args.get("sid")
    
    mycursor = mydb.cursor()
    

    if request.method=='POST':
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            mycursor.execute("SELECT max(id)+1 FROM ap_files")
            maxid = mycursor.fetchone()[0]
            if maxid is None:
                maxid=1
            
            fname = file.filename
            filename = secure_filename(fname)
            fname="F"+str(maxid)+filename
            file.save(os.path.join("static/upload/", fname))
            
            sql = "INSERT INTO ap_files(id,cid,sid,filename) VALUES (%s,%s,%s,%s)"
            val = (maxid,cid,sid,fname)
            mycursor.execute(sql, val)
            mydb.commit()
            msg="success"

    mycursor.execute("SELECT * FROM ap_files where sid=%s",(sid,))
    data = mycursor.fetchall()
    
    return render_template('addfile.html', msg=msg,sid=sid,cid=cid,data=data) 


@app.route('/add_test', methods=['GET', 'POST'])
def add_test():
    msg=""
    act=request.args.get("act")
    cid=request.args.get("cid")
    sid=request.args.get("sid")
    mycursor = mydb.cursor()
    
    mycursor.execute("SELECT * FROM ap_subcat where id=%s",(sid,))
    dd1 = mycursor.fetchone()
    category=dd1[2]
    if request.method=='POST':
        
        question=request.form['question']
        option1=request.form['option1']
        option2=request.form['option2']
        option3=request.form['option3']
        option4=request.form['option4']
        answer=request.form['answer']
        
        
        mycursor.execute("SELECT max(id)+1 FROM ap_test_question")
        maxid = mycursor.fetchone()[0]
        if maxid is None:
            maxid=1
        
        now = date.today() #datetime.datetime.now()
        rdate=now.strftime("%d-%m-%Y")
        
        sql = "INSERT INTO ap_test_question(id,cid,sid,question,option1,option2,option3,option4,answer) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (maxid,cid,sid,question,option1,option2,option3,option4,answer)
        mycursor.execute(sql, val)
        mydb.commit()

        
        print(mycursor.rowcount, "Registered Success")
        msg="success"
        
        #if cursor.rowcount==1:
        #    return redirect(url_for('index',act='1'))

    mycursor.execute("SELECT * FROM ap_test_question where sid=%s",(sid,))
    data = mycursor.fetchall()

    if act=="del":
        did=request.args.get("did")
        mycursor.execute("delete from ap_test_question where id=%s",(did,))
        mydb.commit()
        return redirect(url_for('add_test',cid=cid,sid=sid)) 
    
    return render_template('add_test.html', msg=msg,sid=sid,cid=cid,data=data,category=category)

@app.route('/add_exam', methods=['GET', 'POST'])
def add_exam():
    msg=""
    act=request.args.get("act")
    sid=request.args.get("sid")
    mycursor = mydb.cursor()
    

    if request.method=='POST':
        
        num_question=request.form['num_question']
        mark=request.form['mark']
        
        
        
        mycursor.execute("SELECT max(id)+1 FROM ap_exam")
        maxid = mycursor.fetchone()[0]
        if maxid is None:
            maxid=1
        
        now = date.today() #datetime.datetime.now()
        rdate=now.strftime("%d-%m-%Y")
        
        sql = "INSERT INTO ap_exam(id,sid,num_question,mark) VALUES (%s,%s,%s,%s)"
        val = (maxid,sid,num_question,mark)
        mycursor.execute(sql, val)
        mydb.commit()

        
        print(mycursor.rowcount, "Registered Success")
        msg="success"
        
        #if cursor.rowcount==1:
        #    return redirect(url_for('index',act='1'))

    mycursor.execute("SELECT * FROM ap_exam where sid=%s",(sid,))
    data = mycursor.fetchall()


    if act=="del":
        did=request.args.get("did")
        mycursor.execute("delete from ap_exam where id=%s",(did,))
        mydb.commit()
        return redirect(url_for('add_exam')) 
    
    return render_template('add_exam.html', msg=msg,data=data,sid=sid)


@app.route('/user_test', methods=['GET', 'POST'])
def user_test():
    msg=""
    act=request.args.get("act")
    eid=request.args.get("eid")
    sid=request.args.get("sid")
    category=""
    data1=[]
    data2=[]
    uname=""
    if 'username' in session:
        uname = session['username']

    print(uname)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ap_user where uname=%s",(uname, ))
    data = mycursor.fetchone()

    
    mycursor.execute("SELECT * FROM ap_subcat where id=%s",(sid,))
    dd2 = mycursor.fetchone()
    category=dd2[2]

    if act=="test":
        mycursor.execute("SELECT * FROM ap_exam where id=%s",(eid,))
        dd3 = mycursor.fetchone()
        numq=dd3[2]
        
        mycursor.execute("SELECT * FROM ap_train_question where sid=%s order by rand() limit 0,%s",(sid,numq))
        e2 = mycursor.fetchall()
        e4=[]
        for e3 in e2:
            e4.append(str(e3[0]))

        vv=','.join(e4)
        mycursor.execute("update ap_user set questions=%s,eid=%s where uname=%s",(vv,eid,uname))
        mydb.commit()

        mycursor.execute("delete from ap_exam_attend where eid=%s && uname=%s",(eid,uname))
        mydb.commit()    
        return redirect(url_for('exam',sid=sid,eid=eid)) 
    

    mycursor.execute("SELECT * FROM ap_exam where sid=%s",(sid,))
    data3 = mycursor.fetchall()
        
    return render_template('user_test.html',data=data,data3=data3,act=act,sid=sid,category=category)


@app.route('/exam',methods=['POST','GET'])
def exam():
    msg=""

    mycursor = mydb.cursor()
    data1=[]
    qid=0
    sts=0
    uname=""
    if 'username' in session:
        uname = session['username']
    sid=request.args.get("sid")
    eid=request.args.get("eid")
 


    mycursor.execute("SELECT * FROM ap_user where uname=%s",(uname,))
    e1 = mycursor.fetchone()
    ques=e1[11]
    eid=e1[12]
    

    mycursor.execute("SELECT * FROM ap_exam where id=%s",(eid,))
    e11 = mycursor.fetchone()
    total=e11[2]
    tmark=e11[3]
    fullmark=total*tmark
    tot=total-1

    qq=ques.split(',')
    tq=len(qq)

    mycursor.execute("SELECT count(*) FROM ap_exam_attend where eid=%s && uname=%s",(eid,uname))
    e1 = mycursor.fetchone()[0]

    q1=0
   
    attend=0
    if e1>0:
        mycursor.execute("SELECT * FROM ap_exam_attend where eid=%s && uname=%s",(eid,uname))
        e2 = mycursor.fetchone()
        sts=e2[8]
        attend=e2[4]
        
        q1=attend
    else:
        q1=0

    if attend<=tot and sts==0:
        qid=qq[q1]
        mycursor.execute("SELECT * FROM ap_train_question where id=%s",(qid,))
        data1 = mycursor.fetchone()
        print("ans="+str(data1[8]))
        
    else:
        #mycursor.execute("update ap_exam_attend set attend=0,correct=0,mark=0,percent=0,status=0 where eid=%s && uname=%s",(eid,uname))
        #mydb.commit()
        msg="complete"

    if request.method=='POST':
        
        ans1=request.form['ans1']
        print("myans=="+ans1)
        qidd=request.form['qidd']
        correct=0
        mark=0
        percent=0

        if attend<=tot:
            
                
            if q1==0:
                mycursor.execute("SELECT max(id)+1 FROM ap_exam_attend")
                maxid = mycursor.fetchone()[0]
                if maxid is None:
                    maxid=1
                
                now = date.today() #datetime.datetime.now()
                rdate=now.strftime("%d-%m-%Y")

                mycursor.execute("SELECT * FROM ap_train_question where id=%s",(qidd,))
                dd2 = mycursor.fetchone()
                c=str(dd2[8])
                if ans1==c:
                    correct=1
                else:
                    correct=0

                print("myans="+ans1+", c="+c+", corr1="+str(correct))
                
                mark=tmark*correct
                if mark>0:
                    p=(mark/fullmark)*100
                    percent=round(p,2)
                
                sql = "INSERT INTO ap_exam_attend(id,uname,eid,total,attend,correct,mark,percent,qid,sid) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = (maxid,uname,eid,total,'1',correct,mark,percent,qid,sid)
                mycursor.execute(sql, val)
                mydb.commit()
                msg="ok"
            else:
                mycursor.execute("SELECT * FROM ap_exam_attend where eid=%s && uname=%s",(eid,uname))
                dd3 = mycursor.fetchone()
                totq=dd3[3]
                corr=dd3[5]
                
                mycursor.execute("SELECT * FROM ap_train_question where id=%s",(qidd,))
                dd2 = mycursor.fetchone()
                c=str(dd2[8])
                if ans1==c:
                    correct=corr+1
                else:
                    correct=corr

                print("myans="+ans1+", c="+c+", corr2="+str(correct))
                mark=tmark*correct
                if mark>0:
                    p=(mark/fullmark)*100
                    percent=round(p,2)
                    
                mycursor.execute("update ap_exam_attend set attend=attend+1,correct=%s,mark=%s,percent=%s where eid=%s && uname=%s",(correct,mark,percent,eid,uname))
                mydb.commit()
                
                mycursor.execute("SELECT * FROM ap_exam_attend where eid=%s && uname=%s",(eid,uname))
                dd4 = mycursor.fetchone()
                if dd4[4]==total:
                    mycursor.execute("update ap_exam_attend set status=1 where eid=%s && uname=%s",(eid,uname))
                    mydb.commit()
                    
                msg="ok"
        else:
            
            msg="complete"

    return render_template('exam.html',msg=msg,eid=eid,data1=data1,qid=qid)

@app.route('/user_status', methods=['GET', 'POST'])
def user_status():
    msg=""
    act=request.args.get("act")
    uname=""
    if 'username' in session:
        uname = session['username']

    if uname=="":
        name=request.args.get("name")
        session['username'] = name
        
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM ap_user where uname=%s",(uname,))
    data = mycursor.fetchone()


    mycursor.execute("SELECT * FROM ap_exam c,ap_exam_attend e where c.id=e.eid && e.uname=%s",(uname,))
    data1 = mycursor.fetchall()

    return render_template('user_status.html', msg=msg,data=data,uname=uname,data1=data1)

@app.route('/view_exam', methods=['GET', 'POST'])
def view_exam():
    msg=""
    act=request.args.get("act")
    eid=request.args.get("eid")
    rid=request.args.get("rid")
    uname=""
    
    mycursor = mydb.cursor()

    
    mycursor.execute("SELECT * FROM cam_exam c,cam_exam_attend e where c.id=e.eid")
    data1 = mycursor.fetchall()

    if act=="del":
        mycursor.execute("delete from cam_exam_attend where id=%s",(rid,))
        mydb.commit()
        return redirect(url_for('view_exam',eid=eid))
        
    return render_template('view_exam.html', act=act,msg=msg,data1=data1,eid=eid)




@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=5000)
