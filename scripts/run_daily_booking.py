#!/usr/bin/env python3
"""
Daily booking script to be run by cron at 4pm
Add to crontab with: crontab -e
Then add this line: 0 16 * * * /usr/bin/python3 /path/to/tennis_booking/scripts/run_daily_booking.py
"""

import sys
import os
import time
import random
from datetime import datetime

# Add the scripts directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from check_court_availability import book_court

def main():
    print(f"\n{'='*60}")
    print(f"🎾 Running daily booking at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}\n")
    
    # Run the booking job
    book_court(user_info={
        'first_name': 'Jason',
        'last_name': 'Feng',
        'email': 'jiefeng@jupiter-analytics.biz',
        'times_per_week': '3-4 times per week',
        'favorite_color': 'Green',
        'court_type': 'Tennis'
    }, days_ahead=6, preferred_time='4:00 PM', auto_submit=True)
    
    time.sleep(10 * random.random())
    
    print(f"\n✅ Daily booking completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()