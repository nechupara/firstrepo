# scale1 : scale2
scale1 = 1
scale2 = 100000

mm_to_m = scale2/(scale1*1000)
m_to_mm = scale1*1000/scale2

mm_to_km = mm_to_m/1000
km_to_mm = m_to_mm*1000

print('масштаб %s:%s' % (scale1, scale2))
print('в 1 мм %s м\t\t(/%s)' % (mm_to_m, m_to_mm))
print('в 1 м  %s мм\t\t(/%s)' % (m_to_mm, mm_to_m))
print()
print('в 1 мм %s км\t\t(/%s)' % (mm_to_km, km_to_mm))
print('в 1 км %s мм\t\t(/%s)' % (km_to_mm, mm_to_km))
