from playwright.sync_api import sync_playwright, Page
from datetime import datetime, timedelta
import time
import random
from fill_booking_form import fill_and_submit_booking

def normalize_text(text):
    """Normalize text by removing extra whitespaces"""
    return ' '.join(text.strip().split())

def find_dates(page: Page):
    """Find all dates displayed on the page"""
    date_containers = page.query_selector_all('div.css-flfhzc')
    dates = []

    for container in date_containers:
        label = container.query_selector('p.css-1jk5q58')
        day = container.query_selector('p.css-fd79o')
        date = container.query_selector('p.css-r0fex2')

        if label and day and date:
            dates.append({
                'label': normalize_text(label.inner_text()),
                'day': normalize_text(day.inner_text()),
                'date': normalize_text(date.inner_text()),
                'element': date  # Keep reference to the element for clicking
            })

    return dates

def find_timeslots_for_date(page: Page, date_label=None):
    """Find all available timeslots"""
    timeslot_buttons = page.query_selector_all('button.time-selection')
    timeslots = []

    for button in timeslot_buttons:
        aria_label = button.get_attribute('aria-label')
        time_text = button.query_selector('p.css-1j0qzde')

        if aria_label and 'Available Timeslot' in aria_label and time_text:
            timeslots.append({
                'time': normalize_text(time_text.inner_text()),
                'button': button  # Keep reference for clicking
            })

    return timeslots

def find_next_button(page: Page):
    """Find the 'Next' button by looking for the specific SVG path"""
    main_element = page.query_selector('main')
    if not main_element:
        return None
    
    buttons = main_element.query_selector_all('button')
    for btn in buttons:
        svg_path = btn.query_selector('svg path')
        if svg_path:
            d_attr = svg_path.get_attribute('d')
            if d_attr == "M6.25 4H9l7 7-7 7H6.25l7-7-7-7z":
                return btn
    
    return None

def book_court(user_info: dict, days_ahead: int = 6, preferred_time: str = '1:00 PM', auto_submit: bool = True):
    with sync_playwright() as p:
        # Launch browser - headless in CI, visible locally
        import os
        headless = os.environ.get('CI') == 'true'
        browser = p.chromium.launch(headless=headless)
        page = browser.new_page()
        
        try:
            # Navigate to the booking page
            print('Navigating to booking page...')
            page.goto('https://app.acuityscheduling.com/schedule/88825638/appointment/15247850/calendar/any')
            
            # Wait for date elements to load
            page.wait_for_selector('p.css-r0fex2', timeout=10000)
            
            # Calculate target date
            target_date = datetime.now() + timedelta(days=days_ahead)
            target_day = target_date.day
            target_month = target_date.strftime('%b')  # Short month format (Jan, Feb, Mar, etc.)
            target_year = target_date.year
            
            # Format target date as 'Jul 6' or 'Jul 10'
            target_date_str = f'{target_month} {target_day}'
            print(f'Looking for date: {target_date_str}, {target_year}')
            
            found_date = False
            attempts = 0
            max_attempts = 10
            
            while not found_date and attempts < max_attempts:
                # Get all date elements
                date_elements = page.query_selector_all('p.css-r0fex2')
                dates = [el.text_content().strip() for el in date_elements]
                
                print('Available dates:', dates)
                
                # Check if target date is in the list
                found_date = target_date_str in dates
                
                if found_date:
                    print('✅ Found the date!')
                    
                    # Get available timeslots for the found date
                    timeslots = find_timeslots_for_date(page, target_date_str)
                    print(f'\nAvailable timeslots for {target_date_str}:')
                    if timeslots:
                        for slot in timeslots:
                            print(f"  - {slot['time']}")
                        
                        # Look for 4pm timeslot and click it
                        found_1pm = False
                        for slot in timeslots:
                            if preferred_time in slot['time']:
                                print(f"\n🎯 Found {preferred_time} slot! Clicking on {slot['time']}...")
                                slot['button'].click()
                                # Wait after clicking timeslot
                                time.sleep(3 * random.random())
                                found_1pm = True
                                break
                        
                        if not found_1pm:
                                print(f'\n⚠️  No {preferred_time} timeslot found')
                        else:
                            # Wait for booking form to load
                            time.sleep(2)
                            try:
                                print('\n📝 Filling booking form...')
                                fill_and_submit_booking(page, user_info, auto_submit=True)
                            except Exception as e:
                                print(f'❌ Error filling form: {e}')
                    else:
                        print('  No timeslots available')
                    break
                else:
                    print('Date not found, checking for "More Times" button...')
                    
                    # Look for "More Times" button
                    next_button = find_next_button(page)
                    
                    if next_button:
                        print('Clicking "More Times" button...')
                        next_button.click()
                        
                        # Wait for new dates to load
                        time.sleep(3 * random.random())
                        attempts += 1
                    else:
                        print('No "More Times" button found. Target date may not be available.')
                        break
            
            if not found_date:
                print('❌ Could not find the target date after checking all available dates.')
            
            # Keep browser open for manual inspection
            print('Script complete. Press Enter to close browser...')
            
        except Exception as error:
            print(f'Error occurred: {error}')
        finally:
            browser.close()

if __name__ == "__main__":
    book_court(user_info={
        'first_name': 'Jason',
        'last_name': 'Feng',
        'email': 'jiefeng@jupiter-analytics.biz',
        'times_per_week': '3-4 times per week',
        'favorite_color': 'Green',
        'court_type': 'Tennis'
    }, days_ahead=6, preferred_time='12:00 PM', auto_submit=True)
    time.sleep(10*random.random())