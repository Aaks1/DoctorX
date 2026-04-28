from datetime import datetime, timedelta
from django.utils import timezone
from .models import Doctor, Availability, AppointmentSlot

def generate_appointment_slots(doctor, weeks=4):
    """
    Generate appointment slots for a doctor based on their weekly schedule
    for the specified number of weeks
    """
    # Get doctor's weekly availability
    availabilities = Availability.objects.filter(doctor=doctor, is_active=True)
    
    if not availabilities.exists():
        return 0  # No availability set for this doctor
    
    slots_created = 0
    start_date = timezone.now().date()
    
    # Generate slots for each week
    for week_offset in range(weeks):
        for day_offset in range(7):  # 0-6 for Monday to Sunday
            current_date = start_date + timedelta(days=week_offset * 7 + day_offset)
            
            # Get the day of week name
            day_name = current_date.strftime('%A').upper()
            
            # Check if doctor is available on this day
            day_availability = availabilities.filter(day_of_week=day_name).first()
            
            if day_availability:
                # Generate 30-minute slots for the available time range
                slots_created += generate_daily_slots(
                    doctor, current_date, 
                    day_availability.start_time, 
                    day_availability.end_time
                )
    
    return slots_created

def generate_daily_slots(doctor, date, start_time, end_time):
    """
    Generate 30-minute slots for a specific day
    """
    slots_created = 0
    current_time = datetime.combine(date, start_time)
    end_datetime = datetime.combine(date, end_time)
    
    # Generate 30-minute slots
    while current_time + timedelta(minutes=30) <= end_datetime:
        slot_start = current_time.time()
        slot_end = (current_time + timedelta(minutes=30)).time()
        
        # Create slot if it doesn't exist
        slot, created = AppointmentSlot.objects.get_or_create(
            doctor=doctor,
            date=date,
            start_time=slot_start,
            end_time=slot_end,
            defaults={'is_booked': False}
        )
        
        if created:
            slots_created += 1
        
        current_time += timedelta(minutes=30)
    
    return slots_created

def get_available_slots(doctor, weeks=4):
    """
    Get available slots for a doctor for the specified number of weeks
    Returns slots grouped by week and day
    """
    start_date = timezone.now().date()
    end_date = start_date + timedelta(weeks=weeks)
    
    available_slots = AppointmentSlot.objects.filter(
        doctor=doctor,
        date__gte=start_date,
        date__lte=end_date,
        is_booked=False
    ).order_by('date', 'start_time')
    
    # Group slots by week
    weeks_data = {}
    for slot in available_slots:
        week_num = (slot.date - start_date).days // 7
        if week_num not in weeks_data:
            weeks_data[week_num] = {}
        
        # Group by date within the week
        date_str = slot.date.strftime('%Y-%m-%d')
        if date_str not in weeks_data[week_num]:
            weeks_data[week_num][date_str] = []
        
        weeks_data[week_num][date_str].append(slot)
    
    return weeks_data

def clear_old_slots(doctor, days_to_keep=30):
    """
    Clear old slots that are beyond the specified number of days
    """
    cutoff_date = timezone.now().date() - timedelta(days=days_to_keep)
    
    deleted_count = AppointmentSlot.objects.filter(
        doctor=doctor,
        date__lt=cutoff_date
    ).delete()[0]
    
    return deleted_count

def refresh_doctor_slots(doctor, weeks=4):
    """
    Refresh all slots for a doctor - clear old slots and generate new ones
    """
    # Clear existing slots
    AppointmentSlot.objects.filter(doctor=doctor).delete()
    
    # Generate new slots
    return generate_appointment_slots(doctor, weeks)
