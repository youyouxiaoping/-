def alpha28(dv):
    def SMA(A,n,m):
    # 设置alpha的比例
    alpha = m/n
    #通过ewm计算递归函数
    return A.ewm(alpha=alpha, adjust=False).mean()

alpha28 = dv.add_formula('alpha28', 
               "3*SMA((close-Ts_Min(low,9))/(Ts_Max(high,9)-Ts_Min(low,9))*100,3,1)-2*SMA(SMA((close-Ts_Min(low,9))/(Max(high,9)-Ts_Max(low,9))*100,3,1),3,1)"
             , is_quarterly=False, add_data=True,
             register_funcs={"SMA":SMA}
             )
     return alpha28
