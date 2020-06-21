from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect
from django.conf import settings as s
from django.http import HttpResponse
from . import models


curl=s.CURRENT_URL


def base(req):
	return render(req,'Base.html')

@csrf_exempt
def login(req):
	if req.method=="GET":
		return render(req,'Login.html',{'c':curl})

	else:
		EnRoll=req.POST.get('user')
		Pwd=req.POST.get('pwd')

		query="select * from Info where EnRoll='%s' and Pwd='%s'" %(EnRoll,Pwd)
		models.cursor.execute(query)
		a=models.cursor.fetchall()

		if len(a)>0:
			if a[0][6]=="S":
				response = redirect(curl+'S/home')

			else:
				response = redirect(curl+'T/home')

			response.set_cookie('enr',a[0][0],3600*24)
			return response

		else:
			return render(req,'login.html',{'c':curl,'out':'Invalid Login details'})



def signup(req):
	if req.method=="GET":
		return render(req,'Register.html',{'c':curl})

	if req.method=="POST":

		Name=req.POST.get('name')
		Gender=req.POST.get('gender')
		DOB=req.POST.get('dob')
		Email=req.POST.get('email')
		Pwd=req.POST.get('pwd')
		User=req.POST.get('a')
		Mobile=req.POST.get('mobile')
		Address=req.POST.get('add')

		query="insert into Info values(NULL,'%s','%s','%s','%s','%s','%s','%s','%s')" %(Name,Gender,DOB,Email,Pwd,User,Mobile,Address)

		try:
			models.cursor.execute(query)

		except:
			return render(req,'Register.html',{'c':curl,'out':'This email address is already in use.'})

		else:
			models.db.commit()

			query="select EnRoll from Info where Email='%s'" %(Email)
			models.cursor.execute(query)
			a=models.cursor.fetchall()
			EnRoll = a[0][0]

			if User == 'S':
				query="insert into student values('%s',NULL)" %(EnRoll)
				models.cursor.execute(query)
				models.db.commit()

				query="insert into marks values('%s',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL)" %(EnRoll)
				models.cursor.execute(query)
				models.db.commit()

			if User == 'T':
				query="insert into teacher values('%s',0,NULL)" %(EnRoll)
				models.cursor.execute(query)
				models.db.commit()

			return render(req,'Successful.html',{'c':curl,'out':"Registration Successful",'eno':EnRoll})



def shome(req):
	EnRoll = req.COOKIES.get('enr')

	query = "select * from Info where EnRoll=%s" %(EnRoll)
	models.cursor.execute(query)
	a=models.cursor.fetchall()
	Name = a[0][1]

	query = "select * from student where EnRoll=%s" %(EnRoll)
	models.cursor.execute(query)
	b=models.cursor.fetchall()

	if b[0][1] == None:
		return redirect(curl+'S/home1')

	else:
		query = "select Year from student where EnRoll=%s" %(EnRoll)
		models.cursor.execute(query)
		c=models.cursor.fetchall()
		Year = c[0][0]

		return render(req,'shome.html',{'c':curl,'a':'home','Name':Name,'Details':a,'year':Year})

@csrf_exempt
def shome1(req):
	EnRoll = req.COOKIES.get('enr')

	query = "select * from Info where EnRoll=%s" %(EnRoll)
	models.cursor.execute(query)
	a=models.cursor.fetchall()
	Name = a[0][1]

	if req.method=="GET":
		return render(req,'shome1.html',{'c':curl,'a':'home','Name':Name,'Details':a})

	else:
		Year=int(req.POST.get('input'))
		query="update student set Year = %d where EnRoll = %s" %(Year, EnRoll)
		models.cursor.execute(query)
		models.db.commit()

		return render(req,'shome.html',{'c':curl,'a':'home','Name':Name,'Details':a,'year':Year})


def thome(req):
	EnRoll = req.COOKIES.get('enr')

	query = "select * from Info where EnRoll=%s" %(EnRoll)
	models.cursor.execute(query)
	a=models.cursor.fetchall()
	Name = a[0][1]

	query = "select * from teacher where EnRoll=%s" %(EnRoll)
	models.cursor.execute(query)
	b=models.cursor.fetchall()


	if b[0][1] == 0:
		return render(req,'Auth.html',{'c':curl})

	elif b[0][2] == None:
		return redirect(curl+'T/home1')

	else:
		sub = b[0][2]
		return render(req,'thome.html',{'c':curl,'a':'home','Name':Name,'Details':a,'Sub':sub})

@csrf_exempt
def thome1(req):
	EnRoll = req.COOKIES.get('enr')

	query = "select * from Info where EnRoll=%s" %(EnRoll)
	models.cursor.execute(query)
	a=models.cursor.fetchall()
	Name = a[0][1]

	b = ()
	for i in range(1,5):
		query = "select Sub1,Sub2,Sub3 from Course where Year = %d" %(i)
		models.cursor.execute(query)
		c = models.cursor.fetchall()
		b = b + c[0]

	if req.method=="GET":
		return render(req,'thome1.html',{'c':curl,'a':'home','Name':Name,'Details':a,'Sub':b,'out':''})

	if req.method=="POST":
		Sub = req.POST.get('sub')
		query="update teacher set Subject = '%s' where EnRoll = '%s'" %(Sub,EnRoll)

		try:
			models.cursor.execute(query)

		except:
			return render(req,'thome1.html',{'c':curl,'a':'home','Name':Name,'Details':a,'Sub':b,'out':'*This Subject is already taken'})

		else:
			models.db.commit()
			return render(req,'thome.html',{'c':curl,'a':'home','Name':Name,'Details':a,'Sub':Sub})

@csrf_exempt
def mk(req):
	EnRoll = req.COOKIES.get('enr')

	query = "select * from Info where EnRoll=%s" %(EnRoll)
	models.cursor.execute(query)
	a=models.cursor.fetchall()
	Name = a[0][1]

	query = "select Year from student where EnRoll=%s" %(EnRoll)
	models.cursor.execute(query)
	b=models.cursor.fetchall()

	if b[0][0] == None:
		return render(req,'Year.html',{'c':curl,'a':'mark'})

	else:
		Year = b[0][0]

		c = []
		for i in range(1,Year+1):
			c.append(i)

		if req.method=="GET":

			query = "select Sub1,Sub2,Sub3 from Course where Year = 1"
			models.cursor.execute(query)
			Sub=models.cursor.fetchall()

			query = "select * from marks where EnRoll = %s" %(EnRoll)
			models.cursor.execute(query)
			m=models.cursor.fetchall()
			marks=[m[0][1],m[0][2],m[0][3]]
			print(marks)

			per = 0
			for i in marks:
				if i == None:
					per = per + 0
				else:
					per = per + i


			percentage = (per/300) * 100
			percentage = round(percentage,2)

			return render(req,'marksheet.html',{'c':curl,'a':'mark','Name':Name,'Sub':Sub,'years':c,'k':marks,'cy':'1','P':percentage})

		else:
			cy = int (req.POST.get('cyear'))

			query = "select Sub1,Sub2,Sub3 from Course where Year = %d" %(cy)
			models.cursor.execute(query)
			Sub=models.cursor.fetchall()

			x=0
			if cy > 1:
				x = (cy-1) * 3

			query = "select * from marks where EnRoll = %s" %(EnRoll)
			models.cursor.execute(query)
			m=models.cursor.fetchall()
			marks=[m[0][x+1],m[0][x+2],m[0][x+3]]

			per = 0
			for i in marks:
				if i == None:
					per = per + 0
				else:
					per = per + i


			percentage = (per/300) * 100
			percentage = round(percentage,2)

			return render(req,'marksheet.html',{'c':curl,'a':'mark','Name':Name,'Sub':Sub,'years':c,'k':marks,'cy':cy,'P':percentage})




def em(req):
	EnRoll = req.COOKIES.get('enr')

	query = "select * from Info where EnRoll=%s" %(EnRoll)
	models.cursor.execute(query)
	a=models.cursor.fetchall()
	Name = a[0][1]

	query = "select * from teacher where EnRoll=%s" %(EnRoll)
	models.cursor.execute(query)
	b=models.cursor.fetchall()


	if b[0][2] == None:
		return render(req,'Sub.html',{'c':curl,'a':'mark'})

	else:
		sub = b[0][2]

		b = ()
		for i in range(1,5):
			query = "select Sub1,Sub2,Sub3 from Course where Year = %d" %(i)
			models.cursor.execute(query)
			c = models.cursor.fetchall()
			b = b + c[0]

		Year = int ((b.index(sub)/3)) + 1

		query = " select EnRoll from student where Year = %d" %(Year)
		models.cursor.execute(query)
		x=models.cursor.fetchall()

		c = []
		for i in range(0,len(x)):
			c.append(x[i][0])

		d=[]
		for i in c:
			query = "select %s from marks where EnRoll = %d" %(sub,i)
			models.cursor.execute(query)
			e = models.cursor.fetchall()
			d.append(e[0][0])

		e = []
		for i in range(0,len(c)):
			e.append([c[i],d[i]])

		return render(req,'entermarks1.html',{'c':curl,'a':'mark','Name':Name,'marks':e})


@csrf_exempt
def enter(req):
	EnRoll = req.COOKIES.get('enr')

	query = "select * from Info where EnRoll=%s" %(EnRoll)
	models.cursor.execute(query)
	a=models.cursor.fetchall()
	Name = a[0][1]

	query = "select * from teacher where EnRoll=%s" %(EnRoll)
	models.cursor.execute(query)
	b=models.cursor.fetchall()

	sub = b[0][2]

	b = ()
	for i in range(1,5):
		query = "select Sub1,Sub2,Sub3 from Course where Year = %d" %(i)
		models.cursor.execute(query)
		c = models.cursor.fetchall()
		b = b + c[0]

	Year = int ((b.index(sub)/3)) + 1

	query = " select EnRoll from student where Year = %d" %(Year)
	models.cursor.execute(query)
	x=models.cursor.fetchall()

	c = []
	for i in range(0,len(x)):
		c.append(x[i][0])

	if req.method == 'GET':
		d=[]
		for i in c:
			query = "select %s from marks where EnRoll = %d" %(sub,i)
			models.cursor.execute(query)
			e = models.cursor.fetchall()
			d.append(e[0][0])

		e = []
		for i in range(0,len(c)):
			e.append([c[i],d[i]])

		return render(req,'entermarks.html',{'c':curl,'a':'mark','Name':Name,'marks':e})

	else:
		d=[]
		for i in c:
			query = "select %s from marks where EnRoll = %d" %(sub,i)
			models.cursor.execute(query)
			e = models.cursor.fetchall()
			d.append(e[0][0])

		e = []
		for i in range(0,len(c)):
			e.append([c[i],d[i]])

		mark = []
		for i in range(0,len(c)):
			try:
				mark.append(int (req.POST.get('mark'+str (c[i]))))
			except:
				return render(req,'entermarks.html',{'c':curl,'a':'mark','Name':Name,'marks':e,'error':"You didn't enter marks of some students"})

		for i in range (0,len(c)):
			query = "update marks set %s = %d where EnRoll = %d" %(sub,mark[i],c[i])
			models.cursor.execute(query)
			models.db.commit()

		d=[]
		for i in c:
			query = "select %s from marks where EnRoll = %d" %(sub,i)
			models.cursor.execute(query)
			e = models.cursor.fetchall()
			d.append(e[0][0])

		e = []
		for i in range(0,len(c)):
			e.append([c[i],d[i]])

		return render(req,'entermarks1.html',{'c':curl,'a':'mark','Name':Name,'marks':e,'error':""})
