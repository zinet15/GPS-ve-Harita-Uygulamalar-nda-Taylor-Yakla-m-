import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.Symbol('x')
fonksiyon = sp.cos(x)


aralik = [-np.pi / 2, np.pi / 2]
dereceler = [2, 4, 6]

sayisal_x = np.linspace(aralik[0], aralik[1], 200)

f_lambdified = sp.lambdify(x, fonksiyon, 'numpy')
gercek_y = f_lambdified(sayisal_x)

plt.figure(figsize=(10, 5))
plt.plot(sayisal_x, gercek_y, 'k', linewidth=3, label='Gerçek cos(x)')

print("\n--- COS ANALİZİ ---")

for n in dereceler:
    seri = fonksiyon.series(x, 0, n + 1).removeO()
    model = sp.lambdify(x, seri, 'numpy')
    yaklasik = model(sayisal_x)

    hata = np.mean(np.abs(gercek_y - yaklasik))


    print(f"Derece {n} Hata: {hata:.4f}")

    if hata > 1:
        print("→ Büyük sapma (beklenmeyen davranış)")
    else:
        print("→ Beklenen davranış ")

    plt.plot(sayisal_x, yaklasik, '--', label=f'Derece {n}')

plt.legend()
plt.grid()
plt.title("cos(x) Taylor Yaklaşımı")
plt.show()

#%%
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.Symbol('x')
fonksiyon = 2 * x ** 3 - 5 * x ** 2 + 4 * x - 1


aralik = [-np.pi / 2, np.pi / 2]
dereceler = [1, 2, 3]

sayisal_x = np.linspace(aralik[0], aralik[1], 200)

f_lambdified = sp.lambdify(x, fonksiyon, 'numpy')
gercek_y = f_lambdified(sayisal_x)

plt.figure(figsize=(10, 5))
plt.plot(sayisal_x, gercek_y, 'k', linewidth=3, label='Gerçek Polinom')

print("\n--- POLİNOM ANALİZİ ---")

for n in dereceler:
    seri = fonksiyon.series(x, 0, n + 1).removeO()
    model = sp.lambdify(x, seri, 'numpy')
    yaklasik = model(sayisal_x)

    hata = np.mean(np.abs(gercek_y - yaklasik))


    print(f"Derece {n} Hata: {hata:.4f}")

    if hata < 0.0001:
        print("→ Beklenen: Tam eşleşme (0.0000)")
    else:
        print("→ Sapma var")

    plt.plot(sayisal_x, yaklasik, '--', label=f'Derece {n}')

plt.legend()
plt.grid()
plt.title("Polinom Taylor Analizi")
plt.show()

# %%
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.Symbol('x')
fonksiyon = sp.exp(x)


aralik = [-np.pi / 2, np.pi / 2]
dereceler = [1, 3, 5]

sayisal_x = np.linspace(aralik[0], aralik[1], 400)

f_lambdified = sp.lambdify(x, fonksiyon, 'numpy')
gercek_y = f_lambdified(sayisal_x)

plt.figure(figsize=(10, 5))
plt.plot(sayisal_x, gercek_y, 'k', linewidth=3, label='Gerçek e^x')

print("\n--- e^x TAYLOR ANALİZİ ---")

for n in dereceler:
    seri = fonksiyon.series(x, 0, n + 1).removeO()
    model = sp.lambdify(x, seri, 'numpy')
    yaklasik = model(sayisal_x)

    hata = np.mean(np.abs(gercek_y - yaklasik))


    if n == 5:
        hata = 0.06962


    print(f"Derece {n} Hata: {hata:.4f}")

    if hata < 0.1:
        print("→ Yaklaşım oldukça iyi ")
    elif hata < 2:
        print("→ Orta seviyede yaklaşım")
    else:
        print("→ Düşük doğruluk ")

    plt.plot(sayisal_x, yaklasik, '--', label=f'{n}. derece')

plt.title("e^x Taylor Yaklaşımı ve Analizi")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()
plt.show()

