def run_formula(dv):
    MoneyFlow20=dv.add_formula('MoneyFlow_J',
               'Ts_Sum(1/3*(close+high_adj+low_adj)*volume,20)',is_quarterly=False,
               add_data=True)
    return MoneyFlow20
