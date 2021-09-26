clear all; close all; clc;

X = 60:1:220;

hold on

for i = 1:1:length(X)
    low(i) = zFunc(X(i),80,100);
    moderate(i) = pFunc(X(i),100,115,125,140);
    high(i) = zFunc(X(i),140,160);
end

notVeryLow = 1 - low.^2;
moreOrLessModerate = moderate.^(0.5);
veryHigh = high.^2;

plot(X, low)
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

title('Без використання внутрішніх функцій')

function r = zFunc(x, a, b)
    if (x <= a)
        r = 1;
    elseif (a <= x & x <= ((a + b) / 2 ))
        r = (1 - 2 * (((x - a) / (b - a))^2));
    elseif ((a + b) / 2 <= x & x <= b)
        r = 2 * (((b - x) / (b - a))^2);
    elseif (x >= b)
        r = 0;
    end
end


function r = sFunc(x, a, b)
    r = 1 - zFunc(x,a,b);
end

function r = pFunc(x, a, b, c, d)
    if(x <= a)
        r = 0;
    elseif(a <= x & x <= b)
        r = sFunc(x,a,b);
    elseif(b <= x & x <= c)
        r = 1;
    elseif(c <= x & x <= d)
        r = zFunc(x,c,d);
    elseif(x >= d)
        r = 0;
    end
end