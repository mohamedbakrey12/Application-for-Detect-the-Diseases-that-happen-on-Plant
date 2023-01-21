# Application-for-Detect-the-Diseases-that-happen-on-Plant

## Introduction
There is increasing difficulty in identifying new plant leaf diseases as a result of environmental change. There is a need to identify the factors influencing the emergence and the increasing incidences of these diseases. Here, we present emerging fungal plant leaf diseases and describe their environmental speciation. We considered the factors controlling for local adaptation associated with environmental speciation. We determined that the advent of emergent fungal leaf diseases is closely connected to environmental speciation. Fungal pathogens targeting the leaves may adversely affect the entire plant body. To mitigate the injury caused by these pathogens, it is necessary to be able to detect and identify them early in the infection process. In this way, their distribution, virulence, incidence, and severity could be attenuated.


## Who is the target of this problem:
The target is the farm owners who work to grow these plants and who suffer from those diseases that affect the leaves of the plants of uncle, such as tomatoes, potatoes, apples and other problems. Where those leaves are affected by rot that appears on the outer surface of the leaves.

## About Dataset:
Human society needs to increase food production by an estimated 70% by 2050 to feed an expected population size that is predicted to be over 9 billion people. Currently, infectious diseases reduce the potential yield by an average of 40% with many farmers in the developing world experiencing yield losses as high as 100%.
The widespread distribution of smartphones among crop growers around the world with an expected 5 billion smartphones by 2020 offers the potential of turning the smartphone into a valuable tool for diverse communities growing food. One potential application is the development of mobile disease diagnostics through machine learning and crowdsourcing. Here we announce the release of over 50,000 expertly curated images on healthy and infected leaves of crops plants through the existing online platform PlantVillage. We describe both the data and the platform. These data are the beginning of an on-going, crowdsourcing effort to enable computer vision approaches to help solve the problem of yield losses in crop plants due to infectious diseases.

Dataset have many kind of plant like 'Tomato___Late_blight', 'Tomato___healthy', 'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Potato___healthy', 'Corn_(maize)___Northern_Leaf_Blight', 'Tomato___Early_blight', 'Tomato___Septoria_leaf_spot', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Strawberry___Leaf_scorch', 'Peach___healthy', 'Apple___Apple_scab', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Bacterial_spot', 'Apple___Black_rot', 'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Peach___Bacterial_spot', 'Apple___Cedar_apple_rust', 'Tomato___Target_Spot', 'Pepper,_bell___healthy', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Potato___Late_blight', 'Tomato___Tomato_mosaic_virus', 'Strawberry___healthy', 'Apple___healthy', 'Grape___Black_rot', 'Potato___Early_blight', 'Cherry_(including_sour)___healthy', 'Corn_(maize)___Common_rust_', 'Grape___Esca_(Black_Measles)', 'Raspberry___healthy', 'Tomato___Leaf_Mold', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Pepper,_bell___Bacterial_spot', 'Corn_(maize)___healthy']

`Types of classes labels found:  38` 

some of image we have in dataset: 

![image](https://user-images.githubusercontent.com/66233001/213864875-97d83693-2c77-4b79-843e-44671db46b4e.png)
![image](https://user-images.githubusercontent.com/66233001/213864881-f18e32ae-041b-40cb-810e-e988773c730e.png)
![image](https://user-images.githubusercontent.com/66233001/213864890-1187d464-f71c-4978-a231-c1b063e49003.png)


![image](https://user-images.githubusercontent.com/66233001/213864940-d8e2798b-f16d-4055-8e9d-a1127c3ddfed.png)
![image](https://user-images.githubusercontent.com/66233001/213864943-4c65aa43-cb86-4d97-b2d2-159e970f3b4f.png)
![image](https://user-images.githubusercontent.com/66233001/213864958-48cd7977-ece0-4a89-971b-bef38fccb826.png)


## What is the proposed solution:
Here I made the perfect solution, which uses multiple techniques, one of the most important of these techniques is deep learning, where this application works entirely on the algorithms of neural networks, which work to classify these diseases in their normal cases, as these diseases are in cases such as beginner, intermediate, and advanced, and there are also those In a healthy condition. Here he works to reveal and clarify those cases. And with great accuracy.


## The result we achive after training the model:
First, I created a neural network model from scratch, where I placed the basic layers, 
and then I invaded the network with the data we have, and the network shape became as follows:
![image](https://user-images.githubusercontent.com/66233001/213865056-5e284fd1-1e0b-467f-adb4-3808b1b99af7.png)

#### Results:
![image](https://user-images.githubusercontent.com/66233001/213865085-d78cdc1e-75d9-47a1-8f7f-be8d8da13755.png)

#### The predictive of the model:
![image](https://user-images.githubusercontent.com/66233001/213865105-c53de2d3-7bc2-477c-9514-3cbb40c3b71e.png)



## Tools
1. Deep Learning model (CNN)
2. Tensorflow : For the implement the model and create the layers
3. Keras: That is the framwork as well as using it to create the model
4. Python as Language. 
5. Flask: That is the Framework we using it for deployment the model
6. HTML & CSS That using it to create the style and form of the application.
