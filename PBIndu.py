def run_formula(dv):
    sw1 = dv.get_ts('sw1').stack()
    pb = dv.get_ts('PB').stack()
    return PBIndu
    pb_sw1 = pd.concat([sw1,pb],axis=1,keys=['sw1','pb'])
    Indu_mean = pb_sw1.groupby(['sw1']).mean().pb.to_dict()
    Indu_std = pb_sw1.groupby(['sw1']).std().pb.to_dict()
    pb_sw1['PBIndu_Mean'] = [Indu_mean[c] for c in pb_sw1['sw1'].values]
    pb_sw1['PBIndu_Std'] = [Indu_std[c] for c in pb_sw1['sw1'].values]
    pb_sw1['PBIndu'] = (pb_sw1['pb']-pb_sw1['PBIndu_Mean'])/pb_sw1['PBIndu_Std']
    PBIndu = pb_sw1.PBIndu.unstack()
    PBIndu=dv.append_df(PBIndu, 'PBIndu')
    return(PBIndu)
