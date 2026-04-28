from datetime import datetime, timedelta
from django.utils import timezone
from .models import Doctor, Availability, AppointmentSlot

class SlotGenerationService:
    """Service to generate appointment slots based on doctor availability"""
    
    SLOT_DURATION = 20  # minutes
    SLOT_GAP = 5  # minutes between slots
    
    @classmethod
    def generate_slots_for_availability(cls, availability, start_date, end_date):
        """
        Generate slots for a given availability period
        availability: Availability instance
        start_date: date object
        end_date: date object
        """
        slots_created = 0
        current_date = start_date
        
        while current_date <= end_date:
            # Check if current date matches the availability day
            day_name = current_date.strftime('%A').upper()
            if day_name == availability.day_of_week:
                # Generate slots for this day
                day_slots = cls._generate_daily_slots(availability, current_date)
                AppointmentSlot.objects.bulk_create(day_slots)
                slots_created += len(day_slots)
            
            current_date += timedelta(days=1)
        
        return slots_created
    
    @classmethod
    def _generate_daily_slots(cls, availability, date):
        """Generate slots for a specific day"""
        slots = []
        
        # Convert times to datetime objects for calculation
        start_datetime = datetime.combine(date, availability.start_time)
        end_datetime = datetime.combine(date, availability.end_time)
        
        current_time = start_datetime
        slot_number = 1
        
        while current_time + timedelta(minutes=cls.SLOT_DURATION) <= end_datetime:
            slot_end_time = current_time + timedelta(minutes=cls.SLOT_DURATION)
            
            slot = AppointmentSlot(
                doctor=availability.doctor,
                date=date,
                start_time=current_time.time(),
                end_time=slot_end_time.time(),
                is_booked=False
            )
            slots.append(slot)
            
            # Move to next slot with gap
            current_time = slot_end_time + timedelta(minutes=cls.SLOT_GAP)
            slot_number += 1
        
        return slots
    
    @classmethod
    def generate_slots_for_doctor(cls, doctor, start_date, end_date):
        """Generate slots for all availabilities of a doctor"""
        total_slots = 0
        availabilities = doctor.availabilities.filter(is_active=True)
        
        for availability in availabilities:
            slots = cls.generate_slots_for_availability(availability, start_date, end_date)
            total_slots += slots
        
        return total_slots
    
    @classmethod
    def clear_existing_slots(cls, doctor, start_date, end_date):
        """Clear existing slots for a doctor in date range"""
        return AppointmentSlot.objects.filter(
            doctor=doctor,
            date__gte=start_date,
            date__lte=end_date
        ).delete()
