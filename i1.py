from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
import bs4
import requests
import pyrebase
import matplotlib.pyplot as plt
import pandas as pd
from heapq import nlargest

def f1():
	add_window.deiconify()
	main_window.withdraw()
	view_window.withdraw()
	delete_window.withdraw()
	update_window.withdraw()
	aw_ent_id.focus()
	aw_ent_id.delete(0,END)
	aw_ent_name.delete(0,END)
	aw_ent_salary.delete(0,END)
def f2():
	vw_st_data.delete(1.0,END)
	try:
		view_window.deiconify()
		main_window.withdraw()
		add_window.withdraw()
		delete_window.withdraw()
		update_window.withdraw()
		firebaseConfig = {
			"apiKey": "##Your database api key##",
			"authDomain": "##Your database authDomain##",
			"databaseURL": "##Your database URL##",
			"projectId": "##Your database projectID##",
			"storageBucket": "##Your database StorageBucket##",
			"messagingSenderId": "##Your Database SenderID##",
			"appId": "##Your Database APP ID##"
		}
		firebase=pyrebase.initialize_app(firebaseConfig)
		db = firebase.database()
		data = db.child("employee").get()
		if data.pyres is not None and data.each():
			#for d in data.each():
				#m=[]
				#n=[]
				#m.append(d.key())
				#n.append(d.val())
			#if (id) in m:
			#print(data.pyres)
			#print(data.val)
			for d in data.each():
				msg="id:",d.key(),d.val(),"->"
				vw_st_data.insert(INSERT,msg)	
				#abc=d.val()
				#print(abc)
				#print("id ", d.key(), "---->", d.val())
				#print(m)
				#print(n)
				#emp = list(data.each())
				#print(emp)
				#print(d.key())
				#print(d.val())
				#id="id:",(d.key())
				#print(id)
				#namsal=(d.val())
				#msg = (id,namsal)
				#print(id)
				#print(namsal)
				#msg=(id,"   ",namsal,"  ")
				#msg = "id:",emp[0],emp[1],emp[2]
				#vw_st_data.insert(INSERT,msg)
										
		else:
			showerror("Issue","Data is not found")
	except Exception as e:
		showerror("Issue","Data is not found")
		print(e)

def f3():
	update_window.deiconify()
	main_window.withdraw()
	view_window.withdraw()
	delete_window.withdraw()
	add_window.withdraw()
	ud_ent_id.focus()
	ud_ent_id.delete(0,END)
	ud_ent_name.delete(0,END)
	ud_ent_salary.delete(0,END)

def f4():
	delete_window.deiconify()
	main_window.withdraw()
	view_window.withdraw()
	add_window.withdraw()
	update_window.withdraw()
	dw_ent_id.focus()
	dw_ent_id.delete(0,END)
	

def f5():
	vw_st_data.delete(1.0,END)
	try:
		view_window.deiconify()
		main_window.withdraw()
		firebaseConfig = {
			"apiKey": "##Your database api key##",
			"authDomain": "##Your database authDomain##",
			"databaseURL": "##Your database URL##",
			"projectId": "##Your database projectID##",
			"storageBucket": "##Your database StorageBucket##",
			"messagingSenderId": "##Your Database SenderID##",
			"appId": "##Your Database APP ID##"
		}
		firebase=pyrebase.initialize_app(firebaseConfig)
		db = firebase.database()
		data = db.child("employee").get()
		if data.pyres is not None and data.each():
			a12=[]
			a13=[]
			for d in data.each():
				a=d.val()
				#b=data[0]
				#print(b)
				#print(d.val)
				if d.val() is None:
					continue
				else:
					#a7=[]
					a1=list(a.items())
					#print(a1)
					#print(len(a1))
					#print(a1[0])
					#print(a1[1])
					a2=a1[0]
					#print(a2)
					#print(len(a2))
					a3=a1[1]
					#print(a2[0])
					#print(a2[1])
					a8=str(a2[1])
					a12.append(a8)
					#print(a3[0])
					#print(a3[1])
					a9=str(a3[1])
					a13.append(a9)
					a11=a3[1]
					#a4=a2[1]
					#a5=a3[1]
					#print(a4)
					#print(a5)
					#for i in a4:
					#a6[a4]=a5
					#print(a6)
					#for i in a:
						#b=i.keys()
						#c=i.values()
						#print(b)
						#print(c)
					#w=0
					#a10=[]
					#for i in range(0,len(a11)):
					#a8.insert(len(a11)-1,i)
					#print(10)
					for o in a9:
						a7=[]
						#a7.append()
						a7.append(a8)
						a7.append(a9)
						#a12.append(a9)
					#print(a7)
			#a13=str(a3[1])
			#for o in a13:
			#a12.(a13)
			#print(a12)
			#print(a13)
			z=1
			for i in range (0,len(a12)):
				msg="\n","id:",z,"name:",a12[i],"salary:",a13[i],"\n"
				#msg="id",":",i,a2[0],":",a12[i],a3[i],":",a13[i],"--->"
				vw_st_data.insert(INSERT,msg)
				z+=1
				

	except Exception as e:
		print("Issue",e)

def aback():
	main_window.deiconify()
	add_window.withdraw()

def vback():
	main_window.deiconify()
	view_window.withdraw()

def uback():
	main_window.deiconify()
	update_window.withdraw()

def dback():
	main_window.deiconify()
	delete_window.withdraw()

def usave():
	try:
		id=int(ud_ent_id.get())
		firebaseConfig = {
			"apiKey": "##Your database api key##",
			"authDomain": "##Your database authDomain##",
			"databaseURL": "##Your database URL##",
			"projectId": "##Your database projectID##",
			"storageBucket": "##Your database StorageBucket##",
			"messagingSenderId": "##Your Database SenderID##",
			"appId": "##Your Database APP ID##"
		}
		firebase=pyrebase.initialize_app(firebaseConfig)
		db=firebase.database()
		data = db.child("employee").get()
		l = []	
		#i=1
		if data.pyres is not None:
			for i in data.each():	
				l.append(i.key()) 
		if int(id) in l:
			name=ud_ent_name.get()
			salary=int(ud_ent_salary.get())
			if (id>0):
				if (len(name)>=2):
					if (salary>8000):
						info={}
						info["name"]=name
						info["salary"]=salary	
						db.child("employee").child(id).set(info)
						showinfo("Success","Record Updated !")
						ud_ent_id.delete(0,END)
						ud_ent_name.delete(0,END)
						ud_ent_salary.delete(0,END)
						ud_ent_id.focus()
					else:
						showerror("Issue","Please enter valid Employee salary")
						ud_ent_salary.delete(0,END)
						ud_ent_salary.focus()
				else:
					showerror("Issue","Please enter valid Employee name")
					ud_ent_name.delete(0,END)
					ud_ent_name.focus()
			else:
				showerror("Issue","Please enter valid Employee id")		
				ud_ent_id.delete(0,END)
				ud_ent_id.focus()
			
		else:
			showerror("Issue","Id does not exists!")
	except Exception as e:
		showerror("Issue:","Please enter values")
		print(e)


def asave():
	try:
		id=int(aw_ent_id.get())
		firebaseConfig = {
			"apiKey": "##Your database api key##",
			"authDomain": "##Your database authDomain##",
			"databaseURL": "##Your database URL##",
			"projectId": "##Your database projectID##",
			"storageBucket": "##Your database StorageBucket##",
			"messagingSenderId": "##Your Database SenderID##",
			"appId": "##Your Database APP ID##"
		}
		firebase=pyrebase.initialize_app(firebaseConfig)
		db=firebase.database()
		
		id=int(aw_ent_id.get())
		data = db.child("employee").get()
		l=[]
		#i=1
		#for i in data.each():
		#l.append(i.key())
		#print(data.val())
		#print(str(id) in data.key())
		if data.pyres is not None:	
			for i in data.each():
				l.append(i.key())
		#if data.pyres is not None and str(id) in data.val():
		if int(id) in l:
			print("hi")
			showerror("Issue:","Id already exists!")
			aw_ent_id.delete(0,END)
			aw_ent_name.delete(0,END)
			aw_ent_salary.delete(0,END)
		else:
			name=aw_ent_name.get()
			salary=int(aw_ent_salary.get())
			if (id>0):
				if (len(name)>=2):
					if (salary>8000):
						info={}
						info["name"]=name
						info["salary"]=salary	
						db.child("employee").child(id).set(info)
						showinfo("Success","Employee Added !")
						aw_ent_id.delete(0,END)
						aw_ent_name.delete(0,END)
						aw_ent_salary.delete(0,END)
						aw_ent_id.focus()
					else:
						showerror("Issue","Please enter valid employee salary")
						aw_ent_salary.delete(0,END)
						aw_ent_salary.focus()
				else:
					showerror("Issue","Please enter valid eployee name")
					aw_ent_name.delete(0,END)
					aw_ent_name.focus()
			else:
				showerror("Issue","Please enter valid employee id")		
				aw_ent_id.delete(0,END)
				aw_ent_id.focus()
	except Exception as e:
		showerror("Issue:","Please enter values")
		print(e)

def dsave():
	try:
		id=int(dw_ent_id.get())
		firebaseConfig = {
			"apiKey": "##Your database api key##",
			"authDomain": "##Your database authDomain##",
			"databaseURL": "##Your database URL##",
			"projectId": "##Your database projectID##",
			"storageBucket": "##Your database StorageBucket##",
			"messagingSenderId": "##Your Database SenderID##",
			"appId": "##Your Database APP ID##"
		}
		firebase=pyrebase.initialize_app(firebaseConfig)
		db=firebase.database()
		data = db.child("employee").get()
		l=[]
		#i=1
		for i in data.each():
			l.append(i.key())
		if int(id) in l:
			print("hi")
			db.child("employee").child(id).remove()
			showinfo("Success","Record removed!")
			dw_ent_id.delete(0,END)
			dw_ent_id.focus()
		else:
			showerror("Issue","Please enter valid employee id")		
			dw_ent_id.delete(0,END)
			dw_ent_id.focus()
	except Exception as e:
		showerror("Issue:","Please enter values")
		print(e)
	
def charts():
	firebaseConfig = {
		"apiKey": "##Your database api key##",
			"authDomain": "##Your database authDomain##",
			"databaseURL": "##Your database URL##",
			"projectId": "##Your database projectID##",
			"storageBucket": "##Your database StorageBucket##",
			"messagingSenderId": "##Your Database SenderID##",
			"appId": "##Your Database APP ID##"
	}
	firebase=pyrebase.initialize_app(firebaseConfig)
	db=firebase.database()
	data = db.child("employee").get()
	#id = data[""]
	if data.pyres is not None and data.each():
		a6={}
		a8=[]
		for d in data.each():
			a=d.val()
			#print(a)
			if d.val() is None:
				continue
			else:
				a1=list(a.items())
				#print(a1)
				#print(len(a1))
				#print(a1[0])
				#print(a1[1])
				a2=a1[0]
				#print(a2)
				#print(len(a2))
				a3=a1[1]
				#print(a2[1])
				#print(a3[1])
				a4=a2[1]
				a5=a3[1]
				#print(a4)
				#print(a5)
				#for i in a4:
				a6[a4]=a5
				#print(a6)
				#for i in a:
					#b=i.keys()
					#c=i.values()
					#print(b)
					#print(c)
		#print(a6)
		a7=nlargest(5,a6,key=a6.get)		
		#print(a7)
		for x in a7:
			val=a6.get(x)
			a8.append(val)	
		#print(a8)
	
	plt.bar(a7,a8,color=["#70416D","#FB3640","#FDCA40","#51C4D3","#CE1F6A"],width=0.4)
	plt.xlabel("Employee")
	plt.ylabel("Salary")
	plt.title("Top 5 Highest Earning Employee's")
	plt.show()
	
		

main_window = Tk()
main_window.title("E.M.S")
main_window.geometry("1200x550+100+100")
main_window['bg'] = '#FFF8D9'

f=("Courier New",20,"bold")
mw_btn_add=Button(main_window,text="Add",font=f,width=10,command=f1)
mw_btn_view=Button(main_window,text="View",font=f,width=10,command=f5)
mw_btn_update=Button(main_window,text="Update",font=f,width=10,command=f3)
mw_btn_delete=Button(main_window,text="Delete",font=f,width=10,command=f4)
mw_btn_charts=Button(main_window,text="Charts",font=f,width=10,command=charts)
f2=('Courier New',14,"bold")

#(Optional) For showing Quote on your window
#res=requests.get("https://www.brainyquote.com/quote_of_the_day")
#data=bs4.BeautifulSoup(res.text,"html.parser")
#info=data.find("img",{"class":"bqPhotoFullDesktop"})
#mw_lab_quote=Label(main_window,text=("QOTD:"+info["alt"]),font=f2)

mw_btn_add.pack(pady=10)
mw_btn_view.pack(pady=10)
mw_btn_update.pack(pady=10)
mw_btn_delete.pack(pady=10)
mw_btn_charts.pack(pady=10)
#mw_lab_quote.pack(pady=30)

add_window = Toplevel(main_window)
add_window.title("Add Empployee")
add_window.geometry("600x500+100+100")
add_window['bg']='#FFF8D9'

aw_lbl_id=Label(add_window,text="enter id:",font=f)
aw_ent_id=Entry(add_window,font=f,bd=3)
aw_lbl_name=Label(add_window,text="enter name:",font=f)
aw_ent_name=Entry(add_window,font=f,bd=3)
aw_lbl_salary=Label(add_window,text="enter salary:",font=f)
aw_ent_salary=Entry(add_window,font=f,bd=3)
aw_btn_save=Button(add_window,text="Save",font=f,width=10,command=asave)
aw_btn_back=Button(add_window,text="Back",font=f,width=10,command=aback)

aw_lbl_id.pack(pady=10)
aw_ent_id.pack(pady=10)
aw_lbl_name.pack(pady=10)
aw_ent_name.pack(pady=10)
aw_lbl_salary.pack(pady=10)
aw_ent_salary.pack(pady=10)
aw_btn_save.pack(pady=10)
aw_btn_back.pack(pady=10)

view_window = Toplevel(main_window)
add_window.title("View Employee")
view_window.geometry("680x500+100+100")
view_window['bg']='#FFF8D9'

f1=("Courier New",20,"bold")
vw_st_data= ScrolledText(view_window,width=40,height=10,font=f1)
vw_btn_back = Button (view_window,text="Back",font=f,command=vback)
vw_st_data.pack(pady=10)
vw_btn_back.pack(pady=10)

update_window = Toplevel(main_window)
update_window.title("Update Employee")
update_window.geometry("600x500+100+100")
update_window['bg']='#FFF8D9'

ud_lbl_id=Label(update_window,text="enter id:",font=f)
ud_ent_id=Entry(update_window,font=f,bd=3)
ud_lbl_name=Label(update_window,text="enter name:",font=f)
ud_ent_name=Entry(update_window,font=f,bd=3)
ud_lbl_salary=Label(update_window,text="enter salary:",font=f)
ud_ent_salary=Entry(update_window,font=f,bd=3)

ud_btn_save=Button(update_window,text="Save",font=f,width=10,command=usave)
ud_btn_back=Button(update_window,text="Back",font=f,width=10,command=uback)

ud_lbl_id.pack(pady=10)
ud_ent_id.pack(pady=10)
ud_lbl_name.pack(pady=10)
ud_ent_name.pack(pady=10)
ud_lbl_salary.pack(pady=10)
ud_ent_salary.pack(pady=10)
ud_btn_save.pack(pady=10)
ud_btn_back.pack(pady=10)

delete_window = Toplevel(main_window)
delete_window.title("Delete employee")
delete_window.geometry("600x500+100+100")
delete_window['bg']='#FFF8D9'

dw_lbl_id=Label(delete_window,text="enter id:",font=f)
dw_ent_id=Entry(delete_window,font=f,bd=3)

dw_btn_save=Button(delete_window,text="Save",font=f,width=10,command=dsave)
dw_btn_back=Button(delete_window,text="Back",font=f,width=10,command=dback)

dw_lbl_id.pack(pady=10)
dw_ent_id.pack(pady=10)
dw_btn_save.pack(pady=10)
dw_btn_back.pack(pady=10)

main_window.mainloop()
