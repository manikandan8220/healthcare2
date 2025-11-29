from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Patient, HealthRecord
from .forms import PatientForm, HealthForm


# Overview Page
def overview(request):
    return render(request, "overview.html")


# Login
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})
    return render(request, "login.html")


# Logout
@login_required
def logout_view(request):
    logout(request)
    return redirect("login")


# Dashboard
@login_required
def dashboard(request):
    total_patients = Patient.objects.count()
    total_records = HealthRecord.objects.count()
    return render(request, "dashboard.html", {
        "total_patients": total_patients,
        "total_records": total_records
    })


# List Patients
@login_required
def patient_list(request):
    search = request.GET.get("search", "")
    if search:
        patients = Patient.objects.filter(name__icontains=search) | \
                   Patient.objects.filter(contact__icontains=search) | \
                   Patient.objects.filter(gender__icontains=search)
    else:
        patients = Patient.objects.all()
    return render(request, "patient_list.html", {"patients": patients})


# Add Patient
@login_required
def patient_add(request):
    form = PatientForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("patient_list")
    return render(request, "patient_add.html", {"form": form})


# Patient Detail & Add Health Record
@login_required
def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    records = HealthRecord.objects.filter(patient=patient).order_by('-updated_at')
    form = HealthForm()

    if request.method == "POST":
        form = HealthForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.patient = patient
            record.save()
            return redirect("patient_detail", pk=pk)

    return render(request, "patient_detail.html", {
        "patient": patient,
        "records": records,
        "form": form
    })
