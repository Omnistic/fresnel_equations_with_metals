# Polarization Effects At Metallic Mirror Interfaces
Although it is thaught early in introductory physics lectures, the effect a metallic mirror can have on polarization is often overlooked.

The first time I was reminded about such a phenomenon was during my time at Zemax, when my colleague Katsumoto Ikeda gave an answer to the question: [Why do I get an elliptical polarization after a 45-degree reflection in a mirror?](https://community.zemax.com/got-a-question-7/why-do-i-get-an-elliptical-polarization-after-a-45-degree-reflection-in-a-mirror-957)

I guess that for simplicity we are tempted to assume that mirrors do exactly that, they mirror whatever was coming onto them. And so why should they have any effect on the polarization?

In addition to what Katsumoto wrote in the forum answer, I wanted to give more insights into this topic by showing a simulation. I used the [Fresnel equations](https://en.wikipedia.org/wiki/Fresnel_equations) from Wikipedia.

Below are the formulas I used from the article (the background is transparent and doesn't appear well in dark mode).

![r_s](https://wikimedia.org/api/rest_v1/media/math/render/svg/1ef14e8fb7b00e2b3e3e81b249fe280c9e748d35)
![r_p](https://wikimedia.org/api/rest_v1/media/math/render/svg/b087790ec188db86770d80b136c778fa3b28481e)

Note that I used the very last part of the equation where ```theta_t``` has been eliminated.

In my code, ```air``` and ```silver``` are n_1 and n_2 from the formulas, respectively. Since silver is a metal, the refractive index is a complex number. I took the values for the refractive index of silver from [refractiveindex.info](https://refractiveindex.info/?shelf=main&book=Ag&page=Jiang) (Shelf:MAIN, Book:Ag, Page: Jiang et al. 2016) using a wavelength of 0.88um. The actual values are ```n=0.010400``` (the real part) and ```k=5.8570``` (the imaginary part), leading to ```silver = n + i*k```.

Lastly, in my code ```aoi``` is the angle of incidence or ```theta_i``` in the Wikipedia formula. The phase of each reflection coefficient (*s* and *p*) as a function of the angle of incidence. The resulting figure is also saved as [fresnel_silver.pdf](https://github.com/Omnistic/fresnel_equations_with_metals/blob/main/fresnel_silver.pdf) in the repository. At normal incidence (```aoi=0```), there is no phase difference between the *s* and *p* polarizations and the polarization state can be preserved. However, at 45 degree incidence, the *s* and *p* polarizations experience a phase difference of about 13.7 degree, which explains why an initially linearly polarized beam that is not purely *s* or *p* polarized can become elliptically polarized.

