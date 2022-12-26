import os
import uuid
import flask
import urllib
import random
from PIL import Image
from tensorflow.keras.models import load_model
from flask import Flask , render_template  , request , send_file
from tensorflow.keras.preprocessing.image import load_img , img_to_array

app = Flask(__name__)
#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = load_model('Model.h5',compile=False)


ALLOWED_EXT = set(['jpg' , 'jpeg' , 'png' , 'jfif'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXT

classes = [
'Tomato_Late_blight',
 'Tomato_healthy', 
'Grape_healthy',
 'Orange_Haunglongbing_(Citrus_greening)', 
'Soybean_healthy',
 'Squash_Powdery_mildew', 
'Potato_healthy', 
'Corn_(maize)_Northern_Leaf_Blight',
 'Tomato_Early_blight',
 'Tomato_Septoria_leaf_spot', 
'Corn_(maize)_Cercospora_leaf_spot Gray_leaf_spot', 
'Strawberry_Leaf_scorch',
 'Peach_healthy',
 'Apple_Apple_scab', 
'Tomato_Tomato_Yellow_Leaf_Curl_Virus', 
'Tomato_Bacterial_spot',
 'Apple_Black_rot',
 'Blueberry_healthy',
 'Cherry_(including_sour)_Powdery_mildew',
 'Peach_Bacterial_spot',
 'Apple_Cedar_apple_rust', 
'Tomato_Target_Spot', 
'Pepper,_bell_healthy',
 'Grape_Leaf_blight_(Isariopsis_Leaf_Spot)', 
'Potato_Late_blight',
 'Tomato_Tomato_mosaic_virus',
 'Strawberry_healthy', 
'Apple_healthy',
 'Grape_Black_rot',
 'Potato_Early_blight',
'Cherry_(including_sour)_healthy', 
'Corn_(maize)_Common_rust_', 
'Grape_Esca_(Black_Measles)', 
'Raspberry_healthy',
 'Tomato_Leaf_Mold',
 'Tomato_Spider_mites Two-spotted_spider_mite',
 'Pepper, _bell_Bacterial_spot',
 'Corn_(maize)___healthy']             
   

def predict(filename , model):
    img = load_img(filename , target_size = (224 , 224))
    img = img_to_array(img)
    img = img.reshape(1,224 ,224 ,3)

    img = img.astype('float32')
    img = img/255.0
    result = model.predict(img)

    dict_result = {}
    for i in range(38):
        dict_result[result[0][i]] = classes[i]

    res = result[0]
    res.sort()
    res = res[::-1]
    prob = res[:38]
    
    prob_result = []
    class_result = []
    for i in range(38):
        prob_result.append((prob[i]).round(2))
        class_result.append(dict_result[prob[i]])

    return class_result , prob_result



@app.route('/')
def home():
        return render_template("index.html")

@app.route('/success' , methods = ['GET' , 'POST'])
def success():
    error = ''
    target_img = os.path.join(os.getcwd() , 'static/images')
    if request.method == 'POST':
        if(request.form):
            link = request.form.get('link')
            try :
                resource = urllib.request.urlopen(link)
                unique_filename = str(uuid.uuid4())
                filename = unique_filename+".jpg"
                img_path = os.path.join(target_img + filename)
                output = open(img_path , "wb")
                output.write(resource.read())
                output.close()
                img = filename

                class_result , prob_result = predict(img_path , model)

                predictions = {
                                       "class1":class_result[0],
                                        "class2":class_result[1],
                                        "class3":class_result[2],
                                        "class4":class_result[3],
                                        "class5":class_result[4],
                                        "class6":class_result[5],
                                        "class7":class_result[6],
                                        "class8":class_result[7],
                                        "class9":class_result[8],
                                        "class10":class_result[9],
                                        "class11":class_result[10],
                                        "class12":class_result[11],
                                        "class13":class_result[12],
                                        "class14":class_result[13],
                                        "class15":class_result[14],
                                        "class16":class_result[15],
                                        "class17":class_result[16],
                                        "class18":class_result[17],
                                        "class19":class_result[18],
                                        "class20":class_result[19],
                                        "class21":class_result[20],
                                        "class22":class_result[21],
                                        "class23":class_result[22],
                                        "class24":class_result[23],
                                        "class25":class_result[24],
                                        "class26":class_result[25],
                                        "class27":class_result[26],
                                        "class28":class_result[27],
                                        "class29":class_result[28],
                                        "class30":class_result[29],
                                        "class31":class_result[30],
                                        "class32":class_result[31],
                                        "class33":class_result[32],
                                        "class34":class_result[33],
                                        "class35":class_result[34],
                                        "class36":class_result[35],
                                        "class37":class_result[36],
                                        "class38":class_result[37],
                                        "prob1": prob_result[0],
                                        "prob2": prob_result[1],
                                        "prob3": prob_result[2],
                                        "prob4": prob_result[3],
                                        "prob5": prob_result[4],
                                        "prob6": prob_result[5],
                                        "prob7": prob_result[6],
                                        "prob8": prob_result[7],
                                        "prob9": prob_result[8],
                                        "prob10": prob_result[9],
                                        "prob11": prob_result[10],
                                        "prob12": prob_result[11],
                                        "prob13": prob_result[12],
                                        "prob14": prob_result[13],
                                        "prob15": prob_result[14],
                                        "prob16": prob_result[15],
                                        "prob17": prob_result[16],
                                        "prob18": prob_result[17],
                                        "prob19": prob_result[18],
                                        "prob20": prob_result[19],
                                        "prob21": prob_result[20],
                                        "prob22": prob_result[21],
                                        "prob23": prob_result[22],
                                        "prob24": prob_result[23],
                                        "prob25": prob_result[24],
                                        "prob26": prob_result[25],
                                        "prob27": prob_result[26],
                                        "prob28": prob_result[27],
                                        "prob29": prob_result[28],
                                        "prob30": prob_result[29],
                                        "prob31": prob_result[30],
                                        "prob32": prob_result[31],
                                        "prob33": prob_result[32],
                                        "prob34": prob_result[33],
                                        "prob35": prob_result[34],
                                        "prob36": prob_result[35],
                                        "prob37": prob_result[36],
                                        "prob38": prob_result[37]



                }

            except Exception as e : 
                print(str(e))
                error = 'Sorry, We can not found this Image'

            if(len(error) == 0):
                return  render_template('success.html' , img  = img , predictions = predictions)
            else:
                return render_template('index.html' , error = error) 

            
        elif (request.files):
            file = request.files['file']
            if file and allowed_file(file.filename):
                file.save(os.path.join(target_img , file.filename))
                img_path = os.path.join(target_img , file.filename)
                img = file.filename

                class_result , prob_result = predict(img_path , model)

                predictions = {
                                    "class1":class_result[0],
                                        "class2":class_result[1],
                                        "class3":class_result[2],
                                        "class4":class_result[3],
                                            "class5":class_result[4],
                                            "class6":class_result[5],
                                            "class7":class_result[6],
                                                "class8":class_result[7],
                                                "class9":class_result[8],
                                           "class10":class_result[9],
                              
                                        "class11":class_result[10],
                        
                                            "class12":class_result[11],
                                             "class13":class_result[12],
                                              "class14":class_result[13],
                                              "class15":class_result[14],
                                            "class16":class_result[15],
                                           "class17":class_result[16],
                                             "class18":class_result[17],
                                             "class19":class_result[18],
                                              "class20":class_result[19],
                                          "   class21":class_result[20],
                                              "class22":class_result[21],
                                             "class23":class_result[22],
                                             "class24":class_result[23],
                                         
                                            "class25":class_result[24],
                                            "class26":class_result[25],
                                            "class27":class_result[26],
                                            "class28":class_result[27],
                                                    
                                                "class29":class_result[28],
                                      "class30":class_result[29],
                                       "class31":class_result[30],
                                       
                        "class32":class_result[31],
                         "class33":class_result[32],
                          "class34":class_result[33],
                          "class35":class_result[34],
                         "class36":class_result[35],
                         "class37":class_result[36],
                          "class38":class_result[37],
                          
                          "prob1": prob_result[0],

                        "prob2": prob_result[1],

                       
                       "prob3": prob_result[2],

                       
                       "prob4": prob_result[3],

                       
                       "prob5": prob_result[4],

                        
                       "prob6": prob_result[5],

                       
                       "prob7": prob_result[6],

                      
                       "prob8": prob_result[7],

                        
                       "prob9": prob_result[8],

                       
                       "prob10": prob_result[9],

                       "prob11": prob_result[10],

                       "prob12": prob_result[11],

                        
                       "prob13": prob_result[12],

                       "prob14": prob_result[13],

            
                       "prob15": prob_result[14],

                   
                       "prob16": prob_result[15],

                      
                       "prob17": prob_result[16],

                  
                       "prob18": prob_result[17],

                      
                       "prob19": prob_result[18],

                       
                       "prob20": prob_result[19],

                       
                       "prob21": prob_result[20],

                        
                       "prob22": prob_result[21],

                       
                       "prob23": prob_result[22],

                       "prob24": prob_result[23],

                       "prob25": prob_result[24],

              
                       "prob26": prob_result[25],

                       
                       "prob27": prob_result[26],

                    
                       "prob28": prob_result[27],

                       "prob29": prob_result[28],

                      
                       "prob30": prob_result[29],

                       
                       "prob31": prob_result[30],

                       "prob32": prob_result[31],

                       
                       "prob33": prob_result[32],

                       
                       "prob34": prob_result[33],

                        
                       "prob35": prob_result[34],

                        
                       "prob36": prob_result[35],


                       
                       "prob37": prob_result[36],

                       
                       "prob38": prob_result[37]

                       

        }


            else:
                error = "Please upload images of jpg , jpeg and png extension only"

            if(len(error) == 0):
                return  render_template('success.html' , img  = img , predictions = predictions)
            else:
                return render_template('index.html' , error = error)

    else:
        return render_template('index.html')






if __name__ == "__main__":
    app.run(debug = True)


