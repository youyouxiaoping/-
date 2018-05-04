def run_formula(dv):
    NetNonOIToTPLatest_A = dv.add_formula('NetNonOIToTPLatest_A',"(nonopprofit-less_non_oper_exp)/tot_profit",is_quarterly=False, add_data=True)
    return NetNonOIToTPLatest_A
