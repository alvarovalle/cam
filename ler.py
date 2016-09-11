import pickle
with open('cam_data.pkl', 'rb') as input:
    cam_data = pickle.load(input)
    if(cam_data[0]):
        print(cam_data[1][1][1][0], cam_data[1][1][1][1], cam_data[1][1][1][2])
