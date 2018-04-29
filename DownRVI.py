def DownRVI(dv):
    DSD=dv.add_formula('DSD', 
                   "If(Return(close,1)<0,StdDev(Return(close,1),%s),0)"%(param['t1'])
                   , is_quarterly=False, add_data=True)
    
    DownRVI = dv.add_formula('DownRVI_J', 
                   "Ta('EMA',0,DSD,DSD,DSD,DSD,DSD,%s)"%(param['t2'])
                   , is_quarterly=False, add_data=True)
    return DownRVI
