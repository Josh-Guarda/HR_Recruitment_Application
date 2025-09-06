from my_app import BARANGAY_DATA, MUNICIPALITY_DATA, PROVINCE_DATA
from wtforms.validators import ValidationError
import os
from my_app.models import Users
import secrets
import string







# def validate_username(self, username_to_check):
#         user = Users.query.filter_by(username=username_to_check.data).first()
#         if user:
#             raise ValidationError('UserName Already exist! Please try different UserName.')
        

        
        
def validate_email_address(email_address_to_check):
    # Remove .data since we're passing a string directly
    email_address = Users.query.filter_by(email_address=email_address_to_check).first()
    if email_address:
        return 'Email Already exists! Please try a different Email Address.'
    return None  # Return None if email is valid


def validate_mobile_number(number_to_check):
        if not number_to_check.data.isdigit():
            raise ValidationError('Only numbers are allowed.')
        
        number_to_save = Users.query.filter_by(mobile_number=number_to_check.data).first()
        if number_to_save != number_to_save:
            raise ValidationError('Mobile number already exists.')
        
def validate_phone_number(number_to_check):
    if not number_to_check.data.isdigit():
        raise ValidationError('Only numbers are allowed.')

    number_to_save = Users.query.filter_by(phone_number=number_to_check.data).first()
    if number_to_save != number_to_save:
        raise ValidationError('Phone number already exists.')





# def get_users_search_results(search_term=None):
#     """
#     Fetches users from the database, optionally filtering by a search term.
#     Returns a list of User objects.
#     """
#     # Start with a base query
#     query = Users.query
    
#     # Apply filters if a search term is provided
#     if search_term and search_term.strip() != '':
#         search_filter = (
#             (Users.firstname.ilike(f"%{search_term}%")) |
#             (Users.lastname.ilike(f"%{search_term}%")) |
#             (Users.email_address.ilike(f"%{search_term}%"))
#         )   
#         query = query.filter(search_filter)

#     # Execute the query and return the results
#     return query.order_by(Users.firstname).all()


















def set_form_choices(form, user):
    
    print(f"Fetch user: {user}")
    # Set province choices
    form.prov_id.choices = [('', '-- Select Province --')] + sorted(
        [(str(p['provCode']), p['provDesc']) for p in PROVINCE_DATA],
        key=lambda x: x[1].lower()
    )
    
    # Get the selected values, ensuring they're strings
    selected_prov = form.prov_id.data or (str(user.prov_id) if user and user.prov_id else None)
    selected_muni = form.munci_id.data or (str(user.munci_id) if user and user.munci_id else None)
    
    # Set municipality choices based on selected province
    if selected_prov:
        form.munci_id.choices = [('', '-- Select Municipality --')] + sorted(
            [(str(m['citymunCode']), m['citymunDesc']) for m in MUNICIPALITY_DATA if str(m['provCode']) == selected_prov],
            key=lambda x: x[1].lower()
        )
    else:
        form.munci_id.choices = [('', '-- Select Municipality --')]

    # Set barangay choices based on selected municipality
    if selected_muni:
        form.brgy_id.choices = [('', '-- Select Barangay --')] + sorted(
            [(str(b['brgyCode']), b['brgyDesc']) for b in BARANGAY_DATA if str(b['citymunCode']) == selected_muni],
            key=lambda x: x[1].lower()
        )
    else:
        form.brgy_id.choices = [('', '-- Select Barangay --')]
        
        




#GENERATE RANDOM CHARACTER FOR GENERATE PASSWORD.
# def generate_random():
#     size = 6 
#     return os.urandom(size)

def generate_random():
    # Generate a more readable password
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(10))
    return password