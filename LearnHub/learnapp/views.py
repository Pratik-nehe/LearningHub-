from django.shortcuts import render,HttpResponse,redirect
from learnapp.models import *

from django.contrib.auth.models import User  # Correct model


from django.contrib.auth import authenticate,login,logout
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from datetime import date  # ✅ this line is required


#from .forms import *



def login_data(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('notes')  # Change 'home' to your actual landing page after login
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html', {
                'username': username
            })  # Optional: send back the username

    return render(request, 'login.html')


def video_detail(request, id):
    video = get_object_or_404(Video, id=id)
    return render(request, 'video_detail.html', {'video': video})

# def sample_viws(request):

#     return HttpResponse("<h1>welcome to django</h1>")



# def Index(request):
#     data={'firstname':'pratik','lastname':'nehe'}
#     da=gallery.objects.all()
#     return render(request,'index.html',context={'da':da}) 

# def nav(request):
#     return render(request,'nav.html')

def contact(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        bdata=chats.objects.create(name=name,email=email,
                                  message=message)
        bdata.save()
        return redirect('main')
    else:
        return render(request,'contact.html')
    

def index(request):
    
    
    v=Video.objects.all()
    p=exam.objects.all()
    return render(request,'index.html',context={'v':v ,'p':p}) 

def  home(request):
     return render(request ,'home.html' )

# def upload_video(request):
#     if request.method == 'POST':
#          title=request.POST['title']
#          video=request.FILES['video']
#          info=request.POST['info']
#          time=request.POST['time']
#          data=Video.objects.create(title=title,video=video ,info=info,time=time)
#          data.save()
#          return redirect('show')
#     else:
#          return render(request,'upload.html')
    
def nav(request):
    return render(request ,'nav.html')

def features(request):
    return render(request,'features.html')


@login_required(login_url='login')
def courses(request):
    v=Video.objects.all()
    p=exam.objects.all()
    return render(request,'courses.html',context={'v':v ,'p':p}) 

    

def aboute(request):
    profile_count = Profile.objects.count()
    notes_count = notes.objects.count()
    exam_count = exam.objects.count()
    video_count = Video.objects.count()
    team_members = Team.objects.all()

    print("DEBUG COUNTS:", profile_count, notes_count, exam_count, video_count)

    return render(request, 'aboute.html', {
        'profile_count': profile_count,
        'notes_count': notes_count,
        'exam_count': exam_count,
        'video_count': video_count,
        't': team_members,
    })

        

    
def footer(request):
    return render(request,'footer.html')



@login_required(login_url='login')
def note(request):
    n=notes.objects.all()
    return render(request, 'notes.html' , context={'n':n})

def pr(request):
    i= profileicon.objects.all()
    return render(request,'nav.html', context={'i':i})


    
# def show(request):
#     data=gallery.objects.all()
#     return render(request,'show.html',context={'data':data}) 


# def delete(request,id):
#     s=Employee.objects.get(id=id)
#     s.delete()
#     return redirect('show')

# def update(request,id):
#     u=Employee.objects.get(id=id)
#     if request.method == 'POST':
#         name=request.POST['name']
#         salary=request.POST['salary']
#         depname=request.POST['depname']
#         u.name=name
#         u.salary=salary
#         u.depname=depname
#         u.save()
#         return redirect(request,'show')

#     else:
#         return render(request ,'update.html',context={'u':u}) 

# def bupdate(request,id):
#     bu=book.objects.get(id=id)
#     if request.method == 'POST':
#         Title=request.POST['Title']
#         Author_name=request.POST['Author_name']
#         Price=request.POST['Price']
#         Publication_Date=request.POST['Publication_Date']
#         bu.Title=Title
#         bu.Author_name=Author_name
#         bu.Price=Price
#         bu.Publication_Date=Publication_Date
 
#         bu.save()
#         return redirect(request,'show')

#     else:
#         return render(request ,'bupdate.html',context={'bu':bu}) 
    
# def bdelete(request,id):
#     bd=book.objects.get(id=id)
#     bd.delete()
#     return redirect('show')

def show(request):
    v=Video.objects.all()
    return render(request,'show.html',context={'v':v}) 

# def form(request):
#     return render(request,'add.html')

def add(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        bdata=chats.objects.create(name=name,email=email,
                                  message=message)
        bdata.save()
        return redirect('vedio')
    else:
        return render(request,'add',context={'bdata':bdata})
    
# def upload(request):
#     if request.method == 'POST':
#         title=request.POST['title']
#         image=request.FILES['image']
#         data=gallery.objects.create(title=title,image=image)
#         data.save()
#         return redirect('show')
#     else:
#         return render(request,'upload.html')
    
# Replace with your actual model names and imports
# views.py
from django.shortcuts import render
from .models import Profile, notes, exam, Video, Team  # Ensure these are the actual model names

def users(request):
    profile_count = Profile.objects.count()
    notes_count = notes.objects.count()
    exam_count = exam.objects.count()
    video_count = Video.objects.count()
    team_members = Team.objects.all()

    print("DEBUG COUNTS:", profile_count, notes_count, exam_count, video_count)

    return render(request, 'aboute.html', {
        'profile_count': profile_count,
        'notes_count': notes_count,
        'exam_count': exam_count,
        'video_count': video_count,
        't': team_members,
    })

        


def out(request):
    logout(request)
    return redirect('main')

# def registration(request):
#     if request.method == 'POST' :
#         form=UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('loginpage')
#     else:
#         form=UserCreationForm()
#         return render(request,'register.html',context={'form':form})    
    
# def colleg(request):
#     if request.method == 'POST' :
#         form=CollegeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('loginpage')
#     else:
#         form=CollegeForm()

#         return render(request,'register.html',context={'form':form})



# def Llogin(request):
#     if request.method =='POST' :
#         email=request.POST['email']
#         password=request.POST['password']
#         user=authenticate(request,email=email,password=password)

#         if user is not None:
#             login(request,user)

#             return redirect('Llogin')
#         else:
#             messages.error(request,'invalid user name and passeorsd')
#             return render(request,'learn.html')


#     return render(request,'Llogin.html')


# @login_required(login_url='Llogin')    
# def learn(request):
#     return render(request,'learn.html')





# def upload_video(request):
#     if request.method == 'POST':
#         form = VedioForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('video_list')
#     else:
#         form = VedioForm()
#     return render(request, 'upload.html', {'form': form})

# def video_list(request):
#     videos = Vedio.objects.all()
#     return render(request, 'video_list.html', {'videos': videos})
# Create your views here.
from .forms import RegisterForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('main')  # Change to your home page URL name
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Change to your home page URL name
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


from django.shortcuts import render, redirect
from django import forms
from .models import Profile

# Form for Profile creation
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'title', 'bio', 'photo', 'email', 'github', 'linkedin']
@login_required(login_url='login')
def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile_success')  # Redirect after successful creation
    else:
        form = ProfileForm()
    return render(request, 'profile_form.html', {'form': form, 'action': 'Create'})
@login_required(login_url='login')
def profile_success(request):
    return render(request, 'profile_success.html')

@login_required(login_url='login')
def view_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login if not authenticated

    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None  # or redirect to a profile creation page

    return render(request, 'view_profile.html', {
        'profile': profile,
        'user': request.user
    })



from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserUpdateForm, ProfileUpdateForm

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm
@login_required(login_url='login')
def update_profile(request):
    user = request.user

    # Ensure profile exists or create one
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('view_profile')  # Replace with your profile page URL name
    else:
        user_form = UserUpdateForm(instance=user)
        profile_form = ProfileUpdateForm(instance=profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'update_profile.html', context)



def policy(request):
    return render(request ,'privacy_policy.html')


from django.shortcuts import render, redirect
from .models import Question, UserScore
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from reportlab.pdfgen import canvas  # for PDF certificate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from datetime import date
from .models import Question, UserScore

@login_required(login_url='login')
def quiz_view(request):
    questions = Question.objects.all()[:60]

    if request.method == 'POST':
        correct = 0
        for question in questions:
            user_answer = request.POST.get(str(question.id))
            if user_answer == question.correct_option:
                correct += 1

        passing_score =36
        score_obj, created = UserScore.objects.get_or_create(user=request.user)
        score_obj.score = correct
        score_obj.certificate_issued = (correct >= passing_score)
        score_obj.save()

        return redirect('quiz_result')

    return render(request, 'quiz.html', {'questions': questions})



@login_required(login_url='login')
def quiz_result(request):
    try:
        score_obj = UserScore.objects.get(user=request.user)
    except UserScore.DoesNotExist:
        return redirect('quiz')  # No score yet, redirect to quiz page

    return render(request, 'result.html', {
        'score': score_obj.score,
        'certificate_available': score_obj.certificate_issued  # <-- Use this name
    })

@login_required(login_url='login')
def generate_certificate(request):
    try:
        score_obj = UserScore.objects.get(user=request.user)
    except UserScore.DoesNotExist:
        return HttpResponse("Score not found.", status=404) # Return 404 for not found

    if not score_obj.certificate_issued:
        return HttpResponse("You haven't passed the quiz yet.", status=403) # Return 403 for forbidden

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'

    p = canvas.Canvas(response, pagesize=A4)
    width, height = A4

    # --- Colors and Fonts ---
    # Define a color palette for consistency
    PRIMARY_COLOR = colors.HexColor('#0056b3')  # Darker blue
    SECONDARY_COLOR = colors.HexColor('#007bff') # Lighter blue
    ACCENT_COLOR = colors.HexColor("#f5376d")   # Green for success
    TEXT_COLOR = colors.black
    LIGHT_GREY = colors.HexColor('#f0f0f0')     # For backgrounds/details

    # Register custom fonts if you have them (e.g., in static files)
    # from reportlab.pdfbase import pdfmetrics
    # from reportlab.pdfbase.ttfonts import TTFont
    # try:
    #     pdfmetrics.registerFont(TTFont('Montserrat-Bold', os.path.join(settings.STATIC_ROOT, 'fonts/Montserrat-Bold.ttf')))
    #     pdfmetrics.registerFont(TTFont('Montserrat-Regular', os.path.join(settings.STATIC_ROOT, 'fonts/Montserrat-Regular.ttf')))
    #     BODY_FONT = "Montserrat-Regular"
    #     HEADLINE_FONT = "Montserrat-Bold"
    # except Exception as e:
    #     print(f"Error loading custom fonts: {e}")
    #     BODY_FONT = "Helvetica"
    #     HEADLINE_FONT = "Helvetica-Bold"
    
    # For now, stick to standard fonts for broader compatibility
    BODY_FONT = "Helvetica"
    HEADLINE_FONT = "Helvetica-Bold"
    ITALIC_FONT = "Helvetica-Oblique"


    # --- Background and Watermark (Optional but highly recommended for UI) ---
    # You'd typically have a background image in your static files
    # For example, a light logo watermark or a decorative pattern.
    # Make sure the image path is correct.
    # BACKGROUND_IMAGE_PATH = os.path.join(settings.STATIC_ROOT, 'images/certificate_bg.png')
    # if os.path.exists(BACKGROUND_IMAGE_PATH):
    #     p.drawImage(BACKGROUND_IMAGE_PATH, 0, 0, width=width, height=height, mask='auto')
    # else:
    #     # Fallback: a simple light grey rectangle or pattern
    p.setFillColor(LIGHT_GREY)
    p.rect(0, 0, width, height, fill=1) # Fill the entire page with a light background

    # --- Borders and Decorative Elements ---
    # Use a more visually appealing border
    border_margin = 25
    p.setLineWidth(5)
    p.setStrokeColor(PRIMARY_COLOR)
    # Outer decorative border
    p.roundRect(border_margin, border_margin, width - 2 * border_margin, height - 2 * border_margin, 15, stroke=1, fill=0)

    # Inner decorative border (e.g., a dashed line or a different color)
    inner_border_margin = 40
    p.setLineWidth(2)
    p.setStrokeColor(SECONDARY_COLOR)
    p.setDash(1, 2) # Dashed line for inner border
    p.roundRect(inner_border_margin, inner_border_margin, width - 2 * inner_border_margin, height - 2 * inner_border_margin, 10, stroke=1, fill=0)
    p.setDash(1, 0) # Reset dash pattern

    # --- Certificate Header ---
    header_y = height - 100

    # Title
    p.setFont(HEADLINE_FONT, 42)
    p.setFillColor(PRIMARY_COLOR)
    p.drawCentredString(width / 2, header_y, "Certificate of Achievement")

    # Subtitle
    p.setFont(BODY_FONT, 20)
    p.setFillColor(TEXT_COLOR)
    p.drawCentredString(width / 2, header_y - 40, "This certificate is proudly presented to")

    # --- User Name ---
    name = request.user.get_full_name() or request.user.username
    p.setFont(HEADLINE_FONT, 36)
    p.setFillColor(ACCENT_COLOR) # Use accent color for the name
    p.drawCentredString(width / 2, header_y - 110, name) # Adjusted Y for better spacing

    # --- Achievement Message ---
    message_y = header_y - 170
    p.setFont(BODY_FONT, 18)
    p.setFillColor(TEXT_COLOR)
    p.drawCentredString(width / 2, message_y, "For successfully completing the quiz")
    p.drawCentredString(width / 2, message_y - 25, f"with an outstanding score of {score_obj.score} out of 60")

    # Add a little flourish/icon for achievement
    # You could draw a star or a checkmark if you have icons available
    # p.setFont("ZapfDingbats", 24)
    # p.setFillColor(ACCENT_COLOR)
    # p.drawCentredString(width / 2, message_y - 60, "✔")


    # --- Footer Information ---
    footer_y = 150 # Adjusted footer Y for more space
    
    # Organization Name/Motto
    p.setFont(ITALIC_FONT, 16)
    p.setFillColor(PRIMARY_COLOR)
    p.drawCentredString(width / 2, footer_y + 40, "LearnHub • Empowering Minds, Achieving Excellence")

    # Signature and Date Lines
    line_length = 200
    line_y = footer_y

    # Instructor Signature
    p.setStrokeColor(colors.black)
    p.setLineWidth(1)
    p.line(width / 2 - line_length / 2 - 100, line_y, width / 2 + line_length / 2 - 100, line_y)
    p.setFont(BODY_FONT, 12)
    p.setFillColor(TEXT_COLOR)
    p.drawCentredString(width / 2 - 100, line_y - 15, "Signature of Instructor")
    p.drawCentredString(width / 2 - 100, line_y - 30, "A. Certified Trainer") # Example name

    # Date
    p.line(width / 2 - line_length / 2 + 100, line_y, width / 2 + line_length / 2 + 100, line_y)
    p.drawCentredString(width / 2 + 100, line_y - 15, "Date of Issue")
    p.drawCentredString(width / 2 + 100, line_y - 30, date.today().strftime('%B %d, %Y'))

    # --- Finalize PDF ---
    p.showPage()
    p.save()

    return response
@login_required(login_url='login')
def generate_certificate_pdf(request):
    # Provide the certificate as a downloadable PDF
    try:
        score_obj = UserScore.objects.get(user=request.user)
    except UserScore.DoesNotExist:
        return HttpResponse("Score not found.")

    if not score_obj.certificate_issued:
        return HttpResponse("You haven't passed the quiz yet.")

    html_string = render_to_string('certificate.html', {
        'user': request.user,
        'score': score_obj.score,
        'date': date.today()
    })
    html = HTML(string=html_string)
    pdf_file = html.write_pdf()

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
    return response


@login_required(login_url='login')
def certificate_view(request):
    try:
        score_obj = UserScore.objects.get(user=request.user)
    except UserScore.DoesNotExist:
        return HttpResponse("Score not found.")

    if not score_obj.certificate_issued:
        return HttpResponse("You haven't passed the quiz yet.")

    return render(request, 'certificate.html', {
        'user': request.user,
        'score': score_obj.score,
        'date': date.today()
    })


@login_required(login_url='login')
def exam_list(request):
    exams = exam.objects.all()  # get all exam objects
    return render(request, 'exam_list.html', {'exams': exams})