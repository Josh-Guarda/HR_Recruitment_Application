from my_app import BARANGAY_DATA, MUNICIPALITY_DATA, PROVINCE_DATA
    
    
    
    
    
def set_form_choices(form, user=None):
    form.prov_id.choices = [('', '-- Select Province --')] + sorted(
        [(p['provCode'], p['provDesc']) for p in PROVINCE_DATA],
        key=lambda x: x[1].lower()
    )

    selected_prov = form.prov_id.data or (user.prov_id if user else None)
    selected_muni = form.munci_id.data or (user.munci_id if user else None)

    if selected_prov:
        form.munci_id.choices = [('', '-- Select Municipality --')] + sorted(
            [(m['citymunCode'], m['citymunDesc']) for m in MUNICIPALITY_DATA if m['provCode'] == selected_prov],
            key=lambda x: x[1].lower()
        )
    else:
        form.munci_id.choices = [('', '-- Select Municipality --')]

    if selected_muni:
        form.brgy_id.choices = [('', '-- Select Barangay --')] + sorted(
            [(b['brgyCode'], b['brgyDesc']) for b in BARANGAY_DATA if b['citymunCode'] == selected_muni],
            key=lambda x: x[1].lower()
        )
    else:
        form.brgy_id.choices = [('', '-- Select Barangay --')]
    