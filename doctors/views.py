from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.utils import timezone
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from datetime import timedelta
from .models import Doctor, Availability, AppointmentSlot
from .forms import DoctorForm, AvailabilityForm, SlotGenerationForm
from .services import SlotGenerationService

def is_admin(user):
    return user.is_authenticated and user.is_staff

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    """Main admin dashboard"""
    context = {
        'total_doctors': Doctor.objects.filter(is_active=True).count(),
        'total_appointments': AppointmentSlot.objects.filter(is_booked=True).count(),
        'total_available_slots': AppointmentSlot.objects.filter(is_booked=False, date__gte=timezone.now().date()).count(),
        'recent_appointments': AppointmentSlot.objects.filter(is_booked=True).order_by('-date')[:10],
    }
    return render(request, 'admin/dashboard.html', context)

class DoctorListView(ListView):
    """List all doctors"""
    model = Doctor
    template_name = 'admin/doctors/list.html'
    context_object_name = 'doctors'
    paginate_by = 20
    
    def get_queryset(self):
        return Doctor.objects.all().order_by('first_name', 'last_name')

class DoctorCreateView(CreateView):
    """Create new doctor"""
    model = Doctor
    form_class = DoctorForm
    template_name = 'admin/doctors/form.html'
    success_url = reverse_lazy('admin:doctors')
    
    def form_valid(self, form):
        messages.success(self.request, f'Dr. {form.instance.first_name} {form.instance.last_name} created successfully!')
        return super().form_valid(form)

class DoctorUpdateView(UpdateView):
    """Update doctor"""
    model = Doctor
    form_class = DoctorForm
    template_name = 'admin/doctors/form.html'
    success_url = reverse_lazy('admin:doctors')
    
    def form_valid(self, form):
        messages.success(self.request, f'Dr. {form.instance.first_name} {form.instance.last_name} updated successfully!')
        return super().form_valid(form)

class DoctorDeleteView(DeleteView):
    """Delete doctor"""
    model = Doctor
    template_name = 'admin/doctors/confirm_delete.html'
    success_url = reverse_lazy('admin:doctors')
    
    def delete(self, request, *args, **kwargs):
        doctor = self.get_object()
        messages.success(request, f'Dr. {doctor.first_name} {doctor.last_name} deleted successfully!')
        return super().delete(request, *args, **kwargs)

@login_required
@user_passes_test(is_admin)
def manage_schedules(request):
    """Manage doctor schedules"""
    doctors = Doctor.objects.filter(is_active=True)
    availabilities = Availability.objects.select_related('doctor').order_by('doctor__first_name', 'day_of_week')
    
    context = {
        'doctors': doctors,
        'availabilities': availabilities,
    }
    return render(request, 'admin/schedules/list.html', context)

@login_required
@user_passes_test(is_admin)
def create_availability(request, doctor_id):
    """Create availability for a doctor"""
    doctor = get_object_or_404(Doctor, id=doctor_id)
    
    if request.method == 'POST':
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            availability = form.save(commit=False)
            availability.doctor = doctor
            availability.save()
            messages.success(request, f'Availability created for Dr. {doctor.first_name} {doctor.last_name}')
            return redirect('admin:schedules')
    else:
        form = AvailabilityForm()
    
    context = {
        'form': form,
        'doctor': doctor,
    }
    return render(request, 'admin/schedules/form.html', context)

@login_required
@user_passes_test(is_admin)
def generate_slots(request):
    """Generate appointment slots"""
    if request.method == 'POST':
        form = SlotGenerationForm(request.POST)
        if form.is_valid():
            doctor = form.cleaned_data['doctor']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            
            # Clear existing slots
            cleared = SlotGenerationService.clear_existing_slots(doctor, start_date, end_date)
            
            # Generate new slots
            slots_created = SlotGenerationService.generate_slots_for_doctor(doctor, start_date, end_date)
            
            messages.success(
                request, 
                f'Cleared {cleared} existing slots and generated {slots_created} new slots '
                f'for Dr. {doctor.first_name} {doctor.last_name}'
            )
            return redirect('admin:slots')
    else:
        form = SlotGenerationForm()
    
    return render(request, 'admin/slots/generate.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def manage_slots(request):
    """Manage appointment slots"""
    slots = AppointmentSlot.objects.select_related('doctor').order_by('-date', 'start_time')
    
    # Filter by date range if provided
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')
    doctor_filter = request.GET.get('doctor')
    
    if date_from:
        slots = slots.filter(date__gte=date_from)
    if date_to:
        slots = slots.filter(date__lte=date_to)
    if doctor_filter:
        slots = slots.filter(doctor_id=doctor_filter)
    
    context = {
        'slots': slots,
        'doctors': Doctor.objects.filter(is_active=True),
        'filters': {
            'date_from': date_from,
            'date_to': date_to,
            'doctor': doctor_filter,
        }
    }
    return render(request, 'admin/slots/list.html', context)

@login_required
@user_passes_test(is_admin)
def manage_appointments(request):
    """Manage all appointments"""
    from appointments.models import Appointment
    
    appointments = Appointment.objects.select_related('patient', 'slot__doctor').order_by('-created_at')
    
    context = {
        'appointments': appointments,
    }
    return render(request, 'admin/appointments/list.html', context)
