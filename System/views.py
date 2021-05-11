from django.shortcuts import render , get_object_or_404 ,redirect ,HttpResponse
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.models import User
from  django.contrib.auth.decorators import login_required , user_passes_test
from .models import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import  AuthenticationForm
from .forms import *

# Create your views here.





Gaming = {
    'CPU':0.20 ,
    'GPU':0.30 , 
    'MOBO':0.1 ,
    'PSU':0.07 , 
    'RAM':0.05 , 
    'STORAGE':0.06 , 
    'CASE': 0.03 ,
    'PERIPHERALS':0.03 ,
    'MONITOR':0.12 ,
    'LCS':0.04
}

Trading = {
    'CPU':0.30 ,
    'GPU':0.20 , 
    'MOBO':0.1 ,
    'PSU':0.07 , 
    'RAM':0.05 , 
    'STORAGE':0.06 , 
    'CASE': 0.03 ,
    'PERIPHERALS':0.03 ,
    'MONITOR':0.12 ,
    'LCS':0.04
}


def Scrapper(request):
    from selenium import webdriver
    from selenium.common.exceptions import NoSuchElementException
    from selenium.webdriver.chrome.options import Options  
    import time
    chrome_options = Options()  
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')  
    PATH ="C:\Program Files\chromedriver.exe" 

    # component_list =['processor','ram for pc','motherboard','graphics card','power supply unit','liquid cooling system for pc','speaker for pc','keyboard' , 'computer monitor' , 'computer mouse' ,'computer Harddisk' , 'cpu case']
    component_list =['cpu case']

   

    for component in component_list:
        time.sleep(5)
        driver = webdriver.Chrome(chrome_options=chrome_options , executable_path= PATH)
        searchname = component

        def amazon(url):
            chrome_options = Options()  
            # chrome_options.add_argument("--headless")  
            PATH ="C:\Program Files\chromedriver.exe" 
            driver = webdriver.Chrome(chrome_options=chrome_options , executable_path= PATH)
            driver.get(url)
            dic = {}
            check = True
            try:
                container = driver.find_element_by_id('productDetails_techSpec_section_1')
                dic['img'] = driver.find_element_by_id('imgTagWrapperId').find_elements_by_tag_name('img')[0].get_attribute('src')
                dic['url'] = str(url)
                dic['name'] = driver.find_element_by_class_name('a-size-large').text
                for i, j in zip(container.find_elements_by_tag_name('th'),container.find_elements_by_tag_name('td')):
                    dic[i.text.lower().replace(' ', '_')] =  j.text
                x = dic
                try:
                    try:
                        dic['price'] = float(driver.find_element_by_class_name('a-size-medium').text[2:].replace(',' , ''))
                    except:
                        driver.find_element_by_id("buybox-see-all-buying-choices-announce").click()
                        time.sleep(2)
                        dic['price'] = float(driver.find_element_by_class_name('a-size-large.a-color-price.olpOfferPrice.a-text-bold').text[2:].replace(',' , ''))
                except:
                    dic['price']= float(0)
            except NoSuchElementException:
                x = 'Unavailable'
                
            driver.quit()
            return x

        count=0
        links= []

        for i in range(1, 3):
            url1 = 'https://www.amazon.in/s?k=' + searchname + '&page=' + str(i) # for cpu case
            driver.get(url1)
            for i in driver.find_elements_by_css_selector('.sg-col-4-of-12.sg-col-8-of-16.sg-col-12-of-20.sg-col'):
                links.append(WebDriverWait(i, 100).until(EC.presence_of_element_located((By.CLASS_NAME,'a-link-normal'))).get_attribute('href'))
        links = list(dict.fromkeys(links))
        print(links)
 
        for link in links:
            temp  = amazon(link)
            if temp=='Unavailable':
                print(temp)
                count+=1
                pass
            else:
                if searchname=='processor':
                    List = Processor._meta.get_fields()
                    field_list=[]
                    for i in List:
                        try:
                            print(str(i))
                            field_list.append((str(i).split('.')[2]))
                        except:
                            pass
                    Processor.objects.create(**{key: value for key, value in temp.items() if key in field_list})
                    print(field_list)
                    print('done for processor')
                    
                elif searchname=='ram for pc':
                    List = RAM._meta.get_fields()
                    field_list=[]
                    for i in List:
                        try:
                            print(str(i))
                            field_list.append((str(i).split('.')[2]))
                        except:
                            pass
                    RAM.objects.create(**{key: value for key, value in temp.items() if key in field_list})
                    print(field_list)
                    print('done for RAM')
                elif searchname=='motherboard':
                    List = Motherboard._meta.get_fields()
                    field_list=[]
                    for i in List:
                        try:
                            print(str(i))
                            field_list.append((str(i).split('.')[2]))
                        except:
                            pass
                    Motherboard.objects.create(**{key: value for key, value in temp.items() if key in field_list})
                    print(field_list)
                    print('done for motherboard')
                elif searchname=='graphics card':
                    List = Graphics_Card._meta.get_fields()
                    field_list=[]
                    for i in List:
                        try:
                            print(str(i))
                            field_list.append((str(i).split('.')[2]))
                        except:
                            pass
                    Graphics_Card.objects.create(**{key: value for key, value in temp.items() if key in field_list})
                    print(field_list)
                    print('done for graphics_card')
                elif searchname=='power supply unit':
                    List = Power_Supply_Unit._meta.get_fields()
                    field_list=[]
                    for i in List:
                        try:
                            print(str(i))
                            field_list.append((str(i).split('.')[2]))
                        except:
                            pass
                    Power_Supply_Unit.objects.create(**{key: value for key, value in temp.items() if key in field_list})
                    print(field_list)
                    print('done for psu')
                elif searchname=='liquid cooling system for pc':
                    List = Liquid_Cooling_System._meta.get_fields()
                    field_list=[]
                    for i in List:
                        try:
                            print(str(i))
                            field_list.append((str(i).split('.')[2]))
                        except:
                            pass
                    Liquid_Cooling_System.objects.create(**{key: value for key, value in temp.items() if key in field_list})
                    print(field_list)
                    print('done for lcs')
                elif searchname=='speaker for pc':
                    List = Speaker._meta.get_fields()
                    field_list=[]
                    for i in List:
                        try:
                            print(str(i))
                            field_list.append((str(i).split('.')[2]))
                        except:
                            pass
                    Speaker.objects.create(**{key: value for key, value in temp.items() if key in field_list})
                    print(field_list)
                    print('done for speaker')
                elif searchname=='cpu case':
                    List = Case._meta.get_fields()
                    field_list=[]
                    for i in List:
                        try:
                            print(str(i))
                            field_list.append((str(i).split('.')[2]))
                        except:
                            pass
                    Case.objects.create(**{key: value for key, value in temp.items() if key in field_list})
                    print(field_list)
                    print('done for case')
                elif searchname=='keyboard':
                    List = Keyboard._meta.get_fields()
                    field_list=[]
                    for i in List:
                        try:
                            print(str(i))
                            field_list.append((str(i).split('.')[2]))
                        except:
                            pass
                    Keyboard.objects.create(**{key: value for key, value in temp.items() if key in field_list})
                    print(field_list)
                    print('done for keyboard')
                elif searchname=='computer monitor':
                    List = Monitor._meta.get_fields()
                    field_list=[]
                    for i in List:
                        try:
                            print(str(i))
                            field_list.append((str(i).split('.')[2]))
                        except:
                            pass
                    Monitor.objects.create(**{key: value for key, value in temp.items() if key in field_list})
                    print(field_list)
                    print('done for monitor')
                elif searchname=='computer Harddisk':
                    List = Harddisk._meta.get_fields()
                    field_list=[]
                    for i in List:
                        try:
                            print(str(i))
                            field_list.append((str(i).split('.')[2]))
                        except:
                            pass
                    Harddisk.objects.create(**{key: value for key, value in temp.items() if key in field_list})
                    print(field_list)
                    print('done for Harddisk')
                else:
                    List = Mouse._meta.get_fields()
                    field_list=[]
                    for i in List:
                        try:
                            print(str(i))
                            field_list.append((str(i).split('.')[2]))
                        except:
                            pass
                    Mouse.objects.create(**{key: value for key, value in temp.items() if key in field_list})
                    print(field_list)
                    print('done for Mouse')


    driver.quit()
    context= {
        'count':count
    }
    return render(request , 'scrapper.html', context)

def Money_Distribution(price,type_):
    temp1 = {}
    if type_ == 'Gaming':
        temp = Gaming
    else:
        temp = Trading
    for key , value in temp.items():
        temp1[key] = round(temp[key]*float(price), 2)
    return temp1


def clear_db(request):
    Processor.objects.all().delete()
    Motherboard.objects.all().delete()
    RAM.objects.all().delete()
    Graphics_Card.objects.all().delete()
    Harddisk.objects.all().delete()
    Power_Supply_Unit.objects.all().delete()
    Liquid_Cooling_System.objects.all().delete()
    Monitor.objects.all().delete()
    Case.objects.all().delete()
    Keyboard.objects.all().delete()
    Mouse.objects.all().delete()
    OS.objects.all().delete()
    Speaker.objects.all().delete()
    
    return render(request ,'scrapper.html')



def Add_Fav(request , id ):
    build = Build.objects.get(id = id)
    Favourites.objects.create(user = request.user , Build = build )
    return redirect('/view_fav/')

def View_Fav(request):
    F = Favourites.objects.filter(user = request.user)
    context = {
        'Fav':F
    }
    return render(request , 'view_fav.html' , context)


def Algorithm(request):
    temp = None
    price= request.POST.get('price')
    type_= request.POST.get('type')
    temp = Money_Distribution(price , type_)
    print(temp)
    for key , value in temp.items():
        if key=='CPU':
            P = Processor.objects.filter(price__range = (value , value + 4000.0))
            P = list(P)
            if not P:
                for p in Processor.objects.all():
                    if p.price < value:
                        print(p)
                        P.append(p)
                        break
        elif key=="GPU":
            G = Graphics_Card.objects.filter(price__range = (value , value + 4000.0))
            G = list(G)
            if not G:
                for g in Graphics_Card.objects.all():
                    if g.price < value:
                        G.append(g)
                        break
        elif key=="MOBO":
            M = Motherboard.objects.filter(price__range = (value , value + 4000.0))
            M = list(M)
            if not M:
                for m in Motherboard.objects.all():
                    if m.price < value:
                        M.append(m)
                        break
        elif key=="PSU":
            PSU = Power_Supply_Unit.objects.filter(price__range = (value , value + 4000.0))
            PSU = list(PSU)
            if not PSU:
                for psu in Power_Supply_Unit.objects.all():
                    if psu.price < value:
                        PSU.append(psu)
                        break
        elif key=="RAM":
            R = list(RAM.objects.filter(price__range = (value , value + 4000.0)))
            if not R:
                for r in RAM.objects.all():
                    if r.price < value:
                        R.append(r)
                        break
        elif key=="STORAGE":
            H = list(Harddisk.objects.filter(price__range = (value , value + 4000.0)))
            if not H:
                for h in Harddisk.objects.all():
                    if h.price < value:
                        H.append(h)
                        break
        elif key=="CASE":
            C = list(Case.objects.filter(price__range = (value , value + 4000.0)))
            if not C:
                for c in Case.objects.all():
                    if c.price < value:
                        C.append(c)
                        break
        elif key=="LCS":
            LCS = list(Liquid_Cooling_System.objects.filter(price__range= (value , value + 4000.0)))
            if not LCS:
                for lcs in Liquid_Cooling_System.objects.all():
                    if lcs.price <value:
                        LCS.append(lcs)
                        break
        
        elif key=="MONITOR":
            monitor = list(Monitor.objects.filter(price__range =(value  , value + 4000.0)))
            if not monitor:
                for mon in Monitor.objects.all():
                    if mon.price < value:
                        monitor.append(mon)
                        break

        else:
            Mo = list(Mouse.objects.filter(price__range = (value/2 , value + 4000.0)))
            if not Mo:
                for mo in Mouse.objects.all():
                    if mo.price < value:
                        Mo.append(mo)
                        break
            K = list(Keyboard.objects.filter(price__range =(value/2 , value + 4000.0) ))
            if not K:
                for k in Keyboard.objects.all():
                    if k.price < value:
                        K.append(k)
                        break
    
    print( P )
    print( G )
    print( M )
    print( PSU )
    print( R )
    print( H )
    print( Mo )
    print(K)

    
        
    context = {
        'Processor':P , 
        'Graphics': G , 
        'Motherboard':M  , 
        'PSU':PSU , 
        'RAM':R , 
        'Harddisk':H , 
        'Mouse':Mo,
        'Keyboard':K , 
        'data':'data',
        'Monitor':monitor , 
        'LCS':LCS , 
        'Case':C
    }
    return render(request , 'homepage.html' , context)


def Build_Pc(request , id):
    if request.method=="POST":
        kb = Keyboard.objects.get(id = request.POST.get('keyboard'))
        ram = RAM.objects.get(id = request.POST.get('ram'))
        monitor = Monitor.objects.get(id = request.POST.get('monitor') )
        ssd = Harddisk.objects.get(id = request.POST.get('ssd'))
        processor = Processor.objects.get(id = request.POST.get('processor'))
        mouse = Mouse.objects.get(id = request.POST.get('mouse'))
        case = Case.objects.get(id = request.POST.get('case'))
        gpu = Graphics_Card.objects.get(id =request.POST.get('gpu')) 
        psu = Power_Supply_Unit.objects.get(id = request.POST.get('psu'))
        lcs = Liquid_Cooling_System.objects.get(id = request.POST.get('cooling'))
        total_price = int(kb.price + ram.price + monitor.price + ssd.price  + processor.price + mouse.price + gpu.price  + psu.price  + lcs.price + case.price)
        b = Build.objects.create(user = request.user , Processor = processor , Mouse = mouse , Graphics_Card = gpu  , Keyboard = kb  , Ram = ram , Power_Supply_Unit=psu ,  Monitor=monitor ,  Harddisk=ssd  , Liquid_Cooling_System=lcs , Case = case , total_price=total_price)
    else:
        b = Build.objects.get(id=id)
        kb = b.Keyboard
        ram = b.Ram
        monitor = b.Monitor
        ssd = b.Harddisk
        processor = b.Processor
        mouse = b.Mouse
        gpu = b.Graphics_Card
        psu = b.Power_Supply_Unit
        lcs = b.Liquid_Cooling_System
        case = b.Case
        total_price =b.total_price
    

    print(psu)
    context  = {
        'keyboard' : kb , 
        'ram' :ram , 
        'monitor':monitor , 
        'ssd' : ssd , 
        'processor':processor , 
        'mouse'  : mouse  , 
        'gpu' : gpu , 
        'psu' : psu,
        'lcs':lcs,
        'case':case,
        'id': b.id ,
        'total_price':total_price
        
    }

    return render(request , 'product_links.html' , context)


def Homepage(request):
    return render(request , 'homepage.html')



def Login(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    else:
        if request.method=="POST":
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request , user)
                    return redirect('/home/')
                else:
                    messages.add_message(request, messages.ERROR, "Invalid credentials , Enter again", extra_tags="error")
                    return redirect('')
            else:
                messages.add_message(request, messages.ERROR, "Invalid credentials , Enter again", extra_tags="error")
                return redirect(request.path_info)
        else:
            form = AuthenticationForm(None)
            context = {
                'form':form , 
            }
            return render(request , 'login.html' , context)


def Logout(request):
    logout(request)
    return redirect('/')


def Register(request):
    if request.method=="POST":
        rform = RegistrationForm(request.POST)
        if rform.is_valid():
            username = rform.cleaned_data['username']
            password = rform.cleaned_data['password']
            first_name = rform.cleaned_data['first_name']
            last_name = rform.cleaned_data['last_name']
            email= rform.cleaned_data['email']
            u = User.objects.create_user(username=username, password = password , first_name= first_name  , last_name=last_name , email = email)
            u.save()
            messages.add_message(request, messages.SUCCESS, 'User Registered Successfully', extra_tags="success")
            return redirect('/')
        else:
            return redirect("/")

    else:
        rform = RegistrationForm(None)
        print("This is getting printed")
        context = {
            'rform':rform
        }
        return render(request , 'register.html' , context)



def Recent(request):
    all = Build.objects.all()
    recents = []
    for a in all:
        if a.user == request.user:
            pass
        else:
            recents.append(a)
    print(recents)
    context ={
        'recents':recents,
        'ref_count':Referrals.objects.filter(To=request.user).count()
    }
    return render(request , 'recent_buys.html' , context)




def Delete_Fav(request , id):
    Favourites.objects.get(id=id).delete()
    return redirect('/view_fav/')


def Refer(request , id):
    if request.method=="POST":
        username = request.POST.get('username')
        if User.objects.filter(username=username).exists():
            u = User.objects.filter(username=username)
            Referrals.objects.create(From = str(request.user) , To = u[0]  , Build = Build.objects.get(id =id))
            messages.success(request , 'Build reffered to the user')
            return redirect('/view_fav/')
        else:
            url = '/refer/'  +  id
            messages.error(request , 'No user found , enter another one')
            return redirect(url)     
    else:
        context = {
            'b': Build.objects.get(id = id)
        }
    return render(request , 'referrals.html' , context)


def View_Ref(request):
    Ref = Referrals.objects.filter(To= request.user)
    context = {
        'Ref':Ref
    }
    return render(request , 'view_referrals.html' , context)

def Delete_Ref(request , id):
    Referrals.objects.get(id=id).delete()
    return redirect('/view_ref/')