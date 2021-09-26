clear all; close all; clc;

X = 60:1:220;

hold on

plot(X, zmf(X,[80,100]))
plot(X, pimf(X,[100,115,125,140]))
plot(X, smf(X,[140,160]))
plot(X, 1 - zmf(X,[80,100]).^2)
plot(X, pimf(X,[100,115,125,140]).^(1/2))
plot(X, smf(X,[140,160]).^2)

legend("Низький","Помірний","Високий","Не дуже низький", "Більш-менш помірний","Дуже високий")

grid on
xlim([min(X) max(X)])
xlabel('Тиск')
ylabel('Належність')

title('Використовуючи внутрішні функції')