from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoansForm
from .models import Loans

def home(request):
    loans = Loans.objects.all() 
    return render(request, "base.html", {'loans': loans})

def loans(request):
    form = LoansForm()
    if request.method == 'POST':
        form = LoansForm(request.POST)
        if form.is_valid():
            form.save()
            print("Redirecting to home...")
            return redirect('home')
    loans = Loans.objects.all()
    return render(request, "loans.html", {'loans': loans, 'form': form})

def update_loan(request, loan_id):
    if request.method == 'POST':
        loan = get_object_or_404(Loans, id=loan_id)
        loan.is_paid = 'is_paid' in request.POST
        loan.save()
    return redirect('home')
def delete_loan(request, loan_id):
    loan = get_object_or_404(Loans, id=loan_id)
    loan.delete()
    return redirect('home')
