from my_app import BARANGAY_DATA, MUNICIPALITY_DATA, PROVINCE_DATA
from wtforms.validators import ValidationError
    

def set_form_choices(form, user):
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
        
        
        