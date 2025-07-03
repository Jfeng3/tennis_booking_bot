#!/bin/bash

echo "🎾 Tennis Court Booking Daily Scheduler Setup"
echo "==========================================="

# Install schedule library if not installed
echo "📦 Checking dependencies..."
pip3 install schedule playwright

# Make the scheduler executable
chmod +x daily_scheduler.py

echo -e "\n🚀 Starting Options:"
echo "1. Run in foreground (for testing):"
echo "   python3 daily_scheduler.py"
echo ""
echo "2. Run in background:"
echo "   nohup python3 daily_scheduler.py > scheduler.log 2>&1 &"
echo ""
echo "3. Run with screen (recommended):"
echo "   screen -dmS tennis_booking python3 daily_scheduler.py"
echo "   To view: screen -r tennis_booking"
echo "   To detach: Ctrl+A then D"
echo ""

read -p "Start scheduler now? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
    echo "Starting scheduler in screen session..."
    screen -dmS tennis_booking python3 daily_scheduler.py
    echo "✅ Scheduler started in screen session 'tennis_booking'"
    echo "View with: screen -r tennis_booking"
fi