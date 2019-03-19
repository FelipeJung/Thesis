close all;
clc;

% Planta

L1_1=9e-005;
L1=2*9e-005;
C1=	1e-006;
Cd=	1e-006;
L2_1=0.0006;
L2=2*0.0006;
Rd=	15;
Vrede=	311.126983722081;
Vcc=400;

s=tf('s');

Gid=Vcc*(Rd*Cd*s+1)/((s^4)*L1*L2*C1*Cd*Rd + (s^3)*L1*L2*(C1+Cd) + (s^2)*Cd*Rd*(L1+L2) + (s)*(L1+L2));

% Controle Repetitivo

wc=12600;
Frede=60;
T=1/Frede;
At=exp(-s*T);
F=wc/(s+wc);
cr=0.6;

Cr=1/(1-cr*F*At);
Cr1=1/(1-cr*At);

% Controle Avanço de fase

wz=80;
Kp=0.05;

Cav=Kp*(s+wz)/(s+10*wz);

Ftma=Cr*Cav*Gid;
Ftma1=Cr1*Cav*Gid;
w=logspace(2,5,100000);
FTMF=minreal(Cav*Gid/(1+Cav*Gid));
% bode(Ftma1,w);
bode(Ftma1,w);
hold on;
title ('Bode diagram of the open-loop repetitive-control system')
grid;

[mag1, ph1] = bode(Ftma1,w);
mag1 = squeeze(mag1);
ph1 = squeeze (ph1);
FTMA1 = [w', mag1, ph1];
header={'w','g1','f1'};

[mag, ph] = bode(Ftma,w);
mag = squeeze(mag);
ph = squeeze (ph);
FTMA = [w', mag, ph];
csvwrite_with_headers('FTMA.csv', FTMA, header);
csvwrite_with_headers('FTMA1.csv', FTMA1, header);

%% Plot do controle repetitivo com diferentes ganhos

Cr2=1/(1-1*F*At);
Cr3=1/(1-0.6*F*At);
Cr4=1/(1-0.1*F*At);



figure
bode(Cr2,w)
hold on
bode(Cr3,w);
bode(Cr4,w);
axis_handle=findall(gcf,'type','axes')
title('Repetitive control - gain variation')
grid on
h = legend(axis_handle(3),'c_r = 1','c_r = 0.6','c_r = 0.1', 'Location', 'NorthEast');
set(h,'string',{'c_r = 1','c_r = 0.6','c_r = 0.1'});


[mag1, ph1] = bode(Cr2, w);
[mag2, ph2] = bode(Cr3, w);
[mag3, ph3] = bode(Cr4, w);
mag1 = 20*log10(squeeze(mag1));
mag2 = 20*log10(squeeze(mag2));
mag3 = 20*log10(squeeze(mag3));
ph1 = squeeze(ph1);
ph2 = squeeze(ph2);
ph3 = squeeze(ph3);

M= [w', mag1, mag2, mag3, ph1, ph2, ph3];
header={'w','g1', 'g2', 'g3','f1', 'f2', 'f3'};
csvwrite_with_headers('Comp_rep_gain_variation.csv', M, header)

