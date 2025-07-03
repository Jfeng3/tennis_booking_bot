#!/usr/bin/env python3
"""
Script to run Thursday 1PM tennis court booking locally
"""

import os
import sys
import time
import random
from datetime import datetime
from check_court_availability import book_court

def main():
    print(f'🎾 Thursday 1PM Tennis Court Booking (Local Run)')
    print(f'Started at: {datetime.now()}')
    print('='*60)
    
    # User info - you can modify these values or use environment variables
    user_info = {
        'first_name': os.environ.get('FIRST_NAME', 'Jason'),
        'last_name': os.environ.get('LAST_NAME', 'Feng'),
        'email': os.environ.get('EMAIL', 'jiefeng@jupiter-analytics.biz'),
        'times_per_week': os.environ.get('TIMES_PER_WEEK', '3-4 times per week'),
        'favorite_color': os.environ.get('FAVORITE_COLOR', 'Green'),
        'court_type': os.environ.get('COURT_TYPE', 'Tennis')
    }
    
    # Booking parameters
    days_ahead = 7
    preferred_time = '1:00 PM'
    
    print(f'Booking for: {user_info["first_name"]} {user_info["last_name"]}')
    print(f'Email: {user_info["email"]}')
    print(f'Days ahead: {days_ahead}')
    print(f'Preferred time: {preferred_time}')
    print('='*60)
    
    try:
        # Run the booking
        book_court(
            user_info=user_info,
            days_ahead=days_ahead,
            preferred_time=preferred_time,
            auto_submit=True
        )
        
        # Wait as specified
        wait_time = 10 * random.random()
        print(f'\nWaiting {wait_time:.2f} seconds...')
        time.sleep(wait_time)
        
        print('\n✅ Thursday 1PM booking completed successfully!')
        
    except Exception as e:
        print(f'\n❌ 1PM booking failed with error: {e}')
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()