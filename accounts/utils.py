import random
import string
from django.utils.text import slugify

def generate_password_from_name(first_name, last_name):

    return generate_username_from_name(first_name, last_name)

def generate_secure_password_from_name(first_name, last_name):
    """
    Generate a secure random password based on the user's name
    Format: [first_name][random_number][last_name_initial][random_chars]
    Example: john123S!x
    """
    # Get the first 3 letters of first name (lowercase)
    name_part = slugify(first_name)[:3].lower()
    
    # Generate a random number between 100-999
    random_number = random.randint(100, 999)
    
    # Get last name initial (uppercase)
    last_initial = last_name[0].upper() if last_name else 'X'
    
    # Generate random special characters
    special_chars = '!@#$%^&*'
    random_special = random.choice(special_chars)
    
    # Generate random lowercase letters
    random_letters = ''.join(random.choices(string.ascii_lowercase, k=2))
    
    # Combine all parts
    password = f"{name_part}{random_number}{last_initial}{random_special}{random_letters}"
    
    return password

def generate_secure_password(length=12):
    """
    Generate a secure random password with mixed characters
    """
    characters = string.ascii_letters + string.digits + '!@#$%^&*'
    password = ''.join(random.choices(characters, k=length))
    return password

def generate_username_from_name(first_name, last_name):
    """
    Generate a username from first and last name
    Format: firstname.lastname
    """
    username = f"{slugify(first_name)}.{slugify(last_name)}".lower()
    return username
