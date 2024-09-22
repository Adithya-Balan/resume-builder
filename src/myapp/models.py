from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.core.exceptions import ValidationError
from django.urls import reverse
from multiselectfield import MultiSelectField

# Create your models here.

# Validation
def validate_numeric(value):
    if not value.isdigit():
        raise ValidationError("This fields contains only digit")
    if len(f'{value}') > 6 and len(f'{value}') <= 0  :
        raise ValidationError("This field must not exceed 6 characters.")
    
def validate_phone(value):
    if len(f'{value}') != 10:
        raise ValidationError("This Field must contain 10 characters.")
    
class userinfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='info')
    first_name = models.CharField(max_length=25)
    sur_name =  models.CharField(max_length=25)
    email = models.EmailField(max_length=254)
    city =  models.CharField(max_length=25) 
    country = models.CharField(max_length=25)
    pincode = models.CharField(validators=[
        validate_numeric,
        MinLengthValidator(1),
        MaxLengthValidator(6)
    ])
    phone = models.BigIntegerField(validators=[
        validate_phone,
    ]
    )
    career_objective = models.TextField(max_length=250, null=True)
    
class working_info(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="working_info_s")
    company_name = models.CharField(max_length=50)
    location = models.CharField(max_length=25)
    your_role = models.CharField(max_length=100)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    role_description = models.TextField(blank=True) 
    

    class Meta:
        verbose_name_plural = "working_info"

    # def get_absolute_url(self):
    #     return reverse("working_info_detail", kwargs={"pk": self.pk})


class education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="education_info")
    degree_list = {
        "SL": "Select",
        "HSD": "High school Diploma",
        "GED": "GED",
        "AOA": "Associate of Arts",
        "AOS": "Associate of science",
        "AAS": "Associate of Applied science",
        "BA": "Bachelor of Arts",
        "B.E": "Bachelor of Engineering",
        "BTECH": "Bachelor of Technology",
        "BBA": "BBA",
        "MS": "Master of Science",
        "MAA": "Master of Arts",
        "JD": "J.D",
        "MD": "M.D.",
        "PH.D": "PH.D.",
        "ND": "No Degree"
    }
    school_name = models.CharField(max_length=50)
    school_location = models.CharField(max_length=50)
    degree = models.CharField(max_length=5, choices=degree_list, default='SL')
    field_of_study = models.CharField(max_length=50, null=True)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    CGPA = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    
class skill(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='skills_info')
    LANGUAGES = [
    ('python', 'Python'),
    ('javascript', 'JavaScript'),
    ('typescript', 'TypeScript'),
    ('html', 'HTML'),
    ('css', 'CSS'),
    ('java', 'Java'),
    ('kotlin', 'Kotlin'),
    ('swift', 'Swift'),
    ('objective_c', 'Objective-C'),
    ('c', 'C'),
    ('cpp', 'C++'),
    ('csharp', 'C#'),
    ('ruby', 'Ruby'),
    ('php', 'PHP'),
    ('go', 'Go (Golang)'),
    ('rust', 'Rust'),
    ('perl', 'Perl'),
    ('r', 'R'),
    ('sql', 'SQL'),
]
    TECHNOLOGIES = [
    ('Django', 'Django'),
    ('react', 'React'),
    ('angular', 'Angular'),
    ('vue', 'Vue.js'),
    ('nodejs', 'Node.js'),
    ('express', 'Express.js'),
    ('rails', 'Ruby on Rails'),
    ('laravel', 'Laravel'),
    ('symfony', 'Symfony'),
    ('graphql', 'GraphQL'),
    ('firebase', 'Firebase'),
    ('postgresql', 'PostgreSQL'),
    ('mysql', 'MySQL'),
    ('sqlite', 'SQLite'),
    ('mongodb', 'MongoDB'),
    ('redis', 'Redis'),
    ('pytorch', 'PyTorch'),
    ('tensorflow', 'TensorFlow'),
    ('scikit_learn', 'Scikit-Learn'),
    ('pandas', 'Pandas'),
    ('numpy', 'NumPy'),
    ('opencv', 'OpenCV'),
]
    CORE_TOOLS = [
    ('git', 'Git'),
    ('bash', 'Bash'),
    ('powershell', 'PowerShell'),
    ('linux', 'Linux'),
    ('docker', 'Docker'),
    ('kubernetes', 'Kubernetes'),
    ('aws', 'AWS'),
    ('azure', 'Azure'),
    ('gcp', 'Google Cloud Platform'),
    ('terraform', 'Terraform'),
    ('ansible', 'Ansible'),
    ('jenkins', 'Jenkins'),
    ('circleci', 'CircleCI'),
    ('travisci', 'Travis CI'),
    ('selenium', 'Selenium'),
    ('cypress', 'Cypress'),
    ('pytest', 'Pytest'),
    ('unittest', 'UnitTest'),
    ('junit', 'JUnit'),
    ('vscode', 'VS Code'),
    ('intellij', 'IntelliJ IDEA'),
    ('eclipse', 'Eclipse IDE'),
    ('github_actions', 'GitHub Actions'),
    ('gitlab_ci', 'GitLab CI'),
    ('nginx', 'NGINX'),
    ('apache', 'Apache HTTP Server'),
]
    language = MultiSelectField(choices = LANGUAGES)
    technologies = MultiSelectField(choices = TECHNOLOGIES)
    core = MultiSelectField(choices = CORE_TOOLS)
  
class others(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='other_info')
    portfolio = models.CharField(blank=True)
    linked_in = models.CharField()
    github = models.CharField()
    leet_code = models.CharField()
    other_link = models.CharField(blank=True, null=True)
    projects = models.TextField(blank=True)
   
    

    
