import numpy as np
import skfuzzy as fuzz
import skfuzzy.membership as mf
import matplotlib.pyplot as plt

öğrenci_ortalamaları = np.arange(0,5,0.1)
yatırım_sektörleri = np.arange(20,100,10)

print(öğrenci_ortalamaları)
# öğrencilerin sınıflandırılması
üstün_başarılı = mf.trimf(öğrenci_ortalamaları,[3.5,4,4])
başarılı = mf.trimf(öğrenci_ortalamaları,[2.5,3,3.5])
az_başarılı = mf.trimf(öğrenci_ortalamaları,[1.8,2,2.5])
# yüksek yatırımların sınıflandırılması
yüksek_yatırımlar = mf.trimf(yatırım_sektörleri,[50,80,100])
orta_yatırımlar = mf.trimf(yatırım_sektörleri,[25,40,60])
düşük_yatırımlar = mf.trimf(yatırım_sektörleri, [20,30,40])

fig, (ax0,ax1,ax2) = plt.subplots(nrow = 3, figsize = (6,10))

ax0.plot(öğrenci_ortalamaları, üstün_başarılı, 'w', linewidth = 2, label = 'Üstün Başarılı')
ax0.plot(öğrenci_ortalamaları, başarılı, 'n', linewidth = 2, label = 'Başarılı')
ax0.plot(öğrenci_ortalamaları, az_başarılı, 'l', linewidth = 2, label = 'Az Başarılı')

ax1.plot(yatırım_sektörleri, yüksek_yatırımlar, 'w', linewidth = 2, label = 'Yüksek Yatırımlı Ders1')
ax1.plot(yatırım_sektörleri, orta_yatırımlar, 'n', linewidth = 2, label = 'Orta Yatırımlı Ders2')
ax1.plot(yatırım_sektörleri, düşük_yatırımlar, 'l', linewidth = 2, label = 'Düşük Yatırımlı Ders3')

ax0.set_title('Başarı Durumları')
ax0.legend()

ax1.set_title('Yüksek Yatırımlı Derslerin Yatırım Durumları')
ax1.legend()

plt.tight_layout()

input_not = 3.4
input_ders = 50

student_fit_low = fuzz.interp_membership(öğrenci_ortalamaları, az_başarılı, input_not)
student_fit_med = fuzz.interp_membership(öğrenci_ortalamaları, başarılı, input_not)
student_fit_hig = fuzz.interp_membership(öğrenci_ortalamaları,üstün_başarılı, input_not)

investment_fit_low = fuzz.interp_membership(yatırım_sektörleri, düşük_yatırımlar, input_ders)
investment_fit_med = fuzz.interp_membership(yatırım_sektörleri, orta_yatırımlar, input_ders)
investment_fit_hig = fuzz.interp_membership(yatırım_sektörleri,yüksek_yatırımlar, input_ders)

rule1 = np.fmin(np.fmin(student_fit_med,student_fit_hig),np.fmax(investment_fit_low,investment_fit_med))
rule2 = np.fmin(student_fit_hig, investment_fit_hig)
rule3 = np.fmin(student_fit_low, investment_fit_low)

out_strong = np.fmax(rule2,rule1)
out_poor = np.fmax(rule3,rule1)













