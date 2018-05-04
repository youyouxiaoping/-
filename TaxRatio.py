def run_formula(dv):
    TaxRatio = dv.add_formula('TaxRatio_J',"TTM(less_taxes_surcharges_ops)/TTM(oper_rev)",is_quarterly=False, add_data=True)
    return TaxRatio
