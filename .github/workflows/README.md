# GitHub Actions Tennis Court Booking Setup

Three separate workflows handle automatic tennis court booking:

1. **Daily 4PM Booking** - Runs every day at 4:01 PM PST/PDT for 4:00 PM slots
2. **Wednesday 5PM Booking** - Runs every Wednesday at 5:01 PM PST/PDT for 5:00 PM slots
3. **Thursday 1PM Booking** - Runs every Thursday at 1:01 PM PST/PDT for 1:00 PM slots

## Setup Instructions

### 1. Set Up GitHub Secrets (Recommended for Privacy)

Go to your repository Settings → Secrets and variables → Actions, and add these secrets:

- `FIRST_NAME`: Your first name (e.g., Jason)
- `LAST_NAME`: Your last name (e.g., Feng)
- `EMAIL`: Your email address
- `TIMES_PER_WEEK`: Answer for bot prevention (e.g., "3-4 times per week")
- `FAVORITE_COLOR`: Answer for bot prevention (e.g., "Green")
- `COURT_TYPE`: Tennis or Pickleball

### 2. Schedule Information

**Daily 4PM Booking:**
- Runs every day at 4:01 PM Pacific Time
- Books 4:00 PM court slots

**Wednesday 5PM Booking:**
- Runs every Wednesday at 5:01 PM Pacific Time  
- Books 5:00 PM court slots

**Thursday 1PM Booking:**
- Runs every Thursday at 1:01 PM Pacific Time
- Books 1:00 PM court slots

All schedules automatically adjust for daylight saving time:
- During PDT (March-November): Adjusted UTC times
- During PST (November-February): Adjusted UTC times

### 3. Manual Testing

You can manually trigger the workflow:
1. Go to Actions tab in your repository
2. Select "Daily Tennis Court Booking"
3. Click "Run workflow"
4. Optionally adjust parameters
5. Click "Run workflow" button

### 4. Monitor Runs

- Check the Actions tab to see run history
- Failed runs will be marked with a red X
- Successful runs will have a green checkmark
- Click on any run to see detailed logs

### 5. Notifications

To get notified of booking results:
1. Go to Settings → Notifications
2. Enable workflow run notifications
3. You'll get emails for failed runs

## Cron Schedule Format

The cron format is: `minute hour day month weekday`
- `1 16 * * *` = 1st minute of 16th hour (4:01 PM) every day

## Troubleshooting

- If the action fails, check the logs in the Actions tab
- Ensure all secrets are properly set
- Verify the browser installation steps complete successfully
- Check that the booking page hasn't changed its structure