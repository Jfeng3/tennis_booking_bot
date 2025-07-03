#!/bin/bash
# Setup local cron job for daily 4PM tennis court booking

# Get the absolute path to the project directory
PROJECT_DIR="/Users/jiefeng/WebstormProjects/tennis_booking"
PYTHON_PATH=$(which python3)

# Create log directory
mkdir -p "$PROJECT_DIR/logs"

# Cron entry for daily 4:01 PM PST/PDT
CRON_ENTRY="1 16 * * * cd $PROJECT_DIR && $PYTHON_PATH scripts/run_daily_4pm_booking.py >> logs/daily_4pm_booking.log 2>&1"

echo "Setting up cron job for daily 4PM tennis court booking..."
echo "Cron entry: $CRON_ENTRY"

# Add to crontab
(crontab -l 2>/dev/null; echo "$CRON_ENTRY") | crontab -

echo "✅ Cron job added successfully!"
echo ""
echo "The booking will run daily at 4:01 PM with visible browser window."
echo "Logs will be saved to: $PROJECT_DIR/logs/daily_4pm_booking.log"
echo ""
echo "To check your cron jobs: crontab -l"
echo "To remove this cron job: crontab -e (then delete the line)"
echo "To view logs: tail -f $PROJECT_DIR/logs/daily_4pm_booking.log"