def run_formula(dv):
    factor2 = dv.add_formula('factor2',"EMA10*(-Correlation(Delta(Log(volume),1),(close-open)/open,6))",is_quarterly=False, add_data=True)
    return factor2
