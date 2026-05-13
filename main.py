import pickle
file_path = "diet_recommended_prediction_model.pkl"
with open(file_path, "rb") as file:
    model = pickle.load(file)
print(model)
print(type(model))