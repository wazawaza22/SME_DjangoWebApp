from django.shortcuts import render, redirect
from django.db.models import Count
from .models import Student



def student_create(request):
    if request.method == "POST":
        student_name = request.POST.get("student_name")
        program = request.POST.get("program")
        student.year_level = request.POST.get("year_level")
        email = request.POST.get("email")
        Student.objects.create(
            student_name=student_name,
            program=program,
            year_level=year_level,
            email=email
        )
        return redirect("student_list")
    
    return render(request, "registration/student_form.html")  # ✅ SHOWS the form!



def student_list(request):
    students = Student.objects.all()
    return render(request, "student_list.html", {"students": students})



def student_update(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == "POST":
        student.student_name = request.POST.get("student_name")
        student.program = request.POST.get("program")
        student.year_level = request.POST.get("year_level")
        student.email = request.POST.get("email")
        student.save()
        return redirect("student_list")
    return render(request, "registration/student_form.html", {"student": student})



def student_delete(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == "POST":
        student.delete()
        return redirect("student_list")
    return render(request, "registration/student_confirm_delete.html", {"student": student})



def student_dashboard(request):
    students = Student.objects.all()
    total_students = students.count()

    program_summary = (
        students
        .values('program')
        .annotate(total=Count('id'))
        .order_by('program')
    )

    year_summary = (
        students
        .values('year_level')
        .annotate(total=Count('id'))
        .order_by('year_level')
    )

    return render(
        request,
        'registration/student_dashboard.html',
        {
            'total_students': total_students,
            'program_summary': program_summary,
            'year_summary': year_summary,
        }
    )