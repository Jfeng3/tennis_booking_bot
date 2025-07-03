from playwright.sync_api import Page
import pdb
import time
import random

def fill_and_submit_booking(page: Page, user_info: dict, auto_submit: bool = True):
    """
    Fill in the tennis court booking form and optionally submit it.
    
    Args:
        page: Playwright page object
        user_info: Dictionary containing user information with keys:
            - first_name: str
            - last_name: str
            - phone: str (optional)
            - email: str
            - times_per_week: str (answer to bot prevention question)
            - favorite_color: str (answer to bot prevention question)
            - court_type: str (Tennis or Pickleball)
        auto_submit: If True, automatically clicks the Confirm Appointment button (default: True)
    """
    try:
        # Fill First Name
        first_name_input = page.locator('#client\\.firstName')
        first_name_input.fill(user_info.get('first_name', ''))
        print(f"✅ First name filled: {user_info.get('first_name', '')}")
        
        # Fill Last Name
        last_name_input = page.locator('#client\\.lastName')
        last_name_input.fill(user_info.get('last_name', ''))
        print(f"✅ Last name filled: {user_info.get('last_name', '')}")
        
        # Fill Phone (optional)
        if 'phone' in user_info:
            phone_input = page.locator('#client\\.phone')
            phone_input.clear()  # Clear the default +1
            phone_input.fill(user_info['phone'])
            print(f"✅ Phone filled: {user_info['phone']}")
        
        # Fill Email
        email_input = page.locator('#client\\.email')
        email_input.fill(user_info.get('email', ''))
        print(f"✅ Email filled: {user_info.get('email', '')}")
        
        # Bot Prevention Questions
        # Question 1: How many times a week are you on the courts?
        times_per_week = page.locator('#fields\\[field-15042433\\]')
        times_per_week.fill(user_info.get('times_per_week', '3-4 times per week'))
        print(f"✅ Times per week filled: {user_info.get('times_per_week', '3-4 times per week')}")
        
        # Question 2: What is your favorite color?
        favorite_color = page.locator('#fields\\[field-15042441\\]')
        favorite_color.fill(user_info.get('favorite_color', 'Green'))
        print(f"✅ Favorite color filled: {user_info.get('favorite_color', 'Green')}")
        
        # Tennis or Pickleball dropdown
        # First find the dropdown button by its aria-labelledby attribute
        court_type_dropdown = page.locator('[aria-labelledby="fields[field-14027630]-label"]')
        
        # Click the dropdown to open it
        print("📋 Opening court type dropdown...")
        court_type_dropdown.click()
        
        # Wait after clicking dropdown (1 * random seconds)
        wait_time = 1 * random.random()
        print(f"⏳ Waiting {wait_time:.2f} seconds after dropdown click...")
        time.sleep(wait_time)
        
        # Select the court type (Tennis or Pickleball)
        court_type = user_info.get('court_type', 'Tennis')
        
        # Look for the option in the dropdown list
        option = page.locator(f'li:has-text("{court_type}")').first
        if not option.is_visible():
            # Fallback: try different selector
            option = page.locator(f'text="{court_type}"').first
            
        option.click()
        print(f"✅ Court type selected: {court_type}")
        
        # Wait after clicking option (3 * random seconds)
        wait_time = 3 * random.random()
        print(f"⏳ Waiting {wait_time:.2f} seconds after option click...")
        time.sleep(wait_time)
        
        print("✅ Form filled successfully!")
        
        # Find the confirm button
        confirm_button = page.locator('button:has-text("Confirm Appointment")')
        
        if auto_submit:
            print("🎯 Clicking Confirm Appointment button...")
            confirm_button.click()
            
            # Wait after clicking confirm button (3 * random seconds)
            wait_time = 3 * random.random()
            print(f"⏳ Waiting {wait_time:.2f} seconds after confirm button click...")
            time.sleep(wait_time)
            
            print("✅ Appointment confirmed!")
        else:
            print("ℹ️  Form filled. Click 'Confirm Appointment' button to submit.")
            
        return confirm_button
        
    except Exception as e:
        print(f"❌ Error filling form: {e}")
        raise


# Example usage:
if __name__ == "__main__":
    # Example user information
    sample_user = {
        'first_name': 'Jason',
        'last_name': 'Feng',
        'email': 'jiefeng@jupiter-analytics.com',
        'times_per_week': '2-3 times per week',
        'favorite_color': 'Blue',
        'court_type': 'Tennis'
    }
    
    # Usage in your script:
    # fill_booking_form(page, sample_user)
    # or
    # fill_and_submit_booking(page, sample_user, auto_submit=True)