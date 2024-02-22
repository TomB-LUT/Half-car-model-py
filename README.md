This program is simulating vehicle vertical dynamics. It uses mathematical model of the vehicle that consists of set of ordinary differential equations describing vehicle vertical motion. 
The vehicle is runing on artificially generated road profile that is created and saved to .txt using **Stochastic_excitation_generator.py** 
The equations of motion (Ordinary differential equations) describing vehicle dynamics are gathered in the file **Eq_half-car.py**
File **Integration_half_car_.py** is using scipy library to integrate equations of motion. The file also creates animation using files **Plot_solar_pre** and **Plot_solar**. The latter file is 
generating the contour of the vehicle from .png file and the former is plotting the vehicle in consecutive instances of time. Animation is saved as a gif file. 
