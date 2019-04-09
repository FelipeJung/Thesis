close all
clear all
% A1048576
%0.053652 tempo de inicio da captura no PSIM

%% Simulação em 20 kHz
R1=1;
C1=0;
R2=1000000;%333333;
C2=2;
RNG = [R1 C1 R2 C2];
RNG1 = [R1 C1 R2 1];
PI = csvread('HIL_MA_05-078.csv',R1,C1);
plot((PI(:,1)-PI(1:1)),PI(:,5))
hold
% plot(PI(:,1),PI(:,3))
% -plot(PI(:,1),PI(:,4))

PI_PSIM = csvread('validacao_degrau_amplitude_PSIM.csv',R1,C1);
plot(PI_PSIM(:,1)-PI_PSIM(1:1),PI_PSIM(:,2))
grid on
% axis([0,0.1,-2,2]);
title('Comparison between HIL simulation and PSIM')
legend ('HIL simulation response','PSIM simulation')
% 
% PI_PSIM=csvread('PI_PSIM.csv',R1,C1, RNG1);
% 
% PR=csvread('PR.csv',R1,C1,RNG);
% PR_PSIM=csvread('PR_PSIM.csv',R1,C1);
% 
% MR=csvread('MR.csv',R1,C1,RNG);
% MR_PSIM=csvread('MR_PSIM.csv',R1,C1);
% 
% Rep=csvread('Repetitivo.csv',R1,C1,RNG);
% Rep_PSIM=csvread('Repetitivo_PSIM.csv',R1,C1);
% 
% % load('PI.mat');
% Time=PR(:,1)/10;
% Time_pi=PI_PSIM(:,1)-PI_PSIM(1,1);
% IL2_PI=PI(:,3);
% IL2_PI_PSIM=PI_PSIM(:,2);
% voltage_pi=PI(:,2)/311;
% 
% Time_pr=PR_PSIM(:,1)-PR_PSIM(1,1);
% IL2_PR=PR(:,3);
% IL2_PR_PSIM=PR_PSIM(:,2);
% voltage_pr=PR(:,2)/311;
% 
% Time_mr=MR_PSIM(:,1)-MR_PSIM(1,1);
% IL2_MR=MR(:,3);
% IL2_MR_PSIM=MR_PSIM(:,2);
% voltage_mr=MR(:,2)/311;
% 
% Time_rep=Rep_PSIM(:,1)-Rep_PSIM(1,1);
% IL2_Rep=Rep(:,3);
% IL2_Repetitivo_PSIM=Rep_PSIM(:,2);
% voltage_rep=Rep(:,2)/311;
% 
% %%
% close all
% x1={'0','0,05','0,1','0,15','0,2','0,25','0,3','0,35','0,4','0,45','0,5'};
% y1={'-2','-1,5','-1','-0,5','0','0,5','1','1,5','2'};
% figure(1)
% plot(Time_pi, IL2_PI, 'r-','LineWidth',2)
% hold on
% plot(Time_pi, IL2_PI_PSIM, 'k-','LineWidth',1)
% plot(Time,voltage_pi,'b','LineWidth',2)
% grid
% legend('Modelo simulado Typhoon HIL','Modelo simulado PSIM','Tensão (Amplitude unitária)')
% title('Controlador PI')
% xlabel('Tempo (s)')
% xticklabels(x1);
% yticklabels(y1);
% 
% figure(2)
% plot(Time, IL2_PR, 'r-','LineWidth',2)
% hold on
% plot(Time_pr, IL2_PR_PSIM, 'k-','LineWidth',1)
% plot(Time,voltage_pr,'b','LineWidth',2)
% grid
% legend('Modelo simulado Typhoon HIL','Modelo simulado PSIM','Tensão (Amplitude unitária)')
% title('Controlador PR')
% xlabel('Tempo (s)')
% xticklabels(x1);
% yticklabels(y1);
% 
% figure(3)
% plot(Time, IL2_MR, 'r-','LineWidth',2)
% hold on
% plot(Time_mr, IL2_MR_PSIM, 'k-','LineWidth',1)
% plot(Time,voltage_mr,'b','LineWidth',2)
% grid
% legend('Modelo simulado Typhoon HIL','Modelo simulado PSIM','Tensão (Amplitude unitária)')
% title('Controlador MR')
% xlabel('Tempo (s)')
% xticklabels(x1);
% yticklabels(y1);
% 
% figure(4)
% plot(Time, IL2_Rep, 'r-','LineWidth',2)
% hold on
% plot(Time_rep, IL2_Repetitivo_PSIM, 'k-','LineWidth',1)
% plot(Time,voltage_rep,'b','LineWidth',2)
% grid
% legend('Modelo simulado Typhoon HIL','Modelo simulado PSIM','Tensão (Amplitude unitária)')
% title('Controlador Repetitivo')
% xlabel('Tempo (s)')
% axis([0 0.05 -2 2])
% xticklabels(x1);
% yticklabels(y1);
% 
% %%
% 
% 
% 
% Fs = 1/1e-7;
% x = IL2_PI_PSIM;
% nharm = 60;
% 
% [pxx,f] = periodogram(x,rectwin(length(x)),length(x),Fs);
% [thd_db,harmpow,harmfreq] = thd(pxx,f,nharm,'psd');
% percent_thd = 100*(10^(thd_db/20));
% T = table(harmfreq,harmpow,'VariableNames',{'Frequency','Power'});
% % thd(x,Fs,nharm);
% 
% %  fft_IL2_PI=fft(IL2_PI,333333);
% %  fft_IL2_PI_PSIM=fft(IL2_PI_PSIM,333333);
% %  freq=0:60:length(fft_IL2_PI)*60-1;
% %  figure(5)
% %  bar(freq,2*abs(fft_IL2_PI)/333333,'r')
% %  xlim([90 2000])
% % %  axis([90 2000 0 0.03])
% %  figure
% %  bar(freq,2*abs(fft_IL2_PI_PSIM)/333333,'k')
% %  xlim([90 2000])
% % % 
% % % figure(6)
% % % bar(freq,2*abs(fft_IL2_PI)/333333)
% % % hold
% % % bar(freq,2*abs(fft_IL2_PI_PSIM)/333333)
% % % xlim([100 2720])
% % % 
% % % 
% % % 
% % % 
% %     % Início do cálculo do espectro em frequência (FFT)
% %     Nsample=333333;
% %     Fsample = 1/50e-9;
% %     % Calcula a FFT do sinal importado, multiplicado por uma janela de
% %     % Hann (Hanning) de comprimento igual ao dos dados importados e
% %     % preenchido de zeros até o comprimento NFFT calculado. Estas medidas
% %     % resultam em menor vazamento espectral, menores erros nas amplitudes
% %     % encontradas e maior resolução nas frequências de interesse.
% %     signal_dft = fft(PI.*hann(Nsample));
% %        
% %     % Seleciona apenas o nível DC e as frequências positivas da FFT
% %     signal_dft = signal_dft(1:round(length(signal_dft)/2)+1);
% %     % Divide as amplitudes pelo comprimento do sinal e aplica o fator de
% %     % correção da janela Hanning.
% %     signal_dft = signal_dft/(Nsample*0.5);
% %     % Multiplica as amostras da frequência positiva por 2. Traz o mesmo
% %     % efeito de se somar as frequências positivas e negativas.
% %     signal_dft(2:end) = 2*signal_dft(2:end);
% %      
% %     % Cria o vetor de frequência. Usado para plotar gráficos
% %     freq = 0:20:(Fsample/2);
% %     NFFT=333333;
% %     max_harm=40;
% %     % Encontra o valor da amostra da frequência fundamental, e a partir
% %     % deste valor, encontra qual deve ser o incremento para encontrar as
% %     % próximas harmônicas.
% %     begin = round(60/((Fsample/2)/(NFFT/2 + 1)));
% %     step = 1;  %round(2*60/((Fsample/2)/(NFFT/2 + 1))) - begin;
% %     
% %     % Realiza uma decimação na frequência do sinal resultante. Desta forma,
% %     % o vetor resultante só apresenta as frequências múltiplas da
% %     % fundamental.
% %      fftdata_PI = signal_dft(begin:step:end);
% %     
% %     
% %     
% %             % Calcula a THDi
% %         
% %         THDi_PI = sqrt(sum((abs(fft_IL2_PI_PSIM(2:max_harm))./abs(fft_IL2_PI_PSIM(1))).^2));
% %         
% %         % Monta strings que serão utilizadas para automatizar títulos de
% %         % gráficos e nomes de figuras que precisam ser salvas.
% %         
% %         % Cria nova figura
% %         figure('Units', 'centimeters', 'Position', [5 5 12 7.5]);
% %         % Plota gráficos das FFT's das correntes de entrada
% %         plot(freq, abs(signal_dft),'LineWidth', 2.0, 'Color', [0, 0.7, 0.9]);
% %         grid on
% %         
% %         % Configurações específicas para as figuras
% %         axis([0 2500 0 ceil(max(abs(signal_dft))*2)/2]);
% %         xticks(0:250:2500);
% %         yticks(0:0.25:2.5)
% %         
% %         xlabel('Frequência (Hz)');
% %         ylabel('Amplitude (A)');
% %         
% %         legend('Medição THDi');
% %         title('FFT PI TH');
% %         
% %         set(gca,'FontSize',9);
% %         set(findall(gca, '-Property', 'FontName'), 'FontName', 'Times New Roman');
% %         set(gcf, 'PaperPositionMode', 'auto');
% %         set(gcf,'color','white');
% %         
% % %         % Salva figuras
% % %         filename = strcat('..\figuras\',fld,'_THDi','.emf');
% % %         print(filename, '-dmeta');
% %     