def run_formula(dv):
    factor3 = dv.add_formula('factor3',"MA5*(-Correlation(Delta(Log(volume),1),(close-open)/open,6))",is_quarterly=False, add_data=True)
    return factor3
