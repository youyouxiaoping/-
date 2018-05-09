def run_formula(dv):
    DSD = dv.add_formula('DSD',"If(Return(close,1)<0,StdDev(Return(close,1),10),0)",is_quarterly=False,add_data=True)
    factor6 = dv.add_formula('factor6',"Ta('AD',0,open,high,low,close,volume)*Ta('EMA',0,DSD,DSD,DSD,DSD,DSD,14)",is_quarterly=False, add_data=True)
    return factor6
