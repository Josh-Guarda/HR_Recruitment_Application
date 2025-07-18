from my_app import BARANGAY_DATA, MUNICIPALITY_DATA, PROVINCE_DATA

    
    
# def set_form_choices(prov_id,munci_id,brgy_id):
    
#     selected_prov = prov_id= munci_id if prov_id else None)
#     selected_muni = munci_id= munci_id if user else None)
    
    
    
#     else:
#         prov_id.choices = [('', '-- Select Province --')] + sorted(
#             [(p['provCode'], p['provDesc']) for p in PROVINCE_DATA],
#             key=lambda x: x[1].lower()
#         )

    
    
#     if selected_prov:
#         form.munci_id.choices = [('', '-- Select Municipality --')] + sorted(
#             [(m['citymunCode'], m['citymunDesc']) for m in MUNICIPALITY_DATA if m['provCode'] == selected_prov],
#             key=lambda x: x[1].lower()
#         )
#     else:
#         munci_id.choices = [('', '-- Select Municipality --')]
#     if selected_muni:
#         brgy_id.choices = [('', '-- Select Barangay --')] + sorted(
#             [(b['brgyCode'], b['brgyDesc']) for b in BARANGAY_DATA if b['citymunCode'] == selected_muni],
#             key=lambda x: x[1].lower()
#         )
#     else:
#         brgy_id.choices = [('', '-- Select Barangay --')]
    