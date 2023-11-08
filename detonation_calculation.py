from math import sqrt

# List of materials

c7h5n3o6 = [7, 5, 3, 6, 0, 56.6, 227]
c12h26 = [12, 26, 0, 0, 0, 341.9, 170]
nh4no3 = [0, 4, 2, 3, 0, 354.8, 80]
c3h5n3o9 = [3, 5, 3, 9, 0, 350.7, 227]
al = [0, 0, 0, 0, 1, 0, 27]
c13h20 = [13, 20, 0, 0, 0, 158.8, 176]
c2h4o6n2 = [2, 4, 6, 2, 0, 229.61, 152]
c3h6n6o6 = [3, 6, 6, 6, 0, -93.3, 222]
c5h8n4o12 = [5, 8, 4, 12, 0, 402.3, 227]
c4h8n8o8 = [4, 8, 8, 8, 0, -109.4, 296]

vz = {
        'Аммиачная селитра (NH4NO3)': nh4no3,
        'Дизельное топливо (C13H20)': c13h20,
        'Минеральное масло (C12H26)': c12h26,
        'Тротил (C7H5N3O6)': c7h5n3o6,
        'Нитроглицирин (C3H5O9N3)': c3h5n3o9,
        'Алюминий (Al)': al,
        'Нитрогликоль (C2H4O6N2)': c2h4o6n2,
        'Гексоген (C3H6N6O6)': c3h6n6o6,
        'ТНТ (C5H8N4O12)': c5h8n4o12,
        'Октоген (C4H8N8O8)': c4h8n8o8
    }


def detonation(combination_list, percentage, den):
    # Calculation
    a1 = 0
    b1 = 0
    c1 = 0
    d1 = 0
    e1 = 0
    Q12 = 0
    for z in range(len(combination_list)):
        a1 += vz[combination_list[z]][0] * percentage[z] * 10 / vz[combination_list[z]][6]
        b1 += vz[combination_list[z]][1] * percentage[z] * 10 / vz[combination_list[z]][6]
        c1 += vz[combination_list[z]][2] * percentage[z] * 10 / vz[combination_list[z]][6]
        d1 += vz[combination_list[z]][3] * percentage[z] * 10 / vz[combination_list[z]][6]
        e1 += vz[combination_list[z]][4] * percentage[z] * 10 / vz[combination_list[z]][6]
        Q12 += vz[combination_list[z]][5] * percentage[z] * 10 / vz[combination_list[z]][6]

    kb = (d1 - (2 * a1 + 1.5 * e1 + b1 * 0.5)) * 1.6
    if d1 >= (2 * a1 + 0.5 * b1):
        kbn = 1
        val2o3 = 0.5 * e1
        vh2o = 0.5 * b1
        vco2 = a1
        vco = 0
        vo2 = 0.5 * (d1 - 2 * a1 - 0.5 * b1 - 1.5 * e1)
        vn2 = c1 * 0.5
        vh2 = 0
        vc = 0

    elif (a1 + 0.5 * b1) <= d1 < (2 * a1 + 0.5 * b1):
        kbn = 2
        val2o3 = 0.5 * e1
        vh2o = 0.5 * (d1 - a1 - 1.5 * e1)
        vco2 = 0.5 * (d1 - a1 - 1.5 * e1)
        vco = 0.5 * (3 * a1 - (d1 - 1.5 * e1))
        vo2 = 0
        vn2 = c1 * 0.5
        vh2 = 0.5 * (a1 + b1 - (d1 - 1.5 * e1))
        vc = 0
        if vh2 < 0 or vn2 < 0 or vco < 0 or vco2 < 0 or vh2o < 0:
            val2o3 = 0.5 * e1
            vh2o = 0.5 * b1
            vco2 = d1 - a1 - 0.5 * b1 - 0.5 * e1
            vco = 2 * a1 + 0.5 * b1 - (d1 - 0.5 * e1)
            vo2 = 0
            vn2 = c1 * 0.5
            vh2 = 0
            vc = 0
        else:
            val2o3 = 0.5 * e1
            vh2o = 0.5 * (d1 - a1 - 1.5 * e1)
            vco2 = 0.5 * (d1 - a1 - 1.5 * e1)
            vco = 0.5 * (3 * a1 - (d1 - 1.5 * e1))
            vo2 = 0
            vn2 = c1 * 0.5
            vh2 = 0.5 * (a1 + b1 - (d1 - 1.5 * e1))
            vc = 0

    else:
        kbn = 3
        val2o3 = 0.5 * e1
        vh2o = 0.5 * b1
        vco2 = d1 - a1 - 0.5 * b1 - 0.5 * e1
        vco = 2 * a1 + 0.5 * b1 - (d1 - 0.5 * e1)
        vo2 = 0
        vn2 = c1 * 0.5
        vh2 = 0
        vc = 0
        if vco < 0 or vco2 < 0:
            val2o3 = 0.5 * e1
            vh2o = b1 * 0.5
            vco2 = 0
            vco = d1 - 0.5 * b1 - 1.5 * e1
            vo2 = 0
            vn2 = c1 * 0.5
            vh2 = 0
            vc = a1 - (d1 - 1.5 * e1) + 0.5 * b1
        else:
            val2o3 = 0.5 * e1
            vh2o = 0.5 * b1
            vco2 = d1 - a1 - 0.5 * b1 - 0.5 * e1
            vco = 2 * a1 + 0.5 * b1 - (d1 - 0.5 * e1)
            vo2 = 0
            vn2 = c1 * 0.5
            vh2 = 0
            vc = 0

    Q13 = val2o3 * 1666.7 + vco * 113.7 + vco2 * 395.6 + vh2o * 240.6
    Q23 = Q13 - Q12
    na = (vco + vh2 + vo2 + vn2) * 20.1 + vco2 * 41.1 + vh2o * 16.76 + (vc + val2o3) * 24.97
    nb = (vco + vh2 + vo2 + vn2) * 0.001886 + vco2 * 0.00243 + vh2o * 0.00901 + (vc + val2o3) * 0
    T = ((-na + sqrt((na) ** 2 + 4 * (nb) * Q23 * 1000)) / (2 * nb)) + 273
    V = 0.0224 * (vco2 + vco + vo2 + vh2o + vn2)
    if den > 1:
        koefal = 0.0006 * V
    else:
        koefal = 0.0001 * V
    P = (101000 * V * T * den * 1000) / (273 * (1 - koefal * den * 1000))
    vdc = 3600 + 3600 * (den - 1)
    vd = vdc * sqrt(Q23 / 4315)
    Pzh = ((vd ** 2) * den) / 4
    plotpv = (4 / 3) * den
    uv = vd / 4
    uuv = uv / 0.316

    features = [f"Кислородный баланс, %: {kb:.3f}",
                f"Группа: {kbn:.0f}",
                f"Теплота взрыва, кДж/кг: {Q23:.3f}",
                f"Температура взрыва, К: {T:.3f}",
                f"Объём газообразных ПВ, м3/кг: {V:.3f}",
                f"Давление ПВ, Па: {P:.3f}",
                f"Скорость детонации, м/с: {vd:.3f}",
                f"Детонационное давление, Па: {Pzh:.3f}",
                f"Плотность продуктов взрыва, г/см3: {plotpv:.3f}",
                f"Скорость разлета ПВ за фронтом детонации, м/с: {uv}",
                f"Скорость разлета ПВ во фронте детонации, м/с: {uuv}"]
    return features
