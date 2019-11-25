def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
import warnings 
from sklearn.externals import joblib


warnings.filterwarnings(action = 'ignore')

phrase=input("Enter : ")


#filename2 = 'C:\\Users\\DELL\\Downloads\\wp3_Log_model_optimized.sav'
filename2='log_gun_model_trained3.sav'

loaded_model2 = joblib.load(filename2)

arg=loaded_model2.predict(([phrase]))
arg[0]

from json.encoder import JSONEncoder
final_entity = { "predicted_argument": [arg[0]]}
# directly called encode method of JSON
print (JSONEncoder().encode(final_entity))