from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient, HealthRecord
from .forms import PatientForm, HealthForm

# Overview Page
def overview(request):
    return render(request, "overview.html")


# ---------- LOGIN (ANYONE CAN LOGIN) ----------
def login_view(request):
    error = None
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Only rule → password must contain special character
        special_chars = "!@#$%^&*()_+=-{}[]|:;'<>,.?/"
        if not any(ch in special_chars for ch in password):
            error = "Password must contain at least one special character (@,!,#, etc.)"
            return render(request, "login.html", {"error": error})

        # No authentication → direct allow
        request.session["logged_in"] = True  
        return redirect("dashboard")

    return render(request, "login.html", {"error": error})


# ---------- DASHBOARD ----------
def dashboard(request):
    if not request.session.get("logged_in"):
        return redirect("login")

    total_patients = Patient.objects.count()
    total_records = HealthRecord.objects.count()

    return render(request, "dashboard.html", {
        "total_patients": total_patients,
        "total_records": total_records
    })


# ---------- LOGOUT ----------
def logout_view(request):
    request.session.flush()
    return redirect("login")


# ---------- PATIENT LIST ----------
def patient_list(request):
    if not request.session.get("logged_in"):
        return redirect("login")

    search = request.GET.get("search", "")

    if search:
        patients = Patient.objects.filter(name__icontains=search) | \
                   Patient.objects.filter(contact__icontains=search) | \
                   Patient.objects.filter(gender__icontains=search)
    else:
        patients = Patient.objects.all()

    return render(request, "patient_list.html", {"patients": patients})





# ---------- ADD PATIENT ----------
def patient_add(request):
    if not request.session.get("logged_in"):
        return redirect("login")

    form = PatientForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("patient_list")

    return render(request, "patient_add.html", {"form": form})


# ---------- PATIENT DETAIL ----------
def patient_detail(request, pk):
    if not request.session.get("logged_in"):
        return redirect("login")

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

# ---------- DELETE PATIENT ----------
def patient_delete(request, pk):
    if not request.session.get("logged_in"):
        return redirect("login")

    patient = get_object_or_404(Patient, pk=pk)
    patient.delete()
    return redirect("patient_list")