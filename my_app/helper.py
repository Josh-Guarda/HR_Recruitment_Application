from my_app import BARANGAY_DATA, MUNICIPALITY_DATA, PROVINCE_DATA
from wtforms.validators import ValidationError
    

def set_form_choices(form, user):
    # Set province choices - ensure consistent string type for all values
    form.prov_id.choices = [('', '-- Select Province --')] + sorted(
        [(str(p['provCode']), p['provDesc']) for p in PROVINCE_DATA],
        key=lambda x: x[1].lower()
    )
    
    # Debug: Print actual user values to verify what we're working with
    user_prov = str(user.prov_id) if user and user.prov_id is not None else ''
    user_munci = str(user.munci_id) if user and user.munci_id is not None else ''
    user_brgy = str(user.brgy_id) if user and user.brgy_id is not None else ''
    
    print(f"User ID: {user.id}, DB prov_id: {user.prov_id}, As string: {user_prov}")
    
    # Explicitly set form data based on user values
    form.prov_id.data = user_prov
    form.munci_id.data = user_munci
    form.brgy_id.data = user_brgy
    
    # Check if the user's province exists in the choices
    prov_exists = any(user_prov == code for code, _ in form.prov_id.choices if code)
    if not prov_exists and user_prov:
        print(f"Warning: User province {user_prov} not found in choices")
    
    # Set municipality choices based on selected province
    if user_prov:
        form.munci_id.choices = [('', '-- Select Municipality --')] + sorted(
            [(str(m['citymunCode']), m['citymunDesc']) for m in MUNICIPALITY_DATA if str(m['provCode']) == user_prov],
            key=lambda x: x[1].lower()
        )
        
        # Check if the user's municipality exists in the choices
        munci_exists = any(user_munci == code for code, _ in form.munci_id.choices if code)
        if not munci_exists and user_munci:
            print(f"Warning: User municipality {user_munci} not found in choices")
    else:
        form.munci_id.choices = [('', '-- Select Municipality --')]

    # Set barangay choices based on selected municipality
    if user_munci:
        form.brgy_id.choices = [('', '-- Select Barangay --')] + sorted(
            [(str(b['brgyCode']), b['brgyDesc']) for b in BARANGAY_DATA if str(b['citymunCode']) == user_munci],
            key=lambda x: x[1].lower()
        )
        
        # Check if the user's barangay exists in the choices
        brgy_exists = any(user_brgy == code for code, _ in form.brgy_id.choices if code)
        if not brgy_exists and user_brgy:
            print(f"Warning: User barangay {user_brgy} not found in choices")
    else:
        form.brgy_id.choices = [('', '-- Select Barangay --')]















# def set_form_choices(form, user):
    
#     # Set province choices
#     form.prov_id.choices = [('', '-- Select Province --')] + sorted(
#         [(str(p['provCode']), p['provDesc']) for p in PROVINCE_DATA],
#         key=lambda x: x[1].lower()
#     )
    
#     # Get the selected values, ensuring they're strings
#     selected_prov = form.prov_id.data or (str(user.prov_id) if user and user.prov_id else None)
#     selected_muni = form.munci_id.data or (str(user.munci_id) if user and user.munci_id else None)

#     # Set municipality choices based on selected province
#     if selected_prov:
#         form.munci_id.choices = [('', '-- Select Municipality --')] + sorted(
#             [(str(m['citymunCode']), m['citymunDesc']) for m in MUNICIPALITY_DATA if str(m['provCode']) == selected_prov],
#             key=lambda x: x[1].lower()
#         )
#     else:
#         form.munci_id.choices = [('', '-- Select Municipality --')]

#     # Set barangay choices based on selected municipality
#     if selected_muni:
#         form.brgy_id.choices = [('', '-- Select Barangay --')] + sorted(
#             [(str(b['brgyCode']), b['brgyDesc']) for b in BARANGAY_DATA if str(b['citymunCode']) == selected_muni],
#             key=lambda x: x[1].lower()
#         )
#     else:
#         form.brgy_id.choices = [('', '-- Select Barangay --')]
        
        
        

    
    
# def set_form_province(form,user):

#     # raise ValidationError(user.id)
#     form.prov_id.choices = [('', '-- Select Province --')] + sorted(
#         [(p['provCode'], p['provDesc']) for p in PROVINCE_DATA],
#         key=lambda x: x[1].lower()
#     )
#     return form.prov_id.choices
    

# def set_form_municipality(form,user):
#     # raise ValidationError(user.id)
#     if user.prov_id :
#         form.munci_id.choices = [('', '-- Select Municipality --')] + sorted(
#                 [(m['citymunCode'], m['citymunDesc']) for m in MUNICIPALITY_DATA if m['provCode'] == user.prov_id],
#                 key=lambda x: x[1].lower()
#             )
#         return form.munci_id.choices
#     else:
#         form.munci_id.choices = [('', '-- Select Municipality --')]
#         return form.munci_id.choices
        
# def set_form_barangay(form,user):
#     if user.munci_id :
#         form.brgy_id.choices = [('', '-- Select Barangay --')] + sorted(
#             [(b['brgyCode'], b['brgyDesc']) for b in BARANGAY_DATA if b['citymunCode'] == user.munci_id],
#             key=lambda x: x[1].lower()
#         )
#         return form.brgy_id.choices
#     else:
#         form.brgy_id.choices = [('', '-- Select Barangay --')]
#         return form.brgy_id.choices