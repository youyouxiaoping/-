def run_formula(dv):
    factor1= dv.add_formula('factor1',"EMA10*MA5",is_quarterly=False, add_data=True)
    return factor1
