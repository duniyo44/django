from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    enrolled_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    #read

    students = Student.objects.all()
    
    #updating
    student = Student.objects.get(id=1)
    student.first_name = "Jonathan"
    student.save()

#deleting
student = Student.objects.get(id=1)
student.delete()




    class Lab(models.Model):
        lab_name = models.CharField(max_length=100)
    lab_number = models.IntegerField()
    capacity = models.IntegerField()
    
    def __str__(self):
        return self.lab_name


lab = Lab.objects.get(id=1)
lab.teacher_in_charge = None
lab.save()



    




    class Teacher(models.Model):
        first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

#deleting
 Teacher.objects.filter(hire_date__lt="2015-01-01").delete()






student = Student.objects.create(
    first_name="ubah",
    last_name="jama",
    email="hamdaff27@gmail.com",
    date_of_birth="2000-05-15"
)


teacher = Teacher.objects.create(
    first_name="hamda",
    last_name="mohamed",
    email="hamdaff27@gmail.com",
    hire_date="2020-08-01"
)


lab = Lab.objects.create(
    lab_name="Physics Lab",
    lab_number=101,
    capacity=30,
    teacher_in_charge=teacher
)


