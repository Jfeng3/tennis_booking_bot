#!/usr/bin/env python3
"""
Simple Python cron job to run tennis court booking at 4:01 PM daily
Run this script in the background: python3 daily_scheduler.py &
Or use nohup: nohup python3 daily_scheduler.py > scheduler.log 2>&1 &
"""

import schedule
import time
import random
from datetime import datetime
import sys
import os

# Add scripts directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from check_court_availability import book_court

def run_booking():
    """Run the booking job at 4:01 PM"""
    print(f"\n{'='*60}")
    print(f"🎾 Running daily booking at {datetime.now()}")
    print(f"{'='*60}\n")
    
    try:
        book_court(user_info={
            'first_name': 'Jason',
            'last_name': 'Feng',
            'email': 'jiefeng@jupiter-analytics.biz',
            'times_per_week': '3-4 times per week',
            'favorite_color': 'Green',
            'court_type': 'Tennis'
        }, days_ahead=6, preferred_time='4:00 PM', auto_submit=True)
        
        time.sleep(10 * random.random())
        
        print(f"\n✅ Booking completed at {datetime.now()}")
    except Exception as e:
        print(f"\n❌ Booking failed: {e}")

# Schedule the job for 4:01 PM daily
schedule.every().day.at("16:01").do(run_booking)

print("🎾 Tennis Court Booking Scheduler Started")
print(f"⏰ Will run daily at 4:01 PM")
print(f"📅 Current time: {datetime.now()}")
print(f"⏳ Next run: {schedule.next_run()}")
print("\nPress Ctrl+C to stop\n")

# Keep running
while True:
    try:
        schedule.run_pending()
        time.sleep(30)  # Check every 30 seconds
    except KeyboardInterrupt:
        print("\n🛑 Scheduler stopped")
        break