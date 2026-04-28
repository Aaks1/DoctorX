#!/usr/bin/env python3
import secrets
from django.core.management.utils import get_random_secret_key

# Generate a strong secret key
secret_key = get_random_secret_key()
print(f"SECRET_KEY={secret_key}")
print("\nCopy this SECRET_KEY and add it to your Vercel environment variables.")
