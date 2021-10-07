x1 = [0 1];
x2 = [0 1];
y = [1 0 1 1];

% Ініціалізація моделі
mod_name="BS-02 Kryzhanovskyi";
mod = newfis(mod_name, 'mamdani', 'min', 'max', 'min', 'max');

% Додавання до моделі змінних
mod = addvar(mod,'input','x1', x1);
mod = addmf (mod,'input',1,'a1','trimf',[-0.1 0 1]);
mod = addmf (mod,'input',1,'a2','trimf',[0 1 1.1]);
mod = addvar(mod,'input','x2', x2);
mod = addmf (mod,'input',2,'a1','trimf',[-0.1 0 1]);
mod = addmf (mod,'input',2,'a2','trimf',[0 1 1.1]);
mod = addvar(mod,'output','y', [min(y) max(y)]);
mod = addmf (mod,'output',1, ['b1',int2str(1)],'trimf', [-0.1 0 1]);
mod = addmf (mod,'output',1, ['b2',int2str(2)],'trimf', [0 1 1.1]);

rullist = [ 1 1 2 1 1;
            1 2 1 1 1;
            2 1 2 1 1;
            2 2 2 1 1];
        
mod = addrule(mod, rullist);
writefis (mod,  mod_name);
mod = readfis(mod_name);

% Розрахунок виходу моделі при дифазифікації за методом centroid
y = evalfis([0.2 0.8], mod);
disp('Відповідь: y centroid = ');
disp(y);

% Розрахунок виходу моделі при дифазифікації за методом bisector
mod=setfis(mod,'defuzzmethod','bisector');
y = evalfis([0.2 0.8], mod);
disp('Відповідь: y bisector = ');
disp(y);