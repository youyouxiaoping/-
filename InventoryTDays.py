def run_formula(dv):
    InventoryTDays=dv.add_formula('InventoryTDays_J','360/InventoryTRate',is_quarterly=False,add_data=True)
    return InventoryTDays
