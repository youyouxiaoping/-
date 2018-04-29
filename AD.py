def AD(dv):
    AD = dv.add_formula('AD_J', 
       "Ta('AD',0,open,high,low,close,volume)"
       , is_quarterly=False, add_data=True)
    return AD
