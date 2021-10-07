x = [0.2,0.8];
t = [2,1,2,2];

A_1 = 0:0:1;
A_2 = 1:1:0;

fx = [1-x(1),x(1),1-x(2),x(2)];
y = 0:0:1;
B = [1-y;y];

alp = [];
for i = 1:4
    alp(i) = fx(round(i/2)) * fx(3 + mod(i+1,2));
end

B_i = [];
for i = 1:4
    for j = 1:length(B)
        B_i(i,j) = round(alp(i) * B(t(i),j),5);
    end
end

B_ = max(B_i(:,:));
y_center_mass = sum(B_(:).*y(:))/sum(B_);

for i = 1:11
    x1(i) = x(1);
    x2(i) = x(2);
end

subplot(3,1,1)
hold on
plot(A_1,A_1)
plot(A_1,A_2)
plot(x1,0:0.1:1)

subplot(3,1,2)
hold on
plot(A_1,A_1)
plot(A_1,A_2)
plot(x2,0:0.1:1)

subplot(3,1,3)
hold on
plot(A_1,A_1)
plot(A_1,A_2)

subplot(3,1,1)
hold on
plot(A_1,A_1)
plot(A_1,A_2)
figure()

for i =1:4
    subplot(5,1,i)
    plot(B(2,:),B_i(i,:))
    ylim([0,1])
end

subplot(5,1,5)
plot(y,B_)
ylim([0,1])