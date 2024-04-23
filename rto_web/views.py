from django.conf import settings
from django.shortcuts import render,redirect

from django.contrib.auth.models import User

from django.urls import reverse

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.template import loader

from django.contrib import messages

from django.contrib.auth.models import User

import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required(login_url='login')
# Create your views here.



def create_checkout_session(request):
    # Create a new Checkout Session
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'INR',
                    'product_data': {
                        'name': 'Driving Licence',
                    },
                    'unit_amount': 120000,  # Amount in cents
                },
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('success')),
        cancel_url=request.build_absolute_uri(reverse('cancel')),
    )

    return redirect(session.url)


def success(request):
		return render(request, 'index.html')
	
def cancel(request):
    return render(request, 'cancel.html')





# Create your views here.
def index(request):
	return render(request,"index.html",{})

def category(request):
	return render(request,"categorys.html",{})

def about(request):
	return render(request,"about.html",{})

def contact(request):
	return render(request,"contact.html",{})

def guid(request):
	return render(request,"guid.html",{})

def appoinment(request):
	return render(request,"appinment.html",{})

def confirm(request):
	return render(request,"confirm.html",{})



from .models import dl 
def l_form(request):
	if request.method=='POST':
		rto_state=request.POST.get('rto_state')
		rto_office=request.POST.get('rto_office')
		rto_pincode=request.POST.get('rto_pincode')
		name=request.POST.get('f_name')
		father_name=request.POST.get('fathername')
		mother_name=request.POST.get('mothername')
		adhar_card_no=request.POST.get('adh_no')
		date=request.POST.get('dob')
		birth_p=request.POST.get('b_p');
		email=request.POST.get('email');
		mobile=request.POST.get('m_no');
		gender=request.POST.get('gender');
		relation=request.POST.get('relation');
		age=request.POST.get('age');
		qulification=request.POST.get('qualification');
		b_group=request.POST.get('blood_group');
		a_mobile=request.POST.get('a_m_no');
		occupation=request.POST.get('occupation');
		country=request.POST.get('country');
		state=request.POST.get('state');
		city=request.POST.get('city');
		address=request.POST.get('address');
		pincode=request.POST.get('pincode');
		issues_state=request.POST.get('issue_state');
		issue_date=request.POST.get('issue_date');
		expire_date=request.POST.get('expir_date');
		disablity_yn=request.POST.get('d');
		disablit=request.POST.get('disbility');
		doner=request.POST.get('organs');
		all_yes=request.POST.get('data');
		photo=request.POST.get('d_1_2');
		sign=request.POST.get('d_1_3');
		document=request.POST.get('document_1');
		proof=request.POST.get('proof');
		doc_no=request.POST.get('d_no');
		issue_date_doc=request.POST.get('d_issue_date');
		issues_by=request.POST.get('issued_by');
		doc_1=request.POST.get('d_1');
		document_2=request.POST.get('document_2');
		proof_2=request.POST.get('proof_2');
		doc_no_2=request.POST.get('d_no_2');
		issue_date_2=request.POST.get('d_issue_date_2');
		issues_by_2=request.POST.get('issued_by_2');
		doc_2=request.POST.get('d_1_2');
			
		dbs_1 = dl(rto_state=rto_state, rto_office=rto_office, rto_pincode=rto_pincode, name=name, father_name=father_name, mother_name=mother_name, adhar_card_no=adhar_card_no, 
				date=date, birth_p=birth_p, email=email, mobile=mobile, gender=gender, relation=relation, age=age, qulification=qulification, b_group=b_group, a_mobile=a_mobile,
				occupation=occupation, country=country, state=state, city=city, address=address, pincode=pincode, issues_state=issues_state, issue_date=issue_date, 
				expire_date=expire_date, disablity_yn=disablity_yn, disablit=disablit, doner=doner, all_yes=all_yes, photo=photo, sign=sign, document=document, 
				proof=proof, doc_no=doc_no,issue_date_doc=issue_date_doc,issues_by=issues_by,doc_1=doc_1, document_2=document_2,proof_2=proof_2,doc_no_2=doc_no_2,
				issue_date_2=issue_date_2,issues_by_2=issues_by_2,doc_2=doc_2);

		dbs_1.save()
		return redirect('../confirm')				
	return render(request,"l_form.html",{})


from .models import registration 

def singup(request):
	if request.method=='POST':
		uname=request.POST.get('username')
		email=request.POST.get('email')
		pass1=request.POST.get('password1')
		pass2=request.POST.get('cpassword')
		address=request.POST.get('address')
		mobile=request.POST.get('mobile')
		gender=request.POST.get('gender')
		state=request.POST.get('state')
		if User.objects.filter(email=email).exists():
			messages.warning(request,'email is already exists!')
			return redirect(singup)
		elif pass1!=pass2:
			messages.warning(request,'password and confirm password does not match !')
			return redirect(singup)
		else:
			dbs = registration(name=uname, email=email, password=pass1, cpassword=pass2, address=address, mobile=mobile, gender=gender, state=state)
			dbs.save()
			my_user = User.objects.create_user(uname,email,pass1)
			my_user.save()
				
			return redirect('../u_login')
	return render(request,"signup.html",{})

from django.contrib.auth import login as auth_login

def user_login(request):
	if request.method=='POST':
		username=request.POST.get('username')
		pass1=request.POST.get('password1')
		user=authenticate(request,username=username,password=pass1)
		if user is not None:
			login(request,user)
			return redirect('http://127.0.0.1:8000/')
		else:
			#return HttpResponse("username and password incoreect !!")
			return redirect('../u_login')
	return render(request,'login.html')	

def LogoutPage(request):
	logout(request)
	return redirect('../u_login')
