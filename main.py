import scipy.io
import h5py

mat = scipy.io.loadmat('anno_bbox.mat')


print(list(mat.get("bbox_train"))[0][2][0])
print(list(mat.get("bbox_train"))[0][2][1])
print(list(mat.get("bbox_train"))[0][2][3])
#print(list(mat.get("bbox_train"))[0][0][2][0][0][0])
exit()
