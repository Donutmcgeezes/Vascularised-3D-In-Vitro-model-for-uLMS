import matplotlib.pyplot as plt
import numpy as np

'''EXPERIMENT 1: HUVECS VS HUVECS + FIBROBLASTS'''
r1_ec_ld = [238.17, 109.25, 147.21]
r1_ec_bpd = [2226.2, 893.4,  1273.5]
r1_ec_epbp = [1.444,  1.808,  0.867]
r1_ec_tort = [1.209,  1.187,  1.191]

r1_ecf_ld = [294.84, 97.33, 66.53]
r1_ecf_bpd = [2826.0, 866.3,  604.9]
r1_ecf_epbp = [0.794,  1.487,  2.2]
r1_ecf_tort = [1.176,  1.206,  1.219]

r1days = [0, 2, 5]

r2_ec_ld = [84.82,  163.15]
r2_ec_bpd =[555.8,  1887.0]
r2_ec_epbp = [3.686,  1.452]
r2_ec_tort = [1.203,  1.221]

r2_ecm_ld = [44.12,  19.89]
r2_ecm_bpd = [167.0,  32.9]
r2_ecm_epbp = [11.376, 37.558]
r2_ecm_tort = [1.199,  1.198]

r2days = [4,6]

metrics = ['Length Density (mm/mm^3)', 'Branchpoint Density (mm^-3)', 'EP:BP Ratio', 'Median Tortuosity']

fig1, axes1 = plt.subplots(2, 2, figsize = (12,10))
fig1.suptitle('HUVECs vs HUVECs + Fibroblasts', fontsize = 12, fontweight = 'bold')

axes1[0,0].plot(r1days, r1_ec_ld, 'b-o', linewidth = 2) #Length Density (0,0)
axes1[0,0].plot (r1days, r1_ecf_ld, 'r-^', linewidth = 2)
axes1[0,0].set_title(metrics[0])
axes1[0,0].set_xlabel('Days')
axes1[0,0].set_ylabel(metrics[0])
axes1[0,0].legend(['HUVECs', 'HUVECs + Fibroblasts'])
axes1[0,0].set_xticks(r1days)

axes1[0,1].plot(r1days, r1_ec_bpd, 'b-o', linewidth = 2) #Branchpoint Density (0,1)
axes1[0,1].plot(r1days, r1_ecf_bpd, 'r-^', linewidth = 2)
axes1[0,1].set_title(metrics[1])
axes1[0,1].set_xlabel('Days')
axes1[0,1].set_ylabel(metrics[1])
axes1[0,1].legend(['HUVECs', 'HUVECs + Fibroblasts'])
axes1[0,1].set_xticks(r1days)

axes1[1,0].plot(r1days,r1_ec_epbp, 'b-o', linewidth = 2) #EPBP Ratio (1,0)
axes1[1,0].plot(r1days,r1_ecf_epbp, 'r-^', linewidth = 2)
axes1[1,0].set_title(metrics[2])
axes1[1,0].set_xlabel('Days')
axes1[1,0].set_ylabel(metrics[2])
axes1[1,0].legend(['HUVECs', 'HUVECs + Fibroblasts'])
axes1[1,0].set_xticks(r1days)

axes1[1,1].plot(r1days, r1_ec_tort, 'b-o', linewidth = 2) #Median Tortuosity (1,1) - Same format for all
axes1[1,1].plot(r1days, r1_ecf_tort, 'r-^', linewidth = 2)
axes1[1,1].set_title(metrics[3])
axes1[1,1].set_xlabel('Days')
axes1[1,1].set_ylabel(metrics[3])
axes1[1,1].legend(['HUVECs', 'HUVECs + Fibroblasts'])
axes1[1,1].set_xticks(r1days)

fig1.tight_layout()

'''EXPERIMENT 1: HUVECS VS HUVECS + MSCs'''

fig2, axes2 = plt.subplots(2, 2, figsize = (12,10))
fig2.suptitle('HUVECs vs HUVECs + MSCs', fontsize = 12, fontweight = 'bold')

axes2[0,0].plot(r2days, r2_ec_ld, 'b-o', linewidth = 2)
axes2[0,0].plot (r2days, r2_ecm_ld, 'g-s', linewidth = 2)
axes2[0,0].set_title(metrics[0])
axes2[0,0].set_xlabel('Days')
axes2[0,0].set_ylabel(metrics[0])
axes2[0,0].legend(['HUVECs', 'HUVECs + MSCs'])
axes2[0,0].set_xticks(r2days)

axes2[0,1].plot(r2days, r2_ec_bpd, 'b-o', linewidth = 2)
axes2[0,1].plot(r2days, r2_ecm_bpd, 'g-s', linewidth = 2)
axes2[0,1].set_title(metrics[1])
axes2[0,1].set_xlabel('Days')
axes2[0,1].set_ylabel(metrics[1])
axes2[0,1].legend(['HUVECs', 'HUVECs + MSCs'])
axes2[0,1].set_xticks(r2days)

axes2[1,0].plot(r2days,r2_ec_epbp, 'b-o', linewidth = 2)
axes2[1,0].plot(r2days,r2_ecm_epbp, 'g-s', linewidth = 2)
axes2[1,0].set_title(metrics[2])
axes2[1,0].set_xlabel('Days')
axes2[1,0].set_ylabel(metrics[2])
axes2[1,0].legend(['HUVECs', 'HUVECs + MSCs'])
axes2[1,0].set_xticks(r2days)

axes2[1,1].plot(r2days, r2_ec_tort, 'b-o', linewidth = 2)
axes2[1,1].plot(r2days, r2_ecm_tort, 'g-s', linewidth = 2)
axes2[1,1].set_title(metrics[3])
axes2[1,1].set_xlabel('Days')
axes2[1,1].set_ylabel(metrics[3])
axes2[1,1].legend(['HUVECs', 'HUVECs + MSCs'])
axes2[1,1].set_xticks(r2days)

fig2.tight_layout()



'''EXPERIMENT 2 STUFF'''

chan3_days   = [0, 4, 7]
dspw25_days  = [0, 4, 4, 7]   # two D4 replicates
vr5_days     = [0, 4, 7, 7]   # two D7 replicates

# Length Density (mm/mm³)
chan3_ld     = [178.38, 627.81, 475.14]
dspw25_ld   = [95.69,  578.86, 521.60, 206.27]
vr5_ld      = [63.90,  250.62, 576.66, 649.43]

# Branchpoint Density (mm⁻³)
chan3_bpd    = [1635.1, 7451.6, 5923.3]
dspw25_bpd  = [648.9,  6515.1, 5254.5, 1530.5]
vr5_bpd     = [410.4,  2710.2, 5800.3, 8029.4]

# EP:BP Ratio
chan3_epbp   = [2.148, 0.424, 0.454]
dspw25_epbp = [4.000, 0.620, 1.037, 2.164]
vr5_epbp    = [5.245, 0.869, 1.130, 0.405]

# Median Tortuosity
chan3_tort   = [1.220, 1.160, 1.183]
dspw25_tort = [1.221, 1.185, 1.191, 1.207]
vr5_tort    = [1.219, 1.211, 1.207, 1.184]

#Anomalies plotted later
a_chan3_days   = [4,7]
a_chan3 = [[43.07, 85.09], [245.2, 325.9], [7.566, 10.797], [1.183, 1.185]]
# a_chan3_ld     = [43.07, 85.09]
# a_chan3_bpd    = [245.2, 325.9]
# a_chan3_epbp   = [7.566, 10.797]
# a_chan3_tort   = [1.183, 1.185]

a_dspw25_days  = [7]
a_dspw25 = [171.44, 1372.2, 1.81, 1.211]
# a_dspw25_ld    = [171.44]
# a_dspw25_bpd   = [1372.2]
# a_dspw25_epbp  = [1.81]
# a_dspw25_tort  = [1.211]



metrics2 = ['Length Density (mm/mm^3)', 'Branchpoint Density (mm^-3)', 'EP:BP Ratio', 'Median Tortuosity']
dspw25_met = [dspw25_ld, dspw25_bpd, dspw25_epbp, dspw25_tort]
vr5_met = [vr5_ld, vr5_bpd, vr5_epbp, vr5_tort]

#dspw25_means = [(dspw25_ld[1]+dspw25_ld[2])/2, (dspw25_bpd[1]+dspw25_bpd[2])/2, (dspw25_epbp[1]+dspw25_epbp[2])/2, (dspw25_tort[1]+dspw25_tort[2])/2]
dspw25_means = []
vr5_means =[]



for i in range(len(metrics2)):
    dspw25_means.append((dspw25_met[i][1]+dspw25_met[i][2])/2)
    vr5_means.append((vr5_met[i][2]+vr5_met[i][3])/2)
print(dspw25_means)
print(vr5_means)

dspw25_tgt = [
    [dspw25_ld[0], dspw25_means[0] ,dspw25_ld[-1]],
    [dspw25_bpd[0], dspw25_means[1] ,dspw25_bpd[-1]],
    [dspw25_epbp[0], dspw25_means[2] ,dspw25_epbp[-1]],
    [dspw25_tort[0], dspw25_means[3] ,dspw25_tort[-1]]
    ]

vr5_tgt = [
    [vr5_ld[0], vr5_ld[1], vr5_means[0]],
    [vr5_bpd[0], vr5_bpd[1], vr5_means[1]],
    [vr5_epbp[0], vr5_epbp[1], vr5_means[2]],
    [vr5_tort[0], vr5_tort[1], vr5_means[3]]
]


fig3, axes3 = plt.subplots(2, 2, figsize = (12,10))
fig3.suptitle('Chip Design Comparison', fontsize = 12, fontweight = 'bold')

axes3[0,0].scatter(chan3_days, chan3_ld , color='red', marker='o')
axes3[0,0].scatter(dspw25_days, dspw25_ld , color='green', marker='^')
axes3[0,0].scatter(vr5_days, vr5_ld , color='blue', marker='s')
axes3[0,0].plot(chan3_days, chan3_ld,'r')
axes3[0,0].plot(chan3_days, dspw25_tgt[0],'g')
axes3[0,0].plot(chan3_days, vr5_tgt[0],'b')
axes3[0,0].scatter(a_chan3_days, a_chan3[0], color='red', marker='X')
axes3[0,0].scatter(a_dspw25_days, a_dspw25[0], color='green', marker='X')
axes3[0,0].set_title(metrics2[0])
axes3[0,0].set_xlabel('Days')
axes3[0,0].set_ylabel(metrics2[0])
axes3[0,0].legend(['3Chan', 'DSPW25', 'VR5'])
axes3[0,0].set_xticks([0, 4, 7])

axes3[0,1].scatter(chan3_days, chan3_bpd, color='red', marker='o')
axes3[0,1].scatter(dspw25_days, dspw25_bpd, color='green', marker='^')
axes3[0,1].scatter(vr5_days, vr5_bpd, color='blue', marker='s')
axes3[0,1].plot(chan3_days, chan3_bpd,'r')
axes3[0,1].plot(chan3_days, dspw25_tgt[1],'g')
axes3[0,1].plot(chan3_days, vr5_tgt[1],'b')
axes3[0,1].scatter(a_chan3_days, a_chan3[1], color='red', marker='X')
axes3[0,1].scatter(a_dspw25_days, a_dspw25[1], color='green', marker='X')
axes3[0,1].set_title(metrics2[1])
axes3[0,1].set_xlabel('Days')
axes3[0,1].set_ylabel(metrics2[1])
axes3[0,1].legend(['3Chan', 'DSPW25', 'VR5'])
axes3[0,1].set_xticks([0, 4, 7])

axes3[1,0].scatter(chan3_days, chan3_epbp, color='red', marker='o')
axes3[1,0].scatter(dspw25_days, dspw25_epbp, color='green', marker='^')
axes3[1,0].scatter(vr5_days, vr5_epbp, color='blue', marker='s')
axes3[1,0].plot(chan3_days, chan3_epbp,'r')
axes3[1,0].plot(chan3_days, dspw25_tgt[2],'g')
axes3[1,0].plot(chan3_days, vr5_tgt[2],'b')
axes3[1,0].scatter(a_chan3_days, a_chan3[2], color='red', marker='X')
axes3[1,0].scatter(a_dspw25_days, a_dspw25[2], color='green', marker='X')
axes3[1,0].set_title(metrics2[2])
axes3[1,0].set_xlabel('Days')
axes3[1,0].set_ylabel(metrics2[2])
axes3[1,0].legend(['3Chan', 'DSPW25', 'VR5'])
axes3[1,0].set_xticks([0, 4, 7])

axes3[1,1].scatter(chan3_days, chan3_tort, color='red', marker='o')
axes3[1,1].scatter(dspw25_days, dspw25_tort, color='green', marker='^')
axes3[1,1].scatter(vr5_days, vr5_tort, color='blue', marker='s')
axes3[1,1].plot(chan3_days, chan3_tort,'r')
axes3[1,1].plot(chan3_days, dspw25_tgt[3],'g')
axes3[1,1].plot(chan3_days, vr5_tgt[3],'b')
axes3[1,1].scatter(a_chan3_days, a_chan3[3], color='red', marker='X')
axes3[1,1].scatter(a_dspw25_days, a_dspw25[3], color='green', marker='X')
axes3[1,1].set_title(metrics2[3])
axes3[1,1].set_xlabel('Days')
axes3[1,1].set_ylabel(metrics2[3])
axes3[1,1].legend(['3Chan', 'DSPW25', 'VR5'])
axes3[1,1].set_xticks([0, 4, 7])

fig3.tight_layout()
#plt.savefig(f'C:/Users/user/Desktop/Uni things/Y4/MASTERS PROJECT/FINAL Report/IMAGES_FINAL REPORT/Results_Ex2_VESNA.svg', dpi=600, bbox_inches='tight')
plt.show()


