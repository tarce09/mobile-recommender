from django.shortcuts import render
from django.http import HttpResponse
from .models import mobile1,camera,processor,RAM,battery,display
from django.db.models import IntegerField
#myfunctions

#converting into integers only
def remove_non_digit(st):
    st=str(st)
    numlst=['0','1','2','3','4','5','6','7','8','9','.']
    newst=''
    for i in st:
        if i in numlst:
            newst+=i
    return newst

#sortforbattery
def sortforbattery(element):
    return int(remove_non_digit(element.disc4))

#sortforcam    
def sortforcam(element):
    return int(remove_non_digit(element.disc3))

#sortforgaming
def sortforgaming(element):
    ram=RAM.objects.all()
    pro=processor.objects.all()
    string=''
    for i in ram:
        if remove_non_digit(i.id)==remove_non_digit(element.ramid):
            string+=remove_non_digit(i.ram)
            break
    for j in pro:
        if remove_non_digit(j.id)==remove_non_digit(element.proid):
            string+=remove_non_digit(j.freq)
            break
    if string=='':
        string='0'
    return float(string)

#sortforscreen
def sortforscreen(element):
    dis=display.objects.all()
    string1=''
    for i in dis:
        if remove_non_digit(i.id)==remove_non_digit(element.displayid):
            string1+=remove_non_digit(i.Resolution)
            string1+=remove_non_digit(i.Screen_size)
            break
    if string1=='':
        string1=''
    return float(string1)

#loading page initial
def index(request):
    return render(request,'index.html')

#loading page after getting information
def choose(request):
    lst= mobile1.objects.all()
    mainlst=[]
    val1=request.GET['categories']
    val2=request.GET['pricemintomax']
    #converting each smartphone to an object
    for i in lst:   
        phn = mobile1()
        phn.image=i.img
        phn.name=i.ProductName
        phn.price=i.Product_price
        prices=int(remove_non_digit(i.Product_price))
        phn.link=i.link
        phn.disc1=i.storage_info
        phn.disc2=i.display_info
        phn.disc3=i.cam_info
        phn.disc4=i.battery_info
        phn.disc5=i.processor_info
        phn.disc6=i.display_type
        phn.about=i.about_phone
        phn.img1=i.big_img0
        phn.img2=i.big_img1
        phn.img3=i.big_img2
        phn.img4=i.big_img3
        phn.img5=i.big_img4
        phn.brand=i.Brand
        #foreignkeyids
        phn.ramid=i.ram
        phn.proid=i.processor
        phn.displayid=i.display
        #removing non budget phones
        if val2=='0' and prices>(10000):
            continue
        elif val2=='1' and (prices>(20000) or prices<=(10000)):
            continue
        elif val2=='2' and (prices>(30000) or prices<=(20000)):
            continue
        elif val2=='3' and (prices>(40000) or prices<=(30000)):
            continue
        elif val2=='4' and (prices>(50000) or prices<=(40000)):
            continue
        elif val2=='5' and (prices>(65000) or prices<=(50000)):
            continue
        elif val2=='6' and (prices>(80000) or prices<=(65000)):
            continue
        elif val2=='7' and prices<=80000:
            continue
        #calling fuctions defined above to get only necesary information
        if val1=='ios' and 'Apple' in str(phn.brand):
            mainlst.append(phn)
        elif val1!='ios' and 'Apple' not in str(phn.brand):
            mainlst.append(phn)
        if val1=='batterylife':
            mainlst.sort(reverse=True,key=sortforbattery)
        elif val1=='cameraphone':
            mainlst.sort(reverse=True,key=sortforcam)
        elif val1=='gamingphone':
            mainlst.sort(reverse=True,key=sortforgaming)
        elif val1=='display':
            mainlst.sort(reverse=True,key=sortforscreen)
    mainlst=mainlst[:50]
    return render(request,'index.html',{'result':mainlst})

#calling the next page if user selects a smartphone
def shop(request):
    
    lst1=mobile1()
    lst1.name=request.GET['namee']
    lst1.price=request.GET['pricee']
    lst1.image=request.GET['image']
    lst1.disc1=request.GET['disc1']
    lst1.disc2=request.GET['disc2']
    lst1.disc3=request.GET['disc3']
    lst1.disc4=request.GET['disc4']
    lst1.disc5=request.GET['disc5']
    lst1.disc6=request.GET['disc6']
    lst1.link=request.GET['link']
    lst1.about=request.GET['about']
    lst1.img1=request.GET['img1']
    lst1.img2=request.GET['img2']
    lst1.img3=request.GET['img3']
    lst1.img4=request.GET['img4']
    lst1.img5=request.GET['img5']

    return render(request,'shop.html',{'result':lst1})
